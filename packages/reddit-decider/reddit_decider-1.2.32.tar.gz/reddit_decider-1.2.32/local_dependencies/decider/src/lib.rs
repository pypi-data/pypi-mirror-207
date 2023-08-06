#![warn(rust_2018_idioms)]

//! Decider is a library for determining whether a given feature should be available
//! in a given context.  It supports a very expressive set of operations for determining
//! which features should be available (and in what variant, if more than one is desired)
//! in a context.
mod context;
mod events;

use std::collections::HashMap;
use std::convert::identity;
use std::error::Error;
use std::fmt;
use std::fs::File;
use std::io::{BufReader, Read};
use std::ops::{Not, Range};
use std::path::Path;

use crate::events::SerializedEvents;
use events::ExperimentEvent;
use float_cmp::approx_eq;
use num_bigint::BigUint;
use serde::{Deserialize, Serialize};
use serde_json::Value;
use sha1::{Digest, Sha1};
use thiserror::Error;

pub use context::{Context, ContextField};

/// Takes two [`Value`] references, possibly of different variants and compares them for equality.
///
/// If one of the operands is a [`Value::String`] and the other is a [`Value::Number`], the string
/// is parsed as a number before comparison.
///
/// All numbers are treated as floats for comparison. The experiment config and the context's
/// `other_fields` field are both json, which means comparing any two number values as integers may
/// lead to subtly incorrect behavior. The downside is that float equality is approximate by
/// definition. The values that we're expecting to compare, however, are small and imprecise enough
/// that this shouldn't be a problem. For reference, we compare floats using the 64-bit
/// [Machine epsilon](https://en.wikipedia.org/wiki/Machine_epsilon) and 4 [ULPs](https://en.wikipedia.org/wiki/Unit_in_the_last_place).
///
/// For more information, see the [floating point comparison guide](https://floating-point-gui.de/errors/comparison/).
fn value_eq(x: &Value, y: &Value) -> Option<bool> {
    match (&x, &y) {
        (Value::Null, _) => Some(y.is_null()),
        (Value::Bool(b1), Value::Bool(b2)) => Some(b1 == b2),
        (Value::String(s1), Value::String(s2)) => Some(s1 == s2),
        (Value::String(s1), Value::Number(n2)) => {
            match (s1.parse::<f64>(), n2.as_f64()) {
                (Ok(f1), Some(f2)) => Some(approx_eq!(f64, f1, f2)),
                // s1 is not a parseable as number _or_ n2 is not convertible to f64. The latter
                // should never happen.
                _ => Some(false),
            }
        }
        (Value::Number(n1), Value::Number(n2)) => {
            match (n1.as_f64(), n2.as_f64()) {
                (Some(f1), Some(f2)) => Some(approx_eq!(f64, f1, f2)),
                // Number(s) not convertible to float. Should never happen!
                _ => Some(false),
            }
        }
        (Value::Number(n1), Value::String(s2)) => {
            match (n1.as_f64(), s2.parse::<f64>()) {
                (Some(f1), Ok(f2)) => Some(approx_eq!(f64, f1, f2)),
                // n1 is not convertible to float _or_ s2 is not parseable as a number. The former
                // should never happen.
                _ => Some(false),
            }
        }
        _ => None,
    }
}

/// Features represent a unit of controllable code, that we might want to turn off, make
/// available only to some users, etc..  This is what FeatureFlags/AB tests control.
#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct Feature {
    pub id: u32,
    pub name: String,
    pub enabled: bool,
    #[serde(rename(serialize = "type"))]
    pub feature_type: ExperimentType,
    pub version: u32,
    pub owner: String,
    pub emit_event: bool,
    pub platform_bitmask: u64, // TODO: change this to a bitvec
    pub value: Option<Value>,
    pub value_type: Option<ValueType>,
    targeting: Option<TargetingTree>,
    overrides: Option<Vec<HashMap<String, TargetingTree>>>,
    pub variant_set: Option<VariantSet>,
}

impl Feature {
    /// `get_variants` returns this feature's variants.
    pub fn get_variants(&self) -> Vec<Variant> {
        self.variant_set
            .as_ref()
            .map(|vs| vs.variants.clone())
            .unwrap_or_default()
    }

    /// Returns a default decision for this feature. This is called when no decisionmaker
    /// is able to make a decision on a feature.
    fn default_decision(&self, events: Vec<ExperimentEvent>) -> InternalDecision {
        InternalDecision {
            feature_id: self.id,
            feature_name: self.name.clone(),
            feature_version: self.version,
            variant_name: None,
            value: self.value_type.map(Value::from).unwrap_or(Value::Null),
            value_type: self.value_type,
            events,
        }
    }

    fn make_event(
        &self,
        dk: DecisionKind,
        variant_name: &str,
        ctx: &Context,
    ) -> Result<Option<ExperimentEvent>, DeciderError> {
        if !self.emit_event {
            return Ok(None);
        }

        let variant_set = &self
            .variant_set
            .as_ref()
            .ok_or(DeciderError::MissingVariantSet)?;

        let (bucketing_field, bucketing_value) = variant_set
            .bucketing_field
            .as_ref()
            .ok_or(DeciderError::MissingBucketVal)
            .and_then(|bucketing_field| {
                let bucketing_value = bucketing_field
                    .get_value(ctx)
                    .ok_or(DeciderError::MissingBucketVal)
                    .map(|v| match v {
                        // Json strings are formatted surrounded by quotes. Extract the inner value
                        // to avoid this.
                        Value::String(inner) => inner,
                        value => value.to_string(),
                    })?;
                Ok((bucketing_field, bucketing_value))
            })?;

        Ok(Some(ExperimentEvent {
            decision_kind: dk,
            feature_id: self.id,
            feature_name: self.name.clone(),
            feature_version: self.version,
            variant_name: variant_name.to_string(),
            bucketing_field: bucketing_field.clone(),
            bucketing_value,
            start_ts: variant_set.start_ts,
            stop_ts: variant_set.stop_ts,
            owner: self.owner.clone(),
        }))
    }
}

#[derive(Serialize, Copy, Clone, Debug, PartialEq, Eq)]
pub enum DecisionKind {
    FracAvail = 0,
    Override = 1,
    Holdout = 2,
    MutexGroup = 3,
}

impl DecisionKind {
    fn cast_events(&self, events: &mut [ExperimentEvent]) {
        if let Some(head) = events.first_mut() {
            head.decision_kind = *self;
        }
    }
}

impl TryFrom<u8> for DecisionKind {
    type Error = ();

    fn try_from(value: u8) -> Result<Self, Self::Error> {
        match value {
            0 => Ok(Self::FracAvail),
            1 => Ok(Self::Override),
            2 => Ok(Self::Holdout),
            3 => Ok(Self::MutexGroup),
            _ => Err(()),
        }
    }
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct EqMany {
    field: ContextField,
    values: Vec<Value>,
}

impl EqMany {
    fn eval(&self, ctx: &Context) -> Option<bool> {
        self.field.get_value(ctx).and_then(|x| {
            self.values
                .iter()
                .map(|v| value_eq(&x, v))
                .try_fold(false, |acc, res| res.map(|r| acc || r))
        })
    }
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct EqOne {
    field: ContextField,
    value: Value,
}

impl EqOne {
    fn eval(&self, ctx: &Context) -> Option<bool> {
        ctx.cmp(&self.field, &self.value)
    }
}

#[derive(Serialize, Deserialize, Debug, Clone)]
#[serde(untagged)]
pub enum EqEnum {
    EqOne(EqOne),
    EqMany(EqMany),
}

impl EqEnum {
    fn eval(&self, ctx: &Context) -> Option<bool> {
        match self {
            EqEnum::EqOne(eo) => eo.eval(ctx),
            EqEnum::EqMany(em) => em.eval(ctx),
        }
    }
}

/// The TargetingTree allows for arbitrary targeting operations, which can be used to
/// limit an experiment to employees, or users from New Zealand, only to iOS users, etc...
#[allow(clippy::upper_case_acronyms)]
#[derive(Serialize, Deserialize, Debug, Clone)]
enum TargetingTree {
    ALL(Vec<TargetingTree>),
    ANY(Vec<TargetingTree>),
    NOT(Box<TargetingTree>),

    EQ(EqEnum),
    NE { field: ContextField, value: Value },

    GT { field: ContextField, value: f64 },
    LT { field: ContextField, value: f64 },
    GE { field: ContextField, value: f64 },
    LE { field: ContextField, value: f64 },
}

enum Comp {
    GT,
    LT,
    GE,
    LE,
}

impl Comp {
    fn cmp_floats(&self, f1: f64, f2: f64) -> bool {
        match self {
            Comp::GT => f1 > f2,
            Comp::LT => f1 < f2,
            Comp::GE => f1 > f2 || approx_eq!(f64, f1, f2),
            Comp::LE => f1 < f2 || approx_eq!(f64, f1, f2),
        }
    }
}
impl TargetingTree {
    fn eval(&self, ctx: &Context) -> Option<bool> {
        match self {
            TargetingTree::ALL(xs) => Some(
                xs.iter()
                    .map(|x| x.eval(ctx).unwrap_or(false))
                    .all(identity),
            ),
            TargetingTree::ANY(xs) => Some(
                // N.B. `ANY` uses `flat_map` which filters out `None` results. This is to allow
                // ANY targeting to succeed in case some subset of targeted fields is missing in the
                // context. `Iter::any` returns `false` on an empty iterator.
                xs.iter().flat_map(|x| x.eval(ctx)).any(identity),
            ),

            TargetingTree::EQ(es) => es.eval(ctx),
            TargetingTree::NOT(x) => x.eval(ctx).map(Not::not),

            TargetingTree::GT { field, value } => ctx.cmp_op(Comp::GT, field, *value),
            TargetingTree::LT { field, value } => ctx.cmp_op(Comp::LT, field, *value),
            TargetingTree::GE { field, value } => ctx.cmp_op(Comp::GE, field, *value),
            TargetingTree::LE { field, value } => ctx.cmp_op(Comp::LE, field, *value),

            TargetingTree::NE { field, value } => ctx.cmp(field, value).map(Not::not),
        }
    }
}

/// Decider determines feature availability by chaining together simple decision maker
/// functions to enable complicated logic to be expressed as a composition of simple,
/// testable functions. Those compositions are tested against features, an abstraction
/// for bits of code that enabling feature flagging, AB testing, etc..
pub struct Decider {
    features: Vec<Feature>,
    decisionmakers: Vec<Decisionmaker>,
}

impl fmt::Debug for Decider {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "Decider: {:#?}", self.features)
    }
}

impl Decider {
    const DEFAULT_DECISIONMAKERS: &'static str =
        "darkmode overrides targeting holdout mutex_group fractional_availability value";

    /// Creates a new `Decider` with the default decisionmakers. The experiment config is loaded
    /// from the provided file path.
    pub fn new(path: impl AsRef<Path>) -> Result<Self, DeciderInitError> {
        let file = File::open(path)?;
        let read = BufReader::new(file);

        Self::from_bytes(read)
    }

    /// Creates a new `Decider` with the default decisionmakers. The experiment config is loaded
    /// from the provided [`std::io::Read`].
    pub fn from_bytes(config: impl Read) -> Result<Self, DeciderInitError> {
        let value = serde_json::from_reader(config)?;

        Self::with_decisionmakers(value, Self::DEFAULT_DECISIONMAKERS)
    }

    /// Creates a new `Decider` with an experiment config and a decisionmaker config string. Prefer
    /// the other constructors for this type: customizing the set of decisionmakers is rarely what
    /// you want.
    pub fn with_decisionmakers(
        config: Value,
        decisionmakers: &str,
    ) -> Result<Self, DeciderInitError> {
        let raw_config: RawConfig = serde_json::from_value(config)?;
        let (mut features, errs) = raw_config.features();
        features.sort_unstable_by_key(|f| f.name.clone());

        string_to_decisionmakers(decisionmakers).and_then(|decisionmakers| {
            let decider = Decider {
                features,
                decisionmakers,
            };

            if errs.is_empty() {
                Ok(decider)
            } else {
                Err(DeciderInitError::PartialLoad(decider, errs))
            }
        })
    }

    pub fn choose(
        &self,
        feature_name: &str,
        ctx: &Context,
        bucketing_field_opt: Option<ContextField>,
    ) -> Result<Decision, DeciderError> {
        let f = self.feature_by_name(feature_name)?;
        match bucketing_field_opt {
            None => self.decide(f, ctx),
            Some(bucketing_field) => match &f.variant_set {
                None => Err(DeciderError::InvalidFeature),
                Some(vs) => match &vs.bucketing_field {
                    Some(feature_bucketing_field) => {
                        if &bucketing_field == feature_bucketing_field {
                            self.decide(f, ctx)
                        } else {
                            Err(DeciderError::IdentifierTypeBucketValMismatch(
                                bucketing_field,
                                feature_bucketing_field.clone(),
                            ))
                        }
                    }
                    None => Err(DeciderError::InvalidFeature),
                },
            },
        }
    }

    pub fn choose_all(
        &self,
        ctx: &Context,
        bucketing_field_opt: Option<ContextField>,
    ) -> HashMap<String, Result<Decision, DeciderError>> {
        // FIXME: set this up such that we can filter by bucketing platform
        match bucketing_field_opt {
            None => self
                .features
                .iter()
                .filter_map(|f| match &f.feature_type {
                    ExperimentType::DynamicConfig => None,
                    _ => Some((f.name.clone(), self.decide(f, ctx))),
                })
                .collect(),
            Some(bucketing_field) => self
                .features
                .iter()
                .filter_map(|f| match &f.feature_type {
                    ExperimentType::DynamicConfig => None,
                    _ => match &f.variant_set {
                        None => None,
                        Some(vs) => match &vs.bucketing_field {
                            Some(feature_bucketing_field)
                                if &bucketing_field == feature_bucketing_field =>
                            {
                                Some((f.name.clone(), self.decide(f, ctx)))
                            }
                            _ => None,
                        },
                    },
                })
                .collect(),
        }
    }

    pub fn get_bool(&self, feature_name: &str, ctx: &Context) -> Result<bool, DeciderError> {
        match self.get_value(feature_name, ctx) {
            Ok(Value::Bool(b)) => Ok(b),
            Ok(_) => Err(DeciderError::DcTypeMismatch),
            Err(e) => Err(e),
        }
    }

    pub fn get_int(&self, feature_name: &str, ctx: &Context) -> Result<i64, DeciderError> {
        match self.get_value(feature_name, ctx) {
            Ok(Value::Number(n)) => match n.as_i64() {
                Some(int) => Ok(int),
                _ => Err(DeciderError::NumberDeserializationError),
            },
            Ok(_) => Err(DeciderError::DcTypeMismatch),
            Err(e) => Err(e),
        }
    }

    pub fn get_float(&self, feature_name: &str, ctx: &Context) -> Result<f64, DeciderError> {
        match self.get_value(feature_name, ctx) {
            Ok(Value::Number(n)) => match n.as_f64() {
                Some(float) => Ok(float),
                _ => Err(DeciderError::NumberDeserializationError),
            },
            Ok(_) => Err(DeciderError::DcTypeMismatch),
            Err(e) => Err(e),
        }
    }

    pub fn get_string(&self, feature_name: &str, ctx: &Context) -> Result<String, DeciderError> {
        match self.get_value(feature_name, ctx) {
            Ok(Value::String(s)) => Ok(s),
            Ok(_) => Err(DeciderError::DcTypeMismatch),
            Err(e) => Err(e),
        }
    }

    pub fn get_map(
        &self,
        feature_name: &str,
        ctx: &Context,
    ) -> Result<serde_json::Map<String, Value>, DeciderError> {
        match self.get_value(feature_name, ctx) {
            Ok(Value::Object(obj)) => Ok(obj),
            Ok(_) => Err(DeciderError::DcTypeMismatch),
            Err(e) => Err(e),
        }
    }

    pub fn get_all_values(&self, ctx: &Context) -> Result<HashMap<String, Decision>, DeciderError> {
        Ok(self
            .features
            .iter()
            .filter_map(|f| match &f.feature_type {
                ExperimentType::DynamicConfig => Some((
                    f.name.clone(),
                    match self.decide(f, ctx) {
                        Ok(decision) => decision,
                        _ => Decision {
                            feature_id: f.id,
                            feature_name: f.name.clone(),
                            feature_version: f.version,
                            variant_name: None,
                            value: f.value_type.map(Value::from).unwrap_or_default(),
                            value_type: f.value_type,
                            event_data: vec![],
                            events: vec![],
                        },
                    },
                )),
                _ => None,
            })
            .collect())
    }

    pub fn feature_by_name(&self, feature_name: &str) -> Result<&Feature, DeciderError> {
        match self
            .features
            .binary_search_by_key(&feature_name, |f| f.name.as_str())
        {
            Ok(idx) => Ok(&self.features[idx]),
            Err(_) => Err(DeciderError::FeatureNotFoundWithName(
                feature_name.to_string(),
            )),
        }
    }

    fn get_value(&self, feature_name: &str, ctx: &Context) -> Result<Value, DeciderError> {
        let f = self.feature_by_name(feature_name)?;
        match self.decide(f, ctx) {
            Err(e) => Err(e),
            Ok(Decision { value, .. }) => Ok(value),
        }
    }

    fn decide(&self, f: &Feature, ctx: &Context) -> Result<Decision, DeciderError> {
        // First, call `decide_internal` to get an `InternalDecision`...
        self.decide_internal(f, ctx).and_then(|internal| {
            // If that succeeded, hydrate the event strings and convert to a `Decision`.

            let serialized_events = SerializedEvents::new(ctx, internal.events)
                .map_err(DeciderError::MalformedEventError)?;

            Ok(Decision {
                feature_id: internal.feature_id,
                feature_name: internal.feature_name,
                feature_version: internal.feature_version,
                variant_name: internal.variant_name,
                value: internal.value,
                value_type: internal.value_type,
                event_data: serialized_events.event_data,
                events: serialized_events.events,
            })
        })
    }

    fn decide_internal(
        &self,
        feature: &Feature,
        ctx: &Context,
    ) -> Result<InternalDecision, DeciderError> {
        let mut out = vec![];
        for fun in &self.decisionmakers {
            match fun(self, feature, ctx)? {
                Choice::None => break,
                Choice::Pass(_) => (),
                Choice::Continue(events) => out.extend(events),
                Choice::Decided(mut decision) => {
                    if !out.is_empty() {
                        out.extend(decision.events);
                        decision.events = out;
                    }
                    return Ok(decision);
                }
            }
        }
        // If we make it here that means a decision couldn't be made, either because no
        // decisionmaker returned `Choice::Decided`, or because a decisionmaker short-circuited via
        // `Choice::None`. Return a default decision to preserve events.
        Ok(feature.default_decision(out))
    }

    fn holdout(&self, f: &Feature, ctx: &Context) -> Result<Choice, DeciderError> {
        let hgo = f.variant_set.as_ref().and_then(|vs| vs.holdout.as_ref());
        match hgo {
            None => Ok(Choice::Pass("no_holdout_group")),
            Some(hg) => match self.decide_internal(hg, ctx) {
                Err(e) => Err(e),
                Ok(d) => match d.variant_name {
                    None => Ok(Choice::Pass("in_holdout:false")),
                    Some(s) => {
                        let mut events = d.events;
                        DecisionKind::Holdout.cast_events(&mut events);

                        match s.as_str() {
                            "control_1" => Ok(Choice::Continue(events)),
                            "holdout" => Ok(Choice::Decided(InternalDecision {
                                feature_id: f.id,
                                feature_name: f.name.to_string(),
                                feature_version: f.version,
                                variant_name: None,
                                value: hg.value.clone().unwrap_or_default(),
                                value_type: hg.value_type,
                                events,
                            })),
                            _ => Ok(Choice::Pass("in_holdout:false")),
                        }
                    }
                },
            },
        }
    }

    fn mutex_group(&self, f: &Feature, ctx: &Context) -> Result<Choice, DeciderError> {
        let mgo = &f
            .variant_set
            .as_ref()
            .and_then(|vs| vs.mutex_group.as_ref());
        match mgo {
            None => Ok(Choice::Pass("no_mutex_group")),
            Some(mg) => match self.decide_internal(mg, ctx) {
                Err(e) => Err(e),
                Ok(InternalDecision {
                    variant_name: Some(s),
                    mut events,
                    ..
                }) => {
                    // I got a decision!  But am I in the experiment I was asked for?
                    if s == f.name {
                        // Yes.  yes I am.  Let control flow through to the experiments
                        DecisionKind::MutexGroup.cast_events(&mut events);
                        Ok(Choice::Continue(events))
                    } else {
                        // not in exp, terminate early.
                        Ok(Choice::None)
                    }
                }
                // I'm not in the mutex group experiment.
                _ => Ok(Choice::None),
            },
        }
    }

    fn darkmode(&self, f: &Feature, _ctx: &Context) -> Result<Choice, DeciderError> {
        if f.enabled {
            Ok(Choice::Pass("darkmode:enabled"))
        } else {
            Ok(Choice::None)
        }
    }

    fn fractional_availability(&self, f: &Feature, ctx: &Context) -> Result<Choice, DeciderError> {
        match &f.variant_set {
            None => Ok(Choice::Pass("frac_avail:no variant_set")),
            Some(vs) => vs.get_bucket(f, ctx),
        }
    }

    fn overrides(&self, f: &Feature, ctx: &Context) -> Result<Choice, DeciderError> {
        match &f.overrides {
            None => Ok(Choice::Pass("overrides:none_found")),
            Some(ov) => {
                for hm in ov.iter() {
                    for (name, tt) in hm.iter() {
                        match tt.eval(ctx) {
                            Some(true) => {
                                let event = f.make_event(DecisionKind::Override, name, ctx)?;

                                return Ok(Choice::Decided(InternalDecision {
                                    feature_id: f.id,
                                    feature_name: f.name.to_string(),
                                    feature_version: f.version,
                                    // FIXME: check to make sure this is a variant name
                                    variant_name: Some(name.clone()),
                                    value: Value::String(name.clone()),
                                    value_type: Some(ValueType::String),
                                    events: Vec::from_iter(event),
                                }));
                            }
                            Some(false) => continue,
                            None => {
                                // FIXME: propagate the error and continue
                                return Ok(Choice::Pass("t.eval:err"));
                            }
                        }
                    }
                }
                Ok(Choice::Pass("overrides:none_hit"))
            }
        }
    }

    fn targeting(&self, f: &Feature, ctx: &Context) -> Result<Choice, DeciderError> {
        match &f.targeting {
            None => Ok(Choice::Pass("targeting:none_found")),
            Some(tt) => match tt.eval(ctx) {
                Some(true) => Ok(Choice::Pass("targeting:targeted")),
                Some(false) => Ok(Choice::None),
                None => Ok(Choice::None), // FIXME: propagate the error
            },
        }
    }

    fn value(&self, f: &Feature, _ctx: &Context) -> Result<Choice, DeciderError> {
        match &f.value {
            None => Ok(Choice::None),
            Some(value) => match value {
                Value::Null | Value::Array(_) => Ok(Choice::Pass("value:null_or_array")),
                _ => Ok(Choice::Decided(InternalDecision {
                    feature_id: f.id,
                    feature_name: f.name.to_string(),
                    feature_version: f.version,
                    variant_name: None,
                    value: value.clone(),
                    value_type: f.value_type,
                    events: vec![],
                })),
            },
        }
    }
}

/// Variants are primarily used for fractional availability, where, eg., 10% of users
/// are exposed to a given version of a feature.
#[derive(Serialize, Deserialize, Debug, Clone, PartialEq, Eq)]
pub struct Variant {
    pub name: String,
    #[serde(with = "variant_range_aux", flatten)]
    pub range: Range<u16>,
}

const TOTAL_BUCKETS: u16 = 1000;

mod variant_range_aux {
    use crate::TOTAL_BUCKETS;
    use serde::{Deserialize, Deserializer, Serialize, Serializer};
    use std::ops::Range;

    #[derive(Serialize, Deserialize)]
    struct FloatRangeProxy {
        range_start: f32,
        range_end: f32,
    }

    /// Serializes a `Range<u16>` into a floating-point range using `FloatRangeProxy`.
    /// `TOTAL_BUCKETS` is used as the upper limit of the range.
    ///
    /// Expects the input range to have 0.0 <= start <= 1.0 and 0.0 <= end <= 1.0.
    pub fn serialize<S>(range: &Range<u16>, ser: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        let proxy = FloatRangeProxy {
            range_start: (range.start as f32) / (TOTAL_BUCKETS as f32),
            range_end: (range.end as f32) / (TOTAL_BUCKETS as f32),
        };

        proxy.serialize(ser)
    }

    /// Deserializes a `Range<u16>` from a floating-point range using `FloatRangeProxy`.
    /// `TOTAL_BUCKETS` is used as the upper limit of the range.
    ///
    /// The resulting range is guaranteed to have 0 <= start <= TOTAL_BUCKETS and
    /// 0 <= end <= TOTAL_BUCKETS.
    pub fn deserialize<'de, D>(des: D) -> Result<Range<u16>, D::Error>
    where
        D: Deserializer<'de>,
    {
        let proxy = FloatRangeProxy::deserialize(des)?;
        let range = Range {
            start: (proxy.range_start * (TOTAL_BUCKETS as f32)).floor() as u16,
            end: (proxy.range_end * (TOTAL_BUCKETS as f32)).floor() as u16,
        };

        Ok(range)
    }
}

/// VariantSet contains an experiment's variants, and all other fields not in common
/// with dynamic config json.
#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct VariantSet {
    pub start_ts: u64, // TODO: consider whether this should just be created_at
    pub stop_ts: u64,  // TODO: should we get rid of a version by creating a new one?
    pub shuffle_version: u32,
    #[serde(rename = "bucket_val")]
    pub bucketing_field: Option<ContextField>,
    variants: Vec<Variant>,
    holdout: Option<Box<Feature>>,
    mutex_group: Option<Box<Feature>>,
}

impl VariantSet {
    fn bucketing_string(&self, exp_id: &u32, name: &str, bucket_val: Value) -> String {
        let identifier = match bucket_val {
            // Json strings are formatted surrounded by quotes. Extract the inner value
            // to avoid this.
            Value::String(inner) => inner,
            _ => bucket_val.to_string(),
        };

        format!("{}.{}.{}{}", exp_id, name, self.shuffle_version, identifier)
    }

    fn get_bucket(&self, f: &Feature, ctx: &Context) -> Result<Choice, DeciderError> {
        let identifier = self
            .bucketing_field
            .as_ref()
            .ok_or(DeciderError::MissingBucketVal)
            .and_then(|field| {
                field
                    .get_value(ctx)
                    .ok_or_else(|| DeciderError::MissingBucketingFieldInContext(field.clone()))
            })?;

        let bucketing_string = self.bucketing_string(&f.id, &f.name, identifier);
        let bucket = self.bucket_from_str(&bucketing_string);
        let v = self.variants.iter().find(|x| x.range.contains(&bucket));
        match v {
            None => Ok(Choice::Pass("frac_avail:not in variants")),
            Some(variant) => Ok(Choice::Decided(InternalDecision {
                feature_id: f.id,
                feature_name: f.name.to_string(),
                feature_version: f.version,
                variant_name: Some(variant.name.clone()),
                value: Value::Null,
                value_type: None,
                events: Vec::from_iter(f.make_event(
                    DecisionKind::FracAvail,
                    &variant.name,
                    ctx,
                )?),
            })),
        }
    }

    fn bucket_from_str(&self, bucketing_str: &str) -> u16 {
        // FIXME: take in number of buckets as a param.
        let mut hasher = Sha1::new();
        hasher.update(bucketing_str);
        let bigint = BigUint::from_bytes_be(hasher.finalize().as_ref());

        u16::try_from(bigint % TOTAL_BUCKETS)
            .expect("bigint has max value of 1000, should fit in a u16")
    }
}

#[derive(Debug)]
enum Choice {
    // TODO: find a better nome
    Pass(&'static str),             // I didn't make a decision because...
    None,                           // response is nothing
    Continue(Vec<ExperimentEvent>), // a parent decision got called, so save its events and continue
    Decided(InternalDecision),      // an actual decision.
}

#[derive(Debug, Error)]
pub enum DeciderError {
    #[error("Feature \"{0}\" not found")]
    FeatureNotFoundWithName(String),
    #[error("Invalid feature configuration")]
    InvalidFeature,
    #[error("Missing \"bucket_val\" field in experiment config")]
    MissingBucketVal,
    #[error("Missing field \"{0}\" in context for bucket_val = {0}")]
    MissingBucketingFieldInContext(ContextField),
    #[error(
        "Requested identifier_type \"{0}\" is incompatible with experiment's bucket_val = {1}"
    )]
    IdentifierTypeBucketValMismatch(ContextField, ContextField),
    #[error("Missing variant_set")]
    MissingVariantSet,
    #[error("Dynamic Configuration Feature type mismatch")]
    DcTypeMismatch,
    #[error("Number deserialization failed")]
    NumberDeserializationError,
    #[error("Decider returned malformed event: {0}")]
    MalformedEventError(#[source] Box<dyn Error>),
}

#[derive(Debug, Error)]
pub enum DeciderInitError {
    #[error("Std io error: {0}")]
    IoError(
        #[from]
        #[source]
        std::io::Error,
    ),
    #[error("Json error: {0}")]
    SerdeError(
        #[from]
        #[source]
        serde_json::Error,
    ),
    #[error("Invalid decisionmaker: {0:?}")]
    InvalidDecisionMaker(String),
    #[error("Partially loaded Decider: {} features failed to load", .1.len())]
    PartialLoad(Decider, HashMap<String, serde_json::Error>),
}

/// An `Event` holds a hydrated exposure event, serialized as a json string, as well as an explicit
/// `DecisionKind`. The kind can be used by the client to choose whether to expose this event.
#[derive(Serialize, Debug, Clone, PartialEq, Eq)]
pub struct Event {
    pub kind: DecisionKind,

    /// A unique key for this exposure. Equivalent exposures will have the same exposure key.
    /// Clients may use this key to keep track of events that were exposed previously.
    pub exposure_key: String,

    pub json: String,
}

#[derive(Serialize, Debug, Clone, PartialEq, Eq)]
pub struct Decision {
    pub feature_id: u32,
    pub feature_name: String,
    pub feature_version: u32,
    pub variant_name: Option<String>,
    pub value: Value,
    pub value_type: Option<ValueType>,
    // TODO Remove event_data once we've migrated off of the legacy string format.
    #[serde(skip)]
    pub event_data: Vec<String>,
    pub events: Vec<Event>,
}

/// An `InternalDecision` holds the same data as a [Decision] except contains a list of
/// [ExperimentEvent] instead of hydrated strings. It's returned from the [Decisionmaker]s and
/// internal decider methods, and is converted to a `Decision` before returning from `decide`.
#[derive(Debug)]
struct InternalDecision {
    feature_id: u32,
    feature_name: String,
    feature_version: u32,
    variant_name: Option<String>,
    value: Value,
    value_type: Option<ValueType>,
    events: Vec<ExperimentEvent>,
}

type Decisionmaker = fn(d: &Decider, f: &Feature, ctx: &Context) -> Result<Choice, DeciderError>;

fn name_to_decisionmaker(name: &str) -> Result<Decisionmaker, DeciderInitError> {
    match name {
        "darkmode" => Ok(Decider::darkmode),
        "fractional_availability" => Ok(Decider::fractional_availability),
        "targeting" => Ok(Decider::targeting),
        "overrides" => Ok(Decider::overrides),
        "value" => Ok(Decider::value),
        "holdout" => Ok(Decider::holdout),
        "mutex_group" => Ok(Decider::mutex_group),
        _ => Err(DeciderInitError::InvalidDecisionMaker(format!(
            "Invalid decisionmaker name: {:?}",
            name
        ))),
    }
}

fn string_to_decisionmakers(cfg: &str) -> Result<Vec<Decisionmaker>, DeciderInitError> {
    // we get a result of a vec because we want any single error in
    // decisionmaker names to fail the whole thing (no silent errors
    // causing unexpected behavior).  Got the technique from:
    // https://stackoverflow.com/questions/26368288/how-do-i-stop-iteration-and-return-an-error-when-iteratormap-returns-a-result
    cfg.split_whitespace().map(name_to_decisionmaker).collect()
}

// This section is legacy code to deal with reddit's existing experiment format.
#[deprecated(note = "use Decider::new instead")]
pub fn init_decider<P: AsRef<Path>>(
    decisionmakers: &str,
    filepath: P,
) -> Result<Decider, DeciderInitError> {
    let file = File::open(filepath)?;
    let reader = BufReader::new(file);
    let config = serde_json::from_reader(reader)?;

    Decider::with_decisionmakers(config, decisionmakers)
}

type ExperimentConfig = HashMap<String, Experiment>;

fn experiment_config_to_features(ec: &ExperimentConfig) -> Vec<Feature> {
    ec.values()
        .map(|exp| experiment_to_feature(exp, ec))
        .collect()
}

/// An intermediate struct representing a raw experiment config. The experiments are parsed as
/// JSON values.
///
/// This struct allows us to partially load [`Decider`]. When deserializing into a specific type,
/// serde will return an error if any part of the type can't be properly deserialized. This means
/// that if we deserialize into a `HashMap<String, Experiment>`, and any key in the object is not a
/// valid experiment, the entire object is invalid.
///
/// Any valid JSON can be deserialized into a [`Value`], though. When we deserialize the input into
/// a [`RawConfig`], serde will check that:
///   - The input is a valid JSON object.
///   - Each key in the object maps to a valid JSON value.
///
/// We can then individually deserialize the [`Value`]s into [`Feature`]s, and partially load a
/// decider with all valid features.
#[derive(Debug, Clone, Deserialize)]
struct RawConfig {
    #[serde(flatten)]
    raw_experiments: HashMap<String, Value>,
}

impl RawConfig {
    /// Deserializes the raw config into a list of valid features. Any features that can't be
    /// successfully deserialized are returned in the `HashMap`.
    fn features(self) -> (Vec<Feature>, HashMap<String, serde_json::Error>) {
        let mut ec = HashMap::new();
        let mut errs = HashMap::new();

        for (name, feature_json) in self.raw_experiments {
            match serde_json::from_value::<Experiment>(feature_json) {
                Ok(exp) => {
                    ec.insert(name, exp);
                }
                Err(err) => {
                    errs.insert(name, err);
                }
            }
        }

        let features = experiment_config_to_features(&ec);

        (features, errs)
    }
}

#[derive(Deserialize, Debug, Clone)]
struct Experiment {
    id: u32,
    name: String,
    enabled: bool,
    #[allow(dead_code)] // FIXME: Remove this field?
    version: String,
    owner: String,
    #[serde(rename = "type")]
    experiment_type: ExperimentType,
    #[serde(default)]
    emit_event: bool,
    #[serde(default)]
    start_ts: u64,
    #[serde(default)]
    stop_ts: u64,
    value: Option<Value>,
    value_type: Option<ValueType>,
    parent_meg_name: Option<String>,
    parent_hg_name: Option<String>,
    experiment: InnerExperiment,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
#[serde(rename_all = "snake_case")]
pub enum ExperimentType {
    DynamicConfig,
    RangeVariant,
    FeatureRollout, // FIXME: get rid of this after the great RangeVariant takeover.
}

#[derive(Serialize, Deserialize, Debug, Clone, Copy, PartialEq, Eq)]
pub enum ValueType {
    Boolean,
    Integer,
    Float,
    #[serde(alias = "Text")] // FIXME: Remove this once we've moved to `String` in DDG.
    String,
    Map,
}

impl From<ValueType> for Value {
    fn from(value_type: ValueType) -> Self {
        match value_type {
            ValueType::Boolean => Value::Bool(false),
            ValueType::Integer => Value::from(0),
            ValueType::Float => Value::from(0.0),
            ValueType::String => Value::from(""),
            ValueType::Map => Value::Object(serde_json::Map::new()),
        }
    }
}

impl fmt::Display for ValueType {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            ValueType::Boolean => write!(f, "boolean"),
            ValueType::Integer => write!(f, "integer"),
            ValueType::Float => write!(f, "float"),
            ValueType::String => write!(f, "string"),
            ValueType::Map => write!(f, "map"),
        }
    }
}

#[derive(Deserialize, Debug, Clone)]
struct InnerExperiment {
    experiment_version: u32,
    #[serde(default)]
    variants: Vec<Variant>, // TODO: figure out how to make a variable-length array in a struct, maybe?
    #[serde(default)]
    shuffle_version: u32,
    #[serde(rename = "bucket_val")]
    bucketing_field: Option<ContextField>,
    overrides: Option<Vec<HashMap<String, TargetingTree>>>,
    targeting: Option<TargetingTree>,
}

fn experiment_to_feature(exp: &Experiment, ec: &ExperimentConfig) -> Feature {
    let holdout: Option<Box<Feature>> = match &exp.parent_hg_name {
        None => None,
        Some(name) => ec.get(name).map(|e| Box::new(experiment_to_feature(e, ec))),
    };

    let mutex_group = match &exp.parent_meg_name {
        None => None,
        Some(name) => ec.get(name).map(|e| Box::new(experiment_to_feature(e, ec))),
    };

    let variant_set = match exp.experiment_type {
        ExperimentType::DynamicConfig => None,
        _ => Some(VariantSet {
            start_ts: exp.start_ts,
            stop_ts: exp.stop_ts,
            shuffle_version: exp.experiment.shuffle_version,
            variants: exp.experiment.variants.clone(),
            bucketing_field: exp.experiment.bucketing_field.clone(),
            holdout,
            mutex_group,
        }),
    };

    Feature {
        id: exp.id,
        name: exp.name.clone(),
        enabled: exp.enabled,
        feature_type: exp.experiment_type.clone(),
        version: exp.experiment.experiment_version,
        owner: exp.owner.clone(),
        platform_bitmask: 0,
        value: exp.value.clone(),
        value_type: exp.value_type,
        emit_event: exp.emit_event,
        targeting: exp.experiment.targeting.clone(),
        overrides: exp.experiment.overrides.clone(),
        variant_set,
    }
}

#[cfg(test)]
mod tests {
    use proptest::prelude::*;
    use serde_json::json;
    use serde_json::Error;

    use super::*;

    enum Dc {
        Bool(Option<Value>),
        Int(Option<Value>),
        Float(Option<Value>),
        String(Option<Value>),
        Map(Option<String>),
    }

    fn make_feature() -> Feature {
        let v = Variant {
            name: "enabled".to_string(),
            range: 0..100,
        };
        Feature {
            id: 1,
            name: "first_feature".to_string(),
            enabled: true,
            feature_type: ExperimentType::RangeVariant,
            version: 1,
            owner: "test".to_string(),
            platform_bitmask: 0,
            emit_event: true,
            targeting: None,
            overrides: None,
            variant_set: Some(VariantSet {
                start_ts: 0,
                stop_ts: 2147483648, // 2 ** 31 - far future.
                shuffle_version: 0,
                bucketing_field: Some(ContextField::UserId),
                variants: vec![v],
                holdout: None,
                mutex_group: None,
            }),
            value: Some(Value::Null),
            value_type: None,
        }
    }

    fn make_dynamic_config(dc: Dc) -> Feature {
        let name_str: String;
        let value_type: ValueType;

        let value: Value = match dc {
            Dc::Bool(val) => {
                name_str = "bool".to_string();
                value_type = ValueType::Boolean;

                match val {
                    None => Value::Bool(true),
                    Some(b) => b,
                }
            }
            Dc::Int(val) => {
                name_str = "int".to_string();
                value_type = ValueType::Integer;

                match val {
                    None => Value::from(1),
                    Some(i) => i,
                }
            }
            Dc::Float(val) => {
                name_str = "float".to_string();
                value_type = ValueType::Float;

                match val {
                    None => Value::from(2.0),
                    Some(f) => f,
                }
            }
            Dc::String(val) => {
                name_str = "string".to_string();
                value_type = ValueType::String;

                match val {
                    None => Value::from("some_string"),
                    Some(s) => s,
                }
            }
            Dc::Map(val) => {
                name_str = "map".to_string();
                value_type = ValueType::Map;

                match &val {
                    None => {
                        json!({"v":{"nested_map": {"w":false,"x": 1,"y":"some_string","z":3.0}},"w":false,"x": 1,"y":"some_string","z":3.0})
                    }
                    Some(s) => serde_json::from_str(s).unwrap(),
                }
            }
        };

        Feature {
            id: 2,
            name: name_str + "_dynamic_config",
            enabled: true,
            feature_type: ExperimentType::DynamicConfig,
            version: 1,
            owner: "test".to_string(),
            emit_event: true,
            value: Some(value),
            value_type: Some(value_type),
            targeting: None,
            overrides: None,
            platform_bitmask: 0,
            variant_set: None,
        }
    }

    fn make_experiment(name: String, meg: Option<String>, hg: Option<String>) -> Experiment {
        let c = Variant {
            name: "control".to_string(),
            range: 900..1000,
        };
        let t = Variant {
            name: "treatment".to_string(),
            range: 0..100,
        };
        Experiment {
            id: 1,
            name,
            experiment_type: ExperimentType::RangeVariant,
            enabled: true,
            owner: "test".to_string(),
            emit_event: true,
            start_ts: 0,
            stop_ts: 2147483648, // 2 ** 31 - far future.
            version: "1".to_string(),
            experiment: InnerExperiment {
                shuffle_version: 0,
                variants: vec![t, c],
                bucketing_field: Some(ContextField::UserId),
                experiment_version: 1,
                targeting: None,
                overrides: None,
            },
            parent_hg_name: hg,
            parent_meg_name: meg,
            value: None,
            value_type: None,
        }
    }

    fn make_ctx(json: Option<String>) -> Result<Context, Error> {
        let c = Context {
            user_id: Some("795244".to_string()),
            locale: Some("US".to_string()),
            ..Context::default()
        };
        match json {
            None => Ok(c),
            Some(s) => serde_json::from_str(&s),
        }
    }

    fn make_tt(json: String) -> TargetingTree {
        serde_json::from_str(&json).unwrap()
    }

    #[test]
    fn parse_targeting_tree() {
        let tt1 = make_tt(r#"{"EQ": {"field": "user_id", "values": ["795244"]}}"#.to_string());
        let tt2 = make_tt(r#"{"EQ": {"field": "user_id", "value": "795244"}}"#.to_string());
        let tt3 = make_tt(r#"{"NE": {"field": "user_id", "value": "795244"}}"#.to_string());
        let tt4 = make_tt(r#"{"GT": {"field": "user_id", "value": 7}}"#.to_string());
        let tt5 = make_tt(r#"{"LT": {"field": "user_id", "value": 8}}"#.to_string());
        let tt6 = make_tt(r#"{"GE": {"field": "user_id", "value": 8}}"#.to_string());
        let tt7 = make_tt(r#"{"LE": {"field": "user_id", "value": 8}}"#.to_string());
        let tt8 = make_tt(r#"{"ALL": [{"EQ": {"field": "user_id", "value": 7}}]}"#.to_string());
        let tt9 = make_tt(r#"{"ALL": [{"EQ": {"field": "user_id", "value": "7"}}]}"#.to_string());
        let imp = make_tt(r#"{"ALL": [{"EQ": {"field": "user_id", "value": "7"}},{"EQ": {"field": "user_id", "value": "8"}}]}"#.to_string());
        let _big = make_tt(
            r#"{"ALL": [
          {"EQ": {"field": "country_code","values": ["DE"]}},
          {"ANY": [
              {"ALL": [
                  {"EQ": {"field": "app_name","value": "ios"}},
                  {"GE": {"field": "build_number","value": 307593}}
                ]
              },
              {"EQ": {"field": "app_name","value": "android"}}
            ]
          }
        ]
      }"#
            .to_string(),
        );

        let ctx1 = make_ctx(None).unwrap();
        let ctx2: Context = make_ctx(Some(r#"{"user_id": "7"}"#.to_string())).unwrap();
        let _ctx3: Context = make_ctx(Some(
            json!({"user_id": "9",
                   "user_is_employee": false,
                   "country_code": "DE",
                   "app_name": "android",
                   "build_number": 312024,
                   "logged_in": true,
            })
            .to_string(),
        ))
        .unwrap();

        assert!(tt1.eval(&ctx1).unwrap()); // ctx1 has user_id 795244, so EQ passes
        assert!(!tt1.eval(&ctx2).unwrap()); // ctx2 has user_id 7, so EQ fails
        assert!(tt2.eval(&ctx1).unwrap()); // tt1 and tt2 are the same, just different representations
        assert!(!tt2.eval(&ctx2).unwrap()); // so should have same results

        assert!(!tt3.eval(&ctx1).unwrap()); // ctx has user_id 795244, so NE against 795244 fails
        assert!(tt3.eval(&ctx2).unwrap()); // ctx2 has user_id 7, so NE against 7 passes

        assert!(tt4.eval(&ctx1).unwrap()); // ctx has user_id 795244, so GT against 7 passes
        assert!(!tt4.eval(&ctx2).unwrap()); // ctx2 has user_id 7, so GT against 7 fails

        assert!(!tt5.eval(&ctx1).unwrap()); // ctx has user_id 795244, so LT against 8 passes
        assert!(tt5.eval(&ctx2).unwrap()); // ctx2 has user_id 7, so LT against 8 fails

        assert!(tt6.eval(&ctx1).unwrap()); // ctx has user_id 795244, so GE against 8 passes
        assert!(!tt6.eval(&ctx2).unwrap()); // ctx2 has user_id 7, so GE against 8 fails

        assert!(!tt7.eval(&ctx1).unwrap()); // ctx has user_id 795244, so LE against 8 fails
        assert!(tt7.eval(&ctx2).unwrap()); // ctx2 has user_id 7, so LE against 8 passes

        // test {ALL: [{user_id: "7"} ]}
        assert!(!tt8.eval(&ctx1).unwrap()); // ctx1 has user_id 795244, so EQ fails, so ALL fails
        assert!(tt8.eval(&ctx2).unwrap()); // ctx2 has user_id 7, so EQ passes, so ALL passes

        // same as above, but literal int rather than string
        assert!(!tt9.eval(&ctx1).unwrap()); // ctx1 has user_id 795244, so EQ fails, so ALL fails
        assert!(tt9.eval(&ctx2).unwrap()); // ctx2 has user_id 7, so EQ passes, so ALL passes

        // an impossible targeting tree that asks us to have 2 different user_ids at once.
        assert!(!imp.eval(&ctx1).unwrap()); // ctx1 has user_id 795244, so both EQs fail
        assert!(!imp.eval(&ctx2).unwrap()); // ctx1 has user_id 7, so second EQ fails
    }

    fn build_decider(
        cfgo: Option<String>,
        fvo: Option<Vec<Feature>>,
        dcvo: Option<Vec<Feature>>,
    ) -> Result<Decider, DeciderInitError> {
        let mut fv = match fvo {
            None => vec![make_feature()],
            Some(fv) => fv,
        };
        let dcv = match dcvo {
            None => vec![
                make_dynamic_config(Dc::Bool(None)),
                make_dynamic_config(Dc::Int(None)),
                make_dynamic_config(Dc::Float(None)),
                make_dynamic_config(Dc::String(None)),
                make_dynamic_config(Dc::Map(None)),
            ],
            Some(dc) => dc,
        };
        let cfg = match cfgo {
            Some(s) => s,
            None => "darkmode".to_string(), // set a reasonable default here?
        };

        fv.extend(dcv);

        fv.sort_by_key(|f| f.name.clone());
        string_to_decisionmakers(&cfg).map(|decisionmakers| Decider {
            features: fv,
            decisionmakers,
        })
    }

    #[test]
    fn decider_initialization_works() -> Result<(), DeciderInitError> {
        let ctx = make_ctx(None)?;
        let d = build_decider(None, None, None)?;
        assert!(d.choose("first_feature", &ctx, None).is_ok());
        Ok(())
    }

    #[test]
    fn decider_errors_on_missing_name() -> Result<(), DeciderInitError> {
        let ctx = make_ctx(None)?;
        let d = build_decider(None, None, None)?;
        let r = d.choose("missing", &ctx, None);
        match r {
            Ok(_) => panic!(),
            Err(e) => println!("got expected error: {:#?}", e),
        }
        Ok(())
    }

    #[test]
    fn test_name_to_decisionmaker() {
        name_to_decisionmaker("darkmode").unwrap();
        name_to_decisionmaker("fractional_availability").unwrap();
        name_to_decisionmaker("value").unwrap();
        name_to_decisionmaker("overrides").unwrap();
        name_to_decisionmaker("targeting").unwrap();

        let res = name_to_decisionmaker("bad-shouldbreak");
        assert!(res.is_err());
    }

    proptest! {
        #[test]
        fn init_decider_doesnt_crash(s in "\\PC*") {
            #[allow(deprecated)] // testing deprecated function
            let res = init_decider(&s, "../cfgsmall.json");
            match res {
                Ok(d) => println!("success: {:#?}", d),
                Err(e) => println!("error: {:#?}", e),
            }
        }

        #[test]
        fn no_user_id_can_pass_impossible_tt(i in 10..1000000000u64 ) {
            let v = json!({"user_id": i.to_string()});
            let imp = make_tt(r#"{"ALL": [{"EQ": {"field": "user_id", "value": "7"}},{"EQ": {"field": "user_id", "value": "8"}}]}"#.to_string());
            let ctx: Context = make_ctx(Some(v.to_string()))?;

            assert!(!imp.eval(&ctx).unwrap());
        }

        #[test]
        fn test_meg_hg_invariants(i in 1..1000000000u64) {
            let d = Decider::new("../test.json").unwrap();

            let ctx: Context = make_ctx(
                Some(json!({"user_id": i.to_string()}).to_string())
            ).unwrap();

            // let's get all 4 test features bucketed, and out of their Results
            let hghalf = d.choose("hghalf", &ctx, None).unwrap();
            let meg2way = d.choose("meg2way", &ctx, None).unwrap();
            let e1 = d.choose("e1", &ctx, None).unwrap();
            let e2 = d.choose("e2", &ctx, None).unwrap();

            match (massage_holdout(hghalf), meg2way.variant_name) {
                // If you're in the holdout, you don't get any experiments
                ((Some(true), _), _) => both_no_name(e1, e2),
                // Regardless of what's going on in the holdout, if the MEG
                // doesn't give any results, both decisions should have name=None
                (_, None) => both_no_name(e1, e2),
                (_, Some(mgv)) => one_off_one_on(e1, e2, mgv),
            }
        }

        #[test]
        fn test_overrides(i in 6..1000000000u64) {
            let d = Decider::new("../test.json").unwrap();
            let ctx1: Context = make_ctx(Some(
                json!({"user_id": (i * 10).to_string(), "user_is_employee": true}).to_string(),
            )).unwrap();

            let ctx2: Context = make_ctx(Some(
                json!({"user_id": (i * 10 + 1).to_string(),
                       "user_is_employee": false,
                       "country_code": "DE",
                       "app_name": "android",
                       "build_number": 312024,
                       "logged_in": true,
                }).to_string(),
            )).unwrap();

            let ctx3: Context = make_ctx(Some(
                json!({"user_id": (i * 10 + 2).to_string()}).to_string(),
            )).unwrap();

            let ctx4: Context = make_ctx(Some(
                json!({"user_id": (i * 10 + 3).to_string(),
                       "user_is_employee": false,
                       "country_code": "DE",
                       "app_name": "android",
                       "build_number": 312024,
                       "logged_in": true,
                }).to_string(),
            )).unwrap();

            println!("test 1");
            // ctx1 is an employee, so it'll get overridden into control in fancy, and never see holdout/meg
            let control = d.choose("fancy", &ctx1, None).unwrap();
            assert_eq!(control.variant_name, Some("control".to_string()));
            assert_eq!(control.feature_id, 1);
            assert_eq!(control.feature_name, *"fancy");
            assert_eq!(control.feature_version, 4);
            assert_eq!(control.event_data, vec![format!("1::::1::::fancy::::4::::control::::{}::::user_id::::0::::9668199193::::test", i * 10)]);
            assert_eq!(control.events[0].kind, DecisionKind::Override);
            // Json serialization is tested independently. Here we just check that we returned some valid json.
            assert!(serde_json::from_str::<Value>(&control.events[0].json).is_ok());

            let x1 = d.choose("hg", &ctx2, None).unwrap();
            assert_eq!(x1.variant_name, Some("control_1".to_string()));
            assert_eq!(x1.feature_id, 2);
            assert_eq!(x1.feature_name, *"hg");
            assert_eq!(x1.feature_version, 5);
            assert_eq!(x1.event_data, vec![format!("1::::2::::hg::::5::::control_1::::{}::::user_id::::0::::9668199193::::test", i * 10 + 1)]);
            assert_eq!(x1.events[0].kind, DecisionKind::Override);
            assert!(serde_json::from_str::<Value>(&x1.events[0].json).is_ok());

            let x2 = d.choose("meg", &ctx2, None).unwrap();
            assert_eq!(x2.variant_name, Some("fancy".to_string()));
            assert_eq!(x2.feature_id, 3);
            assert_eq!(x2.feature_name, *"meg");
            assert_eq!(x2.feature_version, 7);
            // MEGs don't fire exposures since `emit_event` is false in test.json config
            let empty_vec: Vec<String> = vec![];
            assert_eq!(x2.event_data, empty_vec);
            assert!(x2.events.is_empty());

            println!("test 2");
            // ctx2 employee=false, so in fancy, "none_hit"s the overrides, passes targeting, goes to holdout-is in control(gets experiments).
            // Passes to the meg, it gets "fancy" treatment, which means it is eligible for this experiment, and gets frac_avail in enabled
            let exp1 = d.choose("fancy", &ctx2, None).unwrap();
            assert_eq!(exp1.variant_name, Some("exp1".to_string()));
            assert_eq!(exp1.feature_id, 1);
            assert_eq!(exp1.feature_name, *"fancy");
            assert_eq!(exp1.feature_version, 4);
            println!("exp1.event_data={:#?}", exp1.event_data);
            assert_eq!(exp1.event_data, vec![
                format!("2::::2::::hg::::5::::control_1::::{}::::user_id::::0::::9668199193::::test", i * 10 + 1),
                format!("0::::1::::fancy::::4::::exp1::::{}::::user_id::::0::::9668199193::::test", i * 10 + 1),
            ]);
            assert_eq!(exp1.events.len(), 2);
            assert_eq!(exp1.events[0].kind, DecisionKind::Holdout);
            assert_eq!(exp1.events[1].kind, DecisionKind::FracAvail);
            for event in exp1.events {
                assert!(serde_json::from_str::<Value>(&event.json).is_ok());
            }


            println!("test 3");
            // ctx3 isn't an employee, so misses overrides, and fails targeting, so gets the default decision.
            let decision = d.choose("fancy", &ctx3, None).unwrap();
            assert_eq!(decision, Decision {
                feature_id: 1,
                feature_name: "fancy".to_string(),
                feature_version: 4,
                variant_name: None,
                value: Value::Null,
                value_type: None,
                event_data: Vec::new(),
                events: Vec::new(),
            });

            println!("test 4");
            // ctx4 employee=false, so in fancy, "none_hit"s the overrides,
            // passes targeting, goes to holdout-is in control(gets
            // experiments). Passes to the meg, it misses overrides and gets
            // frac_avail'd into the "fancy" treatment, which means it is
            // allowed into the "fancy" experiment, which in turn means it gets
            // bucketed.
            let fancy = d.choose("fancy", &ctx4, None).unwrap();
            println!("fancy={:#?}", fancy);
            assert_eq!(fancy.variant_name, Some("exp1".to_string()));
            assert_eq!(fancy.feature_id, 1);
            assert_eq!(fancy.feature_name, *"fancy");
            assert_eq!(fancy.feature_version, 4);
            assert_eq!(fancy.event_data, vec![
                format!("2::::2::::hg::::5::::control_1::::{}::::user_id::::0::::9668199193::::test", i * 10 + 3),
                format!("0::::1::::fancy::::4::::exp1::::{}::::user_id::::0::::9668199193::::test", i * 10 + 3),
            ]);
            assert_eq!(fancy.events.len(), 2);
            assert_eq!(fancy.events[0].kind, DecisionKind::Holdout);
            assert_eq!(fancy.events[1].kind, DecisionKind::FracAvail);
            for event in fancy.events {
                assert!(serde_json::from_str::<Value>(&event.json).is_ok());
            }
        }

        fn test_choose_with_optional_identifier_type(i in 0..1000000000u64) {
            let d = Decider::new("../test.json").unwrap();

            // test custom bucketing field arg
            let ctx: Context = make_ctx(Some(
                json!({"canonical_url": i.to_string()}).to_string(),
            )).unwrap();

            println!("test 1");
            // specify `bucketing_field_opt` that matches `bucket_val` of experiment's config
            let c_exp = d.choose("canonical_url_exp", &ctx, Some(ContextField::CanonicalUrl)).unwrap();
            assert_eq!(c_exp.variant_name, Some("enabled".to_string()));
            assert_eq!(c_exp.feature_id, 999);
            assert_eq!(c_exp.feature_name, *"canonical_url_exp");
            assert_eq!(c_exp.feature_version, 8);
            assert_eq!(c_exp.event_data, vec![format!("0::::999::::canonical_url_exp::::8::::enabled::::{}::::canonical_url::::0::::9668199193::::test", i * 10)]);
            assert_eq!(c_exp.events[0].kind, DecisionKind::FracAvail);
            assert!(serde_json::from_str::<Value>(&c_exp.events[0].json).is_ok());

            println!("test 2");
            // specify bucketing_field_opt that does not match experiment's bucket_val
            let err_res = d.choose("canonical_url_exp", &ctx, Some(ContextField::DeviceId));
            assert!(matches!(err_res, Err(DeciderError::IdentifierTypeBucketValMismatch(_,_))));
        }

        #[test]
        fn test_choose_all(i in 0..1000000000u64) {
            let filepath = "../test.json";
            let d = Decider::new(filepath).unwrap();
            let ctx: Context = make_ctx(Some(
                json!({"user_id": i.to_string(), "canonical_url": i.to_string()}).to_string(),
            )).unwrap();

            let file = File::open(filepath)?;
            let reader = BufReader::new(file);
            let ec: ExperimentConfig = serde_json::from_reader(reader)?;
            let hm = d.choose_all(&ctx, None);
            // TODO: come up with something smarter to test here.
            for (k, v) in hm {
                match v {
                    Err(_) => panic!(), // We shouldn't see any errors
                    Ok(d) => { // if a decision has a name, must be from the variant names.
                        if let Some(name) = d.variant_name { // IFF we got a decision, the names should match.
                            let exp_conf = ec.get(&k).unwrap();
                            assert!(exp_conf.experiment.variants.iter().any(|f| f.name == name));
                            assert_eq!(exp_conf.id, d.feature_id);
                            assert_eq!(exp_conf.experiment.experiment_version, d.feature_version);
                            assert_eq!(exp_conf.name, d.feature_name);

                        }
                    }
                }
            }

            // test bucketing_field_opt arg
            let ctx1: Context = make_ctx(Some(
                json!({"canonical_url": i.to_string()}).to_string(),
            )).unwrap();

            println!("test 1");
            // retrieve the only `canonical_url` experiment
            let hm = d.choose_all(&ctx1, Some(ContextField::CanonicalUrl));
            let c_exp = &hm["canonical_url_exp"].as_ref().unwrap();
            assert_eq!(hm.len(), 1);
            assert_eq!(*(c_exp.variant_name.as_ref().unwrap()),  *"enabled");
            assert_eq!(c_exp.feature_name, *"canonical_url_exp");
            assert_eq!(c_exp.feature_id, 999);
            assert_eq!(c_exp.feature_version, 8);

            println!("test 2");
            // `bucketing_field_opt`/`bucket_val` does not match any identifier in ctx
            let ctx2: Context = make_ctx(Some(
                json!({"device_id": i.to_string()}).to_string(),
            )).unwrap();

            let hm = d.choose_all(&ctx2, Some(ContextField::CanonicalUrl));
            assert_eq!(hm.len(), 1);

            let err = &hm["canonical_url_exp"];
            match err {
                Ok(_) => panic!(),
                Err(e) => assert!(matches!(e, DeciderError::MissingBucketingFieldInContext(_))),
            }

            println!("test 4");
            // get empty list since no `device_id` experiments exist in test.json
            let hm = d.choose_all(&ctx, Some(ContextField::DeviceId));
            assert!(hm.is_empty());
        }
    }

    fn massage_holdout(hg: Decision) -> (Option<bool>, Vec<String>) {
        let Decision {
            variant_name: n,
            event_data: ed,
            ..
        } = hg;
        (Some(n == Some("holdout".to_string())), ed)
    }

    fn both_no_name(e1: Decision, e2: Decision) {
        assert!(e1.variant_name.is_none());
        assert!(e2.variant_name.is_none());
    }

    fn one_off_one_on(e1: Decision, e2: Decision, expected_variant: String) {
        // This function is highly specific: it depends on being called with
        // e1 == choose("e1") and e2 == choose("e2")
        match e1.variant_name {
            None => {
                assert_eq!(expected_variant, "e2".to_string());
                assert_eq!(e2.variant_name, Some("e2treat".to_string()));
            }
            Some(variant_name) => {
                assert_eq!(expected_variant, "e1".to_string());
                assert_eq!(variant_name, "e1treat".to_string());
            }
        }
    }

    #[test]
    fn test_init_decider() {
        #[allow(deprecated)] // testing deprecated function
        init_decider(
            "darkmode overrides targeting fractional_availability value",
            "../cfg.json",
        )
        .unwrap();
    }

    fn check_default_decisionmakers(decider: &Decider) {
        let decisionmakers: Vec<Decisionmaker> = vec![
            Decider::darkmode,
            Decider::overrides,
            Decider::targeting,
            Decider::holdout,
            Decider::mutex_group,
            Decider::fractional_availability,
            Decider::value,
        ];

        check_decisionmakers(decider, decisionmakers);
    }

    fn check_decisionmakers(decider: &Decider, decisionmakers: Vec<Decisionmaker>) {
        // decisionmakers are function pointers, so we can compare their addresses.
        let expected_ptrs: Vec<_> = decisionmakers.iter().map(|dm| *dm as usize).collect();
        let actual_ptrs: Vec<_> = decider
            .decisionmakers
            .iter()
            .map(|dm| *dm as usize)
            .collect();

        for (idx, &expected_ptr) in expected_ptrs.iter().enumerate() {
            assert_eq!(expected_ptr, actual_ptrs[idx]);
        }
    }

    #[test]
    fn test_decider_new() {
        let decider = Decider::new("../cfg.json").unwrap();
        check_default_decisionmakers(&decider);
    }

    #[test]
    fn test_decider_from_bytes() {
        let file = File::open("../cfg.json").unwrap();
        let decider = Decider::from_bytes(file).unwrap();
        check_default_decisionmakers(&decider);
    }

    #[test]
    fn test_with_decisionmakers() {
        // This should probably be a proptest, but getting proptest to generate function pointers
        // is really hard.
        let decisionmakers: Vec<Decisionmaker> = vec![
            Decider::fractional_availability,
            Decider::mutex_group,
            Decider::darkmode,
        ];

        let file = File::open("../cfg.json").unwrap();
        let value: Value = serde_json::from_reader(file).unwrap();
        let decider =
            Decider::with_decisionmakers(value, "fractional_availability mutex_group darkmode")
                .unwrap();

        check_decisionmakers(&decider, decisionmakers);
    }

    #[test]
    fn holdout_meg_parsing() -> Result<(), DeciderError> {
        let e1 = make_experiment(
            "first".to_string(),
            Some("meg".to_string()),
            Some("hg".to_string()),
        );
        let e2 = make_experiment(
            "second".to_string(),
            Some("meg_missing".to_string()),
            Some("hg".to_string()),
        );
        let meg = make_experiment("meg".to_string(), None, None);
        let hg = make_experiment("hg".to_string(), None, None);
        let ec: ExperimentConfig = HashMap::from([
            ("first".to_string(), e1),
            ("second".to_string(), e2),
            ("meg".to_string(), meg),
            ("hg".to_string(), hg),
        ]);

        let fv: Vec<Feature> = experiment_config_to_features(&ec);
        let f1 = fv.iter().find(|&f| f.name == "first").unwrap();
        let f2 = fv.iter().find(|&f| f.name == "second").unwrap();
        let fmeg = fv.iter().find(|&f| f.name == "meg").unwrap();
        let fhg = fv.iter().find(|&f| f.name == "hg").unwrap();
        assert_eq!(get_fp(f1, FeatureParent::Holdout).unwrap().name, fhg.name);
        assert_eq!(get_fp(f1, FeatureParent::Meg).unwrap().name, fmeg.name);
        assert!(get_fp(f2, FeatureParent::Meg).is_err());
        assert_eq!(get_fp(f2, FeatureParent::Holdout).unwrap().name, fhg.name);
        assert!(get_fp(fmeg, FeatureParent::Holdout).is_err());
        assert!(get_fp(fmeg, FeatureParent::Meg).is_err());
        assert!(get_fp(fhg, FeatureParent::Holdout).is_err());
        assert!(get_fp(fhg, FeatureParent::Meg).is_err());
        Ok(())
    }

    #[test]
    fn test_bucket_by_arbitrary_field() {
        let decider = Decider::new("../cfgsmall.json").unwrap();

        let ctx = Context {
            other_fields: Some(HashMap::from([(
                "arbitrary_id".to_string(),
                Value::String("t5_1".to_string()),
            )])),
            ..Context::default()
        };

        let decision = decider.choose("arbitrary_id_exp", &ctx, None).unwrap();
        assert_eq!("enabled", decision.variant_name.unwrap());

        let ctx = Context {
            other_fields: Some(HashMap::from([(
                "arbitrary_id".to_string(),
                Value::String("t5_10".to_string()),
            )])),
            ..Context::default()
        };

        let decision = decider.choose("arbitrary_id_exp", &ctx, None).unwrap();
        assert_eq!("control_1", decision.variant_name.unwrap());
    }

    #[test]
    fn test_bucket_by_subreddit_id() {
        let decider = Decider::new("../cfgsmall.json").unwrap();

        let ctx = Context {
            subreddit_id: Some("t5_1".to_string()),
            ..Context::default()
        };

        let decision = decider.choose("subreddit_id_exp", &ctx, None).unwrap();
        assert_eq!("enabled", decision.variant_name.unwrap());

        let ctx = Context {
            subreddit_id: Some("t5_5".to_string()),
            ..Context::default()
        };

        let decision = decider.choose("subreddit_id_exp", &ctx, None).unwrap();
        assert_eq!("control_1", decision.variant_name.unwrap());
    }

    enum FeatureParent {
        Meg,
        Holdout,
    }

    fn get_fp(f: &Feature, fp: FeatureParent) -> Result<Feature, ()> {
        // grab the specified feature_parent(holdout or meg) from a feature, or err trying.
        if let Some(variant_set) = &f.variant_set {
            let fpo = match fp {
                FeatureParent::Meg => variant_set.mutex_group.clone(),
                FeatureParent::Holdout => variant_set.holdout.clone(),
            };
            match fpo {
                None => Err(()),
                Some(feature_parent) => Ok(*feature_parent),
            }
        } else {
            Err(())
        }
    }

    #[test]
    fn get_bool_works() -> Result<(), DeciderInitError> {
        let ctx = make_ctx(None)?;
        let d = build_decider(
            Some("darkmode fractional_availability value".to_string()),
            None,
            None,
        )?;

        if let Ok(true) = d.get_bool("bool_dynamic_config", &ctx) {
            println!("got expected boolean: true");
        } else {
            panic!();
        }

        Ok(())
    }

    #[test]
    fn get_bool_errors_on_missing_name() -> Result<(), DeciderInitError> {
        let ctx = make_ctx(None)?;
        let d = build_decider(
            Some("darkmode fractional_availability value".to_string()),
            None,
            None,
        )?;
        let r = d.get_bool("missing", &ctx);
        match r {
            Ok(_) => panic!(),
            Err(e) => println!("got expected error: {:#?}", e),
        }
        Ok(())
    }

    #[test]
    fn get_int_works() -> Result<(), DeciderInitError> {
        let ctx = make_ctx(None)?;
        let d = build_decider(
            Some("darkmode fractional_availability value".to_string()),
            None,
            None,
        )?;
        let dc_res = d.get_int("int_dynamic_config", &ctx);
        match dc_res {
            Ok(res) => {
                if res == 1 {
                    println!("got expected int: {:#?}", res)
                } else {
                    panic!()
                }
            }
            _ => panic!(),
        }

        Ok(())
    }

    #[test]
    fn get_int_errors_on_missing_name() -> Result<(), DeciderInitError> {
        let ctx = make_ctx(None)?;
        let d = build_decider(
            Some("darkmode fractional_availability value".to_string()),
            None,
            None,
        )?;
        let r = d.get_int("missing", &ctx);
        match r {
            Ok(_) => panic!(),
            Err(e) => println!("got expected error: {:#?}", e),
        }
        Ok(())
    }

    #[test]
    fn get_float_works() -> Result<(), DeciderInitError> {
        let ctx = make_ctx(None)?;
        let d = build_decider(
            Some("darkmode fractional_availability value".to_string()),
            None,
            None,
        )?;
        let dc_res = d.get_float("float_dynamic_config", &ctx);
        match dc_res {
            Ok(res) => {
                if res == 2.0 {
                    println!("got expected float: {:#?}", res)
                } else {
                    panic!()
                }
            }
            _ => panic!(),
        }

        Ok(())
    }

    #[test]
    fn get_float_errors_on_missing_name() -> Result<(), DeciderInitError> {
        let ctx = make_ctx(None)?;
        let d = build_decider(
            Some("darkmode fractional_availability value".to_string()),
            None,
            None,
        )?;
        let r = d.get_float("missing", &ctx);
        match r {
            Ok(_) => panic!(),
            Err(e) => println!("got expected error: {:#?}", e),
        }
        Ok(())
    }

    #[test]
    fn get_string_works() -> Result<(), DeciderInitError> {
        let ctx = make_ctx(None)?;
        let d = build_decider(
            Some("darkmode fractional_availability value".to_string()),
            None,
            None,
        )?;
        let dc_res = d.get_string("string_dynamic_config", &ctx);
        match dc_res {
            Ok(res) => {
                if res == "some_string" {
                    println!("got expected string: {:#?}", res)
                } else {
                    panic!()
                }
            }
            _ => panic!(),
        }

        Ok(())
    }

    #[test]
    fn get_string_errors_on_missing_name() -> Result<(), DeciderInitError> {
        let ctx = make_ctx(None)?;
        let d = build_decider(
            Some("darkmode fractional_availability value".to_string()),
            None,
            None,
        )?;
        let r = d.get_string("missing", &ctx);
        match r {
            Ok(_) => panic!(),
            Err(e) => println!("got expected error: {:#?}", e),
        }
        Ok(())
    }

    #[test]
    fn get_string_with_alias_works() {
        let text_dc = json!({
            "text_dc": {
              "id": 1234,
              "value": "some_string",
              "type": "dynamic_config",
              "version": "1",
              "enabled": true,
              "owner": "test",
              "name": "text_dc",
              "value_type": "Text", // <--
              "experiment": {
                "experiment_version": 1
              }
            },
        });

        let json_str = serde_json::to_string(&text_dc).unwrap();
        let json_bytes = json_str.as_bytes();
        let decider = Decider::from_bytes(json_bytes).unwrap();

        let value = decider.get_string("text_dc", &Context::default()).unwrap();
        assert_eq!("some_string", &value);
    }

    #[test]
    fn get_map_works() -> Result<(), DeciderInitError> {
        let ctx = make_ctx(None)?;
        let map_dc_str = r#"{"v":{"nested_map": {"w":false,"x": 1,"y":"some_string","z":3.0}},"w":false,"x": 1,"y":"some_string","z":3.0}"#;
        let d = build_decider(
            Some("darkmode fractional_availability value".to_string()),
            None,
            Some(vec![make_dynamic_config(Dc::Map(Some(
                map_dc_str.to_string(),
            )))]),
        )?;
        let map = serde_json::from_str(map_dc_str).unwrap();
        let dc_res = d.get_map("map_dynamic_config", &ctx);
        match dc_res {
            Ok(res) => {
                if res == map {
                    println!("got expected map: {:#?}", res)
                } else {
                    panic!()
                }
            }
            _ => panic!(),
        }

        Ok(())
    }

    #[test]
    fn get_map_errors_on_missing_name() -> Result<(), DeciderInitError> {
        let ctx = make_ctx(None)?;
        let d = build_decider(
            Some("darkmode fractional_availability value".to_string()),
            None,
            None,
        )?;
        let r = d.get_map("missing", &ctx);
        match r {
            Ok(_) => panic!(),
            Err(e) => println!("got expected error: {:#?}", e),
        }
        Ok(())
    }

    #[test]
    fn get_all_values_works() -> Result<(), DeciderInitError> {
        let ctx = make_ctx(None)?;
        let d = build_decider(
            Some("darkmode fractional_availability value".to_string()),
            None,
            None,
        )?;
        let all_val_res = d.get_all_values(&ctx);
        match all_val_res {
            Ok(res) => {
                if res.len() == 5 {
                    println!("got expected number of DCs")
                } else {
                    panic!()
                }
            }
            _ => panic!(),
        }

        Ok(())
    }

    #[test]
    fn test_value_eq() -> Result<(), String> {
        let v = json!({
            "s": "a string",
            "s2": "a string",
            "sn": "7",
            "snn": "-7",
            "n": 7i64,
            "nn": -7i64,
            "flt": 7.0f64,
            "fltn": -7.0f64,
            "bt1": true,
            "bt2": true,
            "bf": false,
            "bf2": false,
            "a": ["1", "2"],
            "o": {"a": 7i64}});

        // these comparisons are sensible enough...
        assert!(value_eq(&v["n"].clone(), &v["n"].clone()).unwrap());
        assert!(value_eq(&v["s"].clone(), &v["s"].clone()).unwrap());
        assert!(value_eq(&v["s"].clone(), &v["s2"].clone()).unwrap());
        assert!(value_eq(&v["bf"].clone(), &v["bf2"].clone()).unwrap());
        assert!(value_eq(&v["sn"].clone(), &v["n"].clone()).unwrap());
        assert!(value_eq(&v["n"].clone(), &v["sn"].clone()).unwrap());
        assert!(value_eq(&v["n"].clone(), &v["flt"].clone()).unwrap());
        assert!(value_eq(&v["nn"].clone(), &v["snn"].clone()).unwrap());
        assert!(value_eq(&v["bt1"].clone(), &v["bt2"].clone()).unwrap());
        assert!(value_eq(&v["fltn"].clone(), &v["snn"].clone()).unwrap());
        assert!(value_eq(&v["fltn"].clone(), &v["nn"].clone()).unwrap());
        assert!(value_eq(&v["snn"].clone(), &v["fltn"].clone()).unwrap());

        // ...if sometimes false...
        assert!(!value_eq(&v["sn"].clone(), &v["s2"].clone()).unwrap());
        assert!(!value_eq(&v["n"].clone(), &v["s"].clone()).unwrap());
        assert!(!value_eq(&v["bt"].clone(), &v["bf"].clone()).unwrap());
        assert!(!value_eq(&v["n"].clone(), &v["nn"].clone()).unwrap());
        assert!(!value_eq(&v["flt"].clone(), &v["fltn"].clone()).unwrap());

        // but here lies madness
        assert!(value_eq(&v["n"].clone(), &v["tb"].clone()).is_none());
        assert!(value_eq(&v["n"].clone(), &v["a"].clone()).is_none());
        assert!(value_eq(&v["a"].clone(), &v["o"].clone()).is_none());
        assert!(value_eq(&v["a"].clone(), &v["a"].clone()).is_none());
        Ok(())
    }

    #[test]
    fn test_get_variants_basic() {
        let decider = Decider::new("../test.json").unwrap();

        let feature = decider.feature_by_name("canonical_url_exp").unwrap();
        let expected_variants = vec![
            Variant {
                name: "enabled".to_string(),
                range: 0..1000,
            },
            Variant {
                name: "control_1".to_string(),
                range: 0..0,
            },
        ];

        let actual_variants = feature.get_variants();

        assert_eq!(expected_variants.len(), actual_variants.len());
        assert!(expected_variants
            .iter()
            .all(|item| actual_variants.contains(item)));
    }

    #[test]
    fn test_get_variants_group() {
        let decider = Decider::new("../test.json").unwrap();

        let expected_variants_map = HashMap::from([
            (
                "meg2way",
                vec![
                    Variant {
                        name: "e1".to_string(),
                        range: 0..400,
                    },
                    Variant {
                        name: "e2".to_string(),
                        range: 600..1000,
                    },
                ],
            ),
            (
                "e1",
                vec![
                    Variant {
                        name: "e1treat".to_string(),
                        range: 0..1000,
                    },
                    Variant {
                        name: "control_1".to_string(),
                        range: 0..0,
                    },
                ],
            ),
            (
                "e2",
                vec![
                    Variant {
                        name: "e2treat".to_string(),
                        range: 0..1000,
                    },
                    Variant {
                        name: "control_1".to_string(),
                        range: 0..0,
                    },
                ],
            ),
        ]);

        let features = vec![
            decider.feature_by_name("meg2way").unwrap(),
            decider.feature_by_name("e1").unwrap(),
            decider.feature_by_name("e2").unwrap(),
        ];

        features.iter().for_each(|feature| {
            let expected_variants = expected_variants_map.get(feature.name.as_str()).unwrap();
            let actual_variants = feature.get_variants();

            assert_eq!(expected_variants.len(), actual_variants.len());
            assert!(expected_variants
                .iter()
                .all(|item| actual_variants.contains(item)));
        })
    }

    #[test]
    fn test_get_variants_empty() {
        let decider = Decider::new("../cfg.json").unwrap();

        let feature = decider.feature_by_name("dc_int").unwrap();
        assert!(feature.get_variants().is_empty());
    }

    proptest! {
        #[test]
        fn test_variant_ser(start in 0..1000u16, end in 0..1000u16) {
            prop_assume!(start <= end);

            let expected_start = (start as f32) / (TOTAL_BUCKETS as f32);
            let expected_end = (end as f32) / (TOTAL_BUCKETS as f32);

            let variant = Variant {
                name: "some variant".to_string(),
                range: start..end,
            };

            let jval = serde_json::to_value(variant).unwrap();

            assert_eq!(expected_start, jval["range_start"]);
            assert_eq!(expected_end, jval["range_end"]);
        }

        #[test]
        fn test_variant_des(start in 0.0..1.0f32, end in 0.0..1.0f32) {
            prop_assume!(start <= end);

            let expected_start = (start * (TOTAL_BUCKETS as f32)) as u16;
            let expected_end = (end * (TOTAL_BUCKETS as f32)) as u16;

            let jval = json!({
                "name": "some variant",
                "range_start": start,
                "range_end": end,
            });

            let variant: Variant = serde_json::from_value(jval).unwrap();

            assert_eq!(expected_start, variant.range.start);
            assert_eq!(expected_end, variant.range.end);
        }
    }

    #[test]
    fn test_partial_load() {
        let valid_exp = json!({
            "id": 1,
            "name": "valid_exp",
            "enabled": true,
            "owner": "test",
            "version": "3",
            "type": "range_variant",
            "emit_event": true,
            "start_ts": 37173982,
            "stop_ts": 2147483648u32,
            "experiment": {
              "variants": [
                {
                  "range_start": 0,
                  "range_end": 1,
                  "name": "variant_0"
                }
              ],
              "experiment_version": 3,
              "shuffle_version": 0,
              "bucket_val": "user_id",
              "log_bucketing": false
            },
        });

        let invalid_exp = json!({
            "some_key": [1, 2, 3],
        });

        let config = json!({
            "valid_exp": valid_exp,
            "invalid_exp": invalid_exp,
        });

        let decider_res = Decider::with_decisionmakers(config, Decider::DEFAULT_DECISIONMAKERS);
        let err = decider_res.expect_err("Constructor should return an error");
        let (decider, errs) = match err {
            DeciderInitError::PartialLoad(decider, errs) => (decider, errs),
            _ => unreachable!("Constructor should return a partial load!"),
        };

        // Check valid experiment.
        let ctx = Context {
            user_id: Some("t2_12345".to_string()),
            ..Context::default()
        };
        let decision = decider.choose("valid_exp", &ctx, None).unwrap();
        assert_eq!(decision.feature_id, 1);
        assert_eq!(decision.feature_name, "valid_exp".to_string());
        assert_eq!(decision.feature_version, 3);
        assert_eq!(decision.variant_name, Some("variant_0".to_string()));

        // Check errors.
        assert_eq!(errs.len(), 1);
        assert!(matches!(
            errs.get("invalid_exp"),
            Some(serde_json::Error { .. }),
        ));
    }

    mod regression {
        use crate::{Context, Decider, DecisionKind};
        use serde_json::json;

        #[test]
        fn test_holdout_event_regression() {
            // Holdout groups should emit control events, even when the child feature returns no
            // variant.
            let holdout_group = json!({
                "id": 1,
                "name": "holdout",
                "version": "1",
                "type": "range_variant",
                "enabled": true,
                "emit_event": true,
                "owner": "asdf",
                "experiment": {
                    "variants": [{
                        "name": "holdout",
                        "range_end": 0.0,
                        "range_start": 0.0
                    },{
                        "name": "control_1",
                        "range_end": 1.0,
                        "range_start": 0.0
                    }],
                    "experiment_version": 5,
                    "shuffle_version": 0,
                    "bucket_val": "user_id",
                }
            });

            let child = json!({
                "id": 2,
                "name": "child",
                "version": "1",
                "type": "range_variant",
                "enabled": true,
                "emit_event": true,
                "owner": "asdf",
                "parent_hg_name": "holdout",
                "experiment": {
                    "variants": [{
                        "name": "control_1",
                        "range_end": 0.0,
                        "range_start": 0.0
                    }],
                    "experiment_version": 0,
                    "shuffle_version": 0,
                    "bucket_val": "user_id"
                },
            });

            let config = json!({
                "holdout": holdout_group,
                "child": child,
            });

            let decider =
                Decider::from_bytes(serde_json::to_string(&config).unwrap().as_bytes()).unwrap();

            let ctx = Context {
                user_id: Some("t2_12345".to_string()),
                ..Context::default()
            };

            let feature = decider.feature_by_name("child").unwrap();
            let internal_decision = decider.decide_internal(feature, &ctx).unwrap();

            assert!(internal_decision.variant_name.is_none());
            assert_eq!("child", internal_decision.feature_name);

            assert_eq!(1, internal_decision.events.len());
            let event = internal_decision.events.first().unwrap();
            assert_eq!(DecisionKind::Holdout, event.decision_kind);
            assert_eq!("holdout", event.feature_name);
            assert_eq!("control_1", event.variant_name);
        }
    }
}

#[cfg(test)]
pub(crate) mod generators {
    use super::*;
    use proptest::option;
    use proptest::prelude::*;
    use uuid::Uuid;

    prop_compose! {
        pub(crate) fn context_strategy()(
            user_id in option::of(".*"),
            locale in option::of(".*"),
            country_code in option::of(".*"),
            device_id in option::of(uuid()),
            canonical_url in option::of(".*"),
            subreddit_id in option::of(".*"),
            ad_account_id in option::of(".*"),
            business_id in option::of(".*"),
            origin_service in option::of(".*"),
            user_is_employee in option::of(prop::bool::ANY),
            logged_in in option::of(prop::bool::ANY),
            app_name in option::of(".*"),
            build_number in option::of(prop::num::i32::ANY),
            oauth_client_id in option::of(".*"),
            cookie_created_timestamp in option::of(prop::num::i64::ANY),
            correlation_id in option::of(uuid()),
            // other_fields omitted for sanity
        ) -> Context {
            let device_id = device_id.map(|uuid| uuid.to_string());
            let correlation_id = correlation_id.map(|uuid| uuid.to_string());
            Context {
                user_id,
                locale,
                country_code,
                device_id,
                canonical_url,
                subreddit_id,
                ad_account_id,
                business_id,
                origin_service,
                user_is_employee,
                logged_in,
                app_name,
                build_number,
                oauth_client_id,
                cookie_created_timestamp,
                correlation_id,
                other_fields: None,
            }
        }
    }

    pub(crate) fn uuid() -> impl Strategy<Value = Uuid> {
        Just(Uuid::new_v4())
    }

    pub(crate) fn decision_kind() -> impl Strategy<Value = DecisionKind> {
        let options: Vec<_> = (0u8..)
            .map_while(|v| DecisionKind::try_from(v).ok())
            .collect();

        prop::sample::select(options)
    }

    // TODO Broaden this strategy (and dependent tests) to include all context fields.
    pub(crate) fn bucketing_field() -> impl Strategy<Value = ContextField> {
        prop::sample::select(vec![
            ContextField::UserId,
            ContextField::DeviceId,
            ContextField::CanonicalUrl,
        ])
    }
}

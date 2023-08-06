# TODO: Add License

import copy
import enum
import functools
import json
import logging
import textwrap
import warnings
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import (
    Any,
    Dict,
    Iterable,
    List,
    NamedTuple,
    Optional,
    Sequence,
    Tuple,
    Union,
    cast,
)

import numpy as np
import pandas as pd
import pandas.api.types
import pyarrow as pa
from deprecated import deprecated

from ._version import __version__
from .utils.exceptions import MalformedSchemaException
from .utils.formatting import prettyprint_number, validate_sanitized_names
from .utils.general_checks import (
    is_greater_than_max_value,
    is_less_than_min_value,
    type_enforce,
)
from .utils.pandas import is_datetime

MAX_VECTOR_DIMENSION = 1024
MAX_NUMBER_OF_CLUSTERS = 100
MAX_NUMBER_OF_CUSTOM_FEATURES = 100
DEFAULT_MAX_INFERRED_CARDINALITY = 100

# default for DatasetInfo.data_type_version and ModelInfo.data_type_version
# Introduced to bypass certain data type conversion functions
# from both client and server.
# More details https://fiddlerlabs.atlassian.net/wiki/spaces/FL/pages/1973617158/Introducing+Version+in+DatasetInfo+and+ModelInfo

# v0 means variable is just defined, no change in any logic.
# v0 is launched in python-client release 1.7.0
CURRENT_DATA_TYPE_VERSION: str = 'v0'

LOG = logging.getLogger(__name__)


class IntegrityViolationStatus(NamedTuple):
    is_nullable_violation: bool
    is_type_violation: bool
    is_range_violation: bool


class MonitoringViolation:
    """Object to track monitoring violations for pre-flight checks that can
    be trigerred via publish_event function with dry_run flag
    """

    def __init__(self, _type, desc):
        self.type = _type
        self.desc = desc


@enum.unique
class InitMonitoringModifications(enum.Enum):
    """various checks to perform for init_monitoring. Used to specify to the
    Fiddler `init_monitoring` endpoint whether or not modify (write) access
    is being given. See FNG-1152 for more details"""

    # only support monitoring int, float, category, or boolean types
    MODEL_INFO__COLUMN_TYPE = 'model_info::column_type'
    # ensure that model_info has min-max for all numeric types, and possible-values for all categorical types
    MODEL_INFO__BIN_CONFIG = 'model_info::bin_config'


possible_init_monitoring_modifications = (
    InitMonitoringModifications.MODEL_INFO__COLUMN_TYPE,
    InitMonitoringModifications.MODEL_INFO__BIN_CONFIG,
)


@enum.unique
class MonitoringViolationType(enum.Enum):
    """Fatal violations would cause monitoring to not work whereas warning violation
    can cause one or more monitoring features to not work.
    """

    FATAL = 'fatal'
    WARNING = 'warning'


@enum.unique
class HigherLevelAggregates(enum.Enum):
    """Supported Higher Level Aggregates"""

    TOP_K = 'top K'


@enum.unique
class FiddlerEventColumns(enum.Enum):
    OCCURRED_AT = '__occurred_at'
    MODEL = '__model'
    ORG = '__org'
    PROJECT = '__project'
    UPDATED_AT = '__updated_at'
    EVENT_ID = '__event_id'
    EVENT_TYPE = '__event_type'


@enum.unique
class EventTypes(enum.Enum):
    """We are mostly using execution and update events. Others are *probably* deprecated"""

    EXECUTION_EVENT = 'execution_event'
    UPDATE_EVENT = 'update_event'
    PREDICTION_EVENT = 'prediction_event'
    MODEL_ACTIVITY_EVENT = 'model_activity_event'
    MONITORING_CONFIG_UPDATE = 'monitoring_config_update'


class FiddlerPublishSchema:
    STATIC = '__static'
    DYNAMIC = '__dynamic'
    ITERATOR = '__iterator'
    UNASSIGNED = '__unassigned'
    HEADER_PRESENT = '__header_present'

    ORG = '__org'
    MODEL = '__model'
    PROJECT = '__project'
    TIMESTAMP = '__timestamp'
    DEFAULT_TIMESTAMP = '__default_timestamp'
    TIMESTAMP_FORMAT = '__timestamp_format'
    EVENT_ID = '__event_id'
    IS_UPDATE_EVENT = '__is_update_event'
    STATUS = '__status'
    LATENCY = '__latency'
    ITERATOR_KEY = '__iterator_key'

    CURRENT_TIME = 'CURRENT_TIME'


@enum.unique
class BatchPublishType(enum.Enum):
    """Supported Batch publish for the Fiddler engine."""

    DATAFRAME = 0
    LOCAL_DISK = 1
    AWS_S3 = 2
    GCP_STORAGE = 3


@enum.unique
class FiddlerTimestamp(enum.Enum):
    """Supported timestamp formats for events published to Fiddler"""

    EPOCH_MILLISECONDS = 'epoch milliseconds'
    EPOCH_SECONDS = 'epoch seconds'
    ISO_8601 = '%Y-%m-%d %H:%M:%S.%f'  # LOOKUP
    INFER = 'infer'


@enum.unique
class DataType(enum.Enum):
    """Supported datatypes for the Fiddler engine."""

    FLOAT = 'float'
    INTEGER = 'int'
    BOOLEAN = 'bool'
    STRING = 'str'
    CATEGORY = 'category'
    TIMESTAMP = 'timestamp'

    def is_numeric(self):
        return self.value in (DataType.INTEGER.value, DataType.FLOAT.value)

    def is_bool_or_cat(self):
        return self.value in (DataType.BOOLEAN.value, DataType.CATEGORY.value)

    def is_valid_target(self):
        return self.value != DataType.STRING.value


@enum.unique
class CustomFeatureType(str, enum.Enum):
    """The types of custom features based on how they are created."""

    FROM_COLUMNS = 'FROM_COLUMNS'
    # The following types will be added in later versions
    # FROM_TEXT = 'FROM_TEXT'
    # FROM_VECTOR = 'FROM_VECTOR'
    # FROM_DICTIONARY = 'FROM_DICTIONARY'


@enum.unique
class ArtifactStatus(enum.Enum):
    """Artifact Status, default to USER_UPLOADED"""

    NO_MODEL = 'no_model'
    SURROGATE = 'surrogate'
    USER_UPLOADED = 'user_uploaded'


@enum.unique
class ExplanationMethod(enum.Enum):
    SHAP = 'shap'
    FIDDLER_SV = 'fiddler_shapley_values'
    IG = 'ig'
    IG_FLEX = 'ig_flex'
    MEAN_RESET = 'mean_reset'
    PERMUTE = 'permute'


BUILT_IN_EXPLANATION_NAMES = [method.value for method in ExplanationMethod]


@enum.unique
class ModelTask(enum.Enum):
    """Supported model tasks for the Fiddler engine."""

    BINARY_CLASSIFICATION = 'binary_classification'
    MULTICLASS_CLASSIFICATION = 'multiclass_classification'
    REGRESSION = 'regression'
    RANKING = 'ranking'

    def is_classification(self):
        return self.value in (
            ModelTask.BINARY_CLASSIFICATION.value,
            ModelTask.MULTICLASS_CLASSIFICATION.value,
        )

    def is_regression(self):
        return self.value in (ModelTask.REGRESSION.value)


@enum.unique
class BuiltInMetrics(enum.Enum):
    """Supported metrics for segments."""

    MAPE = 'MAPE'
    WMAPE = 'WMAPE'
    R2 = 'r2'
    MSE = 'mse'
    MAE = 'mae'
    LOG_LOSS = 'log_loss'
    ACCURACY = 'accuracy'
    PRECISION = 'precision'
    RECALL = 'recall'
    F1_SCORE = 'f1_score'
    AUC = 'auc'

    @classmethod
    def get_binary(cls) -> List['BuiltInMetrics']:
        'return binary classification metrics'
        return [
            BuiltInMetrics.ACCURACY,
            BuiltInMetrics.PRECISION,
            BuiltInMetrics.RECALL,
            BuiltInMetrics.F1_SCORE,
            BuiltInMetrics.AUC,
        ]

    @classmethod
    def get_multiclass(cls) -> List['BuiltInMetrics']:
        'return multiclass classification metrics'
        return [BuiltInMetrics.ACCURACY, BuiltInMetrics.LOG_LOSS]

    @classmethod
    def get_regression(cls) -> List['BuiltInMetrics']:
        'return regression metrics'
        return [
            BuiltInMetrics.R2,
            BuiltInMetrics.MSE,
            BuiltInMetrics.MAE,
            BuiltInMetrics.MAPE,
            BuiltInMetrics.WMAPE,
        ]


@enum.unique
class ModelInputType(enum.Enum):
    """Supported model paradigms for the Fiddler engine."""

    TABULAR = 'structured'
    TEXT = 'text'
    MIXED = 'mixed'


@enum.unique
class DeploymentType(str, enum.Enum):
    EXECUTOR = 'executor'
    NO_MODEL = 'no-model'
    PREDICTOR = 'predictor'
    SURROGATE = 'surrogate'


class AttributionExplanation(NamedTuple):
    """The results of an attribution explanation run by the Fiddler engine."""

    algorithm: str
    inputs: List[str]
    attributions: List[float]
    misc: Optional[dict]

    @classmethod
    def from_dict(cls, deserialized_json: dict):
        """Converts a deserialized JSON format into an
        AttributionExplanation object"""

        algorithm = deserialized_json.pop('explanation_type')

        if 'GEM' in deserialized_json:
            return cls(
                algorithm=algorithm,
                inputs=[],
                attributions=deserialized_json.pop('GEM'),
                misc=deserialized_json,
            )

        else:
            if algorithm == 'ig' and deserialized_json['explanation'] == {}:
                input_attr = deserialized_json.pop('explanation_ig')
                inputs, attributions = input_attr[0], input_attr[1]
            else:
                inputs, attributions = zip(
                    *deserialized_json.pop('explanation').items()
                )

        return cls(
            algorithm=algorithm,
            inputs=list(inputs),
            attributions=list(attributions),
            misc=deserialized_json,
        )


class MulticlassAttributionExplanation(NamedTuple):
    """A collection of AttributionExplanation objects explaining several
    classes' predictions in a multiclass classification setting."""

    classes: Tuple[str]
    explanations: Dict[str, AttributionExplanation]

    @classmethod
    def from_dict(cls, deserialized_json: dict):
        """Converts a deserialized JSON format into an
        MulticlassAttributionExplanation object"""
        return cls(
            classes=cast(Tuple[str], tuple(deserialized_json.keys())),
            explanations={
                label_class: AttributionExplanation.from_dict(explanation_dict)
                for label_class, explanation_dict in deserialized_json.items()
            },
        )


class MLFlowParams:
    """Holds the configuration information for a model packaged as an MLFlow
    model."""

    def __init__(
        self,
        relative_path_to_saved_model: Union[str, Path],
        live_endpoint: Optional[str] = None,
    ):
        self.relative_path_to_saved_model = Path(relative_path_to_saved_model)
        self.live_endpoint = live_endpoint

    @classmethod
    def from_dict(cls, d):
        return cls(d['relative_path_to_saved_model'], d.get('live_endpoint', None))

    def to_dict(self):
        res = {
            'relative_path_to_saved_model': str(self.relative_path_to_saved_model),
        }
        if self.live_endpoint is not None:
            res['live_endpoint'] = self.live_endpoint
        return res


class ModelDeploymentParams:
    """Holds configuration information for a model packaged as a container."""

    def __init__(
        self,
        image: str,
    ):
        self.image = image

    @classmethod
    def from_dict(cls, d):
        return cls(d['image'])

    def to_dict(self):
        res = {
            'image': str(self.image),
        }
        return res


@dataclass
class DeploymentOptions:
    deployment_type: str = DeploymentType.SURROGATE
    image: str = None  # image to be used for newly uploaded model
    namespace: Optional[str] = None  # kubernetes namespace
    port: int = 5100  # port on which model is served
    replicas: int = 1  # number of replicas
    cpus: float = 0.25  # number of CPU cores
    memory: str = '128m'  # amount of memory required.
    gpus: int = 0  # number of GPU cores
    await_deployment: bool = True  # wait for deployment

    def to_dict(self):
        return asdict(self)


@dataclass
class CustomFeature:
    """A class used to define custom features such as complex/vector features

    :param name: The name of the custom feature as it will appear in the monitoring tab.
    :param columns: The name of the data column(s) that constitute the custom feature.
    :param transformation: The transformation method applied on the original data.
    :param n_clusters: The number of clusters used for creating clustering-based histograms.
                       If not specified a preprocessing step will run to choose the number of clusters automatically.
    :param monitor: A boolean variable that specifies whether this custom feature will be monitored using the
                            clustering-based histogram binning.
    """

    name: str
    columns: Union[str, List[str]]
    type: CustomFeatureType
    transformation: Optional[str] = None
    n_clusters: Optional[int] = None
    monitor: bool = True

    def __post_init__(self):
        if self.n_clusters is not None and not isinstance(self.n_clusters, int):
            raise TypeError(
                f'n_clusters argument must be of type int but received {type(self.n_clusters)}.'
            )

    def to_dict(self) -> Dict[str, Any]:
        """Converts this object to a more JSON-friendly form."""
        res = {
            'name': self.name,
            'columns': self.columns,
            'type': self.type.value,
            'transformation': self.transformation,
            'n_clusters': self.n_clusters,
            'monitor': self.monitor,
        }
        return res

    @classmethod
    def from_dict(cls, desrialized_json: dict):
        """Creates a CustomFeature object from deserialized JSON"""

        return cls(
            name=desrialized_json['name'],
            columns=desrialized_json['columns'],
            type=CustomFeatureType(desrialized_json['type']),
            transformation=desrialized_json['transformation'],
            n_clusters=desrialized_json['n_clusters'],
            monitor=desrialized_json['monitor'],
        )

    @classmethod
    def from_columns(
        cls,
        cols: List[str],
        custom_name: str,
        transformation: Optional[str] = None,
        n_clusters: Optional[int] = None,
        monitor: bool = True,
    ):
        """Creates a custom feature from multiple numerical columns.
        :param cols: A list of column names that define this custom feature.
        :param custom_name: The name of this custom feature as it will appear in the monitoring tab.
        :param transformation: [Optional] An optional transformation step (eg, dimensionality reduction via SVD).
        :param n_clusters: [Optional] Number of clusters for clustering-based monitoring.
        :param monitor:A boolean variable that specifies whether this custom feature will be monitored using the
                            clustering-based histogram binning.
        """
        if not isinstance(custom_name, str):
            raise TypeError(
                f'custom_name argument must be of type str but received {type(custom_name)}'
            )

        if not (isinstance(cols, list) and all(isinstance(col, str) for col in cols)):
            raise TypeError(
                f'cols argument accepts a list of column names, passed {cols}.'
            )

        if len(cols) > MAX_VECTOR_DIMENSION:
            raise ValueError(
                f'The maximum acceptable dimension for a custom feature is {MAX_VECTOR_DIMENSION}, {len(cols)} columns are passed to cols.'
            )

        if n_clusters and n_clusters > MAX_NUMBER_OF_CLUSTERS:
            raise ValueError(
                f'The number of clusters should not exceed {MAX_NUMBER_OF_CLUSTERS}.'
            )

        return cls(
            name=custom_name,
            columns=cols,
            type=CustomFeatureType.FROM_COLUMNS,
            transformation=transformation,
            n_clusters=n_clusters,
            monitor=monitor,
        )

    # ToDo: This class method will be added later. For the first version we only use from_columns constructor
    # @classmethod
    # def from_text(cls,
    #               text_col: str,
    #               transformation: str,
    #               custom_name: Optional[str] = None,
    #               n_clusters: Optional[int] = None,
    #               monitor: bool = True,
    #               ):
    #     """Creates a custom feature from a single text column.
    #     :param text_col: The name of the dataset column that contains text data.
    #     :param transformation: The transformation used to convert text data to numerical vectors.
    #     :param custom_name: [Optional] A new name assigned to this custom feature. If not specified, the name of the text column will be used.
    #     :param n_clusters: [Optional] Number of clusters for clustering-based monitoring.
    #     :param monitor:A boolean variable that specifies whether this custom feature will be monitored using the
    #                         clustering-based histogram binning.
    #     """
    #     if not isinstance(text_col, str):
    #         raise TypeError(f"The first argument specifies the column that contains text data."
    #                         f" It accepts a string but received {type(text_col)}.")
    #     if custom_name and not isinstance(custom_name, str):
    #         raise TypeError(f"custom_name argument must be of type 'str' but received {type(custom_name)}")
    #
    #     custom_feature_name = custom_name if custom_name else text_col
    #     return cls(name=custom_feature_name,
    #                columns=text_col,
    #                type=CustomFeatureType.FROM_TEXT,
    #                transformation=transformation,
    #                n_clusters=n_clusters,
    #                monitor=monitor)


class Column:
    """Represents a single column of a dataset or model input/output.

    :param name: The name of the column (corresponds to the header row of a
        CSV file)
    :param data_type: The best encoding type for this column's data.
    :param possible_values: If data_type is CATEGORY, then an exhaustive list
        of possible values for this category must be provided. Otherwise
        this field has no effect and is optional.
    :param is_nullable: Optional metadata. Tracks whether or not this column is
        expected to contain some null values.
    :param value_range_x: Optional metadata. If data_type is FLOAT or INTEGER,
        then these values specify a range this column's values are expected to
        stay within. Has no effect for non-numerical data_types.
    """

    def __init__(
        self,
        name: str,
        data_type: DataType,
        possible_values: Optional[List[Any]] = None,
        is_nullable: Optional[bool] = None,
        value_range_min: Optional[float] = None,
        value_range_max: Optional[float] = None,
    ):
        self.name = name
        self.data_type = data_type
        self.possible_values = possible_values
        self.is_nullable = is_nullable
        self.value_range_min = value_range_min
        self.value_range_max = value_range_max

        inappropriate_value_range = not self.data_type.is_numeric() and not (
            self.value_range_min is None and self.value_range_max is None
        )
        if inappropriate_value_range:
            raise ValueError(
                f'Do not pass `value_range` for '
                f'non-numerical {self.data_type} data type.'
            )

    @classmethod
    def from_dict(cls, desrialized_json: dict):
        """Creates a Column object from deserialized JSON"""
        return cls(
            name=desrialized_json['column-name'],
            data_type=DataType(desrialized_json['data-type']),
            possible_values=desrialized_json.get('possible-values', None),
            is_nullable=desrialized_json.get('is-nullable', None),
            value_range_min=desrialized_json.get('value-range-min', None),
            value_range_max=desrialized_json.get('value-range-max', None),
        )

    def copy(self):
        return copy.deepcopy(self)

    def __repr__(self):
        res = (
            f'Column(name="{self.name}", data_type={self.data_type}, '
            f'possible_values={self.possible_values}'
        )
        if self.is_nullable is not None:
            res += f', is_nullable={self.is_nullable}'
        if self.value_range_min is not None or self.value_range_max is not None:
            res += (
                f', value_range_min={self.value_range_min}'
                f', value_range_max={self.value_range_max}'
            )
        res += ')'
        return res

    def _raise_on_bad_categorical(self):
        """Raises a ValueError if data_type=CATEGORY without possible_values"""
        if (
            self.data_type.value == DataType.CATEGORY.value
            and self.possible_values is None
        ):

            # Commenting to allow none possible values
            self.possible_values = []
            # raise ValueError(
            #     f'Mal-formed categorical column missing `possible_values`: ' f'{self}'
            # )

    def get_pandas_dtype(self):
        """Converts the data_type field to a Pandas-friendly form."""
        # Commenting to allow none possible values.
        # self._raise_on_bad_categorical()

        if self.data_type.value == DataType.CATEGORY.value:
            return pandas.api.types.CategoricalDtype(self.possible_values)
        return self.data_type.value

    def get_arrow_field(self) -> pa.Field:
        """Converts the data_type field to a pyarrow field"""

        if self.data_type == DataType.CATEGORY:
            field_type = pa.dictionary(index_type=pa.int64(), value_type=pa.string())
        elif self.data_type == DataType.INTEGER:
            field_type = pa.int64()
        elif self.data_type == DataType.FLOAT:
            field_type = pa.float64()
        elif self.data_type == DataType.BOOLEAN:
            field_type = pa.bool_()
        elif self.data_type == DataType.STRING:
            field_type = pa.string()
        else:
            raise ValueError(
                f'Not able to map data type to arrow field - {self.data_type}'
            )

        return pa.field(self.name, field_type)

    def to_dict(self) -> Dict[str, Any]:
        """Converts this object to a more JSON-friendly form."""
        res = {
            'column-name': self.name,
            'data-type': self.data_type.value,
        }
        if self.possible_values is not None:
            # possible-values can be string, int, etc
            # no need to convert everything to str
            res['possible-values'] = [val for val in self.possible_values]
        if self.is_nullable is not None:
            res['is-nullable'] = self.is_nullable
        if self.value_range_min is not None:
            res['value-range-min'] = self.value_range_min
        if self.value_range_max is not None:
            res['value-range-max'] = self.value_range_max
        return res

    @deprecated(reason='Moved to data_type module in fiddler repo')
    def violation_of_value(self, value):
        if Column._value_is_na_or_none(value):
            return False
        if self.data_type.is_numeric():
            is_too_low = self.value_range_min is not None and is_less_than_min_value(
                value, self.value_range_min
            )
            is_too_high = (
                self.value_range_max is not None
                and is_greater_than_max_value(value, self.value_range_max)
            )
            return is_too_low or is_too_high
        if self.data_type.value in [DataType.CATEGORY.value, DataType.BOOLEAN.value]:
            return value not in self.possible_values
        return False

    @deprecated(reason='Moved to data_type module in fiddler repo')
    def violation_of_type(self, value):
        if Column._value_is_na_or_none(value):
            return False
        if self.data_type.value == DataType.FLOAT.value:
            # json loading from string reads non-decimal number always as int
            return not (isinstance(value, float) or isinstance(value, int))
        if self.data_type.value == DataType.INTEGER.value:
            # pandas converts int columns to float columns, will further cause backend to flag it as type violation
            # e.g: "2" is casted as "2.0" by pandas. And "2.0" will be flagged as type violation. typeof(2.0) != INT
            if isinstance(value, float):
                if int(value) == value:
                    value = int(value)
            return not isinstance(value, int) and not pandas.api.types.is_int64_dtype(
                value
            )
        if self.data_type.value == DataType.STRING.value:
            return not isinstance(value, str)
        if self.data_type.value == DataType.BOOLEAN.value:
            return not isinstance(value, bool) and value not in (0, 1)
        if self.data_type.value == DataType.CATEGORY.value:
            possible_types = tuple(set(type(v) for v in self.possible_values))
            return not isinstance(value, possible_types)

    @deprecated(reason='Moved to data_type module in fiddler repo')
    def violation_of_nullable(self, value):
        if self.is_nullable is not None and self.is_nullable is False:
            return Column._value_is_na_or_none(value)
        return False

    @deprecated(reason='Moved to data_type module in fiddler repo')
    def check_violation(self, value):
        if self.violation_of_nullable(value):
            return IntegrityViolationStatus(True, False, False)
        if self.violation_of_type(value):
            return IntegrityViolationStatus(False, True, False)
        if self.violation_of_value(value):
            return IntegrityViolationStatus(False, False, True)
        return IntegrityViolationStatus(False, False, False)

    @staticmethod
    def _value_is_na_or_none(value):
        if value is None:
            return True
        # This needs to be added because when we add `pandas._libs.missing.NAType` type in rabbitmq.
        # When we read the message, it converts the value to the "<NA>".
        if isinstance(value, str):
            return '<NA>' == value
        try:
            return pd.isnull(value)
        except TypeError:
            return False


def _get_field_pandas_dtypes(
    column_sequence: Sequence[Column],
) -> Dict[str, Union[str, pandas.api.types.CategoricalDtype]]:
    """Get a dictionary describing the pandas datatype of every column in a
    sequence of columns."""
    dtypes = dict()
    for column in column_sequence:
        dtypes[column.name] = column.get_pandas_dtype()
    return dtypes


@dataclass
class WeightingParams:
    """Holds weighting information for class imbalanced models

    :param class_weight: list of floats representing weights for each of the classes. The length
        must equal the no. of classes.
    :param weighted_reference_histograms: Flag indicating if baseline histograms must be weighted or not
        when calculating drift metrics.
    :param weighted_surrogate_training: Flag indicating if weighting scheme should be used when training the
        surrogate model.

    :return: A WeightingParams object
    """

    class_weight: Optional[List[float]] = None
    weighted_reference_histograms: bool = True
    weighted_surrogate_training: bool = True

    def __post_init__(self):
        # raise an error if neither or both class and sample weighting is specified
        if self.class_weight is None:
            raise ValueError('Need to specify class_weights')
        if not isinstance(self.class_weight, List):
            raise ValueError(
                f'Expected class_weight to be a list of floats instead received {type(self.class_weight)}'
            )
        try:
            self.class_weight = [round(float(w), 4) for w in self.class_weight]
            # validate class-weights
            for wt in self.class_weight:
                if wt < 0:
                    raise ValueError('Class-weights cannot be negative.')
        except ValueError:
            raise ValueError('Expected class_weight to be a list of floats')
        return

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, d):
        return cls(**d)


class DatasetInfo:

    """Information about a dataset. Defines the schema.

    :param display_name: A name for user-facing display (different from an id).
    :param columns: A list of Column objects.
    :param files: Optional. If the dataset is stored in one or more CSV files
        with canonical names, this field lists those files. Primarily for use
        only internally to the Fiddler engine.
    :param data_type_version: [Optional] a String indicating CURRENT_DATA_TYPE_VERSION.
        Used mainly for data type conversion rules for possible_values.
    """

    def __init__(
        self,
        display_name: str,
        columns: List[Column],
        files: Optional[List[str]] = None,
        dataset_id: str = None,
        data_type_version: Optional[str] = None,
        **kwargs,
    ):
        self.display_name = display_name
        self.dataset_id = dataset_id
        self.columns = DatasetInfo._datatype_check(columns)
        self.files = files if files is not None else list()
        self.data_type_version = data_type_version
        self.misc = kwargs

    def to_dict(self) -> Dict[str, Any]:
        """Converts this object to a more JSON-friendly form."""
        res = {
            'name': self.display_name,
            'data_type_version': self.data_type_version,
            'columns': [c.to_dict() for c in self.columns],
            'files': self.files,
        }
        return {**res, **self.misc}

    def get_pandas_dtypes(self) -> Dict:
        """
        Convert dataset info columns data types to pandas compatible data types
        :return: Dictionary of pandas data types for dataset columns
        """

        dtypes = {}

        for column in self.columns:
            dtypes[column.name] = column.get_pandas_dtype()

        return dtypes

    def get_arrow_schema(self) -> pa.Schema:
        """
        Convert dataset info columns data types to pyarrow compatible schema
        :return: pyarrow compatible schema
        """

        fields = []

        for column in self.columns:
            fields.append(column.get_arrow_field())

        return pa.schema(fields)

    def get_column_names(self) -> List[str]:
        """Returns a list of column names."""
        return [column.name for column in self.columns]

    def get_column_pandas_dtypes(
        self,
    ) -> Dict[str, Union[str, pandas.api.types.CategoricalDtype]]:
        """Get a dictionary describing the pandas datatype of every column."""
        return _get_field_pandas_dtypes(self.columns)

    def get_event_integrity(
        self, event: Dict[str, Union[str, float, int, bool]]
    ) -> Tuple[IntegrityViolationStatus, ...]:
        if not set(event.keys()).issuperset(set(self.get_column_names())):
            raise ValueError(
                f'Event feature names {set(event.keys())} not'
                f'a superset of column names '
                f'{set(self.get_column_names())}'
            )
        return tuple(
            column.check_violation(event[column.name]) for column in self.columns
        )

    @staticmethod
    def _datatype_check(columns):
        """
        # loop through all columns
        # if the column datatype is numpy datatype, transform to python type
        """
        for column in columns:
            column.value_range_max = DatasetInfo._transform_type(column.value_range_max)
            column.value_range_min = DatasetInfo._transform_type(column.value_range_min)
        return columns

    @staticmethod
    def _transform_type(val):
        if isinstance(val, np.bool_):
            val = bool(val)
        if isinstance(val, np.integer):
            val = int(val)
        if isinstance(val, np.floating):
            val = float(val)
        return val

    @staticmethod
    def datatype_from_pandas_dtype(pd_dtype) -> DataType:
        if pd.api.types.is_float_dtype(pd_dtype):
            return DataType.FLOAT
        if pd.api.types.is_integer_dtype(pd_dtype):
            return DataType.INTEGER
        if pd.api.types.is_bool_dtype(pd_dtype):
            return DataType.BOOLEAN
        if pd.api.types.is_categorical_dtype(pd_dtype):
            return DataType.CATEGORY

        return DataType.STRING

    @classmethod
    def update_stats_for_existing_schema(
        cls, dataset: dict, info, max_inferred_cardinality: Optional[int] = None
    ):
        """Takes a customer/user provided schema along with a bunch
        of files with corresponding data in dataframes and merges them
        together and updates the user schema.
        Please note that we DO NOT update stats in the user provided
        schema if those stats are already there. We assume that the
        user wants those stats for data integrity testing.
        """
        updated_infos = []
        for name, item in dataset.items():
            update_info = DatasetInfo.check_and_update_column_info(
                info, item, max_inferred_cardinality
            )
            updated_infos.append(update_info)
        info = DatasetInfo.as_combination(
            updated_infos,
            display_name=info.display_name,
        )
        return info

    @classmethod
    def check_and_update_column_info(
        cls,
        info_original,
        df: pd.DataFrame,
        max_inferred_cardinality: Optional[int] = None,
    ):
        """When called on a Dataset, this function will calculate stats
        that are used by DI and put add them to each Column in case its
        not already there. Currently stats include is_nullable, possible_values, and
        min/max ranges.
        Please note that we DO NOT update stats in the user provided
        schema if those stats are already there. We assume that the
        user wants those stats for data integrity testing.
        """

        info = copy.deepcopy(info_original)
        if df.index.name is not None:
            # add index column if it is not just an unnamed RangeIndex
            df = df.reset_index(inplace=False)
        name_series_iter = df.items()
        column_stats = {}
        for column_name, column_series in name_series_iter:
            column_info = cls._calculate_stats_for_col(
                column_name, column_series, max_inferred_cardinality
            )
            column_stats[column_name] = column_info

        for column in info.columns:
            # Fill in stats for each column if its not present
            column_info = column_stats[column.name]
            if not column.is_nullable:
                column.is_nullable = column_info.is_nullable
            if not column.value_range_min:
                column.value_range_min = column_info.value_range_min
            if not column.value_range_max:
                column.value_range_max = column_info.value_range_max
            if not column.possible_values:
                column.possible_values = column_info.possible_values

        return cls(
            info.display_name, info.columns, data_type_version=CURRENT_DATA_TYPE_VERSION
        )

    @classmethod
    def from_dataframe(
        cls,
        df: Union[pd.DataFrame, Iterable[pd.DataFrame]],
        display_name: str = '',
        max_inferred_cardinality: Optional[int] = DEFAULT_MAX_INFERRED_CARDINALITY,
        dataset_id: Optional[str] = None,
    ):
        """Infers a DatasetInfo object from a pandas DataFrame
        (or iterable of DataFrames).

        :param df: Either a single DataFrame or an iterable of DataFrame
            objects. If an iterable is given, all dataframes must have the
            same columns.
        :param display_name: A name for user-facing display (different from
            an id).
        :param max_inferred_cardinality: Optional. If not None, any
            string-typed column with fewer than `max_inferred_cardinality`
            unique values will be inferred as a category (useful for cases
            where use of the built-in CategoricalDtype functionality of Pandas
            is not desired). Defaults to 100.
        :param dataset_id: Optionally specify the dataset_id.

        :returns: A DatasetInfo object.
        """
        # if an iterable is passed, infer for each in the iterable and combine
        if not isinstance(df, pd.DataFrame):
            info_gen = (
                cls.from_dataframe(
                    item, max_inferred_cardinality=max_inferred_cardinality
                )
                for item in df
            )
            return cls.as_combination(info_gen, display_name=display_name)

        columns = []
        if df.index.name is not None:
            # add index column if it is not just an unnamed RangeIndex
            df = df.reset_index(inplace=False)
        name_series_iter = df.items()
        for column_name, column_series in name_series_iter:
            column_info = cls._calculate_stats_for_col(
                column_name, column_series, max_inferred_cardinality
            )
            columns.append(column_info)
        return cls(
            display_name,
            columns,
            dataset_id=dataset_id,
            data_type_version=CURRENT_DATA_TYPE_VERSION,
        )

    @staticmethod
    def _calculate_stats_for_col(column_name, column_series, max_inferred_cardinality):
        # @TODO Automatically drop the empty column with warning and proceed instead of aborting the upload
        if column_series.isna().all():
            raise ValueError(
                f'Column {column_name} is empty. '
                f'Please remove it and re-upload the dataset.'
            )

        # if we infer string or categorical, ensure that the underlying data
        # is also string by casting it.
        column_dtype = DatasetInfo.datatype_from_pandas_dtype(
            column_series.infer_objects().dtype
        )
        if column_dtype in [DataType.CATEGORY, DataType.STRING]:
            if 'mixed' in pd.api.types.infer_dtype(column_series):
                LOG.warning(
                    '***********************************\n'
                    'WARNING: The column passed has mixed datatypes.\n'
                    ' We have casted the column to string to ensure smooth functionality.\n'
                    '***********************************'
                )
            column_series = column_series.astype(str)

        # infer categorical if configured to do so
        if (
            max_inferred_cardinality
            and column_dtype.value == DataType.STRING.value
            and not is_datetime(column_series)
            and column_series.nunique() <= max_inferred_cardinality
        ):
            column_dtype = DataType.CATEGORY

        # get possible values for categorical type
        if column_dtype.value in [DataType.CATEGORY.value, DataType.BOOLEAN.value]:
            possible_values = np.sort(column_series.dropna().unique()).tolist()
            possible_values_floats = None
            if column_dtype.value == DataType.CATEGORY.value:
                try:
                    possible_values_floats = [
                        str(float(raw_val)) for raw_val in possible_values
                    ]
                except ValueError:
                    pass
            if possible_values_floats is not None:
                possible_values = possible_values_floats
        else:
            possible_values = None

        # get value range for numerical dtype
        if column_dtype.is_numeric():
            value_min, value_max = column_series.agg(['min', 'max'])
            if np.isnan(value_min):
                value_min = None
            if np.isnan(value_max):
                value_max = None
        else:
            value_min, value_max = None, None

        # get nullability
        is_nullable = bool(column_series.isna().any())
        return Column(
            name=column_name,
            data_type=column_dtype,
            possible_values=possible_values,
            is_nullable=is_nullable,
            value_range_min=value_min,
            value_range_max=value_max,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Converts this object to a more JSON-friendly form."""
        res = {
            'name': self.display_name,
            'data_type_version': self.data_type_version,
            'columns': [c.to_dict() for c in self.columns],
            'files': self.files,
        }
        return {**res, **self.misc}

    @classmethod
    def from_dict(cls, deserialized_json: dict):
        """Transforms deserialized JSON into a DatasetInfo object"""
        # drop down into the "dataset" object inside the deserialized_json
        if 'dataset' in deserialized_json:
            deserialized_json = deserialized_json['dataset']
        if 'chunked_sources' in deserialized_json:
            return cls(
                display_name=deserialized_json['name'],
                columns=[Column.from_dict(c) for c in deserialized_json['columns']],
                files=deserialized_json.get('files', None),
                data_type_version=deserialized_json.get('data_type_version', None),
                misc={
                    'chunked_sources': deserialized_json.get('chunked_sources', None)
                },
            )
        # instantiate the class
        return cls(
            display_name=deserialized_json['name'],
            columns=[Column.from_dict(c) for c in deserialized_json['columns']],
            files=deserialized_json.get('files', None),
            data_type_version=deserialized_json.get('data_type_version', None),
        )

    @classmethod
    def _combine(cls, info_a, info_b, display_name: str = ''):
        """Given two DatasetInfo objects, tries to combine them into
        a single DatasetInfo that describes both sub-datasets."""
        # raise error if column names are incompatible
        if info_a.get_column_names() != info_b.get_column_names():
            raise ValueError(
                f'Incompatible DatasetInfo objects: column names do not '
                f'match:\n{info_a.get_column_names()}\n'
                f'{info_b.get_column_names()}'
            )

        # combine columns
        columns = list()
        for a_column, b_column in zip(info_a.columns, info_b.columns):
            # resolve types
            a_type, b_type = a_column.data_type.value, b_column.data_type.value
            if a_type == b_type:
                col_type = a_column.data_type
            elif {a_type, b_type}.issubset(
                {DataType.BOOLEAN.value, DataType.INTEGER.value}
            ):
                col_type = DataType.INTEGER
            elif {a_type, b_type}.issubset(
                {DataType.BOOLEAN.value, DataType.INTEGER.value, DataType.FLOAT.value}
            ):
                col_type = DataType.FLOAT
            else:
                col_type = DataType.STRING

            # resolve possible_values
            if col_type.value == DataType.CATEGORY.value:
                assert a_column.possible_values is not None  # nosec
                assert b_column.possible_values is not None  # nosec
                # Merging the unique possible values after removing the None values.
                possible_values: Optional[List[Any]] = list(
                    set(list(filter(None, a_column.possible_values)))
                    or set(list(filter(None, b_column.possible_values)))
                )
                # Sort the final list to make sure the order is consistent.
                if possible_values and len(possible_values) > 0:
                    possible_values.sort()
            else:
                possible_values = None

            # resolve is_nullable, priority being True, then False, then None
            if a_column.is_nullable is None and b_column.is_nullable is None:
                is_nullable = None
            elif a_column.is_nullable or b_column.is_nullable:
                is_nullable = True
            else:
                is_nullable = False

            # resolve value range
            value_range_min = a_column.value_range_min
            if b_column.value_range_min is not None:
                if value_range_min is None:
                    value_range_min = b_column.value_range_min
                else:
                    value_range_min = min(value_range_min, b_column.value_range_min)
            value_range_max = a_column.value_range_max
            if b_column.value_range_max is not None:
                if value_range_max is None:
                    value_range_max = b_column.value_range_max
                else:
                    value_range_max = max(value_range_max, b_column.value_range_max)
            columns.append(
                Column(
                    a_column.name,
                    col_type,
                    possible_values,
                    is_nullable,
                    value_range_min,
                    value_range_max,
                )
            )

        # combine file lists
        files = info_a.files + info_b.files

        return cls(
            display_name, columns, files, data_type_version=CURRENT_DATA_TYPE_VERSION
        )

    @classmethod
    def as_combination(cls, infos: Iterable, display_name: str = 'combined_dataset'):
        """Combines an iterable of compatible DatasetInfo objects into one
        DatasetInfo"""
        return functools.reduce(
            lambda a, b: cls._combine(a, b, display_name=display_name), infos
        )

    @staticmethod
    def get_summary_dataframe(dataset_info):
        """Returns a table (pandas DataFrame) summarizing the DatasetInfo."""
        return _summary_dataframe_for_columns(dataset_info.columns)

    def __repr__(self):
        column_info = textwrap.indent(repr(self.get_summary_dataframe(self)), '    ')
        return (
            f'DatasetInfo:\n'
            f'  display_name: {self.display_name}\n'
            f'  files: {self.files}\n'
            f'  columns:\n'
            f'{column_info}'
        )

    def _repr_html_(self):
        column_info = self.get_summary_dataframe(self)
        return (
            f'<div style="border: thin solid rgb(41, 57, 141); padding: 10px;">'
            f'<h3 style="text-align: center; margin: auto;">DatasetInfo\n</h3>'
            f'<pre>display_name: {self.display_name}\nfiles: {self.files}\n</pre>'
            f'<hr>Columns:'
            f'{column_info._repr_html_()}'
            f'</div>'
        )

    def _col_id_from_name(self, name):
        """Look up the index of the column by name"""
        for i, c in enumerate(self.columns):
            if c.name == name:
                return i
        raise KeyError(name)

    def __getitem__(self, item):
        return self.columns[self._col_id_from_name(item)]

    def __setitem__(self, key, value):
        assert isinstance(value, Column), (  # nosec
            'Must set column to be a ' '`Column` object'
        )
        self.columns[self._col_id_from_name(key)] = value

    def __delitem__(self, key):
        del self.columns[self._col_id_from_name(key)]

    def validate(self):
        sanitized_name_dict = dict()
        validate_sanitized_names(self.columns, sanitized_name_dict)


class ModelInfo:

    """Information about a model. Stored in `model.yaml` file on the backend.

    :param display_name: [Deprecated in 1.7.0 and will be removed from 2.0.0 version.]
    A name for user-facing display (different from an id).
    :param input_type: Specifies whether the model is in the tabular or text
        paradigm.
    :param model_task: Specifies the task the model is designed to address.
    :param inputs: A list of Column objects corresponding to the dataset
        columns that are fed as inputs into the model.
    :param outputs: A list of Column objects corresponding to the table
        output by the model when running predictions.
    :param targets: A list of Column objects corresponding to the dataset
        columns used as targets/labels for the model. If not provided, some
        functionality (like scoring) will not be available.
    :param algorithm: A string providing information about the model type.
    :param framework: A string providing information about the software library
        and version used to train and run this model.
    :param description: A user-facing description of the model.
    :param datasets: A list of dataset names assocated with this model.
    :param weighting_params: [Optional] Weighting parameters to account for class-imbalance. These parameters
        will be used to generate reference and production histograms.
    :param mlflow_params: [Deprecated in 1.7.0 and will be removed from 2.0.0 version.]
    MLFlow parameters.
    :param model_deployment_params: [Deprecated in 1.7.0 and will be removed from 2.0.0 version.]
    Model Deployment parameters.
    :param artifact_status: [Deprecated in 1.7.0 and will be removed from 2.0.0 version.]
    Status of the model artifact
    :param preferred_explanation_method: [Deprecated in 1.7.0 and will be removed from 2.0.0 version.]
    [Optional] Specifies a preference
        for the default explanation algorithm.  Front-end will choose
        explanation method if unspecified (typically Fiddler Shapley).
        Must be one of the built-in explanation types (ie an `fdl.core_objects.ExplanationMethod`) or be specified as
        a custom explanation type via `custom_explanation_names` (and in `package.py`).
    :param custom_explanation_names:
    [Optional] List of (string) names that
        can be passed to the explanation_name argument of the optional
        user-defined explain_custom method of the model object defined in
        package.py. The `preferred_explanation_method` can be set to one of these in order to override built-in explanations.
    :param binary_classification_threshold: [Optional] Float representing threshold for labels
    :param ranking_top_k: [Optional] Int used only for Ranking models and representing the top k results to take into
     consideration when computing performance metrics like MAP and NDCG.
    :param group_by: [Optional] A string representing the column name performance metrics have
     to be group by with for performance metrics computation. This have to be given for Ranking for MAP
      and NDCG computations. For ranking models, it represents the query/session id column.
    :param missing_value_encodings(fall_back): [Optional] A dictionary of list representing the values that should be
           replaced with null for each columns. Key is the column name.
    :param tree_shap_enabled: [Optional] Boolean value indicating if Tree SHAP should be enabled for this model.
           If set to True, Tree SHAP will become the default explanation method unless you specify another
           preferred explanation method.
    :param custom_features: [Optional] A list of custom features that are instances of CustomFeature class.
    :param data_type_version: [Optional] a String indicating 'v0', 'v1' etc. Used mainly to apply data type conversion rules.
    :param **kwargs: Additional information about the model to store as `misc`.
    """

    def __init__(
        self,
        display_name: str,
        input_type: ModelInputType,
        model_task: ModelTask,
        inputs: List[Column],
        outputs: List[Column],
        target_class_order: Optional[List] = None,
        metadata: Optional[List[Column]] = None,
        decisions: Optional[List[Column]] = None,
        targets: Optional[List[Column]] = None,
        algorithm: Optional[str] = None,
        framework: Optional[str] = None,
        description: Optional[str] = None,
        datasets: Optional[List[str]] = None,
        weighting_params: Optional[WeightingParams] = None,
        mlflow_params: Optional[MLFlowParams] = None,
        model_deployment_params: Optional[ModelDeploymentParams] = None,
        artifact_status: Optional[ArtifactStatus] = None,
        # TODO: smartly set default preferred_explanation_method (ie infer method here, instead of on BE/FE):
        preferred_explanation_method: Optional[str] = None,
        custom_explanation_names: Optional[List[str]] = None,
        binary_classification_threshold: Optional[float] = None,
        ranking_top_k: Optional[int] = None,
        group_by: Optional[str] = None,
        fall_back: Optional[Dict] = None,
        missing_value_encodings: Optional[Dict] = None,
        tree_shap_enabled: Optional[bool] = False,
        custom_features: Optional[List[CustomFeature]] = None,
        is_binary_ranking_model: Optional[bool] = None,
        data_type_version: Optional[str] = None,
        **kwargs,
    ):
        self.display_name = display_name
        self.input_type = input_type
        self.model_task = model_task
        self.inputs = inputs
        self.outputs = outputs
        self.target_class_order = target_class_order
        self.targets = targets
        self.metadata = metadata
        self.decisions = decisions
        self.algorithm = algorithm
        self.framework = framework
        self.description = description
        self.datasets = datasets
        self.weighting_params = weighting_params
        self.mlflow_params = mlflow_params
        self.model_deployment_params = model_deployment_params
        self.artifact_status = artifact_status
        self.binary_classification_threshold = binary_classification_threshold
        self.ranking_top_k = ranking_top_k
        self.schema_version = CURRENT_MODELINFO_SCHEMA_VERSION
        self.custom_features = custom_features
        self.data_type_version = data_type_version

        # warning for parameters deprecated in version 1.7
        if mlflow_params is not None:
            self.warn_deprecated_parameter(
                param_name='mlflow_params', from_version='1.7'
            )
        if display_name is not None:
            self.warn_deprecated_parameter(
                param_name='display_name', from_version='1.7'
            )
        if model_deployment_params is not None:
            self.warn_deprecated_parameter(
                param_name='model_deployment_params', from_version='1.7'
            )

        # artifact_status is set by Model Service
        # POST /v2/models sets  artifact_status to NO_MODEL
        # POST /v2/<model-id>/deploy-artifacts/... sets USER_UPLOADED
        # POST /v2/<model-id>/deploy-surrogate sets SURROGATE
        if artifact_status is not None:
            self.warn_deprecated_parameter(
                param_name='artifact_status', from_version='1.7'
            )

        if custom_explanation_names is None:
            custom_explanation_names = []

        self.is_binary_ranking_model = is_binary_ranking_model

        if model_task == ModelTask.RANKING:
            if group_by is None:
                raise ValueError(
                    'The argument group_by cannot be empty for Ranking models'
                )
            if target_class_order is not None:
                self.is_binary_ranking_model = len(target_class_order) == 2

        self.group_by = group_by

        if tree_shap_enabled:
            custom_explanation_names.append('Tree Shap')
            if preferred_explanation_method is None:
                preferred_explanation_method = 'Tree Shap'

        # we only store strings, not enums
        if isinstance(preferred_explanation_method, ExplanationMethod):
            preferred_explanation_method = preferred_explanation_method.value

        # Prevent the user from overloading a built-in.
        if custom_explanation_names is not None:
            duplicated_names = []
            for name in custom_explanation_names:
                if type(name) != str:
                    raise ValueError(
                        f"custom_explanation_names for ModelInfo must all be of type 'str', "
                        f"but '{name}' is of type '{type(name)}'"
                    )
                if name in BUILT_IN_EXPLANATION_NAMES:
                    duplicated_names.append(name)
            if len(duplicated_names) > 0:
                raise ValueError(
                    f'Please select different names for your custom explanations. The following are reserved'
                    f' built-ins duplicated in your custom explanation names: {duplicated_names}.'
                )

        # Prevent the user from defaulting to an explanation that doesn't exist
        assert (
            custom_explanation_names is not None
        ), 'custom_explanation_names is unexpectedly None'
        if (
            preferred_explanation_method is not None
            and preferred_explanation_method not in BUILT_IN_EXPLANATION_NAMES
            and preferred_explanation_method not in custom_explanation_names
        ):
            if len(custom_explanation_names) > 0:
                raise ValueError(
                    f'The preferred_explanation_method specified ({preferred_explanation_method}) could not be found '
                    f'in the built-in explanation methods ({BUILT_IN_EXPLANATION_NAMES}) or in the '
                    f'custom_explanation_names ({custom_explanation_names})'
                )
            else:
                raise ValueError(
                    f'The preferred_explanation_method specified ({preferred_explanation_method}) could not be found '
                    f'in the built-in explanation methods ({BUILT_IN_EXPLANATION_NAMES})'
                )

        self.preferred_explanation_method = preferred_explanation_method
        self.custom_explanation_names = custom_explanation_names
        self.misc = kwargs

        if fall_back is not None:
            LOG.warning(
                'WARNING: fall_back will be deprecated in a future version. Use missing_value_encodings instead. '
            )
        if missing_value_encodings is None:
            self.missing_value_encodings = fall_back
        else:
            self.missing_value_encodings = missing_value_encodings
            if fall_back is not None and fall_back != missing_value_encodings:
                LOG.warning(
                    'WARNING: Both missing_value_encodings and fall_back are specified, accept '
                    'missing_value_encodings and ignore fall_back. '
                )
        if self.missing_value_encodings is not None:
            ModelInfo.validate_missing_value_encodings(
                self.missing_value_encodings, self.get_all_cols()
            )
        self.fall_back = self.missing_value_encodings  # backward compatability

        available_cols = (
            self.get_input_names() + self.get_target_names() + self.get_metadata_names()
        )
        if self.custom_features is not None:
            if not isinstance(self.custom_features, List):
                raise ValueError(
                    'The custom_features argument only accepts a list of CustomFeature objects.'
                )
            if len(self.custom_features) > MAX_NUMBER_OF_CUSTOM_FEATURES:
                raise ValueError(
                    f'The maximum number of custom features in a project cannot exceed {MAX_NUMBER_OF_CUSTOM_FEATURES}. {len(self.custom_features)} custom features are defined.'
                )
            unique_cf_names = []
            for feature in self.custom_features:

                if not isinstance(feature, CustomFeature):
                    raise ValueError(
                        'The custom_features argument only accepts a list of CustomFeature objects.'
                    )

                if feature.name in available_cols:
                    raise ValueError(
                        f'A column name "{feature.name}" already exists in the dataset. Please use a different name for custom feature {feature}.'
                    )

                if feature.name in unique_cf_names:
                    raise ValueError(
                        f'Multiple custom features are defined with the same name {feature.name}.'
                    )
                else:
                    unique_cf_names.append(feature.name)

                if isinstance(feature.columns, list):
                    for col in feature.columns:
                        if col not in available_cols:
                            raise ValueError(
                                f"Custom features '{feature.name}' is defined based on column '{col}' which was not found."
                            )
                else:
                    if feature.columns not in available_cols:
                        raise ValueError(
                            f"Custom features '{feature.name}' is defined based on column '{feature.columns}' which was not found."
                        )

    def warn_deprecated_parameter(self, param_name: str, from_version: str) -> None:
        warnings.warn(
            f'WARNING: {param_name} is deprecated in {from_version}. It will be removed from 2.0.0 version.',
            DeprecationWarning,
        )

    def to_dict(self):
        """Dumps to basic python objects (easy for JSON serialization)"""
        res = {
            'name': self.display_name,
            'input-type': self.input_type.value,
            'model-task': self.model_task.value,
            'inputs': [c.to_dict() for c in self.inputs],
            'outputs': [c.to_dict() for c in self.outputs],
            'datasets': self.datasets or [],
        }
        if self.target_class_order is not None:
            res['target-class-order'] = self.target_class_order
        if self.metadata:
            res['metadata'] = [metadata_col.to_dict() for metadata_col in self.metadata]
        if self.decisions:
            res['decisions'] = [
                decision_col.to_dict() for decision_col in self.decisions
            ]
        if self.targets:
            res['targets'] = [target_col.to_dict() for target_col in self.targets]
        if self.description is not None:
            res['description'] = self.description
        if self.algorithm is not None:
            res['algorithm'] = self.algorithm
        if self.framework is not None:
            res['framework'] = self.framework
        if self.mlflow_params is not None:
            res['mlflow'] = self.mlflow_params.to_dict()
        if self.model_deployment_params is not None:
            res['model_deployment'] = self.model_deployment_params.to_dict()
        if self.artifact_status is not None:
            res['artifact_status'] = self.artifact_status.value
        if self.preferred_explanation_method is not None:
            res['preferred-explanation-method'] = self.preferred_explanation_method
        if self.binary_classification_threshold is not None:
            res[
                'binary_classification_threshold'
            ] = self.binary_classification_threshold
        if self.ranking_top_k is not None:
            res['ranking_top_k'] = self.ranking_top_k
        if self.group_by is not None:
            res['group_by'] = self.group_by
        if self.schema_version is not None:
            res['schema_version'] = self.schema_version
        else:
            # Default schema version for old non-handled cases
            res['schema_version'] = DEFUNCT_MODELINFO_SCHEMA_VERSION
        if self.fall_back is not None:
            res['fall_back'] = self.fall_back
        if self.missing_value_encodings is not None:
            res['missing_value_encodings'] = self.missing_value_encodings
        res['custom-explanation-names'] = self.custom_explanation_names
        if self.custom_features is not None:
            res['custom_features'] = [f.to_dict() for f in self.custom_features]
        if self.weighting_params is not None:
            res['weighting_params'] = self.weighting_params.to_dict()
        if self.is_binary_ranking_model is not None:
            res['is_binary_ranking_model'] = self.is_binary_ranking_model
        if self.data_type_version is not None:
            res['data_type_version'] = self.data_type_version
        return {**res, **self.misc}

    @classmethod  # noqa: C901
    def from_dict(cls, deserialized_json: dict):
        """Transforms deserialized JSON into a ModelInfo object"""
        # drop down into the "model" object inside the deserialized_json
        # (work on a copy)
        if 'model' in deserialized_json:
            deserialized_json = copy.deepcopy(deserialized_json['model'])
        else:
            deserialized_json = copy.deepcopy(deserialized_json)

        name = deserialized_json.pop('name')
        input_type = ModelInputType(deserialized_json.pop('input-type'))
        model_task = ModelTask(deserialized_json.pop('model-task'))
        inputs = [Column.from_dict(c) for c in deserialized_json.pop('inputs')]
        outputs = [Column.from_dict(c) for c in deserialized_json.pop('outputs')]
        if 'target-class-order' in deserialized_json:
            target_class_order = deserialized_json.pop('target-class-order')
        else:
            target_class_order = None

        artifact_status: Optional[ArtifactStatus] = None
        if 'artifact_status' in deserialized_json:
            artifact_status = ArtifactStatus(deserialized_json.pop('artifact_status'))

        metadata: Optional[List[Column]] = None
        if 'metadata' in deserialized_json:
            metadata = [Column.from_dict(c) for c in deserialized_json.pop('metadata')]

        decisions: Optional[List[Column]] = None
        if 'decisions' in deserialized_json:
            decisions = [
                Column.from_dict(c) for c in deserialized_json.pop('decisions')
            ]

        targets: Optional[List[Column]] = None
        if 'targets' in deserialized_json:
            targets = [Column.from_dict(c) for c in deserialized_json.pop('targets')]

        if 'missing_value_encodings' in deserialized_json:
            missing_value_encodings = deserialized_json.pop('missing_value_encodings')
        else:
            missing_value_encodings = None
        if 'fall_back' in deserialized_json:
            fall_back = deserialized_json.pop('fall_back')
        else:
            fall_back = None

        if 'tree_shap_enabled' in deserialized_json:
            tree_shap_enabled = deserialized_json.pop('tree_shap_enabled')
        else:
            tree_shap_enabled = False

        description = deserialized_json.pop('description', None)
        algorithm = deserialized_json.pop('algorithm', None)
        framework = deserialized_json.pop('framework', None)
        mlflow_params: Optional[MLFlowParams] = None
        if 'mlflow' in deserialized_json:
            mlflow_params = MLFlowParams.from_dict(deserialized_json.pop('mlflow'))

        model_deployment_params: Optional[ModelDeploymentParams] = None
        if 'model_deployment' in deserialized_json:
            model_deployment_params = ModelDeploymentParams.from_dict(
                deserialized_json.pop('model_deployment')
            )

        datasets: Optional[Any] = None
        if 'datasets' in deserialized_json:
            datasets = deserialized_json.pop('datasets')

        preferred_explanation_method: Optional[Any] = None
        if 'preferred-explanation-method' in deserialized_json:
            preferred_explanation_method = deserialized_json.pop(
                'preferred-explanation-method'
            )

        custom_explanation_names: List[Any] = []
        if 'custom-explanation-names' in deserialized_json:
            custom_explanation_names = deserialized_json.pop('custom-explanation-names')

        binary_classification_threshold: Optional[float] = None
        if model_task == ModelTask.BINARY_CLASSIFICATION:
            # @TODO: https://fiddlerlabs.atlassian.net/browse/FDL-4090
            try:
                binary_classification_threshold = float(
                    deserialized_json.pop('binary_classification_threshold')
                )
            except Exception:
                # Default to 0.5
                LOG.warning(
                    'No `binary_classification_threshold` specified, defaulting to 0.5'
                )
                binary_classification_threshold = 0.5

        ranking_top_k: Optional[int] = None
        group_by: Optional[str] = None
        is_binary_ranking_model: Optional[bool] = None
        if model_task == ModelTask.RANKING:
            try:
                ranking_top_k = int(deserialized_json.pop('ranking_top_k'))
            except Exception:
                # Default to 50
                LOG.warning('No `ranking_top_k` specified, defaulting to 50')
                ranking_top_k = 50
            group_by = deserialized_json.pop('group_by')
            if 'is_binary_ranking_model' in deserialized_json:
                is_binary_ranking_model = deserialized_json.pop(
                    'is_binary_ranking_model'
                )

        schema_version = deserialized_json.pop(
            'schema_version', DEFUNCT_MODELINFO_SCHEMA_VERSION
        )

        weighting_params: Optional[WeightingParams] = None
        if 'weighting_params' in deserialized_json:
            weighting_params = WeightingParams.from_dict(
                deserialized_json.pop('weighting_params')
            )
        custom_features: Optional[List[CustomFeature]] = None
        if 'custom_features' in deserialized_json:
            custom_features = [
                CustomFeature.from_dict(d)
                for d in deserialized_json.pop('custom_features')
            ]

        data_type_version: Optional[str] = None
        if 'data_type_version' in deserialized_json:
            data_type_version = deserialized_json.pop('data_type_version')

        # instantiate the class
        model_info = cls(
            display_name=name,
            input_type=input_type,
            model_task=model_task,
            inputs=inputs,
            outputs=outputs,
            target_class_order=target_class_order,
            metadata=metadata,
            decisions=decisions,
            targets=targets,
            description=description,
            algorithm=algorithm,
            framework=framework,
            datasets=datasets,
            weighting_params=weighting_params,
            mlflow_params=mlflow_params,
            model_deployment_params=model_deployment_params,
            artifact_status=artifact_status,
            preferred_explanation_method=preferred_explanation_method,
            custom_explanation_names=custom_explanation_names,
            binary_classification_threshold=binary_classification_threshold,
            ranking_top_k=ranking_top_k,
            group_by=group_by,
            fall_back=fall_back,
            missing_value_encodings=missing_value_encodings,
            tree_shap_enabled=tree_shap_enabled,
            custom_features=custom_features,
            is_binary_ranking_model=is_binary_ranking_model,
            data_type_version=data_type_version,
            **deserialized_json,
        )
        # Explicitly set the version number
        model_info.schema_version = schema_version
        return model_info

    @staticmethod
    def validate_missing_value_encodings(
        missing_value_encodings: dict, all_columns: List[Column]
    ) -> None:
        unmatched_col = []
        for k, v in missing_value_encodings.items():
            matched_column = None
            for column in all_columns:
                if k == column.name:
                    matched_column = column
            if matched_column is None:
                LOG.warning(
                    f'WARNING: Missing_value_encodings(fall_back): Column {k} Not found in all column names.'
                    'Dropping it.'
                )
                unmatched_col.append(k)
            else:
                # check if the column is specified as is_nullable
                if (
                    matched_column.is_nullable is not None
                    and matched_column.is_nullable is False
                ):
                    matched_column.is_nullable = True
                    LOG.warning(
                        f'Columns in Missing_value_encodings(fall_back) should be nullable. '
                        f'Change Column({k}) to nullable. '
                    )
                # prevent the user from specifying an invalid schema for missing_value_encodings
                if not isinstance(v, List):
                    raise ValueError(
                        f'Missing_value_encodings(fall_back) specified for Column({k}) has to be a list, '
                        f'instead got type of {type(v)}'
                    )
                for ind, value in enumerate(v):
                    if matched_column.data_type.value == DataType.FLOAT.value:
                        if value == float('inf'):
                            missing_value_encodings[k][ind] = 'inf'
                        elif value == -float('inf'):
                            missing_value_encodings[k][ind] = '-inf'

        for k in unmatched_col:
            del missing_value_encodings[k]
        if len(missing_value_encodings) == 0:
            raise ValueError(
                'None of the missing_value_encodings(fall_back) matches the column names entered, please provide '
                'dictionary with valid keys.'
            )

    def get_input_names(self):
        """Returns a list of names for model inputs."""
        return [column.name for column in self.inputs]

    def get_output_names(self):
        """Returns a list of names for model outputs."""
        return [column.name for column in self.outputs]

    def get_metadata_names(self):
        """Returns a list of names for model metadata."""
        if self.metadata is None:
            return []
        return [column.name for column in self.metadata]

    def get_decision_names(self):
        """Returns a list of names for model decisions."""
        if self.decisions is None:
            return []
        return [column.name for column in self.decisions]

    def get_target_names(self):
        """Returns a list of names for model targets."""
        if self.targets is None:
            return []
        return [column.name for column in self.targets]

    def get_input_pandas_dtypes(
        self,
    ) -> Dict[str, Union[str, pandas.api.types.CategoricalDtype]]:
        """Get a dictionary describing the pandas datatype of every input."""
        return _get_field_pandas_dtypes(self.inputs)

    def get_output_pandas_dtypes(
        self,
    ) -> Dict[str, Union[str, pandas.api.types.CategoricalDtype]]:
        """Get a dictionary describing the pandas datatype of every output."""
        return _get_field_pandas_dtypes(self.outputs)

    def get_metadata_pandas_dtypes(
        self,
    ) -> Dict[str, Union[str, pandas.api.types.CategoricalDtype]]:
        """Get a dictionary describing the pandas datatype of every
        metadata column."""
        assert self.metadata is not None
        return _get_field_pandas_dtypes(self.metadata)

    def get_decisions_pandas_dtypes(
        self,
    ) -> Dict[str, Union[str, pandas.api.types.CategoricalDtype]]:
        """Get a dictionary describing the pandas datatype of every decision
        column."""
        assert self.decisions is not None
        return _get_field_pandas_dtypes(self.decisions)

    def get_target_pandas_dtypes(
        self,
    ) -> Dict[str, Union[str, pandas.api.types.CategoricalDtype]]:
        """Get a dictionary describing the pandas datatype of every target."""
        assert self.targets is not None
        return _get_field_pandas_dtypes(self.targets)

    @classmethod  # noqa: C901
    def from_dataset_info(
        cls,
        dataset_info: DatasetInfo,
        target: str,
        dataset_id: Optional[str] = None,
        features: Optional[Sequence[str]] = None,
        fall_back: Optional[Dict] = None,
        missing_value_encodings: Optional[Dict] = None,
        metadata_cols: Optional[Sequence[str]] = None,
        decision_cols: Optional[Sequence[str]] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        algorithm: Optional[str] = None,
        framework: Optional[str] = None,
        input_type: ModelInputType = ModelInputType.TABULAR,
        model_task: Optional[ModelTask] = None,
        outputs: Optional[Any] = None,
        categorical_target_class_details: Optional[Any] = None,
        weighting_params: Optional[WeightingParams] = None,
        model_deployment_params: Optional[ModelDeploymentParams] = None,
        preferred_explanation_method: Optional[str] = None,
        custom_explanation_names: Optional[List[str]] = None,
        binary_classification_threshold: Optional[float] = None,
        ranking_top_k: Optional[int] = None,
        group_by: Optional[str] = None,
        tree_shap_enabled: Optional[bool] = False,
        custom_features: Optional[List[CustomFeature]] = None,
    ):
        """Produces a ModelInfo for a model trained on a dataset.

        :param dataset_info: A DatasetInfo object describing the training
            dataset.
        :param target: The column name of the target the model predicts.
        :param dataset_id: Specify the dataset_id for the model. Must be provided if the dataset_id cannot be inferred from the dataset_info.
        :param features: A list of column names for columns used as features.
        :param missing_value_encodings(fall_back): A dictionary of list representing the values that should be
           replaced with null for each columns. Key is the column name.
        :param metadata_cols: A list of column names for columns used as
        metadata.
        :param decision_cols: A list of column names for columns used as
        decisions.
        :param display_name: A model name for user-facing display (different
            from an id).
        :param description: A user-facing description of the model.
        :param algorithm: A string providing information about the model type.
        :param framework: A string providing information about the software library
            and version used to train and run this model.
        :param input_type: Specifies the paradigm (tabular or text) of the
            model.
        :param model_task: Specifies the prediction task addressed by the
            model. If not explicitly provided, this will be inferred from the
            data type of the target variable.
        :param mlflow_params: MLFlow parameters.
        :param outputs: model output names, if multiclass classification, must be a sequence in the same order as categorical_target_class_details.
            If binary classification, must be a single name signifying the probability of the positive class. # TODO: bulletproofing
            If regression/ranking, must be a dictionary of the form {column_name: (min_value, max_value)}, or a
            dictionary with empty range {column_name:[]} if column_name can be found in the dataset
        :param categorical_target_class_details: specify the output categories of your model (only applicable for classification and ranking models)
            This parameter *must* be provided for multiclass, binary-classification and ranking models where
            the target is of type CATEGORY. It is optional for binary classification with BOOLEAN targets, and ignored for regression.

            For multiclass classification models, provide a list of all the possible
            output categories of your model. The same order will be implicitly assumed
            by register model surrogate, and must match the outputs from custom package.py
            uploads. # TODO: ensure surrogate order matches this order.

            For binary classification models, if you provide a single element (or a list with
            a single element) then that element will be considered to be the positive class.
            Alternatively you can provide a list with 2 elements. The 0th element,
            by convention will be considered to be the negative class, and the 1th element will
            define the positive class. These params can be used to override the default convention
            specified below.

            For binary classification with target of type BOOLEAN:
                - by default `True` is the positive class for `True`/`False` targets.
                - by default `1` or `1.0` for `1`/`0` integer targets or `1.`/`0.` float targets,
            For other binary classification tasks on numeric types:
                - by default the higher of the two possible values will be considered the positive class.
            In all other cases, one of the two classes will arbitrarily be FIXED as the positive class.

            For ranking models, provide a list of all the possible target values in order of relevance. The first element will be considered
            as not relevant, the last element from the list will be considered the most relevant grade.
        :param weighting_params: [Optional] Weighting parameters to account for class-imbalance. These parameters
            will be used to generate reference and production histograms.
        :param model_deployment_params: Model Deployment parameters.
        :param preferred_explanation_method: [Optional] Specifies a preference
            for the default explanation algorithm.  Front-end will choose
            explanaton method if unspecified (typically Fiddler Shapley).
            Providing ExplanationMethod.CUSTOM will cause the first of the
            custom_explanation_names to be the default (which must be defined
            in that case).
        :param custom_explanation_names: [Optional] List of names that
            can be passed to the explanation_name argument of the optional
            user-defined explain_custom method of the model object defined in
            package.py.
        :param binary_classification_threshold: [Optional] Float representing threshold for labels
        :param ranking_top_k: [Optional] Int used only for Ranking models and representing the top k results to take into
         consideration when computing performance metrics like MAP and NDCG.
        :param group_by: [Optional] A string representing the column name performance metrics have
         to be group by with for performance metrics computation. This have to be given for Ranking for MAP
          and NDCG computations. For ranking models, it represents the query/session id column.
        :param tree_shap_enabled: [Optional] Boolean value indicating if Tree SHAP should be enabled for this model.
           If set to True, Tree SHAP will become the default explanation method unless you specify another
           preferred explanation method.
        :param custom_features: [Optional] A list of custom features that are instances of CustomFeature class.

        :returns A ModelInfo object.
        """
        if categorical_target_class_details is not None:
            warnings.warn(
                'WARNING: categorical_target_class_details is deprecated in 1.7 and will be removed from 2.0.0 version. As a replacement, use target_class_order while constructing ModelInfo.',
                DeprecationWarning,
            )

        if custom_explanation_names is None:
            custom_explanation_names = []

        if not isinstance(dataset_info, DatasetInfo):
            raise ValueError(
                f'The dataset_info parameter must be a valid DatasetInfo object'
            )

        if display_name is None:
            if dataset_info.display_name is not None:
                display_name = f'{dataset_info.display_name} model'
            else:
                display_name = ''

        # infer inputs, and add metadata and decision columns, if they exist

        inputs = list()

        additional_columns: List[str] = []
        metadata: Optional[List[Any]] = None
        if metadata_cols is not None:
            additional_columns += list(metadata_cols)
            metadata = []

        decisions: Optional[List[Any]] = None
        if decision_cols is not None:
            additional_columns += list(decision_cols)
            decisions = []

        if isinstance(outputs, List):
            additional_columns += outputs
        elif isinstance(outputs, Dict):
            additional_columns += outputs.keys()

        # ensure that columns are not duplicated
        if len(additional_columns) > 0:
            col_list = [target]
            if features is not None:
                col_list += features

            duplicated_cols = [col for col in additional_columns if col in col_list]

            if len(duplicated_cols) > 0:
                raise ValueError(
                    f'Cols can be either feature, target, '
                    f'outputs, metadata or decisions. Cols '
                    f'{",".join(duplicated_cols)} are present '
                    f'in more than one category'
                )

        target_column: Optional[Column] = None
        if target:
            # determine target column
            try:
                target_column = dataset_info[target]
            except KeyError:
                raise ValueError(f'Target "{target}" not found in dataset.')
        assert target_column is not None, 'target_column unexpectedly None'

        # todo (pradhuman): replace categorical_target_class_details with target_class_order

        if model_task and model_task.value == ModelTask.RANKING.value:
            (
                output_names,
                target_class_order,
                ranking_top_k,
                group_by,
                is_binary_ranking_model,
            ) = ModelInfo.ranking_cls_inference(
                dataset_info=dataset_info,
                target_column=target_column,
                categorical_target_class_details=categorical_target_class_details,
                outputs=outputs,
                ranking_top_k=ranking_top_k,
                group_by=group_by,
            )
        else:
            ranking_top_k = None
            group_by = None
            inferred_type = None
            is_binary_ranking_model = None
            if outputs:
                if type(outputs) != dict:
                    outputs = np.array(outputs).flatten().tolist()
                if (
                    target_column.possible_values
                    and len(target_column.possible_values) == 2
                ):
                    inferred_type = ModelTask.BINARY_CLASSIFICATION
                    if len(outputs) > 1:
                        # if two outputs or more are provided, assume the first few are negative classes and drop them
                        outputs = [outputs[-1]]
                        LOG.warning(
                            f'WARNING: BINARY_CLASSIFICATION only have one output, using {outputs[-1]} as positive class. '
                        )
                    output_names = {output: (0.0, 1.0) for output in outputs}
                elif len(outputs) > 1:
                    inferred_type = ModelTask.MULTICLASS_CLASSIFICATION
                    output_names = {output: (0.0, 1.0) for output in outputs}
                else:
                    # outputs has one item
                    if not model_task:
                        if ModelInfo.check_binary_target(target_column):
                            inferred_type = ModelTask.BINARY_CLASSIFICATION
                        else:
                            inferred_type = ModelTask.REGRESSION
                    task = inferred_type if inferred_type is not None else model_task
                    output_names = ModelInfo.calculate_outputs(
                        outputs=outputs, dataset_info=dataset_info, task=task
                    )
            else:
                # when outputs is None, determine target_levels from target_column data type
                if not target_column.data_type.is_valid_target():
                    raise ValueError(
                        f'Target "{target_column.name}" has invalid datatype "{target_column.data_type}". '
                        f'For regression tasks please use a numeric target. For classification please use boolean or category'
                        f'(Also, are you setting "max_inferred_cardinality" correctly when creating dataset_info?) '
                    )
                target_levels: Optional[List[Any]]
                if model_task:
                    if model_task.value == ModelTask.REGRESSION.value:
                        target_levels = None
                    elif model_task.value == ModelTask.BINARY_CLASSIFICATION.value:
                        if target_column.data_type.value == DataType.BOOLEAN.value:
                            target_levels = [False, True]
                        elif target_column.data_type.value == DataType.CATEGORY.value:
                            target_levels = target_column.possible_values
                            assert len(target_levels) == 2
                        else:
                            if (
                                target_column.value_range_max
                                == target_column.value_range_min
                            ):
                                raise ValueError(
                                    f'Target {target_column.name} has only one unique value.'
                                )
                            target_levels = [
                                target_column.value_range_min,
                                target_column.value_range_max,
                            ]
                    else:
                        assert (
                            target_column.data_type.value == DataType.CATEGORY.value
                        ), f'Target "{target_column.name}" '
                        f'has invalid datatype "{target_column.data_type}". '
                        'For classification task please use boolean or category'
                        '(Also, are you setting "max_inferred_cardinality" correctly when creating dataset_info?) '
                        target_levels = target_column.possible_values
                else:
                    if target_column.data_type.value == DataType.BOOLEAN.value:
                        target_levels = [False, True]
                    elif target_column.data_type.value == DataType.CATEGORY.value:
                        target_levels = target_column.possible_values
                    else:
                        if (
                            target_column.value_range_max
                            == target_column.value_range_min
                        ):
                            raise ValueError(
                                f'Target {target_column.name} has only one unique value.'
                            )
                        # binary case when fitting in 1.0/0.0, 1/0, 1/-1, 1.0/-1.0 special cases or INT max-INT min=1
                        if ModelInfo.check_binary_target(target_column):
                            target_levels = [
                                target_column.value_range_min,
                                target_column.value_range_max,
                            ]
                        else:
                            target_levels = None
                # determine task type from target_levels and format output_names
                if not target_levels:
                    # When outputs column not present, REGRESSION case: use target column range
                    inferred_type = ModelTask.REGRESSION
                    pred_name = f'predicted_{target_column.name}'
                    assert target_column.value_range_min is not None
                    assert target_column.value_range_max is not None
                    output_names = {
                        pred_name: (
                            float(target_column.value_range_min),
                            float(target_column.value_range_max),
                        )
                    }
                else:
                    pred_name = f'probability_{target_column.name}'
                    if len(target_levels) == 2:
                        inferred_type = ModelTask.BINARY_CLASSIFICATION
                        output_names = {f'{pred_name}_{target_levels[1]}': (0.0, 1.0)}
                    else:
                        inferred_type = ModelTask.MULTICLASS_CLASSIFICATION
                        output_names = {
                            f'{pred_name}_{level}': (0.0, 1.0)
                            for level in target_levels
                        }

            # check if inferred type corresponds with entered type
            if not model_task:
                model_task = inferred_type
                LOG.info(f'Assuming given outputs imply {model_task.value} ')
            else:
                if inferred_type and model_task.value != inferred_type.value:
                    raise ValueError(
                        f'Invalid arguments: model_task is specified as {model_task.value} but inferred as '
                        f'{inferred_type.value} due to the type of Argument '
                        f'{"outputs(" + str(type(outputs)) if outputs else "target(" + str(target_column.data_type)}). '
                        '[USAGE for Argument outputs]: If multiclass classification, must specify a sequence in the same order as '
                        'categorical_target_class_details: [cls_1, cls_2 ... cls_n]; if binary classification, must be a '
                        'single name signifying the probability of the positive class: pos_cls_name; if regression or '
                        'ranking, must be a dictionary with the range of the outputs: {output_name: (min_value, max_value)}'
                        ' or a dictionary with empty range {column_name:[]} if column_name can be found in the dataset. '
                    )

            # target_class_order inference
            target_class_order = None
            # todo (pradhuman): move this logic up few lines where categorical_target_class_details is used.
            categorical_target_class_details = (
                np.array(categorical_target_class_details).flatten().tolist()
            )
            if model_task.value == ModelTask.MULTICLASS_CLASSIFICATION.value:
                if categorical_target_class_details[0] is None:
                    raise ValueError(
                        'categorical_target_class_details must be defined for task type = MULTICLASS_CLASSIFICATION'
                    )
                else:
                    assert target_column is not None, 'target_column unexpectedly None'
                    if not target_column.data_type.is_numeric():
                        assert (
                            target_column.possible_values is not None
                        ), 'target_column.possible_values unexpectedly None'
                        if sorted(target_column.possible_values) != sorted(
                            categorical_target_class_details
                        ):
                            raise ValueError(
                                f'categorical_target_class_details does not have the same elements as target column {target_column.name}'
                            )
                    else:
                        LOG.info(
                            'Assuming that categorical_target_class_details has been supplied correctly for numeric target.'
                        )
                    target_class_order = categorical_target_class_details
            if model_task.value == ModelTask.BINARY_CLASSIFICATION.value:
                # infer defaults 1=1.0=True as the positive class
                assert target_column is not None, 'target_column unexpectedly None'
                if (
                    not target_column.data_type.is_numeric()
                ):  # true for category and boolean
                    assert (
                        target_column.possible_values is not None
                    ), 'target_column.possible_values unexpectedly None'
                    if len(target_column.possible_values) != 2:
                        raise ValueError(
                            f'Target {target_column.name} does not have cardinality == 2.'
                        )
                    target_class_order = target_column.possible_values
                else:  # float or int
                    if (
                        target_column.value_range_max is None
                        or target_column.value_range_min is None
                    ):
                        raise ValueError(
                            f'Target {target_column.name} does not have 2 unique non null values.'
                        )
                    elif target_column.value_range_max == target_column.value_range_min:
                        raise ValueError(
                            f'Target {target_column.name} has only one unique value.'
                        )
                    else:
                        target_class_order = [
                            target_column.value_range_min,
                            target_column.value_range_max,
                        ]
                # override defaults if user wants
                if categorical_target_class_details[0] is not None:
                    if len(categorical_target_class_details) == 1:
                        neg_class = list(
                            set(target_class_order)
                            - set(categorical_target_class_details)
                        )
                        if len(neg_class) > 1:
                            raise ValueError(
                                f'Element {categorical_target_class_details[0]} not found in target column {target_column.name}'
                            )
                        categorical_target_class_details = (
                            neg_class + categorical_target_class_details
                        )
                    if len(categorical_target_class_details) == 2:
                        if sorted(target_class_order) != sorted(
                            categorical_target_class_details
                        ):
                            raise ValueError(
                                f'categorical_target_class_details does not have the same elements as target column {target_column.name}'
                            )
                        target_class_order = categorical_target_class_details
                    else:
                        raise ValueError(
                            'Cannot create model with BINARY_CLASSIFICATION task with more than 2 elements in target'
                        )
                else:
                    LOG.info('Using inferred positive class.')

                # TODO: don't catch all exceptions here; if this is about type safety,
                # then implement a runtime type check. Put in some `type: ignore` marks
                # for now.
                try:
                    binary_classification_threshold = float(
                        binary_classification_threshold
                    )  # type: ignore
                except Exception:
                    # Default to 0.5. Override as needed.
                    LOG.warning(
                        'No `binary_classification_threshold` specified, defaulting to 0.5'
                    )
                    binary_classification_threshold = 0.5

        # model_info cols creation
        output_columns = []
        for output, range in output_names.items():
            if model_task.is_classification():
                # Probabilities between 0.0 and 1.0 for classification tasks
                output_columns.append(
                    Column(
                        name=output,
                        data_type=DataType.FLOAT,
                        is_nullable=False,
                        value_range_min=0.0,
                        value_range_max=1.0,
                    )
                )
            else:
                output_columns.append(
                    Column(
                        name=output,
                        data_type=DataType.FLOAT,
                        is_nullable=False,
                        value_range_min=range[0],
                        value_range_max=range[1],
                    )
                )
        for column in dataset_info.columns:
            col_name = column.name
            if (
                col_name != target
                and col_name not in output_names
                and (features is None or col_name in features)
                and (col_name not in additional_columns)
            ):
                inputs.append(column.copy())
            if metadata_cols and col_name in metadata_cols:
                assert metadata is not None, 'metadata unexpectedly None'
                metadata.append(column.copy())
            if decision_cols and col_name in decision_cols:
                assert decisions is not None, 'decisions unexpectedly None'
                decisions.append(column.copy())

        # dataset_id creation
        if dataset_id is not None:
            datasets = [dataset_id]
        elif dataset_info.dataset_id is not None:
            datasets = [dataset_info.dataset_id]
        else:
            raise ValueError(
                'Please specify a dataset_id, it could not be inferred from the '
                'dataset_info.'
            )

        # perform checks for weighting parameters
        if weighting_params is not None:
            if (
                weighting_params.class_weight is not None
                and model_task == ModelTask.BINARY_CLASSIFICATION
            ):
                if len(weighting_params.class_weight) != 2:
                    raise ValueError(
                        f'Expected a class weighting vector of length 2 for binary classification task, '
                        f'instead received vector of length {len(weighting_params.class_weight)}'
                    )
            elif (
                weighting_params.class_weight is not None
                and model_task == ModelTask.MULTICLASS_CLASSIFICATION
            ):
                if len(weighting_params.class_weight) != len(target_class_order):
                    raise ValueError(
                        f'Expected a class weighting vector of length {len(target_class_order)} '
                        f'for multi-class classification task, '
                        f'instead received vector of length {len(weighting_params.class_weight)}'
                    )
            elif not model_task.is_classification():
                LOG.warning(
                    'WARNING: Weighting parameter not supported for non-classification tasks and will be ignored'
                )

        return cls(
            display_name=display_name,
            description=description,
            algorithm=algorithm,
            framework=framework,
            input_type=input_type,
            model_task=model_task,
            inputs=inputs,
            outputs=output_columns,
            target_class_order=target_class_order,
            metadata=metadata,
            decisions=decisions,
            targets=[target_column],
            datasets=datasets,
            weighting_params=weighting_params,
            mlflow_params=None,
            model_deployment_params=model_deployment_params,
            preferred_explanation_method=preferred_explanation_method,
            custom_explanation_names=custom_explanation_names,
            binary_classification_threshold=binary_classification_threshold,
            ranking_top_k=ranking_top_k,
            group_by=group_by,
            fall_back=fall_back,
            missing_value_encodings=missing_value_encodings,
            tree_shap_enabled=tree_shap_enabled,
            custom_features=custom_features,
            is_binary_ranking_model=is_binary_ranking_model,
            data_type_version=dataset_info.data_type_version,
        )

    @staticmethod
    def get_summary_dataframes_dict(model_info):
        """Returns a dictionary of DataFrames summarizing the
        ModelInfo's inputs, outputs, and if they exist, metadata
        and decisions"""

        summary_dict = dict()

        summary_dict['inputs'] = _summary_dataframe_for_columns(model_info.inputs)

        summary_dict['outputs'] = _summary_dataframe_for_columns(model_info.outputs)

        if model_info.metadata:
            summary_dict['metadata'] = _summary_dataframe_for_columns(
                model_info.metadata
            )
        if model_info.decisions:
            summary_dict['decisions'] = _summary_dataframe_for_columns(
                model_info.decisions
            )
        if model_info.targets:
            summary_dict['targets'] = _summary_dataframe_for_columns(model_info.targets)

        if model_info.custom_features:
            summary_dict['custom_features'] = _summary_dataframe_for_custom_features(
                model_info.custom_features
            )

        return summary_dict

    @staticmethod
    def check_binary_target(target_column):
        return (
            int(target_column.value_range_max) == 1
            and int(target_column.value_range_min) in [0, -1]
        ) or (
            target_column.data_type.value == DataType.INTEGER.value
            and target_column.value_range_max - target_column.value_range_min == 1
        )

    @staticmethod
    def calculate_outputs(
        outputs: Any, dataset_info: DatasetInfo, task: ModelTask
    ) -> dict:
        o_min, o_max = float('inf'), -float('inf')
        if type(outputs) == dict:
            pred_name = next(iter(outputs))
            if len(outputs[pred_name]) == 2:
                o_min, o_max = sorted(outputs[pred_name])
        else:
            pred_name = outputs[-1]
        try:
            pred_min, pred_max = (
                dataset_info[pred_name].value_range_min,
                dataset_info[pred_name].value_range_max,
            )
        except KeyError:
            pred_min, pred_max = float('inf'), -float('inf')
            LOG.warning(
                f'WARNING: outputs name {pred_name} can not be found in the dataset. Use user-entered'
                'range for outputs'
            )
        # if both user-defined range and data prediction present, use the max range
        range_min, range_max = float(min(o_min, pred_min)), float(
            max(float(o_max), pred_max)
        )
        # if Neither the user input nor the column gives a range, raise value error
        if range_min == float('inf') or range_max == -float('inf'):
            if task and task.value == ModelTask.BINARY_CLASSIFICATION.value:
                range_min, range_max = 0.0, 1.0
            else:
                raise ValueError(
                    f'Outputs name {pred_name} can not be found in the dataset and the user-entered '
                    'range for outputs is not valid. For regression or ranking task, outputs must be a '
                    'dictionary with the range: {output_name: (min_value, max_value)}. For binary '
                    'classification, please specify Model_task. '
                )
        return {pred_name: (range_min, range_max)}

    @staticmethod
    def ranking_cls_inference(
        dataset_info,
        target_column,
        categorical_target_class_details,
        outputs,
        ranking_top_k,
        group_by,
    ):
        if outputs:
            output_names = ModelInfo.calculate_outputs(
                outputs=outputs, dataset_info=dataset_info, task=ModelTask.RANKING
            )
        else:
            raise ValueError(
                'For RANKING tasks, Argument outputs is required in format'
                '"{column_name: (min_value, max_value)}"  or "{column_name:[]}" where column_name can be '
                'found in the dataset. '
            )

        categorical_target_class_details = (
            np.array(categorical_target_class_details).flatten().tolist()
        )
        if target_column.data_type.is_numeric() and ModelInfo.check_binary_target(
            target_column
        ):
            target_class_order = [
                int(target_column.value_range_min),
                int(target_column.value_range_max),
            ]
            if (
                categorical_target_class_details
                and sorted(categorical_target_class_details) != target_class_order
            ):
                LOG.warning(
                    'Warning: categorical_target_class_details does not match numeric binary target.'
                    f'Ignore and use inferred {target_class_order}'
                )
        else:
            if categorical_target_class_details[0] is None:
                if not target_column.possible_values:
                    raise ValueError(
                        'Categorical_target_class_details must be defined for task type = RANKING for non-binary target as a graded relevance target'
                    )
                if len(target_column.possible_values) == 2:
                    if target_column.data_type.value == DataType.BOOLEAN.value:
                        categorical_target_class_details = [False, True]
                    else:
                        raise ValueError(
                            'Categorical_target_class_details must be defined for task type = RANKING for categorical target'
                        )
                else:
                    raise ValueError(
                        'Categorical_target_class_details must be defined for task type = RANKING for graded relevance target'
                    )
            if not target_column.data_type.is_numeric():
                assert (
                    target_column.possible_values is not None
                ), 'For categorical target, target_column.possible_values unexpectedly None'
                if sorted(target_column.possible_values) != sorted(
                    categorical_target_class_details
                ):
                    raise ValueError(
                        f'Categorical_target_class_details does not have the same elements as target column {target_column.name}'
                    )
            else:
                if target_column.value_range_max != max(
                    categorical_target_class_details
                ) or target_column.value_range_min != min(
                    categorical_target_class_details
                ):
                    raise ValueError(
                        f'Min and max of Categorical_target_class_details does not match target column {target_column.name}'
                    )
            target_class_order = categorical_target_class_details

        try:
            ranking_top_k = int(ranking_top_k)  # type: ignore
        except Exception:
            # Default to 50
            LOG.warning('No `ranking_top_k` specified, defaulting to 50')
            ranking_top_k = 50
        if group_by is None:
            raise ValueError('The argument group_by cannot be empty for Ranking models')
        if isinstance(group_by, list):
            group_by = group_by[0]
        if not isinstance(group_by, str):
            raise ValueError('The argument group_by has to be a string.')

        is_binary_ranking_model = len(target_class_order) == 2
        return (
            output_names,
            target_class_order,
            ranking_top_k,
            group_by,
            is_binary_ranking_model,
        )

    def _repr_html_(self):
        summary_dict = ModelInfo.get_summary_dataframes_dict(self)
        class_order = (
            f'  target_class_order: {self.target_class_order}\n'
            if self.target_class_order is not None
            else ''
        )

        algorithm_info = (
            f'  framework: {self.algorithm}\n' if self.algorithm is not None else ''
        )
        framework_info = (
            f'  framework: {self.framework}\n' if self.framework is not None else ''
        )

        misc_info = json.dumps(self.misc, indent=2)
        target_info = (
            f"<hr>targets:{summary_dict['targets']._repr_html_()}"
            if self.targets is not None
            else ''
        )
        decisions_info = (
            f"<hr>decisions:{summary_dict['decisions']._repr_html_()}"
            if self.decisions is not None
            else ''
        )
        metadata_info = (
            f"<hr>metadata:{summary_dict['metadata']._repr_html_()}"
            if self.metadata is not None
            else ''
        )

        fall_back_info = (
            f'  fall_back: {self.fall_back}\n' if self.fall_back is not None else ''
        )
        missing_value_encodings_info = (
            f'  missing_value_encodings: {self.missing_value_encodings}\n'
            if self.missing_value_encodings is not None
            else ''
        )
        custom_features = (
            f'<hr>custom features:{summary_dict["custom_features"]._repr_html_()}'
            if self.custom_features is not None
            else ''
        )
        data_type_version_info = (
            f'  data_type_version: {self.data_type_version}\n'
            if self.data_type_version is not None
            else ''
        )
        return (
            f'<div style="border: thin solid rgb(41, 57, 141); padding: 10px;">'
            f'<h3 style="text-align: center; margin: auto;">ModelInfo\n</h3><pre>'
            f'  display_name: {self.display_name}\n'
            f'  description: {self.description}\n'
            f'  input_type: {self.input_type}\n'
            f'  model_task: {self.model_task}\n'
            f'{class_order}'
            f'  preferred_explanation: {self.preferred_explanation_method}\n'
            f'  custom_explanation_names: {self.custom_explanation_names}\n'
            f'{algorithm_info}'
            f'{framework_info}'
            f'{fall_back_info}'
            f'{missing_value_encodings_info}'
            f'  misc: {misc_info}</pre>'
            f'{target_info}'
            f"<hr>inputs:{summary_dict['inputs']._repr_html_()}"
            f"<hr>outputs:{summary_dict['outputs']._repr_html_()}"
            f'{custom_features}'
            f'{decisions_info}'
            f'{metadata_info}'
            f'{data_type_version_info}'
            f'</div>'
        )

    def __repr__(self):
        summary_dict = ModelInfo.get_summary_dataframes_dict(self)
        input_info = textwrap.indent(repr(summary_dict['inputs']), '    ')
        output_info = textwrap.indent(repr(summary_dict['outputs']), '    ')
        custom_features_info = (
            f'  custom features:\n'
            f"{textwrap.indent(repr(summary_dict['custom_features']), '    ')}"
            if self.custom_features is not None
            else ''
        )
        class_order = (
            f'  target_class_order: {self.target_class_order}\n'
            if self.target_class_order is not None
            else ''
        )

        metadata_info = (
            f'  metadata:\n'
            f"{textwrap.indent(repr(summary_dict['metadata']), '    ')}"
            if self.metadata is not None
            else ''
        )

        decisions_info = (
            f'  decisions:\n'
            f"{textwrap.indent(repr(summary_dict['decisions']), '    ')}"
            if self.decisions is not None
            else ''
        )

        target_info = (
            f'  targets:\n' f"{textwrap.indent(repr(summary_dict['targets']), '    ')}"
            if self.targets is not None
            else ''
        )
        # target_info = f'  targets: {self.targets}\n' if self.targets is not None else ''
        algorithm_info = (
            f'  algorithm: {self.algorithm}\n' if self.algorithm is not None else ''
        )
        framework_info = (
            f'  framework: {self.framework}\n' if self.framework is not None else ''
        )

        fall_back_info = (
            f'  fall_back: {self.fall_back}\n' if self.fall_back is not None else ''
        )
        missing_value_encodings_info = (
            f'  missing_value_encodings: {self.missing_value_encodings}\n'
            if self.missing_value_encodings is not None
            else ''
        )
        data_type_version_info = (
            f'  data_type_version: {self.data_type_version}\n'
            if self.data_type_version is not None
            else ''
        )
        misc_info = textwrap.indent(json.dumps(self.misc, indent=2), '    ')
        return (
            f'ModelInfo:\n'
            f'  display_name: {self.display_name}\n'
            f'  description: {self.description}\n'
            f'  input_type: {self.input_type}\n'
            f'  model_task: {self.model_task}\n'
            f'{class_order}'
            f'  preferred_explanation: {self.preferred_explanation_method}\n'
            f'  custom_explanation_names: {self.custom_explanation_names}\n'
            f'  inputs:\n'
            f'{input_info}\n'
            f'  outputs:\n'
            f'{output_info}\n'
            f'{custom_features_info}\n'
            f'{metadata_info}\n'
            f'{decisions_info}\n'
            f'{target_info}'
            f'{algorithm_info}'
            f'{framework_info}'
            f'{fall_back_info}'
            f'{missing_value_encodings_info}'
            f'{data_type_version_info}'
            f'  misc:\n'
            f'{misc_info}'
        )

    def validate(self):
        sanitized_name_dict = dict()
        validate_sanitized_names(self.inputs, sanitized_name_dict)
        validate_sanitized_names(self.outputs, sanitized_name_dict)
        validate_sanitized_names(self.targets, sanitized_name_dict)
        validate_sanitized_names(self.metadata, sanitized_name_dict)
        validate_sanitized_names(self.decisions, sanitized_name_dict)

    def get_all_cols(self):
        result = copy.deepcopy(self.inputs)
        if self.outputs is not None:
            result += self.outputs
        if self.metadata is not None:
            result += self.metadata
        if self.decisions is not None:
            result += self.decisions
        if self.targets is not None:
            result += self.targets
        return result

    def get_col(self, col_name):
        for col in self.get_all_cols():
            if col.name == col_name:
                return col
        return None


CURRENT_SCHEMA_VERSION = 0.1
DEFUNCT_MODELINFO_SCHEMA_VERSION = '0.0'
CURRENT_MODELINFO_SCHEMA_VERSION = '1.2'
VALID_OPERATORS = ['==', '>=', '<=', '>', '<']


class SegmentInfo:
    def __init__(
        self,
        project_id,
        model_id,
        segment_id,
        filter=None,
        subsegments=None,
        metrics=None,
        description='',
    ):
        """
        schema-version 0.1
        """
        type_enforce('project_id', project_id, str)
        type_enforce('model_id', model_id, str)
        type_enforce('segment_id', segment_id, str)
        self.schema_version = CURRENT_SCHEMA_VERSION
        self.creator_version = f'FIDDLER-CLIENT-v{__version__}'
        self.project = project_id
        self.model = model_id
        # self.dataset = ''
        self.segment_id = segment_id
        self.description = description
        if filter is None:
            self.filter = ''
        else:
            self.filter = filter
        if subsegments is None:
            self.subsegments = {}
        else:
            self.subsegments = subsegments
        if metrics is None:
            self.metrics = []
        else:
            raise MalformedSchemaException(
                f'Segment specific metrics have not yet been implemented (schema-version {CURRENT_SCHEMA_VERSION}).'
            )
            self.metrics = metrics

    def get_filter(self):
        """
        schema-version 0.1
        """
        # by default, every event should pass through the filter:
        result = 'True'
        for feature, operator, value in self.filter:
            if operator == '==':
                result += f' & (Eq({feature}, {value}))'
            else:
                result += f' & ({feature} {operator} {value})'
        return result

    def get_subsegments(self):
        """
        schema-version 0.1
        """
        return self.subsegments

    def get_metrics(self):
        """
        schema-version 0.1
        """
        return self.metrics

    def to_dict(self) -> Dict:
        """
        Serialize object to a JSON-friendly dict.

        This implementation works for schema-version 0.1
        """
        return self.__dict__
        # TODO: bulletproofing

    @classmethod
    def from_dict(cls, deserialized_json: dict):
        """
        Transform deserialized JSON-friendly dict into a SegmentInfo object.

        This implementation works for schema-version 0.1
        """
        seg_info = cls(
            project_id=deserialized_json['project'],
            model_id=deserialized_json['model'],
            segment_id=deserialized_json['segment_id'],
            filter=deserialized_json['filter'],
            subsegments=deserialized_json['subsegments'],
            description=deserialized_json['description'],
        )
        seg_info.schema_version = deserialized_json['schema_version']
        seg_info.creator_version = deserialized_json['creator_version']
        seg_info.metrics = deserialized_json['metrics']
        return seg_info
        # TODO: bulletproofing to check additional keys don't exist

    def validate(self, model_info):
        """
        Ensure that filters, subsegments, metrics, etc conform to schema-version 0.1.
        """
        result = True
        if len(self.filter) == 0 and len(self.subsegments) == 0:
            raise MalformedSchemaException(
                'Both filter and subsegments are missing from SegmentInfo - please specify at least one.'
            )
        result = result and self._validate_filter_format(model_info)
        result = result and self._validate_subsegments_format(model_info)
        result = result and self._validate_metrics_format(model_info)
        return result

    def _validate_filter_format(self, model_info):
        """
        Validate filters according to schema-version 0.1.
        """
        for filter in self.filter:
            if len(filter) != 3:
                raise MalformedSchemaException(
                    f'Could not parse filters, is {filter} a 3-tuple?'
                )
            feature, operator, value = filter
            if operator not in VALID_OPERATORS:
                raise MalformedSchemaException(
                    f'Could not parse operator in {filter}, please ensure the middle element is from {VALID_OPERATORS}.'
                )
            col = model_info.get_col(feature)
            if col in model_info.targets:  # disallow targets
                raise MalformedSchemaException(
                    f'Cannot include target {col.name} in segment definition.'
                )
            if col is None:
                raise MalformedSchemaException(
                    f'Could not find column {feature} in the ModelInfo.'
                )
            if col.possible_values is not None:
                if operator != '==':
                    raise MalformedSchemaException(
                        f'Only == operation is supported ({operator} is unsupported) for non-numeric features like {feature}.'
                    )
                if value not in col.possible_values:
                    raise MalformedSchemaException(
                        f'Feature {feature} can never take value {value} according to the ModelInfo.'
                    )
            else:
                if value < col.value_range_min or value > col.value_range_max:
                    raise MalformedSchemaException(
                        f'Segment value {value} is defined beyond the permitted value range for feature {feature}: [{col.value_range_min}, {col.value_range_max}].'
                    )
        return True

    def _validate_subsegments_format(self, model_info):
        """
        Validate subsegments according to schema-version 0.1.
        """
        for feature in self.subsegments:
            col = model_info.get_col(feature)
            if col in model_info.targets:  # disallow targets
                raise MalformedSchemaException(
                    f'Cannot include target {col.name} in segment definition.'
                )
            if col is None:
                raise MalformedSchemaException(
                    f'Could not find column {feature} in the ModelInfo.'
                )
            if col.possible_values is not None:
                for value in self.subsegments[feature]:
                    if value not in col.possible_values:
                        raise MalformedSchemaException(
                            f'Could not find group-by value {value} in {feature}.possible_values'
                        )
            else:
                min, max = float('inf'), float('-inf')
                curr = self.subsegments[feature][0] - 1
                for value in self.subsegments[feature]:
                    if value <= curr:
                        raise MalformedSchemaException(
                            f'Group-by for {feature} should be monotonically non-decreasing.'
                        )
                    if value < min:
                        min = value
                    if value > max:
                        max = value
                    curr = value
                if min < col.value_range_min:
                    raise MalformedSchemaException(
                        f'Group-by for {feature} has min value < min value from ModelInfo.'
                    )
                if max > col.value_range_max:
                    raise MalformedSchemaException(
                        f'Group-by for {feature} has max value < max value from ModelInfo.'
                    )
        return True

    def _validate_metrics_format(self, model_info):
        """
        Validate metrics according to schema-version 0.1.
        """
        if len(self.metrics) != 0:
            raise MalformedSchemaException(
                f'SegmentInfo cannot yet specify metrics (schema-version {CURRENT_SCHEMA_VERSION}).'
            )
        else:
            return True
        # TODO: allow generic metrics like traffic count, etc
        valid_metrics = []
        # ToDo: add ranking
        if model_info.model_task == ModelTask.BINARY_CLASSIFICATION:
            valid_metrics += [m.value for m in BuiltInMetrics.get_binary()]
        elif model_info.model_task == ModelTask.MULTICLASS_CLASSIFICATION:
            valid_metrics += [m.value for m in BuiltInMetrics.get_multiclass()]
        elif model_info.model_task == ModelTask.REGRESSION:
            valid_metrics += [m.value for m in BuiltInMetrics.get_regression()]
        else:
            raise MalformedSchemaException(
                f'ModelInfo has an invalid model_task: {model_info.model_task}, for which there is no segment support.'
            )
        for metric in self.metrics:
            if metric not in valid_metrics:
                raise MalformedSchemaException(
                    f'Unknown metric {metric} for specified model_task {model_info.model_task}.'
                )
        return True


def _summary_dataframe_for_columns(
    columns: Sequence[Column], placeholder=''
) -> pd.DataFrame:
    """
        Example:
                 column     dtype count(possible_values) is_nullable            value_range
    0       CreditScore   INTEGER                              False        376 - 850
    1         Geography  CATEGORY                      3       False
    2            Gender  CATEGORY                      2       False
    3               Age   INTEGER                              False         18 - 82
    4            Tenure   INTEGER                              False          0 - 10
    5           Balance     FLOAT                              False        0.0 - 213,100.0
    6     NumOfProducts   INTEGER                              False          1 - 4
    7         HasCrCard  CATEGORY                      2       False
    8    IsActiveMember  CATEGORY                      2       False
    9   EstimatedSalary     FLOAT                              False      371.1 - 199,700.0
    10          Churned  CATEGORY                      2       False

    """  # noqa E501
    column_names = []
    column_dtypes = []
    n_possible_values = []
    is_nullable = []
    mins: List[Any] = []
    maxes: List[Any] = []
    for column in columns:
        column_names.append(column.name)
        column_dtypes.append(column.data_type.name)
        n_possible_values.append(
            len(column.possible_values)
            if column.possible_values is not None
            else placeholder
        )
        is_nullable.append(
            str(column.is_nullable) if column.is_nullable is not None else placeholder
        )
        if not column.data_type.is_numeric():
            mins.append(None)
            maxes.append(None)
        else:
            min_str = (
                prettyprint_number(column.value_range_min)
                if column.value_range_min is not None
                else '*'
            )
            max_str = (
                prettyprint_number(column.value_range_max)
                if column.value_range_max is not None
                else '*'
            )
            mins.append(min_str)
            maxes.append(max_str)
    range_pad_len = max(len(x) if x is not None else 0 for x in mins + maxes)
    value_range = [
        (placeholder if x is None else f'{x:>{range_pad_len}} - {y:<{range_pad_len}}')
        for x, y in zip(mins, maxes)
    ]
    return pd.DataFrame(
        {
            'column': column_names,
            'dtype': column_dtypes,
            'count(possible_values)': n_possible_values,
            'is_nullable': is_nullable,
            'value_range': value_range,
        }
    )


def _summary_dataframe_for_custom_features(
    custom_features: Sequence[CustomFeature], placeholder=''
) -> pd.DataFrame:
    """
        Example:
        name    column                      type                transformation  n_clusters  monitor
    0   F1      'col_name1'                 FROM_TEXT           'Word2vec'      3           True
    1   F2      ['col_name2','col_name3']   FROM_COLUMNS        None            4           True
    2   F3      'col_name4'                 FROM_VECTOR         None            auto        True
    3   F4      'col_name5'                 FROM_DICTIONARY     None            auto        True
    """  # noqa E501
    names = []
    columns = []
    types = []
    transformations = []
    clusters = []
    monitors = []

    for feature in custom_features:
        names.append(feature.name)
        columns.append(feature.columns)
        types.append(feature.type.name)
        transformations.append(feature.transformation)
        if feature.n_clusters is not None:
            clusters.append(feature.n_clusters)
        else:
            clusters.append('auto')
        monitors.append(feature.monitor)

    return pd.DataFrame(
        {
            'name': names,
            'column': columns,
            'type': types,
            'transformation': transformations,
            'n_clusters': clusters,
            'monitor': monitors,
        }
    )


@enum.unique
class BaselineType(str, enum.Enum):
    PRE_PRODUCTION = 'PRE_PRODUCTION'
    STATIC_PRODUCTION = 'STATIC_PRODUCTION'
    ROLLING_PRODUCTION = 'ROLLING_PRODUCTION'

    def __str__(self) -> str:
        return self.value


@enum.unique
class WindowSize(enum.IntEnum):
    FIVE_MINUTES = 300
    ONE_HOUR = 3600
    ONE_DAY = 86400
    ONE_WEEK = 604800
    ONE_MONTH = 2592000

    def __str__(self) -> str:
        return self.name

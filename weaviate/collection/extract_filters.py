import uuid as uuid_lib
from typing import Any, Dict, List, Optional, cast

from weaviate.collection.classes.filters import (
    _Filters,
    _FilterAnd,
    _FilterOr,
    _FilterValue,
    FilterValues,
)
from weaviate.util import _datetime_to_string
from weaviate.weaviate_types import TIME
from weaviate_grpc import weaviate_pb2


class FilterToGRPC:
    @staticmethod
    def convert(weav_filter: Optional[_Filters]) -> Optional[weaviate_pb2.Filters]:
        if weav_filter is None:
            return None

        if isinstance(weav_filter, _FilterValue):
            return FilterToGRPC.__value_filter(weav_filter)
        else:
            return FilterToGRPC.__and_or_filter(weav_filter)

    @staticmethod
    def __value_filter(weav_filter: _FilterValue) -> weaviate_pb2.Filters:

        return weaviate_pb2.Filters(
            operator=weav_filter.operator._to_grpc(),
            value_text=FilterToGRPC.__filter_to_text(weav_filter.value),
            value_int=weav_filter.value if isinstance(weav_filter.value, int) else None,
            value_boolean=weav_filter.value if isinstance(weav_filter.value, bool) else None,  # type: ignore
            value_number=weav_filter.value if isinstance(weav_filter.value, float) else None,
            value_int_array=FilterToGRPC.__filter_to_int_list(weav_filter.value),
            value_number_array=FilterToGRPC.__filter_to_float_list(weav_filter.value),
            value_text_array=FilterToGRPC.__filter_to_text_list(weav_filter.value),
            value_boolean_array=FilterToGRPC.__filter_to_bool_list(weav_filter.value),
            on=weav_filter.path if isinstance(weav_filter.path, list) else [weav_filter.path],
        )

    @staticmethod
    def __filter_to_text(value: FilterValues) -> Optional[str]:
        if not (
            isinstance(value, TIME) or isinstance(value, str) or isinstance(value, uuid_lib.UUID)
        ):
            return None

        if isinstance(value, str):
            return value

        if isinstance(value, uuid_lib.UUID):
            return str(value)

        return _datetime_to_string(value)

    @staticmethod
    def __filter_to_text_list(value: FilterValues) -> Optional[weaviate_pb2.TextArray]:
        if not isinstance(value, list) or not (
            isinstance(value[0], TIME)
            or isinstance(value[0], str)
            or isinstance(value[0], uuid_lib.UUID)
        ):
            return None

        if isinstance(value[0], str):
            value_list = value
        elif isinstance(value[0], uuid_lib.UUID):
            value_list = [str(uid) for uid in value]
        else:
            dates = cast(List[TIME], value)
            value_list = [_datetime_to_string(date) for date in dates]

        return weaviate_pb2.TextArray(values=cast(List[str], value_list))

    @staticmethod
    def __filter_to_bool_list(value: FilterValues) -> Optional[weaviate_pb2.BooleanArray]:
        if not isinstance(value, list) or not isinstance(value[0], bool):
            return None

        return weaviate_pb2.BooleanArray(values=cast(List[bool], value))

    @staticmethod
    def __filter_to_float_list(value: FilterValues) -> Optional[weaviate_pb2.NumberArray]:
        if not isinstance(value, list) or not isinstance(value[0], float):
            return None

        return weaviate_pb2.NumberArray(values=cast(List[float], value))

    @staticmethod
    def __filter_to_int_list(value: FilterValues) -> Optional[weaviate_pb2.IntArray]:
        if not isinstance(value, list) or not isinstance(value[0], int):
            return None

        return weaviate_pb2.IntArray(values=cast(List[int], value))

    @staticmethod
    def __and_or_filter(weav_filter: _Filters) -> Optional[weaviate_pb2.Filters]:
        assert isinstance(weav_filter, _FilterAnd) or isinstance(weav_filter, _FilterOr)
        return weaviate_pb2.Filters(
            operator=weav_filter.operator._to_grpc(),
            filters=[
                filter_
                for single_filter in weav_filter.filters
                if (filter_ := FilterToGRPC.convert(single_filter)) is not None
            ],
        )


class FilterToREST:
    @staticmethod
    def convert(weav_filter: Optional[_Filters]) -> Optional[Dict[str, Any]]:
        if weav_filter is None:
            return None
        if isinstance(weav_filter, _FilterValue):
            return FilterToREST.__value_filter(weav_filter)
        else:
            return FilterToREST.__and_or_filter(weav_filter)

    @staticmethod
    def __value_filter(weav_filter: _FilterValue) -> Dict[str, Any]:
        return {
            "operator": weav_filter.operator.value,
            "path": weav_filter.path if isinstance(weav_filter.path, list) else [weav_filter.path],
            **FilterToREST.__parse_filter(weav_filter.value),
        }

    @staticmethod
    def __parse_filter(value: FilterValues) -> Dict[str, Any]:
        if isinstance(value, str):
            return {"valueText": value}
        if isinstance(value, uuid_lib.UUID):
            return {"valueText": str(value)}
        if isinstance(value, TIME):
            return {"valueDate": _datetime_to_string(value)}
        if isinstance(value, bool):
            return {"valueBoolean": value}
        if isinstance(value, int):
            return {"valueInt": value}
        if isinstance(value, float):
            return {"valueNumber": value}
        if isinstance(value, list):
            if isinstance(value[0], str):
                return {"valueTextArray": value}
            if isinstance(value[0], uuid_lib.UUID):
                return {"valueTextArray": [str(val) for val in value]}
            if isinstance(value[0], TIME):
                return {"valueDateArray": [_datetime_to_string(cast(TIME, val)) for val in value]}
            if isinstance(value[0], bool):
                return {"valueBooleanArray": value}
            if isinstance(value[0], int):
                return {"valueIntArray": value}
            if isinstance(value[0], float):
                return {"valueNumberArray": value}
        return {}

    @staticmethod
    def __and_or_filter(weav_filter: _Filters) -> Dict[str, Any]:
        assert isinstance(weav_filter, _FilterAnd) or isinstance(weav_filter, _FilterOr)
        return {
            "operator": weav_filter.operator.value,
            "operands": [
                filter_
                for single_filter in weav_filter.filters
                if (filter_ := FilterToREST.convert(single_filter)) is not None
            ],
        }

"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Configurations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    NUM_RESPONSES_FIELD_NUMBER: builtins.int
    DATA_SIZE_FIELD_NUMBER: builtins.int
    CUMULATIVE_DATA_FIELD_NUMBER: builtins.int
    RESPONSE_INTERVAL_IN_MS_FIELD_NUMBER: builtins.int
    ERROR_ON_INDEX_FIELD_NUMBER: builtins.int
    name: builtins.str
    num_responses: builtins.int
    data_size: builtins.int
    cumulative_data: builtins.bool
    response_interval_in_ms: builtins.int
    error_on_index: builtins.int
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        num_responses: builtins.int = ...,
        data_size: builtins.int = ...,
        cumulative_data: builtins.bool = ...,
        response_interval_in_ms: builtins.int = ...,
        error_on_index: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cumulative_data", b"cumulative_data", "data_size", b"data_size", "error_on_index", b"error_on_index", "name", b"name", "num_responses", b"num_responses", "response_interval_in_ms", b"response_interval_in_ms"]) -> None: ...

global___Configurations = Configurations

@typing.final
class Outputs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    name: builtins.str
    index: builtins.int
    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        index: builtins.int = ...,
        data: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data", b"data", "index", b"index", "name", b"name"]) -> None: ...

global___Outputs = Outputs

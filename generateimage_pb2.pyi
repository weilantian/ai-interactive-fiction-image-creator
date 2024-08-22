from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImageGenerationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PENDING: _ClassVar[ImageGenerationStatus]
    GENERATING: _ClassVar[ImageGenerationStatus]
    GENERATED: _ClassVar[ImageGenerationStatus]
    FAILED: _ClassVar[ImageGenerationStatus]
PENDING: ImageGenerationStatus
GENERATING: ImageGenerationStatus
GENERATED: ImageGenerationStatus
FAILED: ImageGenerationStatus

class CanGenerateResponse(_message.Message):
    __slots__ = ("canGenerate",)
    CANGENERATE_FIELD_NUMBER: _ClassVar[int]
    canGenerate: bool
    def __init__(self, canGenerate: bool = ...) -> None: ...

class GenerateImageRequest(_message.Message):
    __slots__ = ("prompt",)
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    def __init__(self, prompt: _Optional[str] = ...) -> None: ...

class GenerateImageRequestResponse(_message.Message):
    __slots__ = ("status", "taskId", "errorMsg")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    ERRORMSG_FIELD_NUMBER: _ClassVar[int]
    status: ImageGenerationStatus
    taskId: str
    errorMsg: str
    def __init__(self, status: _Optional[_Union[ImageGenerationStatus, str]] = ..., taskId: _Optional[str] = ..., errorMsg: _Optional[str] = ...) -> None: ...

class CheckGenerationStatusRequest(_message.Message):
    __slots__ = ("taskId",)
    TASKID_FIELD_NUMBER: _ClassVar[int]
    taskId: str
    def __init__(self, taskId: _Optional[str] = ...) -> None: ...

class CheckGenerationStatusResponse(_message.Message):
    __slots__ = ("taskId", "status", "errorMsg")
    TASKID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERRORMSG_FIELD_NUMBER: _ClassVar[int]
    taskId: str
    status: ImageGenerationStatus
    errorMsg: str
    def __init__(self, taskId: _Optional[str] = ..., status: _Optional[_Union[ImageGenerationStatus, str]] = ..., errorMsg: _Optional[str] = ...) -> None: ...

class RetrieveGenerateImageRequest(_message.Message):
    __slots__ = ("taskId",)
    TASKID_FIELD_NUMBER: _ClassVar[int]
    taskId: str
    def __init__(self, taskId: _Optional[str] = ...) -> None: ...

class RetrieveGeneratedImageResponse(_message.Message):
    __slots__ = ("taskId", "imgUrl", "success", "errorMsg")
    TASKID_FIELD_NUMBER: _ClassVar[int]
    IMGURL_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERRORMSG_FIELD_NUMBER: _ClassVar[int]
    taskId: str
    imgUrl: str
    success: bool
    errorMsg: str
    def __init__(self, taskId: _Optional[str] = ..., imgUrl: _Optional[str] = ..., success: bool = ..., errorMsg: _Optional[str] = ...) -> None: ...

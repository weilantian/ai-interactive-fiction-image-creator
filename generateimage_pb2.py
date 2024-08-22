# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: generateimage.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'generateimage.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13generateimage.proto\x12\rgenerateImage\x1a\x1bgoogle/protobuf/empty.proto\"*\n\x13\x43\x61nGenerateResponse\x12\x13\n\x0b\x63\x61nGenerate\x18\x01 \x01(\x08\"&\n\x14GenerateImageRequest\x12\x0e\n\x06prompt\x18\x01 \x01(\t\"v\n\x1cGenerateImageRequestResponse\x12\x34\n\x06status\x18\x01 \x01(\x0e\x32$.generateImage.ImageGenerationStatus\x12\x0e\n\x06taskId\x18\x02 \x01(\t\x12\x10\n\x08\x65rrorMsg\x18\x03 \x01(\t\".\n\x1c\x43heckGenerationStatusRequest\x12\x0e\n\x06taskId\x18\x01 \x01(\t\"w\n\x1d\x43heckGenerationStatusResponse\x12\x0e\n\x06taskId\x18\x01 \x01(\t\x12\x34\n\x06status\x18\x02 \x01(\x0e\x32$.generateImage.ImageGenerationStatus\x12\x10\n\x08\x65rrorMsg\x18\x03 \x01(\t\".\n\x1cRetrieveGenerateImageRequest\x12\x0e\n\x06taskId\x18\x01 \x01(\t\"c\n\x1eRetrieveGeneratedImageResponse\x12\x0e\n\x06taskId\x18\x01 \x01(\t\x12\x0e\n\x06imgUrl\x18\x02 \x01(\t\x12\x0f\n\x07success\x18\x03 \x01(\x08\x12\x10\n\x08\x65rrorMsg\x18\x04 \x01(\t*O\n\x15ImageGenerationStatus\x12\x0b\n\x07PENDING\x10\x00\x12\x0e\n\nGENERATING\x10\x01\x12\r\n\tGENERATED\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x32\xa7\x03\n\rGenerateImage\x12I\n\x0b\x43\x61nGenerate\x12\x16.google.protobuf.Empty\x1a\".generateImage.CanGenerateResponse\x12\x61\n\rGenerateImage\x12#.generateImage.GenerateImageRequest\x1a+.generateImage.GenerateImageRequestResponse\x12r\n\x15\x43heckGenerationStatus\x12+.generateImage.CheckGenerationStatusRequest\x1a,.generateImage.CheckGenerationStatusResponse\x12t\n\x16RetrieveGeneratedImage\x12+.generateImage.RetrieveGenerateImageRequest\x1a-.generateImage.RetrieveGeneratedImageResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'generateimage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_IMAGEGENERATIONSTATUS']._serialized_start=589
  _globals['_IMAGEGENERATIONSTATUS']._serialized_end=668
  _globals['_CANGENERATERESPONSE']._serialized_start=67
  _globals['_CANGENERATERESPONSE']._serialized_end=109
  _globals['_GENERATEIMAGEREQUEST']._serialized_start=111
  _globals['_GENERATEIMAGEREQUEST']._serialized_end=149
  _globals['_GENERATEIMAGEREQUESTRESPONSE']._serialized_start=151
  _globals['_GENERATEIMAGEREQUESTRESPONSE']._serialized_end=269
  _globals['_CHECKGENERATIONSTATUSREQUEST']._serialized_start=271
  _globals['_CHECKGENERATIONSTATUSREQUEST']._serialized_end=317
  _globals['_CHECKGENERATIONSTATUSRESPONSE']._serialized_start=319
  _globals['_CHECKGENERATIONSTATUSRESPONSE']._serialized_end=438
  _globals['_RETRIEVEGENERATEIMAGEREQUEST']._serialized_start=440
  _globals['_RETRIEVEGENERATEIMAGEREQUEST']._serialized_end=486
  _globals['_RETRIEVEGENERATEDIMAGERESPONSE']._serialized_start=488
  _globals['_RETRIEVEGENERATEDIMAGERESPONSE']._serialized_end=587
  _globals['_GENERATEIMAGE']._serialized_start=671
  _globals['_GENERATEIMAGE']._serialized_end=1094
# @@protoc_insertion_point(module_scope)

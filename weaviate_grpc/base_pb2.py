# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nbase.proto\x12\x0cweaviategrpc\":\n\x15NumberArrayProperties\x12\x0e\n\x06values\x18\x01 \x03(\x01\x12\x11\n\tprop_name\x18\x02 \x01(\t\"7\n\x12IntArrayProperties\x12\x0e\n\x06values\x18\x01 \x03(\x03\x12\x11\n\tprop_name\x18\x02 \x01(\t\"8\n\x13TextArrayProperties\x12\x0e\n\x06values\x18\x01 \x03(\t\x12\x11\n\tprop_name\x18\x02 \x01(\t\";\n\x16\x42ooleanArrayProperties\x12\x0e\n\x06values\x18\x01 \x03(\x08\x12\x11\n\tprop_name\x18\x02 \x01(\t*\x89\x01\n\x10\x43onsistencyLevel\x12!\n\x1d\x43ONSISTENCY_LEVEL_UNSPECIFIED\x10\x00\x12\x19\n\x15\x43ONSISTENCY_LEVEL_ONE\x10\x01\x12\x1c\n\x18\x43ONSISTENCY_LEVEL_QUORUM\x10\x02\x12\x19\n\x15\x43ONSISTENCY_LEVEL_ALL\x10\x03\x42\x64\n\x19io.weaviate.grpc.protocolB\x11WeaviateProtoBaseZ4github.com/weaviate/weaviate/grpc/generated;protocolb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031io.weaviate.grpc.protocolB\021WeaviateProtoBaseZ4github.com/weaviate/weaviate/grpc/generated;protocol'
  _globals['_CONSISTENCYLEVEL']._serialized_start=265
  _globals['_CONSISTENCYLEVEL']._serialized_end=402
  _globals['_NUMBERARRAYPROPERTIES']._serialized_start=28
  _globals['_NUMBERARRAYPROPERTIES']._serialized_end=86
  _globals['_INTARRAYPROPERTIES']._serialized_start=88
  _globals['_INTARRAYPROPERTIES']._serialized_end=143
  _globals['_TEXTARRAYPROPERTIES']._serialized_start=145
  _globals['_TEXTARRAYPROPERTIES']._serialized_end=201
  _globals['_BOOLEANARRAYPROPERTIES']._serialized_start=203
  _globals['_BOOLEANARRAYPROPERTIES']._serialized_end=262
# @@protoc_insertion_point(module_scope)
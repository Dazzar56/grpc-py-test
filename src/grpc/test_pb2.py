# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntest.proto\x12\x0btransaction\"C\n\nSumRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x12\n\ntime_start\x18\x02 \x01(\x03\x12\x10\n\x08time_end\x18\x03 \x01(\x03\"\x1c\n\x0bSumResponse\x12\r\n\x05total\x18\x01 \x01(\x02\x32H\n\x03Sum\x12\x41\n\nsum_amount\x12\x17.transaction.SumRequest\x1a\x18.transaction.SumResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'test_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SUMREQUEST']._serialized_start=27
  _globals['_SUMREQUEST']._serialized_end=94
  _globals['_SUMRESPONSE']._serialized_start=96
  _globals['_SUMRESPONSE']._serialized_end=124
  _globals['_SUM']._serialized_start=126
  _globals['_SUM']._serialized_end=198
# @@protoc_insertion_point(module_scope)

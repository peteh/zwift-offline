# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: login-response.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import per_session_info_pb2 as per__session__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14login-response.proto\x1a\x16per-session-info.proto\"E\n\rLoginResponse\x12\x15\n\rsession_state\x18\x01 \x02(\t\x12\x1d\n\x04info\x18\x02 \x02(\x0b\x32\x0f.PerSessionInfo')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'login_response_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOGINRESPONSE._serialized_start=48
  _LOGINRESPONSE._serialized_end=117
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/v1/model.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import kik_unofficial.protobuf.kik_options_pb2 as kik__options__pb2
import kik_unofficial.protobuf.protobuf_validation_pb2 as protobuf__validation__pb2
import kik_unofficial.protobuf.common_model_pb2 as common__model__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x63ommon/v1/model.proto\x12\tcommon.v1\x1a\x11kik_options.proto\x1a\x19protobuf_validation.proto\x1a\x12\x63ommon_model.proto\"@\n\nXiAliasJid\x12\x32\n\nlocal_part\x18\x01 \x01(\tB\x1e\xca\x9d%\x1a\x08\x01\x12\x16^[a-z0-9_-]{52}_[a|b]$\"\x86\x01\n\x17XiBareUserJidOrAliasJid\x12.\n\rbare_user_jid\x18\x01 \x01(\x0b\x32\x15.common.XiBareUserJidH\x00\x12/\n\x0e\x61lias_user_jid\x18\x02 \x01(\x0b\x32\x15.common.v1.XiAliasJidH\x00\x42\n\n\x08jid_type\"\xa0\x01\n\x08XiAnyJid\x12.\n\rbare_user_jid\x18\x01 \x01(\x0b\x32\x15.common.XiBareUserJidH\x00\x12/\n\x0e\x61lias_user_jid\x18\x02 \x01(\x0b\x32\x15.common.v1.XiAliasJidH\x00\x12\'\n\tgroup_jid\x18\x03 \x01(\x0b\x32\x12.common.XiGroupJidH\x00\x42\n\n\x08jid_type\"1\n\x0bXiKinUserId\x12\"\n\x02id\x18\x01 \x01(\tB\x16\xca\x9d%\x12\x08\x01\x12\x0e^[a-z2-7]{52}$\"j\n\tXiConvoId\x12\x30\n\none_to_one\x18\x01 \x01(\x0b\x32\x1a.common.v1.OneToOneConvoIdH\x00\x12#\n\x05group\x18\x02 \x01(\x0b\x32\x12.common.XiGroupJidH\x00\x42\x06\n\x04kind\"G\n\x0fOneToOneConvoId\x12\x34\n\x05users\x18\x01 \x03(\x0b\x32\x15.common.XiBareUserJidB\x0e\xca\x9d%\n\x08\x01x\x02\x80\x01\x02\x88\x01\x00\"O\n\x05XiJWT\x12\x46\n\x03jwt\x18\x01 \x01(\tB9\xca\x9d%5\x08\x01\x12\x31^[a-zA-Z0-9-_]+?.[a-zA-Z0-9-_]+?.[a-zA-Z0-9-_]+?$B{\n\x0e\x63om.kik.commonB\nModelProtoP\x01ZLgithub.com/kikinteractive/xiphias-model-common/generated/go/common/v1;common\xa0\x01\x01\xa2\x02\x03KPB\xaa\xa3*\x02\x08\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.v1.model_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016com.kik.commonB\nModelProtoP\001ZLgithub.com/kikinteractive/xiphias-model-common/generated/go/common/v1;common\240\001\001\242\002\003KPB\252\243*\002\010\001'
  _XIALIASJID.fields_by_name['local_part']._options = None
  _XIALIASJID.fields_by_name['local_part']._serialized_options = b'\312\235%\032\010\001\022\026^[a-z0-9_-]{52}_[a|b]$'
  _XIKINUSERID.fields_by_name['id']._options = None
  _XIKINUSERID.fields_by_name['id']._serialized_options = b'\312\235%\022\010\001\022\016^[a-z2-7]{52}$'
  _ONETOONECONVOID.fields_by_name['users']._options = None
  _ONETOONECONVOID.fields_by_name['users']._serialized_options = b'\312\235%\n\010\001x\002\200\001\002\210\001\000'
  _XIJWT.fields_by_name['jwt']._options = None
  _XIJWT.fields_by_name['jwt']._serialized_options = b'\312\235%5\010\001\0221^[a-zA-Z0-9-_]+?.[a-zA-Z0-9-_]+?.[a-zA-Z0-9-_]+?$'
  _XIALIASJID._serialized_start=102
  _XIALIASJID._serialized_end=166
  _XIBAREUSERJIDORALIASJID._serialized_start=169
  _XIBAREUSERJIDORALIASJID._serialized_end=303
  _XIANYJID._serialized_start=306
  _XIANYJID._serialized_end=466
  _XIKINUSERID._serialized_start=468
  _XIKINUSERID._serialized_end=517
  _XICONVOID._serialized_start=519
  _XICONVOID._serialized_end=625
  _ONETOONECONVOID._serialized_start=627
  _ONETOONECONVOID._serialized_end=698
  _XIJWT._serialized_start=700
  _XIJWT._serialized_end=779
# @@protoc_insertion_point(module_scope)
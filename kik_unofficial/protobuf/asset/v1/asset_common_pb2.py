# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: asset/v1/asset_common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import kik_unofficial.protobuf.protobuf_validation_pb2 as protobuf__validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x61sset/v1/asset_common.proto\x12\x0f\x63ommon.asset.v1\x1a\x19protobuf_validation.proto\"\x84\x02\n\x0eProductContent\x12\x46\n\x06\x61ssets\x18\x01 \x03(\x0b\x32+.common.asset.v1.ProductContent.AssetsEntryB\t\xd2\x9d%\x05(\x01\x30\x80\x01\x12\x32\n\x04type\x18\x02 \x01(\x0e\x32$.common.asset.v1.ProductContent.Type\x1a\x45\n\x0b\x41ssetsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.common.asset.v1.Asset:\x02\x38\x01\"/\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nCHAT_THEME\x10\x01\x12\n\n\x06\x41VATAR\x10\x02\"\xfe\x01\n\x05\x41sset\x12\x34\n\rmedia_content\x18\n \x01(\x0b\x32\x1d.common.asset.v1.MediaContent\x12<\n\x15media_content_preview\x18\x0b \x01(\x0b\x32\x1d.common.asset.v1.MediaContent\x12K\n\x0esimple_content\x18\x0c \x03(\x0b\x32).common.asset.v1.Asset.SimpleContentEntryB\x08\xd2\x9d%\x04(\x01\x30@\x1a\x34\n\x12SimpleContentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa0\x01\n\x0cMediaContent\x12\x1e\n\x0b\x63ontent_url\x18\x01 \x01(\tB\t\xca\x9d%\x05(\x01\x30\xff\x01\x12\x38\n\x08mimetype\x18\x02 \x01(\x0e\x32&.common.asset.v1.MediaContent.Mimetype\"6\n\x08Mimetype\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nIMAGE_JPEG\x10\x01\x12\r\n\tIMAGE_PNG\x10\x02*\xaf\x01\n\x0cPixelDensity\x12\t\n\x05NODPI\x10\x00\x12\x10\n\x0c\x41NDROID_LDPI\x10\x01\x12\x10\n\x0c\x41NDROID_MDPI\x10\x02\x12\x10\n\x0c\x41NDROID_HDPI\x10\x03\x12\x11\n\rANDROID_XHDPI\x10\x04\x12\x12\n\x0e\x41NDROID_XXHDPI\x10\x05\x12\x13\n\x0f\x41NDROID_XXXHDPI\x10\x06\x12\n\n\x06IOS_X1\x10\x07\x12\n\n\x06IOS_X2\x10\x08\x12\n\n\x06IOS_X3\x10\tBa\n\x13\x63om.kik.asset.modelZJgithub.com/kikinteractive/xiphias-model-common/generated/go/asset/v1;assetb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'asset.v1.asset_common_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.kik.asset.modelZJgithub.com/kikinteractive/xiphias-model-common/generated/go/asset/v1;asset'
  _PRODUCTCONTENT_ASSETSENTRY._options = None
  _PRODUCTCONTENT_ASSETSENTRY._serialized_options = b'8\001'
  _PRODUCTCONTENT.fields_by_name['assets']._options = None
  _PRODUCTCONTENT.fields_by_name['assets']._serialized_options = b'\322\235%\005(\0010\200\001'
  _ASSET_SIMPLECONTENTENTRY._options = None
  _ASSET_SIMPLECONTENTENTRY._serialized_options = b'8\001'
  _ASSET.fields_by_name['simple_content']._options = None
  _ASSET.fields_by_name['simple_content']._serialized_options = b'\322\235%\004(\0010@'
  _MEDIACONTENT.fields_by_name['content_url']._options = None
  _MEDIACONTENT.fields_by_name['content_url']._serialized_options = b'\312\235%\005(\0010\377\001'
  _PIXELDENSITY._serialized_start=759
  _PIXELDENSITY._serialized_end=934
  _PRODUCTCONTENT._serialized_start=76
  _PRODUCTCONTENT._serialized_end=336
  _PRODUCTCONTENT_ASSETSENTRY._serialized_start=218
  _PRODUCTCONTENT_ASSETSENTRY._serialized_end=287
  _PRODUCTCONTENT_TYPE._serialized_start=289
  _PRODUCTCONTENT_TYPE._serialized_end=336
  _ASSET._serialized_start=339
  _ASSET._serialized_end=593
  _ASSET_SIMPLECONTENTENTRY._serialized_start=541
  _ASSET_SIMPLECONTENTENTRY._serialized_end=593
  _MEDIACONTENT._serialized_start=596
  _MEDIACONTENT._serialized_end=756
  _MEDIACONTENT_MIMETYPE._serialized_start=702
  _MEDIACONTENT_MIMETYPE._serialized_end=756
# @@protoc_insertion_point(module_scope)
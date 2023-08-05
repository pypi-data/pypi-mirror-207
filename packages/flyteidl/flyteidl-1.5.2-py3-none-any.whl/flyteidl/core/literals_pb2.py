# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/core/literals.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from flyteidl.core import types_pb2 as flyteidl_dot_core_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x66lyteidl/core/literals.proto\x12\rflyteidl.core\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x19\x66lyteidl/core/types.proto\"\x87\x02\n\tPrimitive\x12\x1a\n\x07integer\x18\x01 \x01(\x03H\x00R\x07integer\x12!\n\x0b\x66loat_value\x18\x02 \x01(\x01H\x00R\nfloatValue\x12#\n\x0cstring_value\x18\x03 \x01(\tH\x00R\x0bstringValue\x12\x1a\n\x07\x62oolean\x18\x04 \x01(\x08H\x00R\x07\x62oolean\x12\x38\n\x08\x64\x61tetime\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00R\x08\x64\x61tetime\x12\x37\n\x08\x64uration\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00R\x08\x64urationB\x07\n\x05value\"\x06\n\x04Void\"Q\n\x04\x42lob\x12\x37\n\x08metadata\x18\x01 \x01(\x0b\x32\x1b.flyteidl.core.BlobMetadataR\x08metadata\x12\x10\n\x03uri\x18\x03 \x01(\tR\x03uri\";\n\x0c\x42lobMetadata\x12+\n\x04type\x18\x01 \x01(\x0b\x32\x17.flyteidl.core.BlobTypeR\x04type\"0\n\x06\x42inary\x12\x14\n\x05value\x18\x01 \x01(\x0cR\x05value\x12\x10\n\x03tag\x18\x02 \x01(\tR\x03tag\"I\n\x06Schema\x12\x10\n\x03uri\x18\x01 \x01(\tR\x03uri\x12-\n\x04type\x18\x03 \x01(\x0b\x32\x19.flyteidl.core.SchemaTypeR\x04type\"e\n\x05Union\x12,\n\x05value\x18\x01 \x01(\x0b\x32\x16.flyteidl.core.LiteralR\x05value\x12.\n\x04type\x18\x02 \x01(\x0b\x32\x1a.flyteidl.core.LiteralTypeR\x04type\"y\n\x19StructuredDatasetMetadata\x12\\\n\x17structured_dataset_type\x18\x01 \x01(\x0b\x32$.flyteidl.core.StructuredDatasetTypeR\x15structuredDatasetType\"k\n\x11StructuredDataset\x12\x10\n\x03uri\x18\x01 \x01(\tR\x03uri\x12\x44\n\x08metadata\x18\x02 \x01(\x0b\x32(.flyteidl.core.StructuredDatasetMetadataR\x08metadata\"\xf0\x03\n\x06Scalar\x12\x38\n\tprimitive\x18\x01 \x01(\x0b\x32\x18.flyteidl.core.PrimitiveH\x00R\tprimitive\x12)\n\x04\x62lob\x18\x02 \x01(\x0b\x32\x13.flyteidl.core.BlobH\x00R\x04\x62lob\x12/\n\x06\x62inary\x18\x03 \x01(\x0b\x32\x15.flyteidl.core.BinaryH\x00R\x06\x62inary\x12/\n\x06schema\x18\x04 \x01(\x0b\x32\x15.flyteidl.core.SchemaH\x00R\x06schema\x12\x32\n\tnone_type\x18\x05 \x01(\x0b\x32\x13.flyteidl.core.VoidH\x00R\x08noneType\x12,\n\x05\x65rror\x18\x06 \x01(\x0b\x32\x14.flyteidl.core.ErrorH\x00R\x05\x65rror\x12\x33\n\x07generic\x18\x07 \x01(\x0b\x32\x17.google.protobuf.StructH\x00R\x07generic\x12Q\n\x12structured_dataset\x18\x08 \x01(\x0b\x32 .flyteidl.core.StructuredDatasetH\x00R\x11structuredDataset\x12,\n\x05union\x18\t \x01(\x0b\x32\x14.flyteidl.core.UnionH\x00R\x05unionB\x07\n\x05value\"\xca\x01\n\x07Literal\x12/\n\x06scalar\x18\x01 \x01(\x0b\x32\x15.flyteidl.core.ScalarH\x00R\x06scalar\x12\x42\n\ncollection\x18\x02 \x01(\x0b\x32 .flyteidl.core.LiteralCollectionH\x00R\ncollection\x12-\n\x03map\x18\x03 \x01(\x0b\x32\x19.flyteidl.core.LiteralMapH\x00R\x03map\x12\x12\n\x04hash\x18\x04 \x01(\tR\x04hashB\x07\n\x05value\"G\n\x11LiteralCollection\x12\x32\n\x08literals\x18\x01 \x03(\x0b\x32\x16.flyteidl.core.LiteralR\x08literals\"\xa6\x01\n\nLiteralMap\x12\x43\n\x08literals\x18\x01 \x03(\x0b\x32\'.flyteidl.core.LiteralMap.LiteralsEntryR\x08literals\x1aS\n\rLiteralsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.flyteidl.core.LiteralR\x05value:\x02\x38\x01\"O\n\x15\x42indingDataCollection\x12\x36\n\x08\x62indings\x18\x01 \x03(\x0b\x32\x1a.flyteidl.core.BindingDataR\x08\x62indings\"\xb2\x01\n\x0e\x42indingDataMap\x12G\n\x08\x62indings\x18\x01 \x03(\x0b\x32+.flyteidl.core.BindingDataMap.BindingsEntryR\x08\x62indings\x1aW\n\rBindingsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32\x1a.flyteidl.core.BindingDataR\x05value:\x02\x38\x01\"G\n\tUnionInfo\x12:\n\ntargetType\x18\x01 \x01(\x0b\x32\x1a.flyteidl.core.LiteralTypeR\ntargetType\"\xae\x02\n\x0b\x42indingData\x12/\n\x06scalar\x18\x01 \x01(\x0b\x32\x15.flyteidl.core.ScalarH\x00R\x06scalar\x12\x46\n\ncollection\x18\x02 \x01(\x0b\x32$.flyteidl.core.BindingDataCollectionH\x00R\ncollection\x12:\n\x07promise\x18\x03 \x01(\x0b\x32\x1e.flyteidl.core.OutputReferenceH\x00R\x07promise\x12\x31\n\x03map\x18\x04 \x01(\x0b\x32\x1d.flyteidl.core.BindingDataMapH\x00R\x03map\x12.\n\x05union\x18\x05 \x01(\x0b\x32\x18.flyteidl.core.UnionInfoR\x05unionB\x07\n\x05value\"Q\n\x07\x42inding\x12\x10\n\x03var\x18\x01 \x01(\tR\x03var\x12\x34\n\x07\x62inding\x18\x02 \x01(\x0b\x32\x1a.flyteidl.core.BindingDataR\x07\x62inding\"6\n\x0cKeyValuePair\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\")\n\rRetryStrategy\x12\x18\n\x07retries\x18\x05 \x01(\rR\x07retriesB\xad\x01\n\x11\x63om.flyteidl.coreB\rLiteralsProtoP\x01Z4github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/core\xa2\x02\x03\x46\x43X\xaa\x02\rFlyteidl.Core\xca\x02\rFlyteidl\\Core\xe2\x02\x19\x46lyteidl\\Core\\GPBMetadata\xea\x02\x0e\x46lyteidl::Coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flyteidl.core.literals_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021com.flyteidl.coreB\rLiteralsProtoP\001Z4github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/core\242\002\003FCX\252\002\rFlyteidl.Core\312\002\rFlyteidl\\Core\342\002\031Flyteidl\\Core\\GPBMetadata\352\002\016Flyteidl::Core'
  _LITERALMAP_LITERALSENTRY._options = None
  _LITERALMAP_LITERALSENTRY._serialized_options = b'8\001'
  _BINDINGDATAMAP_BINDINGSENTRY._options = None
  _BINDINGDATAMAP_BINDINGSENTRY._serialized_options = b'8\001'
  _globals['_PRIMITIVE']._serialized_start=170
  _globals['_PRIMITIVE']._serialized_end=433
  _globals['_VOID']._serialized_start=435
  _globals['_VOID']._serialized_end=441
  _globals['_BLOB']._serialized_start=443
  _globals['_BLOB']._serialized_end=524
  _globals['_BLOBMETADATA']._serialized_start=526
  _globals['_BLOBMETADATA']._serialized_end=585
  _globals['_BINARY']._serialized_start=587
  _globals['_BINARY']._serialized_end=635
  _globals['_SCHEMA']._serialized_start=637
  _globals['_SCHEMA']._serialized_end=710
  _globals['_UNION']._serialized_start=712
  _globals['_UNION']._serialized_end=813
  _globals['_STRUCTUREDDATASETMETADATA']._serialized_start=815
  _globals['_STRUCTUREDDATASETMETADATA']._serialized_end=936
  _globals['_STRUCTUREDDATASET']._serialized_start=938
  _globals['_STRUCTUREDDATASET']._serialized_end=1045
  _globals['_SCALAR']._serialized_start=1048
  _globals['_SCALAR']._serialized_end=1544
  _globals['_LITERAL']._serialized_start=1547
  _globals['_LITERAL']._serialized_end=1749
  _globals['_LITERALCOLLECTION']._serialized_start=1751
  _globals['_LITERALCOLLECTION']._serialized_end=1822
  _globals['_LITERALMAP']._serialized_start=1825
  _globals['_LITERALMAP']._serialized_end=1991
  _globals['_LITERALMAP_LITERALSENTRY']._serialized_start=1908
  _globals['_LITERALMAP_LITERALSENTRY']._serialized_end=1991
  _globals['_BINDINGDATACOLLECTION']._serialized_start=1993
  _globals['_BINDINGDATACOLLECTION']._serialized_end=2072
  _globals['_BINDINGDATAMAP']._serialized_start=2075
  _globals['_BINDINGDATAMAP']._serialized_end=2253
  _globals['_BINDINGDATAMAP_BINDINGSENTRY']._serialized_start=2166
  _globals['_BINDINGDATAMAP_BINDINGSENTRY']._serialized_end=2253
  _globals['_UNIONINFO']._serialized_start=2255
  _globals['_UNIONINFO']._serialized_end=2326
  _globals['_BINDINGDATA']._serialized_start=2329
  _globals['_BINDINGDATA']._serialized_end=2631
  _globals['_BINDING']._serialized_start=2633
  _globals['_BINDING']._serialized_end=2714
  _globals['_KEYVALUEPAIR']._serialized_start=2716
  _globals['_KEYVALUEPAIR']._serialized_end=2770
  _globals['_RETRYSTRATEGY']._serialized_start=2772
  _globals['_RETRYSTRATEGY']._serialized_end=2813
# @@protoc_insertion_point(module_scope)

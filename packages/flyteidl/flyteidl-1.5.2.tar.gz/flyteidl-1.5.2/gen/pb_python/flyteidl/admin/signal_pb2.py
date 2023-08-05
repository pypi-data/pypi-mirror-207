# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/admin/signal.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.admin import common_pb2 as flyteidl_dot_admin_dot_common__pb2
from flyteidl.core import identifier_pb2 as flyteidl_dot_core_dot_identifier__pb2
from flyteidl.core import literals_pb2 as flyteidl_dot_core_dot_literals__pb2
from flyteidl.core import types_pb2 as flyteidl_dot_core_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x66lyteidl/admin/signal.proto\x12\x0e\x66lyteidl.admin\x1a\x1b\x66lyteidl/admin/common.proto\x1a\x1e\x66lyteidl/core/identifier.proto\x1a\x1c\x66lyteidl/core/literals.proto\x1a\x19\x66lyteidl/core/types.proto\"{\n\x18SignalGetOrCreateRequest\x12/\n\x02id\x18\x01 \x01(\x0b\x32\x1f.flyteidl.core.SignalIdentifierR\x02id\x12.\n\x04type\x18\x02 \x01(\x0b\x32\x1a.flyteidl.core.LiteralTypeR\x04type\"\xe8\x01\n\x11SignalListRequest\x12^\n\x15workflow_execution_id\x18\x01 \x01(\x0b\x32*.flyteidl.core.WorkflowExecutionIdentifierR\x13workflowExecutionId\x12\x14\n\x05limit\x18\x02 \x01(\rR\x05limit\x12\x14\n\x05token\x18\x03 \x01(\tR\x05token\x12\x18\n\x07\x66ilters\x18\x04 \x01(\tR\x07\x66ilters\x12-\n\x07sort_by\x18\x05 \x01(\x0b\x32\x14.flyteidl.admin.SortR\x06sortBy\"T\n\nSignalList\x12\x30\n\x07signals\x18\x01 \x03(\x0b\x32\x16.flyteidl.admin.SignalR\x07signals\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"q\n\x10SignalSetRequest\x12/\n\x02id\x18\x01 \x01(\x0b\x32\x1f.flyteidl.core.SignalIdentifierR\x02id\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.flyteidl.core.LiteralR\x05value\"\x13\n\x11SignalSetResponse\"\x97\x01\n\x06Signal\x12/\n\x02id\x18\x01 \x01(\x0b\x32\x1f.flyteidl.core.SignalIdentifierR\x02id\x12.\n\x04type\x18\x02 \x01(\x0b\x32\x1a.flyteidl.core.LiteralTypeR\x04type\x12,\n\x05value\x18\x03 \x01(\x0b\x32\x16.flyteidl.core.LiteralR\x05valueB\xb1\x01\n\x12\x63om.flyteidl.adminB\x0bSignalProtoP\x01Z5github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/admin\xa2\x02\x03\x46\x41X\xaa\x02\x0e\x46lyteidl.Admin\xca\x02\x0e\x46lyteidl\\Admin\xe2\x02\x1a\x46lyteidl\\Admin\\GPBMetadata\xea\x02\x0f\x46lyteidl::Adminb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flyteidl.admin.signal_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.flyteidl.adminB\013SignalProtoP\001Z5github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/admin\242\002\003FAX\252\002\016Flyteidl.Admin\312\002\016Flyteidl\\Admin\342\002\032Flyteidl\\Admin\\GPBMetadata\352\002\017Flyteidl::Admin'
  _globals['_SIGNALGETORCREATEREQUEST']._serialized_start=165
  _globals['_SIGNALGETORCREATEREQUEST']._serialized_end=288
  _globals['_SIGNALLISTREQUEST']._serialized_start=291
  _globals['_SIGNALLISTREQUEST']._serialized_end=523
  _globals['_SIGNALLIST']._serialized_start=525
  _globals['_SIGNALLIST']._serialized_end=609
  _globals['_SIGNALSETREQUEST']._serialized_start=611
  _globals['_SIGNALSETREQUEST']._serialized_end=724
  _globals['_SIGNALSETRESPONSE']._serialized_start=726
  _globals['_SIGNALSETRESPONSE']._serialized_end=745
  _globals['_SIGNAL']._serialized_start=748
  _globals['_SIGNAL']._serialized_end=899
# @@protoc_insertion_point(module_scope)

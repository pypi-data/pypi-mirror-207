# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deephaven/proto/partitionedtable.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pydeephaven.proto import table_pb2 as deephaven_dot_proto_dot_table__pb2
from pydeephaven.proto import ticket_pb2 as deephaven_dot_proto_dot_ticket__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&deephaven/proto/partitionedtable.proto\x12!io.deephaven.proto.backplane.grpc\x1a\x1b\x64\x65\x65phaven/proto/table.proto\x1a\x1c\x64\x65\x65phaven/proto/ticket.proto\"\xbc\x01\n\x12PartitionByRequest\x12;\n\x08table_id\x18\x01 \x01(\x0b\x32).io.deephaven.proto.backplane.grpc.Ticket\x12<\n\tresult_id\x18\x02 \x01(\x0b\x32).io.deephaven.proto.backplane.grpc.Ticket\x12\x18\n\x10key_column_names\x18\x03 \x03(\t\x12\x11\n\tdrop_keys\x18\x04 \x01(\x08\"\x15\n\x13PartitionByResponse\"\x92\x01\n\x0cMergeRequest\x12\x44\n\x11partitioned_table\x18\x01 \x01(\x0b\x32).io.deephaven.proto.backplane.grpc.Ticket\x12<\n\tresult_id\x18\x02 \x01(\x0b\x32).io.deephaven.proto.backplane.grpc.Ticket\"\xda\x01\n\x0fGetTableRequest\x12\x44\n\x11partitioned_table\x18\x01 \x01(\x0b\x32).io.deephaven.proto.backplane.grpc.Ticket\x12\x43\n\x10key_table_ticket\x18\x02 \x01(\x0b\x32).io.deephaven.proto.backplane.grpc.Ticket\x12<\n\tresult_id\x18\x04 \x01(\x0b\x32).io.deephaven.proto.backplane.grpc.Ticket\"\xba\x01\n\x1aPartitionedTableDescriptor\x12\x18\n\x10key_column_names\x18\x01 \x03(\t\x12\x1f\n\x17\x63onstituent_column_name\x18\x04 \x01(\t\x12\x13\n\x0bunique_keys\x18\x02 \x01(\x08\x12%\n\x1d\x63onstituent_definition_schema\x18\x03 \x01(\x0c\x12%\n\x1d\x63onstituent_changes_permitted\x18\x05 \x01(\x08\x32\x96\x03\n\x17PartitionedTableService\x12|\n\x0bPartitionBy\x12\x35.io.deephaven.proto.backplane.grpc.PartitionByRequest\x1a\x36.io.deephaven.proto.backplane.grpc.PartitionByResponse\x12z\n\x05Merge\x12/.io.deephaven.proto.backplane.grpc.MergeRequest\x1a@.io.deephaven.proto.backplane.grpc.ExportedTableCreationResponse\x12\x80\x01\n\x08GetTable\x12\x32.io.deephaven.proto.backplane.grpc.GetTableRequest\x1a@.io.deephaven.proto.backplane.grpc.ExportedTableCreationResponseBLH\x01P\x01ZFgithub.com/deephaven/deephaven-core/go/internal/proto/partitionedtableb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'deephaven.proto.partitionedtable_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\001P\001ZFgithub.com/deephaven/deephaven-core/go/internal/proto/partitionedtable'
  _PARTITIONBYREQUEST._serialized_start=137
  _PARTITIONBYREQUEST._serialized_end=325
  _PARTITIONBYRESPONSE._serialized_start=327
  _PARTITIONBYRESPONSE._serialized_end=348
  _MERGEREQUEST._serialized_start=351
  _MERGEREQUEST._serialized_end=497
  _GETTABLEREQUEST._serialized_start=500
  _GETTABLEREQUEST._serialized_end=718
  _PARTITIONEDTABLEDESCRIPTOR._serialized_start=721
  _PARTITIONEDTABLEDESCRIPTOR._serialized_end=907
  _PARTITIONEDTABLESERVICE._serialized_start=910
  _PARTITIONEDTABLESERVICE._serialized_end=1316
# @@protoc_insertion_point(module_scope)

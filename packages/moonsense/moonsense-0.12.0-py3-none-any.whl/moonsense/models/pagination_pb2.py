# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pagination.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pagination.proto',
  package='pagination',
  syntax='proto3',
  serialized_options=b'\n\023io.moonsense.modelsB\020PaginationProtosZ)moonsense.io/pkg/pb/pagination;pagination',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10pagination.proto\x12\npagination\"\x13\n\x11PaginationRequest\"\x98\x01\n\x12PaginationResponse\x12\x14\n\x0c\x63urrent_page\x18\x01 \x01(\x05\x12\x15\n\rprevious_page\x18\x02 \x01(\x05\x12\x11\n\tnext_page\x18\x03 \x01(\x05\x12\x10\n\x08per_page\x18\x04 \x01(\x05\x12\x17\n\x0btotal_pages\x18\x05 \x01(\x05\x42\x02\x18\x01\x12\x17\n\x0btotal_count\x18\x06 \x01(\x05\x42\x02\x18\x01\x42R\n\x13io.moonsense.modelsB\x10PaginationProtosZ)moonsense.io/pkg/pb/pagination;paginationb\x06proto3'
)




_PAGINATIONREQUEST = _descriptor.Descriptor(
  name='PaginationRequest',
  full_name='pagination.PaginationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=51,
)


_PAGINATIONRESPONSE = _descriptor.Descriptor(
  name='PaginationResponse',
  full_name='pagination.PaginationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_page', full_name='pagination.PaginationResponse.current_page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='previous_page', full_name='pagination.PaginationResponse.previous_page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page', full_name='pagination.PaginationResponse.next_page', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='pagination.PaginationResponse.per_page', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_pages', full_name='pagination.PaginationResponse.total_pages', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_count', full_name='pagination.PaginationResponse.total_count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=206,
)

DESCRIPTOR.message_types_by_name['PaginationRequest'] = _PAGINATIONREQUEST
DESCRIPTOR.message_types_by_name['PaginationResponse'] = _PAGINATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PaginationRequest = _reflection.GeneratedProtocolMessageType('PaginationRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAGINATIONREQUEST,
  '__module__' : 'pagination_pb2'
  # @@protoc_insertion_point(class_scope:pagination.PaginationRequest)
  })
_sym_db.RegisterMessage(PaginationRequest)

PaginationResponse = _reflection.GeneratedProtocolMessageType('PaginationResponse', (_message.Message,), {
  'DESCRIPTOR' : _PAGINATIONRESPONSE,
  '__module__' : 'pagination_pb2'
  # @@protoc_insertion_point(class_scope:pagination.PaginationResponse)
  })
_sym_db.RegisterMessage(PaginationResponse)


DESCRIPTOR._options = None
_PAGINATIONRESPONSE.fields_by_name['total_pages']._options = None
_PAGINATIONRESPONSE.fields_by_name['total_count']._options = None
# @@protoc_insertion_point(module_scope)

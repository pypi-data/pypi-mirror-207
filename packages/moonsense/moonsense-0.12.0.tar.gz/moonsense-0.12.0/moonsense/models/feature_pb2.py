# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feature.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='feature.proto',
  package='v2.feature',
  syntax='proto3',
  serialized_options=b'\n\036io.moonsense.models.v2.featureB\rFeatureProtosZ&moonsense.io/pkg/pb/v2/feature;feature',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rfeature.proto\x12\nv2.feature\"\x1a\n\tBytesList\x12\r\n\x05value\x18\x01 \x03(\x0c\"\x1f\n\nDoubleList\x12\x11\n\x05value\x18\x01 \x03(\x01\x42\x02\x10\x01\"j\n\tDoubleMap\x12/\n\x05value\x18\x01 \x03(\x0b\x32 .v2.feature.DoubleMap.ValueEntry\x1a,\n\nValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\x1e\n\tInt64List\x12\x11\n\x05value\x18\x01 \x03(\x03\x42\x02\x10\x01\"\x1b\n\nStringList\x12\r\n\x05value\x18\x01 \x03(\t\"\xf6\x01\n\x07\x46\x65\x61ture\x12+\n\nbytes_list\x18\x01 \x01(\x0b\x32\x15.v2.feature.BytesListH\x00\x12-\n\x0b\x64ouble_list\x18\x02 \x01(\x0b\x32\x16.v2.feature.DoubleListH\x00\x12+\n\nint64_list\x18\x03 \x01(\x0b\x32\x15.v2.feature.Int64ListH\x00\x12-\n\x0bstring_list\x18\x04 \x01(\x0b\x32\x16.v2.feature.StringListH\x00\x12+\n\ndouble_map\x18\x05 \x01(\x0b\x32\x15.v2.feature.DoubleMapH\x00\x42\x06\n\x04kindBW\n\x1eio.moonsense.models.v2.featureB\rFeatureProtosZ&moonsense.io/pkg/pb/v2/feature;featureb\x06proto3'
)




_BYTESLIST = _descriptor.Descriptor(
  name='BytesList',
  full_name='v2.feature.BytesList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v2.feature.BytesList.value', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=29,
  serialized_end=55,
)


_DOUBLELIST = _descriptor.Descriptor(
  name='DoubleList',
  full_name='v2.feature.DoubleList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v2.feature.DoubleList.value', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=57,
  serialized_end=88,
)


_DOUBLEMAP_VALUEENTRY = _descriptor.Descriptor(
  name='ValueEntry',
  full_name='v2.feature.DoubleMap.ValueEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v2.feature.DoubleMap.ValueEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='v2.feature.DoubleMap.ValueEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=196,
)

_DOUBLEMAP = _descriptor.Descriptor(
  name='DoubleMap',
  full_name='v2.feature.DoubleMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v2.feature.DoubleMap.value', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DOUBLEMAP_VALUEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=196,
)


_INT64LIST = _descriptor.Descriptor(
  name='Int64List',
  full_name='v2.feature.Int64List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v2.feature.Int64List.value', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=198,
  serialized_end=228,
)


_STRINGLIST = _descriptor.Descriptor(
  name='StringList',
  full_name='v2.feature.StringList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v2.feature.StringList.value', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=230,
  serialized_end=257,
)


_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='v2.feature.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bytes_list', full_name='v2.feature.Feature.bytes_list', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_list', full_name='v2.feature.Feature.double_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int64_list', full_name='v2.feature.Feature.int64_list', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_list', full_name='v2.feature.Feature.string_list', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_map', full_name='v2.feature.Feature.double_map', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='kind', full_name='v2.feature.Feature.kind',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=260,
  serialized_end=506,
)

_DOUBLEMAP_VALUEENTRY.containing_type = _DOUBLEMAP
_DOUBLEMAP.fields_by_name['value'].message_type = _DOUBLEMAP_VALUEENTRY
_FEATURE.fields_by_name['bytes_list'].message_type = _BYTESLIST
_FEATURE.fields_by_name['double_list'].message_type = _DOUBLELIST
_FEATURE.fields_by_name['int64_list'].message_type = _INT64LIST
_FEATURE.fields_by_name['string_list'].message_type = _STRINGLIST
_FEATURE.fields_by_name['double_map'].message_type = _DOUBLEMAP
_FEATURE.oneofs_by_name['kind'].fields.append(
  _FEATURE.fields_by_name['bytes_list'])
_FEATURE.fields_by_name['bytes_list'].containing_oneof = _FEATURE.oneofs_by_name['kind']
_FEATURE.oneofs_by_name['kind'].fields.append(
  _FEATURE.fields_by_name['double_list'])
_FEATURE.fields_by_name['double_list'].containing_oneof = _FEATURE.oneofs_by_name['kind']
_FEATURE.oneofs_by_name['kind'].fields.append(
  _FEATURE.fields_by_name['int64_list'])
_FEATURE.fields_by_name['int64_list'].containing_oneof = _FEATURE.oneofs_by_name['kind']
_FEATURE.oneofs_by_name['kind'].fields.append(
  _FEATURE.fields_by_name['string_list'])
_FEATURE.fields_by_name['string_list'].containing_oneof = _FEATURE.oneofs_by_name['kind']
_FEATURE.oneofs_by_name['kind'].fields.append(
  _FEATURE.fields_by_name['double_map'])
_FEATURE.fields_by_name['double_map'].containing_oneof = _FEATURE.oneofs_by_name['kind']
DESCRIPTOR.message_types_by_name['BytesList'] = _BYTESLIST
DESCRIPTOR.message_types_by_name['DoubleList'] = _DOUBLELIST
DESCRIPTOR.message_types_by_name['DoubleMap'] = _DOUBLEMAP
DESCRIPTOR.message_types_by_name['Int64List'] = _INT64LIST
DESCRIPTOR.message_types_by_name['StringList'] = _STRINGLIST
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BytesList = _reflection.GeneratedProtocolMessageType('BytesList', (_message.Message,), {
  'DESCRIPTOR' : _BYTESLIST,
  '__module__' : 'feature_pb2'
  # @@protoc_insertion_point(class_scope:v2.feature.BytesList)
  })
_sym_db.RegisterMessage(BytesList)

DoubleList = _reflection.GeneratedProtocolMessageType('DoubleList', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLELIST,
  '__module__' : 'feature_pb2'
  # @@protoc_insertion_point(class_scope:v2.feature.DoubleList)
  })
_sym_db.RegisterMessage(DoubleList)

DoubleMap = _reflection.GeneratedProtocolMessageType('DoubleMap', (_message.Message,), {

  'ValueEntry' : _reflection.GeneratedProtocolMessageType('ValueEntry', (_message.Message,), {
    'DESCRIPTOR' : _DOUBLEMAP_VALUEENTRY,
    '__module__' : 'feature_pb2'
    # @@protoc_insertion_point(class_scope:v2.feature.DoubleMap.ValueEntry)
    })
  ,
  'DESCRIPTOR' : _DOUBLEMAP,
  '__module__' : 'feature_pb2'
  # @@protoc_insertion_point(class_scope:v2.feature.DoubleMap)
  })
_sym_db.RegisterMessage(DoubleMap)
_sym_db.RegisterMessage(DoubleMap.ValueEntry)

Int64List = _reflection.GeneratedProtocolMessageType('Int64List', (_message.Message,), {
  'DESCRIPTOR' : _INT64LIST,
  '__module__' : 'feature_pb2'
  # @@protoc_insertion_point(class_scope:v2.feature.Int64List)
  })
_sym_db.RegisterMessage(Int64List)

StringList = _reflection.GeneratedProtocolMessageType('StringList', (_message.Message,), {
  'DESCRIPTOR' : _STRINGLIST,
  '__module__' : 'feature_pb2'
  # @@protoc_insertion_point(class_scope:v2.feature.StringList)
  })
_sym_db.RegisterMessage(StringList)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), {
  'DESCRIPTOR' : _FEATURE,
  '__module__' : 'feature_pb2'
  # @@protoc_insertion_point(class_scope:v2.feature.Feature)
  })
_sym_db.RegisterMessage(Feature)


DESCRIPTOR._options = None
_DOUBLELIST.fields_by_name['value']._options = None
_DOUBLEMAP_VALUEENTRY._options = None
_INT64LIST.fields_by_name['value']._options = None
# @@protoc_insertion_point(module_scope)

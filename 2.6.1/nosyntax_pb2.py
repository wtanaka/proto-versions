# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nosyntax.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nosyntax.proto',
  package='',
  serialized_pb=_b('\n\x0enosyntax.proto\"\x1c\n\tMyRequest\x12\x0f\n\x07myfield\x18\x01 \x02(\x05\"\x1e\n\nMyResponse\x12\x10\n\x08myresult\x18\x01 \x02(\x05\x32/\n\tMyService\x12\"\n\x07\x44oStuff\x12\n.MyRequest\x1a\x0b.MyResponse')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MYREQUEST = _descriptor.Descriptor(
  name='MyRequest',
  full_name='MyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='myfield', full_name='MyRequest.myfield', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=46,
)


_MYRESPONSE = _descriptor.Descriptor(
  name='MyResponse',
  full_name='MyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='myresult', full_name='MyResponse.myresult', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=78,
)

DESCRIPTOR.message_types_by_name['MyRequest'] = _MYREQUEST
DESCRIPTOR.message_types_by_name['MyResponse'] = _MYRESPONSE

MyRequest = _reflection.GeneratedProtocolMessageType('MyRequest', (_message.Message,), dict(
  DESCRIPTOR = _MYREQUEST,
  __module__ = 'nosyntax_pb2'
  # @@protoc_insertion_point(class_scope:MyRequest)
  ))
_sym_db.RegisterMessage(MyRequest)

MyResponse = _reflection.GeneratedProtocolMessageType('MyResponse', (_message.Message,), dict(
  DESCRIPTOR = _MYRESPONSE,
  __module__ = 'nosyntax_pb2'
  # @@protoc_insertion_point(class_scope:MyResponse)
  ))
_sym_db.RegisterMessage(MyResponse)


# @@protoc_insertion_point(module_scope)

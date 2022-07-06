
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"akash/base/v1beta1/attribute.proto\x12\x12akash.base.v1beta1\x1a\x14gogoproto/gogo.proto"O\n\tAttribute\x12\x1b\n\x03key\x18\x01 \x01(\tB\x0e\xf2\xde\x1f\nyaml:"key"\x12\x1f\n\x05value\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"value":\x04\x88\xa0\x1f\x00"h\n\x08SignedBy\x12*\n\x06all_of\x18\x01 \x03(\tB\x1a\xea\xde\x1f\x06all_of\xf2\xde\x1f\x0cyaml:"allOf"\x12*\n\x06any_of\x18\x02 \x03(\tB\x1a\xea\xde\x1f\x06any_of\xf2\xde\x1f\x0cyaml:"anyOf":\x04\x88\xa0\x1f\x00"\xd1\x01\n\x15PlacementRequirements\x12V\n\tsigned_by\x18\x01 \x01(\x0b2\x1c.akash.base.v1beta1.SignedByB%\xc8\xde\x1f\x00\xea\xde\x1f\tsigned_by\xf2\xde\x1f\x10yaml:"signed_by"\x12Z\n\nattributes\x18\x02 \x03(\x0b2\x1d.akash.base.v1beta1.AttributeB\'\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes":\x04\x88\xa0\x1f\x00B/Z%github.com/ovrclk/akash/types/v1beta1\xd8\xe1\x1e\x00\x80\xe2\x1e\x00b\x06proto3')
_ATTRIBUTE = DESCRIPTOR.message_types_by_name['Attribute']
_SIGNEDBY = DESCRIPTOR.message_types_by_name['SignedBy']
_PLACEMENTREQUIREMENTS = DESCRIPTOR.message_types_by_name['PlacementRequirements']
Attribute = _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), {'DESCRIPTOR': _ATTRIBUTE, '__module__': 'akash.base.v1beta1.attribute_pb2'})
_sym_db.RegisterMessage(Attribute)
SignedBy = _reflection.GeneratedProtocolMessageType('SignedBy', (_message.Message,), {'DESCRIPTOR': _SIGNEDBY, '__module__': 'akash.base.v1beta1.attribute_pb2'})
_sym_db.RegisterMessage(SignedBy)
PlacementRequirements = _reflection.GeneratedProtocolMessageType('PlacementRequirements', (_message.Message,), {'DESCRIPTOR': _PLACEMENTREQUIREMENTS, '__module__': 'akash.base.v1beta1.attribute_pb2'})
_sym_db.RegisterMessage(PlacementRequirements)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z%github.com/ovrclk/akash/types/v1beta1\xd8\xe1\x1e\x00\x80\xe2\x1e\x00'
    _ATTRIBUTE.fields_by_name['key']._options = None
    _ATTRIBUTE.fields_by_name['key']._serialized_options = b'\xf2\xde\x1f\nyaml:"key"'
    _ATTRIBUTE.fields_by_name['value']._options = None
    _ATTRIBUTE.fields_by_name['value']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"value"'
    _ATTRIBUTE._options = None
    _ATTRIBUTE._serialized_options = b'\x88\xa0\x1f\x00'
    _SIGNEDBY.fields_by_name['all_of']._options = None
    _SIGNEDBY.fields_by_name['all_of']._serialized_options = b'\xea\xde\x1f\x06all_of\xf2\xde\x1f\x0cyaml:"allOf"'
    _SIGNEDBY.fields_by_name['any_of']._options = None
    _SIGNEDBY.fields_by_name['any_of']._serialized_options = b'\xea\xde\x1f\x06any_of\xf2\xde\x1f\x0cyaml:"anyOf"'
    _SIGNEDBY._options = None
    _SIGNEDBY._serialized_options = b'\x88\xa0\x1f\x00'
    _PLACEMENTREQUIREMENTS.fields_by_name['signed_by']._options = None
    _PLACEMENTREQUIREMENTS.fields_by_name['signed_by']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\tsigned_by\xf2\xde\x1f\x10yaml:"signed_by"'
    _PLACEMENTREQUIREMENTS.fields_by_name['attributes']._options = None
    _PLACEMENTREQUIREMENTS.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"'
    _PLACEMENTREQUIREMENTS._options = None
    _PLACEMENTREQUIREMENTS._serialized_options = b'\x88\xa0\x1f\x00'
    _ATTRIBUTE._serialized_start = 80
    _ATTRIBUTE._serialized_end = 159
    _SIGNEDBY._serialized_start = 161
    _SIGNEDBY._serialized_end = 265
    _PLACEMENTREQUIREMENTS._serialized_start = 268
    _PLACEMENTREQUIREMENTS._serialized_end = 477

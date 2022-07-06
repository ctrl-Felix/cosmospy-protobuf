
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.base.v1beta2 import attribute_pb2 as akash_dot_base_dot_v1beta2_dot_attribute__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%akash/provider/v1beta2/provider.proto\x12\x16akash.provider.v1beta2\x1a\x14gogoproto/gogo.proto\x1a"akash/base/v1beta2/attribute.proto"q\n\x0cProviderInfo\x121\n\x05email\x18\x01 \x01(\tB"\xe2\xde\x1f\x05EMail\xea\xde\x1f\x05email\xf2\xde\x1f\x0cyaml:"email"\x12.\n\x07website\x18\x02 \x01(\tB\x1d\xea\xde\x1f\x07website\xf2\xde\x1f\x0eyaml:"website""\xe3\x02\n\x11MsgCreateProvider\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12<\n\x08host_uri\x18\x02 \x01(\tB*\xe2\xde\x1f\x07HostURI\xea\xde\x1f\x08host_uri\xf2\xde\x1f\x0fyaml:"host_uri"\x12\x8e\x01\n\nattributes\x18\x03 \x03(\x0b2\x1d.akash.base.v1beta2.AttributeB[\xaa\xdf\x1f0github.com/ovrclk/akash/types/v1beta2.Attributes\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"\x12O\n\x04info\x18\x04 \x01(\x0b2$.akash.provider.v1beta2.ProviderInfoB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04info\xf2\xde\x1f\x0byaml:"info":\x04\xe8\xa0\x1f\x00"\x1b\n\x19MsgCreateProviderResponse"\xe3\x02\n\x11MsgUpdateProvider\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12<\n\x08host_uri\x18\x02 \x01(\tB*\xe2\xde\x1f\x07HostURI\xea\xde\x1f\x08host_uri\xf2\xde\x1f\x0fyaml:"host_uri"\x12\x8e\x01\n\nattributes\x18\x03 \x03(\x0b2\x1d.akash.base.v1beta2.AttributeB[\xaa\xdf\x1f0github.com/ovrclk/akash/types/v1beta2.Attributes\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"\x12O\n\x04info\x18\x04 \x01(\x0b2$.akash.provider.v1beta2.ProviderInfoB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04info\xf2\xde\x1f\x0byaml:"info":\x04\xe8\xa0\x1f\x00"\x1b\n\x19MsgUpdateProviderResponse"C\n\x11MsgDeleteProvider\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner":\x04\xe8\xa0\x1f\x00"\x1b\n\x19MsgDeleteProviderResponse"\xde\x02\n\x08Provider\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12<\n\x08host_uri\x18\x02 \x01(\tB*\xe2\xde\x1f\x07HostURI\xea\xde\x1f\x08host_uri\xf2\xde\x1f\x0fyaml:"host_uri"\x12\x8e\x01\n\nattributes\x18\x03 \x03(\x0b2\x1d.akash.base.v1beta2.AttributeB[\xaa\xdf\x1f0github.com/ovrclk/akash/types/v1beta2.Attributes\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"\x12O\n\x04info\x18\x04 \x01(\x0b2$.akash.provider.v1beta2.ProviderInfoB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04info\xf2\xde\x1f\x0byaml:"info":\x08\xe8\xa0\x1f\x00\x98\xa0\x1f\x002\xd5\x02\n\x03Msg\x12n\n\x0eCreateProvider\x12).akash.provider.v1beta2.MsgCreateProvider\x1a1.akash.provider.v1beta2.MsgCreateProviderResponse\x12n\n\x0eUpdateProvider\x12).akash.provider.v1beta2.MsgUpdateProvider\x1a1.akash.provider.v1beta2.MsgUpdateProviderResponse\x12n\n\x0eDeleteProvider\x12).akash.provider.v1beta2.MsgDeleteProvider\x1a1.akash.provider.v1beta2.MsgDeleteProviderResponseB2Z0github.com/ovrclk/akash/x/provider/types/v1beta2b\x06proto3')
_PROVIDERINFO = DESCRIPTOR.message_types_by_name['ProviderInfo']
_MSGCREATEPROVIDER = DESCRIPTOR.message_types_by_name['MsgCreateProvider']
_MSGCREATEPROVIDERRESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateProviderResponse']
_MSGUPDATEPROVIDER = DESCRIPTOR.message_types_by_name['MsgUpdateProvider']
_MSGUPDATEPROVIDERRESPONSE = DESCRIPTOR.message_types_by_name['MsgUpdateProviderResponse']
_MSGDELETEPROVIDER = DESCRIPTOR.message_types_by_name['MsgDeleteProvider']
_MSGDELETEPROVIDERRESPONSE = DESCRIPTOR.message_types_by_name['MsgDeleteProviderResponse']
_PROVIDER = DESCRIPTOR.message_types_by_name['Provider']
ProviderInfo = _reflection.GeneratedProtocolMessageType('ProviderInfo', (_message.Message,), {'DESCRIPTOR': _PROVIDERINFO, '__module__': 'akash.provider.v1beta2.provider_pb2'})
_sym_db.RegisterMessage(ProviderInfo)
MsgCreateProvider = _reflection.GeneratedProtocolMessageType('MsgCreateProvider', (_message.Message,), {'DESCRIPTOR': _MSGCREATEPROVIDER, '__module__': 'akash.provider.v1beta2.provider_pb2'})
_sym_db.RegisterMessage(MsgCreateProvider)
MsgCreateProviderResponse = _reflection.GeneratedProtocolMessageType('MsgCreateProviderResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATEPROVIDERRESPONSE, '__module__': 'akash.provider.v1beta2.provider_pb2'})
_sym_db.RegisterMessage(MsgCreateProviderResponse)
MsgUpdateProvider = _reflection.GeneratedProtocolMessageType('MsgUpdateProvider', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEPROVIDER, '__module__': 'akash.provider.v1beta2.provider_pb2'})
_sym_db.RegisterMessage(MsgUpdateProvider)
MsgUpdateProviderResponse = _reflection.GeneratedProtocolMessageType('MsgUpdateProviderResponse', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEPROVIDERRESPONSE, '__module__': 'akash.provider.v1beta2.provider_pb2'})
_sym_db.RegisterMessage(MsgUpdateProviderResponse)
MsgDeleteProvider = _reflection.GeneratedProtocolMessageType('MsgDeleteProvider', (_message.Message,), {'DESCRIPTOR': _MSGDELETEPROVIDER, '__module__': 'akash.provider.v1beta2.provider_pb2'})
_sym_db.RegisterMessage(MsgDeleteProvider)
MsgDeleteProviderResponse = _reflection.GeneratedProtocolMessageType('MsgDeleteProviderResponse', (_message.Message,), {'DESCRIPTOR': _MSGDELETEPROVIDERRESPONSE, '__module__': 'akash.provider.v1beta2.provider_pb2'})
_sym_db.RegisterMessage(MsgDeleteProviderResponse)
Provider = _reflection.GeneratedProtocolMessageType('Provider', (_message.Message,), {'DESCRIPTOR': _PROVIDER, '__module__': 'akash.provider.v1beta2.provider_pb2'})
_sym_db.RegisterMessage(Provider)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/ovrclk/akash/x/provider/types/v1beta2'
    _PROVIDERINFO.fields_by_name['email']._options = None
    _PROVIDERINFO.fields_by_name['email']._serialized_options = b'\xe2\xde\x1f\x05EMail\xea\xde\x1f\x05email\xf2\xde\x1f\x0cyaml:"email"'
    _PROVIDERINFO.fields_by_name['website']._options = None
    _PROVIDERINFO.fields_by_name['website']._serialized_options = b'\xea\xde\x1f\x07website\xf2\xde\x1f\x0eyaml:"website"'
    _MSGCREATEPROVIDER.fields_by_name['owner']._options = None
    _MSGCREATEPROVIDER.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGCREATEPROVIDER.fields_by_name['host_uri']._options = None
    _MSGCREATEPROVIDER.fields_by_name['host_uri']._serialized_options = b'\xe2\xde\x1f\x07HostURI\xea\xde\x1f\x08host_uri\xf2\xde\x1f\x0fyaml:"host_uri"'
    _MSGCREATEPROVIDER.fields_by_name['attributes']._options = None
    _MSGCREATEPROVIDER.fields_by_name['attributes']._serialized_options = b'\xaa\xdf\x1f0github.com/ovrclk/akash/types/v1beta2.Attributes\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"'
    _MSGCREATEPROVIDER.fields_by_name['info']._options = None
    _MSGCREATEPROVIDER.fields_by_name['info']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04info\xf2\xde\x1f\x0byaml:"info"'
    _MSGCREATEPROVIDER._options = None
    _MSGCREATEPROVIDER._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGUPDATEPROVIDER.fields_by_name['owner']._options = None
    _MSGUPDATEPROVIDER.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGUPDATEPROVIDER.fields_by_name['host_uri']._options = None
    _MSGUPDATEPROVIDER.fields_by_name['host_uri']._serialized_options = b'\xe2\xde\x1f\x07HostURI\xea\xde\x1f\x08host_uri\xf2\xde\x1f\x0fyaml:"host_uri"'
    _MSGUPDATEPROVIDER.fields_by_name['attributes']._options = None
    _MSGUPDATEPROVIDER.fields_by_name['attributes']._serialized_options = b'\xaa\xdf\x1f0github.com/ovrclk/akash/types/v1beta2.Attributes\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"'
    _MSGUPDATEPROVIDER.fields_by_name['info']._options = None
    _MSGUPDATEPROVIDER.fields_by_name['info']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04info\xf2\xde\x1f\x0byaml:"info"'
    _MSGUPDATEPROVIDER._options = None
    _MSGUPDATEPROVIDER._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGDELETEPROVIDER.fields_by_name['owner']._options = None
    _MSGDELETEPROVIDER.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGDELETEPROVIDER._options = None
    _MSGDELETEPROVIDER._serialized_options = b'\xe8\xa0\x1f\x00'
    _PROVIDER.fields_by_name['owner']._options = None
    _PROVIDER.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _PROVIDER.fields_by_name['host_uri']._options = None
    _PROVIDER.fields_by_name['host_uri']._serialized_options = b'\xe2\xde\x1f\x07HostURI\xea\xde\x1f\x08host_uri\xf2\xde\x1f\x0fyaml:"host_uri"'
    _PROVIDER.fields_by_name['attributes']._options = None
    _PROVIDER.fields_by_name['attributes']._serialized_options = b'\xaa\xdf\x1f0github.com/ovrclk/akash/types/v1beta2.Attributes\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"'
    _PROVIDER.fields_by_name['info']._options = None
    _PROVIDER.fields_by_name['info']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04info\xf2\xde\x1f\x0byaml:"info"'
    _PROVIDER._options = None
    _PROVIDER._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x00'
    _PROVIDERINFO._serialized_start = 123
    _PROVIDERINFO._serialized_end = 236
    _MSGCREATEPROVIDER._serialized_start = 239
    _MSGCREATEPROVIDER._serialized_end = 594
    _MSGCREATEPROVIDERRESPONSE._serialized_start = 596
    _MSGCREATEPROVIDERRESPONSE._serialized_end = 623
    _MSGUPDATEPROVIDER._serialized_start = 626
    _MSGUPDATEPROVIDER._serialized_end = 981
    _MSGUPDATEPROVIDERRESPONSE._serialized_start = 983
    _MSGUPDATEPROVIDERRESPONSE._serialized_end = 1010
    _MSGDELETEPROVIDER._serialized_start = 1012
    _MSGDELETEPROVIDER._serialized_end = 1079
    _MSGDELETEPROVIDERRESPONSE._serialized_start = 1081
    _MSGDELETEPROVIDERRESPONSE._serialized_end = 1108
    _PROVIDER._serialized_start = 1111
    _PROVIDER._serialized_end = 1461
    _MSG._serialized_start = 1464
    _MSG._serialized_end = 1805


'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.base.v1beta1 import attribute_pb2 as akash_dot_base_dot_v1beta1_dot_attribute__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fakash/audit/v1beta1/audit.proto\x12\x13akash.audit.v1beta1\x1a\x14gogoproto/gogo.proto\x1a"akash/base/v1beta1/attribute.proto"\xf5\x01\n\x08Provider\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12.\n\x07auditor\x18\x02 \x01(\tB\x1d\xea\xde\x1f\x07auditor\xf2\xde\x1f\x0eyaml:"auditor"\x12\x8e\x01\n\nattributes\x18\x04 \x03(\x0b2\x1d.akash.base.v1beta1.AttributeB[\xaa\xdf\x1f0github.com/ovrclk/akash/types/v1beta1.Attributes\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes""\x88\x02\n\x11AuditedAttributes\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12.\n\x07auditor\x18\x02 \x01(\tB\x1d\xea\xde\x1f\x07auditor\xf2\xde\x1f\x0eyaml:"auditor"\x12\x8e\x01\n\nattributes\x18\x03 \x03(\x0b2\x1d.akash.base.v1beta1.AttributeB[\xaa\xdf\x1f0github.com/ovrclk/akash/types/v1beta1.Attributes\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes":\x08\xe8\xa0\x1f\x00\x98\xa0\x1f\x01"\x83\x01\n\x12AttributesResponse\x12c\n\nattributes\x18\x01 \x03(\x0b2&.akash.audit.v1beta1.AuditedAttributesB\'\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes":\x08\xe8\xa0\x1f\x00\x98\xa0\x1f\x01"}\n\x11AttributesFilters\x121\n\x08auditors\x18\x01 \x03(\tB\x1f\xea\xde\x1f\x08auditors\xf2\xde\x1f\x0fyaml:"auditors"\x12+\n\x06owners\x18\x02 \x03(\tB\x1b\xea\xde\x1f\x06owners\xf2\xde\x1f\ryaml:"owners":\x08\xe8\xa0\x1f\x00\x98\xa0\x1f\x01"\x8c\x02\n\x19MsgSignProviderAttributes\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12.\n\x07auditor\x18\x02 \x01(\tB\x1d\xea\xde\x1f\x07auditor\xf2\xde\x1f\x0eyaml:"auditor"\x12\x8e\x01\n\nattributes\x18\x03 \x03(\x0b2\x1d.akash.base.v1beta1.AttributeB[\xaa\xdf\x1f0github.com/ovrclk/akash/types/v1beta1.Attributes\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes":\x04\xe8\xa0\x1f\x00"#\n!MsgSignProviderAttributesResponse"\xa4\x01\n\x1bMsgDeleteProviderAttributes\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12.\n\x07auditor\x18\x02 \x01(\tB\x1d\xea\xde\x1f\x07auditor\xf2\xde\x1f\x0eyaml:"auditor"\x12%\n\x04keys\x18\x03 \x03(\tB\x17\xea\xde\x1f\x04keys\xf2\xde\x1f\x0byaml:"keys":\x04\xe8\xa0\x1f\x00"%\n#MsgDeleteProviderAttributesResponse2\x91\x02\n\x03Msg\x12\x80\x01\n\x16SignProviderAttributes\x12..akash.audit.v1beta1.MsgSignProviderAttributes\x1a6.akash.audit.v1beta1.MsgSignProviderAttributesResponse\x12\x86\x01\n\x18DeleteProviderAttributes\x120.akash.audit.v1beta1.MsgDeleteProviderAttributes\x1a8.akash.audit.v1beta1.MsgDeleteProviderAttributesResponseB/Z-github.com/ovrclk/akash/x/audit/types/v1beta1b\x06proto3')
_PROVIDER = DESCRIPTOR.message_types_by_name['Provider']
_AUDITEDATTRIBUTES = DESCRIPTOR.message_types_by_name['AuditedAttributes']
_ATTRIBUTESRESPONSE = DESCRIPTOR.message_types_by_name['AttributesResponse']
_ATTRIBUTESFILTERS = DESCRIPTOR.message_types_by_name['AttributesFilters']
_MSGSIGNPROVIDERATTRIBUTES = DESCRIPTOR.message_types_by_name['MsgSignProviderAttributes']
_MSGSIGNPROVIDERATTRIBUTESRESPONSE = DESCRIPTOR.message_types_by_name['MsgSignProviderAttributesResponse']
_MSGDELETEPROVIDERATTRIBUTES = DESCRIPTOR.message_types_by_name['MsgDeleteProviderAttributes']
_MSGDELETEPROVIDERATTRIBUTESRESPONSE = DESCRIPTOR.message_types_by_name['MsgDeleteProviderAttributesResponse']
Provider = _reflection.GeneratedProtocolMessageType('Provider', (_message.Message,), {'DESCRIPTOR': _PROVIDER, '__module__': 'akash.audit.v1beta1.audit_pb2'})
_sym_db.RegisterMessage(Provider)
AuditedAttributes = _reflection.GeneratedProtocolMessageType('AuditedAttributes', (_message.Message,), {'DESCRIPTOR': _AUDITEDATTRIBUTES, '__module__': 'akash.audit.v1beta1.audit_pb2'})
_sym_db.RegisterMessage(AuditedAttributes)
AttributesResponse = _reflection.GeneratedProtocolMessageType('AttributesResponse', (_message.Message,), {'DESCRIPTOR': _ATTRIBUTESRESPONSE, '__module__': 'akash.audit.v1beta1.audit_pb2'})
_sym_db.RegisterMessage(AttributesResponse)
AttributesFilters = _reflection.GeneratedProtocolMessageType('AttributesFilters', (_message.Message,), {'DESCRIPTOR': _ATTRIBUTESFILTERS, '__module__': 'akash.audit.v1beta1.audit_pb2'})
_sym_db.RegisterMessage(AttributesFilters)
MsgSignProviderAttributes = _reflection.GeneratedProtocolMessageType('MsgSignProviderAttributes', (_message.Message,), {'DESCRIPTOR': _MSGSIGNPROVIDERATTRIBUTES, '__module__': 'akash.audit.v1beta1.audit_pb2'})
_sym_db.RegisterMessage(MsgSignProviderAttributes)
MsgSignProviderAttributesResponse = _reflection.GeneratedProtocolMessageType('MsgSignProviderAttributesResponse', (_message.Message,), {'DESCRIPTOR': _MSGSIGNPROVIDERATTRIBUTESRESPONSE, '__module__': 'akash.audit.v1beta1.audit_pb2'})
_sym_db.RegisterMessage(MsgSignProviderAttributesResponse)
MsgDeleteProviderAttributes = _reflection.GeneratedProtocolMessageType('MsgDeleteProviderAttributes', (_message.Message,), {'DESCRIPTOR': _MSGDELETEPROVIDERATTRIBUTES, '__module__': 'akash.audit.v1beta1.audit_pb2'})
_sym_db.RegisterMessage(MsgDeleteProviderAttributes)
MsgDeleteProviderAttributesResponse = _reflection.GeneratedProtocolMessageType('MsgDeleteProviderAttributesResponse', (_message.Message,), {'DESCRIPTOR': _MSGDELETEPROVIDERATTRIBUTESRESPONSE, '__module__': 'akash.audit.v1beta1.audit_pb2'})
_sym_db.RegisterMessage(MsgDeleteProviderAttributesResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/ovrclk/akash/x/audit/types/v1beta1'
    _PROVIDER.fields_by_name['owner']._options = None
    _PROVIDER.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _PROVIDER.fields_by_name['auditor']._options = None
    _PROVIDER.fields_by_name['auditor']._serialized_options = b'\xea\xde\x1f\x07auditor\xf2\xde\x1f\x0eyaml:"auditor"'
    _PROVIDER.fields_by_name['attributes']._options = None
    _PROVIDER.fields_by_name['attributes']._serialized_options = b'\xaa\xdf\x1f0github.com/ovrclk/akash/types/v1beta1.Attributes\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"'
    _AUDITEDATTRIBUTES.fields_by_name['owner']._options = None
    _AUDITEDATTRIBUTES.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _AUDITEDATTRIBUTES.fields_by_name['auditor']._options = None
    _AUDITEDATTRIBUTES.fields_by_name['auditor']._serialized_options = b'\xea\xde\x1f\x07auditor\xf2\xde\x1f\x0eyaml:"auditor"'
    _AUDITEDATTRIBUTES.fields_by_name['attributes']._options = None
    _AUDITEDATTRIBUTES.fields_by_name['attributes']._serialized_options = b'\xaa\xdf\x1f0github.com/ovrclk/akash/types/v1beta1.Attributes\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"'
    _AUDITEDATTRIBUTES._options = None
    _AUDITEDATTRIBUTES._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x01'
    _ATTRIBUTESRESPONSE.fields_by_name['attributes']._options = None
    _ATTRIBUTESRESPONSE.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"'
    _ATTRIBUTESRESPONSE._options = None
    _ATTRIBUTESRESPONSE._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x01'
    _ATTRIBUTESFILTERS.fields_by_name['auditors']._options = None
    _ATTRIBUTESFILTERS.fields_by_name['auditors']._serialized_options = b'\xea\xde\x1f\x08auditors\xf2\xde\x1f\x0fyaml:"auditors"'
    _ATTRIBUTESFILTERS.fields_by_name['owners']._options = None
    _ATTRIBUTESFILTERS.fields_by_name['owners']._serialized_options = b'\xea\xde\x1f\x06owners\xf2\xde\x1f\ryaml:"owners"'
    _ATTRIBUTESFILTERS._options = None
    _ATTRIBUTESFILTERS._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x01'
    _MSGSIGNPROVIDERATTRIBUTES.fields_by_name['owner']._options = None
    _MSGSIGNPROVIDERATTRIBUTES.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGSIGNPROVIDERATTRIBUTES.fields_by_name['auditor']._options = None
    _MSGSIGNPROVIDERATTRIBUTES.fields_by_name['auditor']._serialized_options = b'\xea\xde\x1f\x07auditor\xf2\xde\x1f\x0eyaml:"auditor"'
    _MSGSIGNPROVIDERATTRIBUTES.fields_by_name['attributes']._options = None
    _MSGSIGNPROVIDERATTRIBUTES.fields_by_name['attributes']._serialized_options = b'\xaa\xdf\x1f0github.com/ovrclk/akash/types/v1beta1.Attributes\xc8\xde\x1f\x00\xea\xde\x1f\nattributes\xf2\xde\x1f\x11yaml:"attributes"'
    _MSGSIGNPROVIDERATTRIBUTES._options = None
    _MSGSIGNPROVIDERATTRIBUTES._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGDELETEPROVIDERATTRIBUTES.fields_by_name['owner']._options = None
    _MSGDELETEPROVIDERATTRIBUTES.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGDELETEPROVIDERATTRIBUTES.fields_by_name['auditor']._options = None
    _MSGDELETEPROVIDERATTRIBUTES.fields_by_name['auditor']._serialized_options = b'\xea\xde\x1f\x07auditor\xf2\xde\x1f\x0eyaml:"auditor"'
    _MSGDELETEPROVIDERATTRIBUTES.fields_by_name['keys']._options = None
    _MSGDELETEPROVIDERATTRIBUTES.fields_by_name['keys']._serialized_options = b'\xea\xde\x1f\x04keys\xf2\xde\x1f\x0byaml:"keys"'
    _MSGDELETEPROVIDERATTRIBUTES._options = None
    _MSGDELETEPROVIDERATTRIBUTES._serialized_options = b'\xe8\xa0\x1f\x00'
    _PROVIDER._serialized_start = 115
    _PROVIDER._serialized_end = 360
    _AUDITEDATTRIBUTES._serialized_start = 363
    _AUDITEDATTRIBUTES._serialized_end = 627
    _ATTRIBUTESRESPONSE._serialized_start = 630
    _ATTRIBUTESRESPONSE._serialized_end = 761
    _ATTRIBUTESFILTERS._serialized_start = 763
    _ATTRIBUTESFILTERS._serialized_end = 888
    _MSGSIGNPROVIDERATTRIBUTES._serialized_start = 891
    _MSGSIGNPROVIDERATTRIBUTES._serialized_end = 1159
    _MSGSIGNPROVIDERATTRIBUTESRESPONSE._serialized_start = 1161
    _MSGSIGNPROVIDERATTRIBUTESRESPONSE._serialized_end = 1196
    _MSGDELETEPROVIDERATTRIBUTES._serialized_start = 1199
    _MSGDELETEPROVIDERATTRIBUTES._serialized_end = 1363
    _MSGDELETEPROVIDERATTRIBUTESRESPONSE._serialized_start = 1365
    _MSGDELETEPROVIDERATTRIBUTESRESPONSE._serialized_end = 1402
    _MSG._serialized_start = 1405
    _MSG._serialized_end = 1678

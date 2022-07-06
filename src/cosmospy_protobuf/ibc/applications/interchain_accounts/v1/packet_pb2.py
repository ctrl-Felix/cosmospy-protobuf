
'Generated protocol buffer code.'
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4ibc/applications/interchain_accounts/v1/packet.proto\x12\'ibc.applications.interchain_accounts.v1\x1a\x19google/protobuf/any.proto\x1a\x14gogoproto/gogo.proto"v\n\x1bInterchainAccountPacketData\x12;\n\x04type\x18\x01 \x01(\x0e2-.ibc.applications.interchain_accounts.v1.Type\x12\x0c\n\x04data\x18\x02 \x01(\x0c\x12\x0c\n\x04memo\x18\x03 \x01(\t"2\n\x08CosmosTx\x12&\n\x08messages\x18\x01 \x03(\x0b2\x14.google.protobuf.Any*X\n\x04Type\x12%\n\x10TYPE_UNSPECIFIED\x10\x00\x1a\x0f\x8a\x9d \x0bUNSPECIFIED\x12#\n\x0fTYPE_EXECUTE_TX\x10\x01\x1a\x0e\x8a\x9d \nEXECUTE_TX\x1a\x04\x88\xa3\x1e\x00BGZEgithub.com/cosmos/ibc-go/v3/modules/apps/27-interchain-accounts/typesb\x06proto3')
_TYPE = DESCRIPTOR.enum_types_by_name['Type']
Type = enum_type_wrapper.EnumTypeWrapper(_TYPE)
TYPE_UNSPECIFIED = 0
TYPE_EXECUTE_TX = 1
_INTERCHAINACCOUNTPACKETDATA = DESCRIPTOR.message_types_by_name['InterchainAccountPacketData']
_COSMOSTX = DESCRIPTOR.message_types_by_name['CosmosTx']
InterchainAccountPacketData = _reflection.GeneratedProtocolMessageType('InterchainAccountPacketData', (_message.Message,), {'DESCRIPTOR': _INTERCHAINACCOUNTPACKETDATA, '__module__': 'ibc.applications.interchain_accounts.v1.packet_pb2'})
_sym_db.RegisterMessage(InterchainAccountPacketData)
CosmosTx = _reflection.GeneratedProtocolMessageType('CosmosTx', (_message.Message,), {'DESCRIPTOR': _COSMOSTX, '__module__': 'ibc.applications.interchain_accounts.v1.packet_pb2'})
_sym_db.RegisterMessage(CosmosTx)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZEgithub.com/cosmos/ibc-go/v3/modules/apps/27-interchain-accounts/types'
    _TYPE._options = None
    _TYPE._serialized_options = b'\x88\xa3\x1e\x00'
    _TYPE.values_by_name['TYPE_UNSPECIFIED']._options = None
    _TYPE.values_by_name['TYPE_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x0bUNSPECIFIED'
    _TYPE.values_by_name['TYPE_EXECUTE_TX']._options = None
    _TYPE.values_by_name['TYPE_EXECUTE_TX']._serialized_options = b'\x8a\x9d \nEXECUTE_TX'
    _TYPE._serialized_start = 318
    _TYPE._serialized_end = 406
    _INTERCHAINACCOUNTPACKETDATA._serialized_start = 146
    _INTERCHAINACCOUNTPACKETDATA._serialized_end = 264
    _COSMOSTX._serialized_start = 266
    _COSMOSTX._serialized_end = 316

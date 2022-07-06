
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'bitsong/fantoken/v1beta1/fantoken.proto\x12\x18bitsong.fantoken.v1beta1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto"Q\n\x08Metadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x14\n\x03uri\x18\x03 \x01(\tB\x07\xe2\xde\x1f\x03URI\x12\x11\n\tauthority\x18\x04 \x01(\t"\xdd\x01\n\x08FanToken\x12\r\n\x05denom\x18\x01 \x01(\t\x12W\n\nmax_supply\x18\x02 \x01(\tBC\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x11yaml:"max_supply"\xc8\xde\x1f\x00\x12\x0e\n\x06minter\x18\x03 \x01(\t\x12O\n\tmeta_data\x18\x04 \x01(\x0b2".bitsong.fantoken.v1beta1.MetadataB\x18\xf2\xde\x1f\x10yaml:"meta_data"\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00B<Z6github.com/bitsongofficial/go-bitsong/x/fantoken/types\xc8\xe1\x1e\x00b\x06proto3')
_METADATA = DESCRIPTOR.message_types_by_name['Metadata']
_FANTOKEN = DESCRIPTOR.message_types_by_name['FanToken']
Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {'DESCRIPTOR': _METADATA, '__module__': 'bitsong.fantoken.v1beta1.fantoken_pb2'})
_sym_db.RegisterMessage(Metadata)
FanToken = _reflection.GeneratedProtocolMessageType('FanToken', (_message.Message,), {'DESCRIPTOR': _FANTOKEN, '__module__': 'bitsong.fantoken.v1beta1.fantoken_pb2'})
_sym_db.RegisterMessage(FanToken)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/bitsongofficial/go-bitsong/x/fantoken/types\xc8\xe1\x1e\x00'
    _METADATA.fields_by_name['uri']._options = None
    _METADATA.fields_by_name['uri']._serialized_options = b'\xe2\xde\x1f\x03URI'
    _FANTOKEN.fields_by_name['max_supply']._options = None
    _FANTOKEN.fields_by_name['max_supply']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x11yaml:"max_supply"\xc8\xde\x1f\x00'
    _FANTOKEN.fields_by_name['meta_data']._options = None
    _FANTOKEN.fields_by_name['meta_data']._serialized_options = b'\xf2\xde\x1f\x10yaml:"meta_data"\xc8\xde\x1f\x00'
    _FANTOKEN._options = None
    _FANTOKEN._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _METADATA._serialized_start = 123
    _METADATA._serialized_end = 204
    _FANTOKEN._serialized_start = 207
    _FANTOKEN._serialized_end = 428

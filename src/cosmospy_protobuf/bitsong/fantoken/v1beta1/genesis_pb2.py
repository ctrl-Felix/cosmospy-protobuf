
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....bitsong.fantoken.v1beta1 import fantoken_pb2 as bitsong_dot_fantoken_dot_v1beta1_dot_fantoken__pb2
from ....bitsong.fantoken.v1beta1 import params_pb2 as bitsong_dot_fantoken_dot_v1beta1_dot_params__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&bitsong/fantoken/v1beta1/genesis.proto\x12\x18bitsong.fantoken.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\'bitsong/fantoken/v1beta1/fantoken.proto\x1a%bitsong/fantoken/v1beta1/params.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x84\x01\n\x0cGenesisState\x126\n\x06params\x18\x01 \x01(\x0b2 .bitsong.fantoken.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12<\n\nfan_tokens\x18\x02 \x03(\x0b2".bitsong.fantoken.v1beta1.FanTokenB\x04\xc8\xde\x1f\x00B8Z6github.com/bitsongofficial/go-bitsong/x/fantoken/typesb\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'bitsong.fantoken.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/bitsongofficial/go-bitsong/x/fantoken/types'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['fan_tokens']._options = None
    _GENESISSTATE.fields_by_name['fan_tokens']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE._serialized_start = 203
    _GENESISSTATE._serialized_end = 335


'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....bitsong.merkledrop.v1beta1 import merkledrop_pb2 as bitsong_dot_merkledrop_dot_v1beta1_dot_merkledrop__pb2
from ....bitsong.merkledrop.v1beta1 import params_pb2 as bitsong_dot_merkledrop_dot_v1beta1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(bitsong/merkledrop/v1beta1/genesis.proto\x12\x1abitsong.merkledrop.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a+bitsong/merkledrop/v1beta1/merkledrop.proto\x1a\'bitsong/merkledrop/v1beta1/params.proto"M\n\x07Indexes\x12%\n\rmerkledrop_id\x18\x01 \x01(\x04B\x0e\xf2\xde\x1f\nyaml:"mdi"\x12\x1b\n\x05index\x18\x02 \x03(\x04B\x0c\xf2\xde\x1f\x08yaml:"i""\xdd\x01\n\x0cGenesisState\x12\x1a\n\x12last_merkledrop_id\x18\x01 \x01(\x04\x12A\n\x0bmerkledrops\x18\x02 \x03(\x0b2&.bitsong.merkledrop.v1beta1.MerkledropB\x04\xc8\xde\x1f\x00\x124\n\x07indexes\x18\x03 \x03(\x0b2#.bitsong.merkledrop.v1beta1.Indexes\x128\n\x06params\x18\x04 \x01(\x0b2".bitsong.merkledrop.v1beta1.ParamsB\x04\xc8\xde\x1f\x00B>Z8github.com/bitsongofficial/go-bitsong/x/merkledrop/types\xc8\xe1\x1e\x00b\x06proto3')
_INDEXES = DESCRIPTOR.message_types_by_name['Indexes']
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
Indexes = _reflection.GeneratedProtocolMessageType('Indexes', (_message.Message,), {'DESCRIPTOR': _INDEXES, '__module__': 'bitsong.merkledrop.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(Indexes)
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'bitsong.merkledrop.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/bitsongofficial/go-bitsong/x/merkledrop/types\xc8\xe1\x1e\x00'
    _INDEXES.fields_by_name['merkledrop_id']._options = None
    _INDEXES.fields_by_name['merkledrop_id']._serialized_options = b'\xf2\xde\x1f\nyaml:"mdi"'
    _INDEXES.fields_by_name['index']._options = None
    _INDEXES.fields_by_name['index']._serialized_options = b'\xf2\xde\x1f\x08yaml:"i"'
    _GENESISSTATE.fields_by_name['merkledrops']._options = None
    _GENESISSTATE.fields_by_name['merkledrops']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _INDEXES._serialized_start = 212
    _INDEXES._serialized_end = 289
    _GENESISSTATE._serialized_start = 292
    _GENESISSTATE._serialized_end = 513

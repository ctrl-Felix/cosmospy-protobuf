
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....osmosis.txfees.v1beta1 import feetoken_pb2 as osmosis_dot_txfees_dot_v1beta1_dot_feetoken__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$osmosis/txfees/v1beta1/genesis.proto\x12\x16osmosis.txfees.v1beta1\x1a\x14gogoproto/gogo.proto\x1a%osmosis/txfees/v1beta1/feetoken.proto"\\\n\x0cGenesisState\x12\x11\n\tbasedenom\x18\x01 \x01(\t\x129\n\tfeetokens\x18\x02 \x03(\x0b2 .osmosis.txfees.v1beta1.FeeTokenB\x04\xc8\xde\x1f\x00B3Z1github.com/osmosis-labs/osmosis/v7/x/txfees/typesb\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'osmosis.txfees.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/osmosis-labs/osmosis/v7/x/txfees/types'
    _GENESISSTATE.fields_by_name['feetokens']._options = None
    _GENESISSTATE.fields_by_name['feetokens']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE._serialized_start = 125
    _GENESISSTATE._serialized_end = 217

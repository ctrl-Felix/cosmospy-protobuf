
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...osmosis.lockup import lock_pb2 as osmosis_dot_lockup_dot_lock__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cosmosis/lockup/genesis.proto\x12\x0eosmosis.lockup\x1a\x14gogoproto/gogo.proto\x1a\x19osmosis/lockup/lock.proto"\x93\x01\n\x0cGenesisState\x12\x14\n\x0clast_lock_id\x18\x01 \x01(\x04\x12/\n\x05locks\x18\x02 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00\x12<\n\x0fsynthetic_locks\x18\x03 \x03(\x0b2\x1d.osmosis.lockup.SyntheticLockB\x04\xc8\xde\x1f\x00B3Z1github.com/osmosis-labs/osmosis/v7/x/lockup/typesb\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'osmosis.lockup.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/osmosis-labs/osmosis/v7/x/lockup/types'
    _GENESISSTATE.fields_by_name['locks']._options = None
    _GENESISSTATE.fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['synthetic_locks']._options = None
    _GENESISSTATE.fields_by_name['synthetic_locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE._serialized_start = 98
    _GENESISSTATE._serialized_end = 245

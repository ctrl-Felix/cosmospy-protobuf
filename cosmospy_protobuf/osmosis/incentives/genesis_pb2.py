
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ...osmosis.incentives import params_pb2 as osmosis_dot_incentives_dot_params__pb2
from ...osmosis.incentives import gauge_pb2 as osmosis_dot_incentives_dot_gauge__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n osmosis/incentives/genesis.proto\x12\x12osmosis.incentives\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fosmosis/incentives/params.proto\x1a\x1eosmosis/incentives/gauge.proto"\xe6\x01\n\x0cGenesisState\x120\n\x06params\x18\x01 \x01(\x0b2\x1a.osmosis.incentives.ParamsB\x04\xc8\xde\x1f\x00\x12/\n\x06gauges\x18\x02 \x03(\x0b2\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00\x12\\\n\x12lockable_durations\x18\x03 \x03(\x0b2\x19.google.protobuf.DurationB%\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x19yaml:"lockable_durations"\x12\x15\n\rlast_gauge_id\x18\x04 \x01(\x04B7Z5github.com/osmosis-labs/osmosis/v7/x/incentives/typesb\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'osmosis.incentives.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/osmosis-labs/osmosis/v7/x/incentives/types'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['gauges']._options = None
    _GENESISSTATE.fields_by_name['gauges']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['lockable_durations']._options = None
    _GENESISSTATE.fields_by_name['lockable_durations']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x19yaml:"lockable_durations"'
    _GENESISSTATE._serialized_start = 176
    _GENESISSTATE._serialized_end = 406


'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....umee.oracle.v1beta1 import oracle_pb2 as umee_dot_oracle_dot_v1beta1_dot_oracle__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!umee/oracle/v1beta1/genesis.proto\x12\x1fumeenetwork.umee.oracle.v1beta1\x1a\x14gogoproto/gogo.proto\x1a umee/oracle/v1beta1/oracle.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xad\x04\n\x0cGenesisState\x12=\n\x06params\x18\x01 \x01(\x0b2\'.umeenetwork.umee.oracle.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12S\n\x12feeder_delegations\x18\x02 \x03(\x0b21.umeenetwork.umee.oracle.v1beta1.FeederDelegationB\x04\xc8\xde\x1f\x00\x12f\n\x0eexchange_rates\x18\x03 \x03(\x0b22.umeenetwork.umee.oracle.v1beta1.ExchangeRateTupleB\x1a\xaa\xdf\x1f\x12ExchangeRateTuples\xc8\xde\x1f\x00\x12I\n\rmiss_counters\x18\x04 \x03(\x0b2,.umeenetwork.umee.oracle.v1beta1.MissCounterB\x04\xc8\xde\x1f\x00\x12m\n aggregate_exchange_rate_prevotes\x18\x05 \x03(\x0b2=.umeenetwork.umee.oracle.v1beta1.AggregateExchangeRatePrevoteB\x04\xc8\xde\x1f\x00\x12g\n\x1daggregate_exchange_rate_votes\x18\x06 \x03(\x0b2:.umeenetwork.umee.oracle.v1beta1.AggregateExchangeRateVoteB\x04\xc8\xde\x1f\x00"E\n\x10FeederDelegation\x12\x16\n\x0efeeder_address\x18\x01 \x01(\t\x12\x19\n\x11validator_address\x18\x02 \x01(\t">\n\x0bMissCounter\x12\x19\n\x11validator_address\x18\x01 \x01(\t\x12\x14\n\x0cmiss_counter\x18\x02 \x01(\x04B0Z.github.com/umee-network/umee/v2/x/oracle/typesb\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_FEEDERDELEGATION = DESCRIPTOR.message_types_by_name['FeederDelegation']
_MISSCOUNTER = DESCRIPTOR.message_types_by_name['MissCounter']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'umee.oracle.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
FeederDelegation = _reflection.GeneratedProtocolMessageType('FeederDelegation', (_message.Message,), {'DESCRIPTOR': _FEEDERDELEGATION, '__module__': 'umee.oracle.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(FeederDelegation)
MissCounter = _reflection.GeneratedProtocolMessageType('MissCounter', (_message.Message,), {'DESCRIPTOR': _MISSCOUNTER, '__module__': 'umee.oracle.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(MissCounter)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z.github.com/umee-network/umee/v2/x/oracle/types'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['feeder_delegations']._options = None
    _GENESISSTATE.fields_by_name['feeder_delegations']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['exchange_rates']._options = None
    _GENESISSTATE.fields_by_name['exchange_rates']._serialized_options = b'\xaa\xdf\x1f\x12ExchangeRateTuples\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['miss_counters']._options = None
    _GENESISSTATE.fields_by_name['miss_counters']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['aggregate_exchange_rate_prevotes']._options = None
    _GENESISSTATE.fields_by_name['aggregate_exchange_rate_prevotes']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['aggregate_exchange_rate_votes']._options = None
    _GENESISSTATE.fields_by_name['aggregate_exchange_rate_votes']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE._serialized_start = 159
    _GENESISSTATE._serialized_end = 716
    _FEEDERDELEGATION._serialized_start = 718
    _FEEDERDELEGATION._serialized_end = 787
    _MISSCOUNTER._serialized_start = 789
    _MISSCOUNTER._serialized_end = 851

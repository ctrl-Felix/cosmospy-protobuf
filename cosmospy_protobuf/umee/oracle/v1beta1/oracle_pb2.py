
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n umee/oracle/v1beta1/oracle.proto\x12\x1fumeenetwork.umee.oracle.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xa9\x05\n\x06Params\x12+\n\x0bvote_period\x18\x01 \x01(\x04B\x16\xf2\xde\x1f\x12yaml:"vote_period"\x12_\n\x0evote_threshold\x18\x02 \x01(\tBG\xf2\xde\x1f\x15yaml:"vote_threshold"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12Y\n\x0breward_band\x18\x03 \x01(\tBD\xf2\xde\x1f\x12yaml:"reward_band"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12I\n\x1areward_distribution_window\x18\x04 \x01(\x04B%\xf2\xde\x1f!yaml:"reward_distribution_window"\x12d\n\x0baccept_list\x18\x05 \x03(\x0b2&.umeenetwork.umee.oracle.v1beta1.DenomB\'\xf2\xde\x1f\x12yaml:"accept_list"\xaa\xdf\x1f\tDenomList\xc8\xde\x1f\x00\x12_\n\x0eslash_fraction\x18\x06 \x01(\tBG\xf2\xde\x1f\x15yaml:"slash_fraction"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12-\n\x0cslash_window\x18\x07 \x01(\x04B\x17\xf2\xde\x1f\x13yaml:"slash_window"\x12k\n\x14min_valid_per_window\x18\x08 \x01(\tBM\xf2\xde\x1f\x1byaml:"min_valid_per_window"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00"\x96\x01\n\x05Denom\x12)\n\nbase_denom\x18\x01 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"base_denom"\x12-\n\x0csymbol_denom\x18\x02 \x01(\tB\x17\xf2\xde\x1f\x13yaml:"symbol_denom"\x12%\n\x08exponent\x18\x03 \x01(\rB\x13\xf2\xde\x1f\x0fyaml:"exponent":\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00"\x9b\x01\n\x1cAggregateExchangeRatePrevote\x12\x1d\n\x04hash\x18\x01 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:"hash"\x12\x1f\n\x05voter\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"voter"\x12-\n\x0csubmit_block\x18\x03 \x01(\x04B\x17\xf2\xde\x1f\x13yaml:"submit_block":\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00"\xd8\x01\n\x19AggregateExchangeRateVote\x12\x8b\x01\n\x14exchange_rate_tuples\x18\x01 \x03(\x0b22.umeenetwork.umee.oracle.v1beta1.ExchangeRateTupleB9\xf2\xde\x1f\x1byaml:"exchange_rate_tuples"\xaa\xdf\x1f\x12ExchangeRateTuples\xc8\xde\x1f\x00\x12\x1f\n\x05voter\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"voter":\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00"\xa1\x01\n\x11ExchangeRateTuple\x12\x1f\n\x05denom\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"denom"\x12]\n\rexchange_rate\x18\x02 \x01(\tBF\xf2\xde\x1f\x14yaml:"exchange_rate"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00B0Z.github.com/umee-network/umee/v2/x/oracle/typesb\x06proto3')
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
_DENOM = DESCRIPTOR.message_types_by_name['Denom']
_AGGREGATEEXCHANGERATEPREVOTE = DESCRIPTOR.message_types_by_name['AggregateExchangeRatePrevote']
_AGGREGATEEXCHANGERATEVOTE = DESCRIPTOR.message_types_by_name['AggregateExchangeRateVote']
_EXCHANGERATETUPLE = DESCRIPTOR.message_types_by_name['ExchangeRateTuple']
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {'DESCRIPTOR': _PARAMS, '__module__': 'umee.oracle.v1beta1.oracle_pb2'})
_sym_db.RegisterMessage(Params)
Denom = _reflection.GeneratedProtocolMessageType('Denom', (_message.Message,), {'DESCRIPTOR': _DENOM, '__module__': 'umee.oracle.v1beta1.oracle_pb2'})
_sym_db.RegisterMessage(Denom)
AggregateExchangeRatePrevote = _reflection.GeneratedProtocolMessageType('AggregateExchangeRatePrevote', (_message.Message,), {'DESCRIPTOR': _AGGREGATEEXCHANGERATEPREVOTE, '__module__': 'umee.oracle.v1beta1.oracle_pb2'})
_sym_db.RegisterMessage(AggregateExchangeRatePrevote)
AggregateExchangeRateVote = _reflection.GeneratedProtocolMessageType('AggregateExchangeRateVote', (_message.Message,), {'DESCRIPTOR': _AGGREGATEEXCHANGERATEVOTE, '__module__': 'umee.oracle.v1beta1.oracle_pb2'})
_sym_db.RegisterMessage(AggregateExchangeRateVote)
ExchangeRateTuple = _reflection.GeneratedProtocolMessageType('ExchangeRateTuple', (_message.Message,), {'DESCRIPTOR': _EXCHANGERATETUPLE, '__module__': 'umee.oracle.v1beta1.oracle_pb2'})
_sym_db.RegisterMessage(ExchangeRateTuple)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z.github.com/umee-network/umee/v2/x/oracle/types'
    _PARAMS.fields_by_name['vote_period']._options = None
    _PARAMS.fields_by_name['vote_period']._serialized_options = b'\xf2\xde\x1f\x12yaml:"vote_period"'
    _PARAMS.fields_by_name['vote_threshold']._options = None
    _PARAMS.fields_by_name['vote_threshold']._serialized_options = b'\xf2\xde\x1f\x15yaml:"vote_threshold"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['reward_band']._options = None
    _PARAMS.fields_by_name['reward_band']._serialized_options = b'\xf2\xde\x1f\x12yaml:"reward_band"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['reward_distribution_window']._options = None
    _PARAMS.fields_by_name['reward_distribution_window']._serialized_options = b'\xf2\xde\x1f!yaml:"reward_distribution_window"'
    _PARAMS.fields_by_name['accept_list']._options = None
    _PARAMS.fields_by_name['accept_list']._serialized_options = b'\xf2\xde\x1f\x12yaml:"accept_list"\xaa\xdf\x1f\tDenomList\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['slash_fraction']._options = None
    _PARAMS.fields_by_name['slash_fraction']._serialized_options = b'\xf2\xde\x1f\x15yaml:"slash_fraction"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['slash_window']._options = None
    _PARAMS.fields_by_name['slash_window']._serialized_options = b'\xf2\xde\x1f\x13yaml:"slash_window"'
    _PARAMS.fields_by_name['min_valid_per_window']._options = None
    _PARAMS.fields_by_name['min_valid_per_window']._serialized_options = b'\xf2\xde\x1f\x1byaml:"min_valid_per_window"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS._options = None
    _PARAMS._serialized_options = b'\xe8\xa0\x1f\x01\x98\xa0\x1f\x00'
    _DENOM.fields_by_name['base_denom']._options = None
    _DENOM.fields_by_name['base_denom']._serialized_options = b'\xf2\xde\x1f\x11yaml:"base_denom"'
    _DENOM.fields_by_name['symbol_denom']._options = None
    _DENOM.fields_by_name['symbol_denom']._serialized_options = b'\xf2\xde\x1f\x13yaml:"symbol_denom"'
    _DENOM.fields_by_name['exponent']._options = None
    _DENOM.fields_by_name['exponent']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"exponent"'
    _DENOM._options = None
    _DENOM._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _AGGREGATEEXCHANGERATEPREVOTE.fields_by_name['hash']._options = None
    _AGGREGATEEXCHANGERATEPREVOTE.fields_by_name['hash']._serialized_options = b'\xf2\xde\x1f\x0byaml:"hash"'
    _AGGREGATEEXCHANGERATEPREVOTE.fields_by_name['voter']._options = None
    _AGGREGATEEXCHANGERATEPREVOTE.fields_by_name['voter']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"voter"'
    _AGGREGATEEXCHANGERATEPREVOTE.fields_by_name['submit_block']._options = None
    _AGGREGATEEXCHANGERATEPREVOTE.fields_by_name['submit_block']._serialized_options = b'\xf2\xde\x1f\x13yaml:"submit_block"'
    _AGGREGATEEXCHANGERATEPREVOTE._options = None
    _AGGREGATEEXCHANGERATEPREVOTE._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _AGGREGATEEXCHANGERATEVOTE.fields_by_name['exchange_rate_tuples']._options = None
    _AGGREGATEEXCHANGERATEVOTE.fields_by_name['exchange_rate_tuples']._serialized_options = b'\xf2\xde\x1f\x1byaml:"exchange_rate_tuples"\xaa\xdf\x1f\x12ExchangeRateTuples\xc8\xde\x1f\x00'
    _AGGREGATEEXCHANGERATEVOTE.fields_by_name['voter']._options = None
    _AGGREGATEEXCHANGERATEVOTE.fields_by_name['voter']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"voter"'
    _AGGREGATEEXCHANGERATEVOTE._options = None
    _AGGREGATEEXCHANGERATEVOTE._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _EXCHANGERATETUPLE.fields_by_name['denom']._options = None
    _EXCHANGERATETUPLE.fields_by_name['denom']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"denom"'
    _EXCHANGERATETUPLE.fields_by_name['exchange_rate']._options = None
    _EXCHANGERATETUPLE.fields_by_name['exchange_rate']._serialized_options = b'\xf2\xde\x1f\x14yaml:"exchange_rate"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _EXCHANGERATETUPLE._options = None
    _EXCHANGERATETUPLE._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _PARAMS._serialized_start = 124
    _PARAMS._serialized_end = 805
    _DENOM._serialized_start = 808
    _DENOM._serialized_end = 958
    _AGGREGATEEXCHANGERATEPREVOTE._serialized_start = 961
    _AGGREGATEEXCHANGERATEPREVOTE._serialized_end = 1116
    _AGGREGATEEXCHANGERATEVOTE._serialized_start = 1119
    _AGGREGATEEXCHANGERATEVOTE._serialized_end = 1335
    _EXCHANGERATETUPLE._serialized_start = 1338
    _EXCHANGERATETUPLE._serialized_end = 1499

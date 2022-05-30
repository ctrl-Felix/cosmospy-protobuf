
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....umee.oracle.v1 import oracle_pb2 as umee_dot_oracle_dot_v1_dot_oracle__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aumee/oracle/v1/query.proto\x12\x1aumeenetwork.umee.oracle.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bumee/oracle/v1/oracle.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"4\n\x19QueryExchangeRatesRequest\x12\r\n\x05denom\x18\x01 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x87\x01\n\x1aQueryExchangeRatesResponse\x12i\n\x0eexchange_rates\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00"!\n\x1fQueryActiveExchangeRatesRequest"8\n QueryActiveExchangeRatesResponse\x12\x14\n\x0cactive_rates\x18\x01 \x03(\t"@\n\x1cQueryFeederDelegationRequest\x12\x16\n\x0evalidator_addr\x18\x01 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"4\n\x1dQueryFeederDelegationResponse\x12\x13\n\x0bfeeder_addr\x18\x01 \x01(\t";\n\x17QueryMissCounterRequest\x12\x16\n\x0evalidator_addr\x18\x01 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"0\n\x18QueryMissCounterResponse\x12\x14\n\x0cmiss_counter\x18\x01 \x01(\x04"@\n\x1cQueryAggregatePrevoteRequest\x12\x16\n\x0evalidator_addr\x18\x01 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"z\n\x1dQueryAggregatePrevoteResponse\x12Y\n\x11aggregate_prevote\x18\x01 \x01(\x0b28.umeenetwork.umee.oracle.v1.AggregateExchangeRatePrevoteB\x04\xc8\xde\x1f\x00"\x1f\n\x1dQueryAggregatePrevotesRequest"|\n\x1eQueryAggregatePrevotesResponse\x12Z\n\x12aggregate_prevotes\x18\x01 \x03(\x0b28.umeenetwork.umee.oracle.v1.AggregateExchangeRatePrevoteB\x04\xc8\xde\x1f\x00"=\n\x19QueryAggregateVoteRequest\x12\x16\n\x0evalidator_addr\x18\x01 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"q\n\x1aQueryAggregateVoteResponse\x12S\n\x0eaggregate_vote\x18\x01 \x01(\x0b25.umeenetwork.umee.oracle.v1.AggregateExchangeRateVoteB\x04\xc8\xde\x1f\x00"\x1c\n\x1aQueryAggregateVotesRequest"s\n\x1bQueryAggregateVotesResponse\x12T\n\x0faggregate_votes\x18\x01 \x03(\x0b25.umeenetwork.umee.oracle.v1.AggregateExchangeRateVoteB\x04\xc8\xde\x1f\x00"\x14\n\x12QueryParamsRequest"O\n\x13QueryParamsResponse\x128\n\x06params\x18\x01 \x01(\x0b2".umeenetwork.umee.oracle.v1.ParamsB\x04\xc8\xde\x1f\x002\xa1\r\n\x05Query\x12\xb5\x01\n\rExchangeRates\x125.umeenetwork.umee.oracle.v1.QueryExchangeRatesRequest\x1a6.umeenetwork.umee.oracle.v1.QueryExchangeRatesResponse"5\x82\xd3\xe4\x93\x02/\x12-/umee/oracle/v1/denoms/exchange_rates/{denom}\x12\xc6\x01\n\x13ActiveExchangeRates\x12;.umeenetwork.umee.oracle.v1.QueryActiveExchangeRatesRequest\x1a<.umeenetwork.umee.oracle.v1.QueryActiveExchangeRatesResponse"4\x82\xd3\xe4\x93\x02.\x12,/umee/oracle/v1/denoms/active_exchange_rates\x12\xc3\x01\n\x10FeederDelegation\x128.umeenetwork.umee.oracle.v1.QueryFeederDelegationRequest\x1a9.umeenetwork.umee.oracle.v1.QueryFeederDelegationResponse":\x82\xd3\xe4\x93\x024\x122/umee/oracle/v1/validators/{validator_addr}/feeder\x12\xb2\x01\n\x0bMissCounter\x123.umeenetwork.umee.oracle.v1.QueryMissCounterRequest\x1a4.umeenetwork.umee.oracle.v1.QueryMissCounterResponse"8\x82\xd3\xe4\x93\x022\x120/umee/oracle/v1/validators/{validator_addr}/miss\x12\xce\x01\n\x10AggregatePrevote\x128.umeenetwork.umee.oracle.v1.QueryAggregatePrevoteRequest\x1a9.umeenetwork.umee.oracle.v1.QueryAggregatePrevoteResponse"E\x82\xd3\xe4\x93\x02?\x12=/umee/oracle/v1/validators/{validator_addr}/aggregate_prevote\x12\xc1\x01\n\x11AggregatePrevotes\x129.umeenetwork.umee.oracle.v1.QueryAggregatePrevotesRequest\x1a:.umeenetwork.umee.oracle.v1.QueryAggregatePrevotesResponse"5\x82\xd3\xe4\x93\x02/\x12-/umee/oracle/v1/validators/aggregate_prevotes\x12\xc2\x01\n\rAggregateVote\x125.umeenetwork.umee.oracle.v1.QueryAggregateVoteRequest\x1a6.umeenetwork.umee.oracle.v1.QueryAggregateVoteResponse"B\x82\xd3\xe4\x93\x02<\x12:/umee/oracle/v1/valdiators/{validator_addr}/aggregate_vote\x12\xb5\x01\n\x0eAggregateVotes\x126.umeenetwork.umee.oracle.v1.QueryAggregateVotesRequest\x1a7.umeenetwork.umee.oracle.v1.QueryAggregateVotesResponse"2\x82\xd3\xe4\x93\x02,\x12*/umee/oracle/v1/validators/aggregate_votes\x12\x89\x01\n\x06Params\x12..umeenetwork.umee.oracle.v1.QueryParamsRequest\x1a/.umeenetwork.umee.oracle.v1.QueryParamsResponse"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/umee/oracle/v1/paramsB0Z.github.com/umee-network/umee/v2/x/oracle/typesb\x06proto3')
_QUERYEXCHANGERATESREQUEST = DESCRIPTOR.message_types_by_name['QueryExchangeRatesRequest']
_QUERYEXCHANGERATESRESPONSE = DESCRIPTOR.message_types_by_name['QueryExchangeRatesResponse']
_QUERYACTIVEEXCHANGERATESREQUEST = DESCRIPTOR.message_types_by_name['QueryActiveExchangeRatesRequest']
_QUERYACTIVEEXCHANGERATESRESPONSE = DESCRIPTOR.message_types_by_name['QueryActiveExchangeRatesResponse']
_QUERYFEEDERDELEGATIONREQUEST = DESCRIPTOR.message_types_by_name['QueryFeederDelegationRequest']
_QUERYFEEDERDELEGATIONRESPONSE = DESCRIPTOR.message_types_by_name['QueryFeederDelegationResponse']
_QUERYMISSCOUNTERREQUEST = DESCRIPTOR.message_types_by_name['QueryMissCounterRequest']
_QUERYMISSCOUNTERRESPONSE = DESCRIPTOR.message_types_by_name['QueryMissCounterResponse']
_QUERYAGGREGATEPREVOTEREQUEST = DESCRIPTOR.message_types_by_name['QueryAggregatePrevoteRequest']
_QUERYAGGREGATEPREVOTERESPONSE = DESCRIPTOR.message_types_by_name['QueryAggregatePrevoteResponse']
_QUERYAGGREGATEPREVOTESREQUEST = DESCRIPTOR.message_types_by_name['QueryAggregatePrevotesRequest']
_QUERYAGGREGATEPREVOTESRESPONSE = DESCRIPTOR.message_types_by_name['QueryAggregatePrevotesResponse']
_QUERYAGGREGATEVOTEREQUEST = DESCRIPTOR.message_types_by_name['QueryAggregateVoteRequest']
_QUERYAGGREGATEVOTERESPONSE = DESCRIPTOR.message_types_by_name['QueryAggregateVoteResponse']
_QUERYAGGREGATEVOTESREQUEST = DESCRIPTOR.message_types_by_name['QueryAggregateVotesRequest']
_QUERYAGGREGATEVOTESRESPONSE = DESCRIPTOR.message_types_by_name['QueryAggregateVotesResponse']
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
QueryExchangeRatesRequest = _reflection.GeneratedProtocolMessageType('QueryExchangeRatesRequest', (_message.Message,), {'DESCRIPTOR': _QUERYEXCHANGERATESREQUEST, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryExchangeRatesRequest)
QueryExchangeRatesResponse = _reflection.GeneratedProtocolMessageType('QueryExchangeRatesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYEXCHANGERATESRESPONSE, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryExchangeRatesResponse)
QueryActiveExchangeRatesRequest = _reflection.GeneratedProtocolMessageType('QueryActiveExchangeRatesRequest', (_message.Message,), {'DESCRIPTOR': _QUERYACTIVEEXCHANGERATESREQUEST, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryActiveExchangeRatesRequest)
QueryActiveExchangeRatesResponse = _reflection.GeneratedProtocolMessageType('QueryActiveExchangeRatesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYACTIVEEXCHANGERATESRESPONSE, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryActiveExchangeRatesResponse)
QueryFeederDelegationRequest = _reflection.GeneratedProtocolMessageType('QueryFeederDelegationRequest', (_message.Message,), {'DESCRIPTOR': _QUERYFEEDERDELEGATIONREQUEST, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryFeederDelegationRequest)
QueryFeederDelegationResponse = _reflection.GeneratedProtocolMessageType('QueryFeederDelegationResponse', (_message.Message,), {'DESCRIPTOR': _QUERYFEEDERDELEGATIONRESPONSE, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryFeederDelegationResponse)
QueryMissCounterRequest = _reflection.GeneratedProtocolMessageType('QueryMissCounterRequest', (_message.Message,), {'DESCRIPTOR': _QUERYMISSCOUNTERREQUEST, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryMissCounterRequest)
QueryMissCounterResponse = _reflection.GeneratedProtocolMessageType('QueryMissCounterResponse', (_message.Message,), {'DESCRIPTOR': _QUERYMISSCOUNTERRESPONSE, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryMissCounterResponse)
QueryAggregatePrevoteRequest = _reflection.GeneratedProtocolMessageType('QueryAggregatePrevoteRequest', (_message.Message,), {'DESCRIPTOR': _QUERYAGGREGATEPREVOTEREQUEST, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryAggregatePrevoteRequest)
QueryAggregatePrevoteResponse = _reflection.GeneratedProtocolMessageType('QueryAggregatePrevoteResponse', (_message.Message,), {'DESCRIPTOR': _QUERYAGGREGATEPREVOTERESPONSE, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryAggregatePrevoteResponse)
QueryAggregatePrevotesRequest = _reflection.GeneratedProtocolMessageType('QueryAggregatePrevotesRequest', (_message.Message,), {'DESCRIPTOR': _QUERYAGGREGATEPREVOTESREQUEST, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryAggregatePrevotesRequest)
QueryAggregatePrevotesResponse = _reflection.GeneratedProtocolMessageType('QueryAggregatePrevotesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYAGGREGATEPREVOTESRESPONSE, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryAggregatePrevotesResponse)
QueryAggregateVoteRequest = _reflection.GeneratedProtocolMessageType('QueryAggregateVoteRequest', (_message.Message,), {'DESCRIPTOR': _QUERYAGGREGATEVOTEREQUEST, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryAggregateVoteRequest)
QueryAggregateVoteResponse = _reflection.GeneratedProtocolMessageType('QueryAggregateVoteResponse', (_message.Message,), {'DESCRIPTOR': _QUERYAGGREGATEVOTERESPONSE, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryAggregateVoteResponse)
QueryAggregateVotesRequest = _reflection.GeneratedProtocolMessageType('QueryAggregateVotesRequest', (_message.Message,), {'DESCRIPTOR': _QUERYAGGREGATEVOTESREQUEST, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryAggregateVotesRequest)
QueryAggregateVotesResponse = _reflection.GeneratedProtocolMessageType('QueryAggregateVotesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYAGGREGATEVOTESRESPONSE, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryAggregateVotesResponse)
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSREQUEST, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsRequest)
QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSRESPONSE, '__module__': 'umee.oracle.v1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z.github.com/umee-network/umee/v2/x/oracle/types'
    _QUERYEXCHANGERATESREQUEST._options = None
    _QUERYEXCHANGERATESREQUEST._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYEXCHANGERATESRESPONSE.fields_by_name['exchange_rates']._options = None
    _QUERYEXCHANGERATESRESPONSE.fields_by_name['exchange_rates']._serialized_options = b'\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _QUERYFEEDERDELEGATIONREQUEST._options = None
    _QUERYFEEDERDELEGATIONREQUEST._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYMISSCOUNTERREQUEST._options = None
    _QUERYMISSCOUNTERREQUEST._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYAGGREGATEPREVOTEREQUEST._options = None
    _QUERYAGGREGATEPREVOTEREQUEST._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYAGGREGATEPREVOTERESPONSE.fields_by_name['aggregate_prevote']._options = None
    _QUERYAGGREGATEPREVOTERESPONSE.fields_by_name['aggregate_prevote']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYAGGREGATEPREVOTESRESPONSE.fields_by_name['aggregate_prevotes']._options = None
    _QUERYAGGREGATEPREVOTESRESPONSE.fields_by_name['aggregate_prevotes']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYAGGREGATEVOTEREQUEST._options = None
    _QUERYAGGREGATEVOTEREQUEST._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYAGGREGATEVOTERESPONSE.fields_by_name['aggregate_vote']._options = None
    _QUERYAGGREGATEVOTERESPONSE.fields_by_name['aggregate_vote']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYAGGREGATEVOTESRESPONSE.fields_by_name['aggregate_votes']._options = None
    _QUERYAGGREGATEVOTESRESPONSE.fields_by_name['aggregate_votes']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['ExchangeRates']._options = None
    _QUERY.methods_by_name['ExchangeRates']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/umee/oracle/v1/denoms/exchange_rates/{denom}'
    _QUERY.methods_by_name['ActiveExchangeRates']._options = None
    _QUERY.methods_by_name['ActiveExchangeRates']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/umee/oracle/v1/denoms/active_exchange_rates'
    _QUERY.methods_by_name['FeederDelegation']._options = None
    _QUERY.methods_by_name['FeederDelegation']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/umee/oracle/v1/validators/{validator_addr}/feeder'
    _QUERY.methods_by_name['MissCounter']._options = None
    _QUERY.methods_by_name['MissCounter']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/umee/oracle/v1/validators/{validator_addr}/miss'
    _QUERY.methods_by_name['AggregatePrevote']._options = None
    _QUERY.methods_by_name['AggregatePrevote']._serialized_options = b'\x82\xd3\xe4\x93\x02?\x12=/umee/oracle/v1/validators/{validator_addr}/aggregate_prevote'
    _QUERY.methods_by_name['AggregatePrevotes']._options = None
    _QUERY.methods_by_name['AggregatePrevotes']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/umee/oracle/v1/validators/aggregate_prevotes'
    _QUERY.methods_by_name['AggregateVote']._options = None
    _QUERY.methods_by_name['AggregateVote']._serialized_options = b'\x82\xd3\xe4\x93\x02<\x12:/umee/oracle/v1/valdiators/{validator_addr}/aggregate_vote'
    _QUERY.methods_by_name['AggregateVotes']._options = None
    _QUERY.methods_by_name['AggregateVotes']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/umee/oracle/v1/validators/aggregate_votes'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18\x12\x16/umee/oracle/v1/params'
    _QUERYEXCHANGERATESREQUEST._serialized_start = 171
    _QUERYEXCHANGERATESREQUEST._serialized_end = 223
    _QUERYEXCHANGERATESRESPONSE._serialized_start = 226
    _QUERYEXCHANGERATESRESPONSE._serialized_end = 361
    _QUERYACTIVEEXCHANGERATESREQUEST._serialized_start = 363
    _QUERYACTIVEEXCHANGERATESREQUEST._serialized_end = 396
    _QUERYACTIVEEXCHANGERATESRESPONSE._serialized_start = 398
    _QUERYACTIVEEXCHANGERATESRESPONSE._serialized_end = 454
    _QUERYFEEDERDELEGATIONREQUEST._serialized_start = 456
    _QUERYFEEDERDELEGATIONREQUEST._serialized_end = 520
    _QUERYFEEDERDELEGATIONRESPONSE._serialized_start = 522
    _QUERYFEEDERDELEGATIONRESPONSE._serialized_end = 574
    _QUERYMISSCOUNTERREQUEST._serialized_start = 576
    _QUERYMISSCOUNTERREQUEST._serialized_end = 635
    _QUERYMISSCOUNTERRESPONSE._serialized_start = 637
    _QUERYMISSCOUNTERRESPONSE._serialized_end = 685
    _QUERYAGGREGATEPREVOTEREQUEST._serialized_start = 687
    _QUERYAGGREGATEPREVOTEREQUEST._serialized_end = 751
    _QUERYAGGREGATEPREVOTERESPONSE._serialized_start = 753
    _QUERYAGGREGATEPREVOTERESPONSE._serialized_end = 875
    _QUERYAGGREGATEPREVOTESREQUEST._serialized_start = 877
    _QUERYAGGREGATEPREVOTESREQUEST._serialized_end = 908
    _QUERYAGGREGATEPREVOTESRESPONSE._serialized_start = 910
    _QUERYAGGREGATEPREVOTESRESPONSE._serialized_end = 1034
    _QUERYAGGREGATEVOTEREQUEST._serialized_start = 1036
    _QUERYAGGREGATEVOTEREQUEST._serialized_end = 1097
    _QUERYAGGREGATEVOTERESPONSE._serialized_start = 1099
    _QUERYAGGREGATEVOTERESPONSE._serialized_end = 1212
    _QUERYAGGREGATEVOTESREQUEST._serialized_start = 1214
    _QUERYAGGREGATEVOTESREQUEST._serialized_end = 1242
    _QUERYAGGREGATEVOTESRESPONSE._serialized_start = 1244
    _QUERYAGGREGATEVOTESRESPONSE._serialized_end = 1359
    _QUERYPARAMSREQUEST._serialized_start = 1361
    _QUERYPARAMSREQUEST._serialized_end = 1381
    _QUERYPARAMSRESPONSE._serialized_start = 1383
    _QUERYPARAMSRESPONSE._serialized_end = 1462
    _QUERY._serialized_start = 1465
    _QUERY._serialized_end = 3162

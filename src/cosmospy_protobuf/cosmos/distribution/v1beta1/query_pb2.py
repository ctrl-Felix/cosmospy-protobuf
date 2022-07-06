
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.distribution.v1beta1 import distribution_pb2 as cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'cosmos/distribution/v1beta1/query.proto\x12\x1bcosmos.distribution.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a.cosmos/distribution/v1beta1/distribution.proto\x1a\x19cosmos_proto/cosmos.proto"\x14\n\x12QueryParamsRequest"P\n\x13QueryParamsResponse\x129\n\x06params\x18\x01 \x01(\x0b2#.cosmos.distribution.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"^\n\'QueryValidatorOutstandingRewardsRequest\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString"{\n(QueryValidatorOutstandingRewardsResponse\x12O\n\x07rewards\x18\x01 \x01(\x0b28.cosmos.distribution.v1beta1.ValidatorOutstandingRewardsB\x04\xc8\xde\x1f\x00"V\n\x1fQueryValidatorCommissionRequest\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString"y\n QueryValidatorCommissionResponse\x12U\n\ncommission\x18\x01 \x01(\x0b2;.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionB\x04\xc8\xde\x1f\x00"\xc9\x01\n\x1cQueryValidatorSlashesRequest\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x17\n\x0fstarting_height\x18\x02 \x01(\x04\x12\x15\n\rending_height\x18\x03 \x01(\x04\x12:\n\npagination\x18\x04 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x01"\xa5\x01\n\x1dQueryValidatorSlashesResponse\x12G\n\x07slashes\x18\x01 \x03(\x0b20.cosmos.distribution.v1beta1.ValidatorSlashEventB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x93\x01\n\x1dQueryDelegationRewardsRequest\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x123\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x84\x01\n\x1eQueryDelegationRewardsResponse\x12b\n\x07rewards\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins"c\n"QueryDelegationTotalRewardsRequest\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\xd6\x01\n#QueryDelegationTotalRewardsResponse\x12M\n\x07rewards\x18\x01 \x03(\x0b26.cosmos.distribution.v1beta1.DelegationDelegatorRewardB\x04\xc8\xde\x1f\x00\x12`\n\x05total\x18\x02 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins"`\n\x1fQueryDelegatorValidatorsRequest\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"@\n QueryDelegatorValidatorsResponse\x12\x12\n\nvalidators\x18\x01 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"e\n$QueryDelegatorWithdrawAddressRequest\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"e\n%QueryDelegatorWithdrawAddressResponse\x122\n\x10withdraw_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x1b\n\x19QueryCommunityPoolRequest"}\n\x1aQueryCommunityPoolResponse\x12_\n\x04pool\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x002\xd8\x0f\n\x05Query\x12\x98\x01\n\x06Params\x12/.cosmos.distribution.v1beta1.QueryParamsRequest\x1a0.cosmos.distribution.v1beta1.QueryParamsResponse"+\x82\xd3\xe4\x93\x02%\x12#/cosmos/distribution/v1beta1/params\x12\x83\x02\n\x1bValidatorOutstandingRewards\x12D.cosmos.distribution.v1beta1.QueryValidatorOutstandingRewardsRequest\x1aE.cosmos.distribution.v1beta1.QueryValidatorOutstandingRewardsResponse"W\x82\xd3\xe4\x93\x02Q\x12O/cosmos/distribution/v1beta1/validators/{validator_address}/outstanding_rewards\x12\xe2\x01\n\x13ValidatorCommission\x12<.cosmos.distribution.v1beta1.QueryValidatorCommissionRequest\x1a=.cosmos.distribution.v1beta1.QueryValidatorCommissionResponse"N\x82\xd3\xe4\x93\x02H\x12F/cosmos/distribution/v1beta1/validators/{validator_address}/commission\x12\xd6\x01\n\x10ValidatorSlashes\x129.cosmos.distribution.v1beta1.QueryValidatorSlashesRequest\x1a:.cosmos.distribution.v1beta1.QueryValidatorSlashesResponse"K\x82\xd3\xe4\x93\x02E\x12C/cosmos/distribution/v1beta1/validators/{validator_address}/slashes\x12\xed\x01\n\x11DelegationRewards\x12:.cosmos.distribution.v1beta1.QueryDelegationRewardsRequest\x1a;.cosmos.distribution.v1beta1.QueryDelegationRewardsResponse"_\x82\xd3\xe4\x93\x02Y\x12W/cosmos/distribution/v1beta1/delegators/{delegator_address}/rewards/{validator_address}\x12\xe8\x01\n\x16DelegationTotalRewards\x12?.cosmos.distribution.v1beta1.QueryDelegationTotalRewardsRequest\x1a@.cosmos.distribution.v1beta1.QueryDelegationTotalRewardsResponse"K\x82\xd3\xe4\x93\x02E\x12C/cosmos/distribution/v1beta1/delegators/{delegator_address}/rewards\x12\xe2\x01\n\x13DelegatorValidators\x12<.cosmos.distribution.v1beta1.QueryDelegatorValidatorsRequest\x1a=.cosmos.distribution.v1beta1.QueryDelegatorValidatorsResponse"N\x82\xd3\xe4\x93\x02H\x12F/cosmos/distribution/v1beta1/delegators/{delegator_address}/validators\x12\xf7\x01\n\x18DelegatorWithdrawAddress\x12A.cosmos.distribution.v1beta1.QueryDelegatorWithdrawAddressRequest\x1aB.cosmos.distribution.v1beta1.QueryDelegatorWithdrawAddressResponse"T\x82\xd3\xe4\x93\x02N\x12L/cosmos/distribution/v1beta1/delegators/{delegator_address}/withdraw_address\x12\xb5\x01\n\rCommunityPool\x126.cosmos.distribution.v1beta1.QueryCommunityPoolRequest\x1a7.cosmos.distribution.v1beta1.QueryCommunityPoolResponse"3\x82\xd3\xe4\x93\x02-\x12+/cosmos/distribution/v1beta1/community_poolB3Z1github.com/cosmos/cosmos-sdk/x/distribution/typesb\x06proto3')
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
_QUERYVALIDATOROUTSTANDINGREWARDSREQUEST = DESCRIPTOR.message_types_by_name['QueryValidatorOutstandingRewardsRequest']
_QUERYVALIDATOROUTSTANDINGREWARDSRESPONSE = DESCRIPTOR.message_types_by_name['QueryValidatorOutstandingRewardsResponse']
_QUERYVALIDATORCOMMISSIONREQUEST = DESCRIPTOR.message_types_by_name['QueryValidatorCommissionRequest']
_QUERYVALIDATORCOMMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['QueryValidatorCommissionResponse']
_QUERYVALIDATORSLASHESREQUEST = DESCRIPTOR.message_types_by_name['QueryValidatorSlashesRequest']
_QUERYVALIDATORSLASHESRESPONSE = DESCRIPTOR.message_types_by_name['QueryValidatorSlashesResponse']
_QUERYDELEGATIONREWARDSREQUEST = DESCRIPTOR.message_types_by_name['QueryDelegationRewardsRequest']
_QUERYDELEGATIONREWARDSRESPONSE = DESCRIPTOR.message_types_by_name['QueryDelegationRewardsResponse']
_QUERYDELEGATIONTOTALREWARDSREQUEST = DESCRIPTOR.message_types_by_name['QueryDelegationTotalRewardsRequest']
_QUERYDELEGATIONTOTALREWARDSRESPONSE = DESCRIPTOR.message_types_by_name['QueryDelegationTotalRewardsResponse']
_QUERYDELEGATORVALIDATORSREQUEST = DESCRIPTOR.message_types_by_name['QueryDelegatorValidatorsRequest']
_QUERYDELEGATORVALIDATORSRESPONSE = DESCRIPTOR.message_types_by_name['QueryDelegatorValidatorsResponse']
_QUERYDELEGATORWITHDRAWADDRESSREQUEST = DESCRIPTOR.message_types_by_name['QueryDelegatorWithdrawAddressRequest']
_QUERYDELEGATORWITHDRAWADDRESSRESPONSE = DESCRIPTOR.message_types_by_name['QueryDelegatorWithdrawAddressResponse']
_QUERYCOMMUNITYPOOLREQUEST = DESCRIPTOR.message_types_by_name['QueryCommunityPoolRequest']
_QUERYCOMMUNITYPOOLRESPONSE = DESCRIPTOR.message_types_by_name['QueryCommunityPoolResponse']
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSREQUEST, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsRequest)
QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSRESPONSE, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsResponse)
QueryValidatorOutstandingRewardsRequest = _reflection.GeneratedProtocolMessageType('QueryValidatorOutstandingRewardsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYVALIDATOROUTSTANDINGREWARDSREQUEST, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryValidatorOutstandingRewardsRequest)
QueryValidatorOutstandingRewardsResponse = _reflection.GeneratedProtocolMessageType('QueryValidatorOutstandingRewardsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYVALIDATOROUTSTANDINGREWARDSRESPONSE, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryValidatorOutstandingRewardsResponse)
QueryValidatorCommissionRequest = _reflection.GeneratedProtocolMessageType('QueryValidatorCommissionRequest', (_message.Message,), {'DESCRIPTOR': _QUERYVALIDATORCOMMISSIONREQUEST, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryValidatorCommissionRequest)
QueryValidatorCommissionResponse = _reflection.GeneratedProtocolMessageType('QueryValidatorCommissionResponse', (_message.Message,), {'DESCRIPTOR': _QUERYVALIDATORCOMMISSIONRESPONSE, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryValidatorCommissionResponse)
QueryValidatorSlashesRequest = _reflection.GeneratedProtocolMessageType('QueryValidatorSlashesRequest', (_message.Message,), {'DESCRIPTOR': _QUERYVALIDATORSLASHESREQUEST, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryValidatorSlashesRequest)
QueryValidatorSlashesResponse = _reflection.GeneratedProtocolMessageType('QueryValidatorSlashesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYVALIDATORSLASHESRESPONSE, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryValidatorSlashesResponse)
QueryDelegationRewardsRequest = _reflection.GeneratedProtocolMessageType('QueryDelegationRewardsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATIONREWARDSREQUEST, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegationRewardsRequest)
QueryDelegationRewardsResponse = _reflection.GeneratedProtocolMessageType('QueryDelegationRewardsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATIONREWARDSRESPONSE, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegationRewardsResponse)
QueryDelegationTotalRewardsRequest = _reflection.GeneratedProtocolMessageType('QueryDelegationTotalRewardsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATIONTOTALREWARDSREQUEST, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegationTotalRewardsRequest)
QueryDelegationTotalRewardsResponse = _reflection.GeneratedProtocolMessageType('QueryDelegationTotalRewardsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATIONTOTALREWARDSRESPONSE, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegationTotalRewardsResponse)
QueryDelegatorValidatorsRequest = _reflection.GeneratedProtocolMessageType('QueryDelegatorValidatorsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATORVALIDATORSREQUEST, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegatorValidatorsRequest)
QueryDelegatorValidatorsResponse = _reflection.GeneratedProtocolMessageType('QueryDelegatorValidatorsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATORVALIDATORSRESPONSE, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegatorValidatorsResponse)
QueryDelegatorWithdrawAddressRequest = _reflection.GeneratedProtocolMessageType('QueryDelegatorWithdrawAddressRequest', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATORWITHDRAWADDRESSREQUEST, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegatorWithdrawAddressRequest)
QueryDelegatorWithdrawAddressResponse = _reflection.GeneratedProtocolMessageType('QueryDelegatorWithdrawAddressResponse', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATORWITHDRAWADDRESSRESPONSE, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegatorWithdrawAddressResponse)
QueryCommunityPoolRequest = _reflection.GeneratedProtocolMessageType('QueryCommunityPoolRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCOMMUNITYPOOLREQUEST, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryCommunityPoolRequest)
QueryCommunityPoolResponse = _reflection.GeneratedProtocolMessageType('QueryCommunityPoolResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCOMMUNITYPOOLRESPONSE, '__module__': 'cosmos.distribution.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryCommunityPoolResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYVALIDATOROUTSTANDINGREWARDSREQUEST.fields_by_name['validator_address']._options = None
    _QUERYVALIDATOROUTSTANDINGREWARDSREQUEST.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYVALIDATOROUTSTANDINGREWARDSRESPONSE.fields_by_name['rewards']._options = None
    _QUERYVALIDATOROUTSTANDINGREWARDSRESPONSE.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYVALIDATORCOMMISSIONREQUEST.fields_by_name['validator_address']._options = None
    _QUERYVALIDATORCOMMISSIONREQUEST.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYVALIDATORCOMMISSIONRESPONSE.fields_by_name['commission']._options = None
    _QUERYVALIDATORCOMMISSIONRESPONSE.fields_by_name['commission']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYVALIDATORSLASHESREQUEST.fields_by_name['validator_address']._options = None
    _QUERYVALIDATORSLASHESREQUEST.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYVALIDATORSLASHESREQUEST._options = None
    _QUERYVALIDATORSLASHESREQUEST._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x01'
    _QUERYVALIDATORSLASHESRESPONSE.fields_by_name['slashes']._options = None
    _QUERYVALIDATORSLASHESRESPONSE.fields_by_name['slashes']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYDELEGATIONREWARDSREQUEST.fields_by_name['delegator_address']._options = None
    _QUERYDELEGATIONREWARDSREQUEST.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYDELEGATIONREWARDSREQUEST.fields_by_name['validator_address']._options = None
    _QUERYDELEGATIONREWARDSREQUEST.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYDELEGATIONREWARDSREQUEST._options = None
    _QUERYDELEGATIONREWARDSREQUEST._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYDELEGATIONREWARDSRESPONSE.fields_by_name['rewards']._options = None
    _QUERYDELEGATIONREWARDSRESPONSE.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _QUERYDELEGATIONTOTALREWARDSREQUEST.fields_by_name['delegator_address']._options = None
    _QUERYDELEGATIONTOTALREWARDSREQUEST.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYDELEGATIONTOTALREWARDSREQUEST._options = None
    _QUERYDELEGATIONTOTALREWARDSREQUEST._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYDELEGATIONTOTALREWARDSRESPONSE.fields_by_name['rewards']._options = None
    _QUERYDELEGATIONTOTALREWARDSRESPONSE.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYDELEGATIONTOTALREWARDSRESPONSE.fields_by_name['total']._options = None
    _QUERYDELEGATIONTOTALREWARDSRESPONSE.fields_by_name['total']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _QUERYDELEGATORVALIDATORSREQUEST.fields_by_name['delegator_address']._options = None
    _QUERYDELEGATORVALIDATORSREQUEST.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYDELEGATORVALIDATORSREQUEST._options = None
    _QUERYDELEGATORVALIDATORSREQUEST._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYDELEGATORVALIDATORSRESPONSE._options = None
    _QUERYDELEGATORVALIDATORSRESPONSE._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYDELEGATORWITHDRAWADDRESSREQUEST.fields_by_name['delegator_address']._options = None
    _QUERYDELEGATORWITHDRAWADDRESSREQUEST.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYDELEGATORWITHDRAWADDRESSREQUEST._options = None
    _QUERYDELEGATORWITHDRAWADDRESSREQUEST._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYDELEGATORWITHDRAWADDRESSRESPONSE.fields_by_name['withdraw_address']._options = None
    _QUERYDELEGATORWITHDRAWADDRESSRESPONSE.fields_by_name['withdraw_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYDELEGATORWITHDRAWADDRESSRESPONSE._options = None
    _QUERYDELEGATORWITHDRAWADDRESSRESPONSE._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYCOMMUNITYPOOLRESPONSE.fields_by_name['pool']._options = None
    _QUERYCOMMUNITYPOOLRESPONSE.fields_by_name['pool']._serialized_options = b'\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/cosmos/distribution/v1beta1/params'
    _QUERY.methods_by_name['ValidatorOutstandingRewards']._options = None
    _QUERY.methods_by_name['ValidatorOutstandingRewards']._serialized_options = b'\x82\xd3\xe4\x93\x02Q\x12O/cosmos/distribution/v1beta1/validators/{validator_address}/outstanding_rewards'
    _QUERY.methods_by_name['ValidatorCommission']._options = None
    _QUERY.methods_by_name['ValidatorCommission']._serialized_options = b'\x82\xd3\xe4\x93\x02H\x12F/cosmos/distribution/v1beta1/validators/{validator_address}/commission'
    _QUERY.methods_by_name['ValidatorSlashes']._options = None
    _QUERY.methods_by_name['ValidatorSlashes']._serialized_options = b'\x82\xd3\xe4\x93\x02E\x12C/cosmos/distribution/v1beta1/validators/{validator_address}/slashes'
    _QUERY.methods_by_name['DelegationRewards']._options = None
    _QUERY.methods_by_name['DelegationRewards']._serialized_options = b'\x82\xd3\xe4\x93\x02Y\x12W/cosmos/distribution/v1beta1/delegators/{delegator_address}/rewards/{validator_address}'
    _QUERY.methods_by_name['DelegationTotalRewards']._options = None
    _QUERY.methods_by_name['DelegationTotalRewards']._serialized_options = b'\x82\xd3\xe4\x93\x02E\x12C/cosmos/distribution/v1beta1/delegators/{delegator_address}/rewards'
    _QUERY.methods_by_name['DelegatorValidators']._options = None
    _QUERY.methods_by_name['DelegatorValidators']._serialized_options = b'\x82\xd3\xe4\x93\x02H\x12F/cosmos/distribution/v1beta1/delegators/{delegator_address}/validators'
    _QUERY.methods_by_name['DelegatorWithdrawAddress']._options = None
    _QUERY.methods_by_name['DelegatorWithdrawAddress']._serialized_options = b'\x82\xd3\xe4\x93\x02N\x12L/cosmos/distribution/v1beta1/delegators/{delegator_address}/withdraw_address'
    _QUERY.methods_by_name['CommunityPool']._options = None
    _QUERY.methods_by_name['CommunityPool']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/cosmos/distribution/v1beta1/community_pool'
    _QUERYPARAMSREQUEST._serialized_start = 275
    _QUERYPARAMSREQUEST._serialized_end = 295
    _QUERYPARAMSRESPONSE._serialized_start = 297
    _QUERYPARAMSRESPONSE._serialized_end = 377
    _QUERYVALIDATOROUTSTANDINGREWARDSREQUEST._serialized_start = 379
    _QUERYVALIDATOROUTSTANDINGREWARDSREQUEST._serialized_end = 473
    _QUERYVALIDATOROUTSTANDINGREWARDSRESPONSE._serialized_start = 475
    _QUERYVALIDATOROUTSTANDINGREWARDSRESPONSE._serialized_end = 598
    _QUERYVALIDATORCOMMISSIONREQUEST._serialized_start = 600
    _QUERYVALIDATORCOMMISSIONREQUEST._serialized_end = 686
    _QUERYVALIDATORCOMMISSIONRESPONSE._serialized_start = 688
    _QUERYVALIDATORCOMMISSIONRESPONSE._serialized_end = 809
    _QUERYVALIDATORSLASHESREQUEST._serialized_start = 812
    _QUERYVALIDATORSLASHESREQUEST._serialized_end = 1013
    _QUERYVALIDATORSLASHESRESPONSE._serialized_start = 1016
    _QUERYVALIDATORSLASHESRESPONSE._serialized_end = 1181
    _QUERYDELEGATIONREWARDSREQUEST._serialized_start = 1184
    _QUERYDELEGATIONREWARDSREQUEST._serialized_end = 1331
    _QUERYDELEGATIONREWARDSRESPONSE._serialized_start = 1334
    _QUERYDELEGATIONREWARDSRESPONSE._serialized_end = 1466
    _QUERYDELEGATIONTOTALREWARDSREQUEST._serialized_start = 1468
    _QUERYDELEGATIONTOTALREWARDSREQUEST._serialized_end = 1567
    _QUERYDELEGATIONTOTALREWARDSRESPONSE._serialized_start = 1570
    _QUERYDELEGATIONTOTALREWARDSRESPONSE._serialized_end = 1784
    _QUERYDELEGATORVALIDATORSREQUEST._serialized_start = 1786
    _QUERYDELEGATORVALIDATORSREQUEST._serialized_end = 1882
    _QUERYDELEGATORVALIDATORSRESPONSE._serialized_start = 1884
    _QUERYDELEGATORVALIDATORSRESPONSE._serialized_end = 1948
    _QUERYDELEGATORWITHDRAWADDRESSREQUEST._serialized_start = 1950
    _QUERYDELEGATORWITHDRAWADDRESSREQUEST._serialized_end = 2051
    _QUERYDELEGATORWITHDRAWADDRESSRESPONSE._serialized_start = 2053
    _QUERYDELEGATORWITHDRAWADDRESSRESPONSE._serialized_end = 2154
    _QUERYCOMMUNITYPOOLREQUEST._serialized_start = 2156
    _QUERYCOMMUNITYPOOLREQUEST._serialized_end = 2183
    _QUERYCOMMUNITYPOOLRESPONSE._serialized_start = 2185
    _QUERYCOMMUNITYPOOLRESPONSE._serialized_end = 2310
    _QUERY._serialized_start = 2313
    _QUERY._serialized_end = 4321

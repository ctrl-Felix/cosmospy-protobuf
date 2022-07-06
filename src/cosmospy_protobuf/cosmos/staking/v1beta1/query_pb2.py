
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
from ....cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"cosmos/staking/v1beta1/query.proto\x12\x16cosmos.staking.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a$cosmos/staking/v1beta1/staking.proto\x1a\x19cosmos_proto/cosmos.proto"d\n\x16QueryValidatorsRequest\x12\x0e\n\x06status\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x93\x01\n\x17QueryValidatorsResponse\x12;\n\nvalidators\x18\x01 \x03(\x0b2!.cosmos.staking.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"I\n\x15QueryValidatorRequest\x120\n\x0evalidator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString"T\n\x16QueryValidatorResponse\x12:\n\tvalidator\x18\x01 \x01(\x0b2!.cosmos.staking.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00"\x90\x01\n QueryValidatorDelegationsRequest\x120\n\x0evalidator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xc7\x01\n!QueryValidatorDelegationsResponse\x12e\n\x14delegation_responses\x18\x01 \x03(\x0b2*.cosmos.staking.v1beta1.DelegationResponseB\x1b\xc8\xde\x1f\x00\xaa\xdf\x1f\x13DelegationResponses\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x99\x01\n)QueryValidatorUnbondingDelegationsRequest\x120\n\x0evalidator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xb9\x01\n*QueryValidatorUnbondingDelegationsResponse\x12N\n\x13unbonding_responses\x18\x01 \x03(\x0b2+.cosmos.staking.v1beta1.UnbondingDelegationB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x86\x01\n\x16QueryDelegationRequest\x120\n\x0edelegator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x120\n\x0evalidator_addr\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"b\n\x17QueryDelegationResponse\x12G\n\x13delegation_response\x18\x01 \x01(\x0b2*.cosmos.staking.v1beta1.DelegationResponse"\x8f\x01\n\x1fQueryUnbondingDelegationRequest\x120\n\x0edelegator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x120\n\x0evalidator_addr\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"e\n QueryUnbondingDelegationResponse\x12A\n\x06unbond\x18\x01 \x01(\x0b2+.cosmos.staking.v1beta1.UnbondingDelegationB\x04\xc8\xde\x1f\x00"\x9a\x01\n QueryDelegatorDelegationsRequest\x120\n\x0edelegator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\xb0\x01\n!QueryDelegatorDelegationsResponse\x12N\n\x14delegation_responses\x18\x01 \x03(\x0b2*.cosmos.staking.v1beta1.DelegationResponseB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\xa3\x01\n)QueryDelegatorUnbondingDelegationsRequest\x120\n\x0edelegator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\xb9\x01\n*QueryDelegatorUnbondingDelegationsResponse\x12N\n\x13unbonding_responses\x18\x01 \x03(\x0b2+.cosmos.staking.v1beta1.UnbondingDelegationB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\xff\x01\n\x19QueryRedelegationsRequest\x120\n\x0edelegator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x124\n\x12src_validator_addr\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x124\n\x12dst_validator_addr\x18\x03 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x04 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\xad\x01\n\x1aQueryRedelegationsResponse\x12R\n\x16redelegation_responses\x18\x01 \x03(\x0b2,.cosmos.staking.v1beta1.RedelegationResponseB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x99\x01\n\x1fQueryDelegatorValidatorsRequest\x120\n\x0edelegator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x9c\x01\n QueryDelegatorValidatorsResponse\x12;\n\nvalidators\x18\x01 \x03(\x0b2!.cosmos.staking.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x8e\x01\n\x1eQueryDelegatorValidatorRequest\x120\n\x0edelegator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x120\n\x0evalidator_addr\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"]\n\x1fQueryDelegatorValidatorResponse\x12:\n\tvalidator\x18\x01 \x01(\x0b2!.cosmos.staking.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00",\n\x1aQueryHistoricalInfoRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03"S\n\x1bQueryHistoricalInfoResponse\x124\n\x04hist\x18\x01 \x01(\x0b2&.cosmos.staking.v1beta1.HistoricalInfo"\x12\n\x10QueryPoolRequest"E\n\x11QueryPoolResponse\x120\n\x04pool\x18\x01 \x01(\x0b2\x1c.cosmos.staking.v1beta1.PoolB\x04\xc8\xde\x1f\x00"\x14\n\x12QueryParamsRequest"K\n\x13QueryParamsResponse\x124\n\x06params\x18\x01 \x01(\x0b2\x1e.cosmos.staking.v1beta1.ParamsB\x04\xc8\xde\x1f\x002\xea\x15\n\x05Query\x12\x99\x01\n\nValidators\x12..cosmos.staking.v1beta1.QueryValidatorsRequest\x1a/.cosmos.staking.v1beta1.QueryValidatorsResponse"*\x82\xd3\xe4\x93\x02$\x12"/cosmos/staking/v1beta1/validators\x12\xa7\x01\n\tValidator\x12-.cosmos.staking.v1beta1.QueryValidatorRequest\x1a..cosmos.staking.v1beta1.QueryValidatorResponse";\x82\xd3\xe4\x93\x025\x123/cosmos/staking/v1beta1/validators/{validator_addr}\x12\xd4\x01\n\x14ValidatorDelegations\x128.cosmos.staking.v1beta1.QueryValidatorDelegationsRequest\x1a9.cosmos.staking.v1beta1.QueryValidatorDelegationsResponse"G\x82\xd3\xe4\x93\x02A\x12?/cosmos/staking/v1beta1/validators/{validator_addr}/delegations\x12\xf9\x01\n\x1dValidatorUnbondingDelegations\x12A.cosmos.staking.v1beta1.QueryValidatorUnbondingDelegationsRequest\x1aB.cosmos.staking.v1beta1.QueryValidatorUnbondingDelegationsResponse"Q\x82\xd3\xe4\x93\x02K\x12I/cosmos/staking/v1beta1/validators/{validator_addr}/unbonding_delegations\x12\xc7\x01\n\nDelegation\x12..cosmos.staking.v1beta1.QueryDelegationRequest\x1a/.cosmos.staking.v1beta1.QueryDelegationResponse"X\x82\xd3\xe4\x93\x02R\x12P/cosmos/staking/v1beta1/validators/{validator_addr}/delegations/{delegator_addr}\x12\xf7\x01\n\x13UnbondingDelegation\x127.cosmos.staking.v1beta1.QueryUnbondingDelegationRequest\x1a8.cosmos.staking.v1beta1.QueryUnbondingDelegationResponse"m\x82\xd3\xe4\x93\x02g\x12e/cosmos/staking/v1beta1/validators/{validator_addr}/delegations/{delegator_addr}/unbonding_delegation\x12\xc9\x01\n\x14DelegatorDelegations\x128.cosmos.staking.v1beta1.QueryDelegatorDelegationsRequest\x1a9.cosmos.staking.v1beta1.QueryDelegatorDelegationsResponse"<\x82\xd3\xe4\x93\x026\x124/cosmos/staking/v1beta1/delegations/{delegator_addr}\x12\xf9\x01\n\x1dDelegatorUnbondingDelegations\x12A.cosmos.staking.v1beta1.QueryDelegatorUnbondingDelegationsRequest\x1aB.cosmos.staking.v1beta1.QueryDelegatorUnbondingDelegationsResponse"Q\x82\xd3\xe4\x93\x02K\x12I/cosmos/staking/v1beta1/delegators/{delegator_addr}/unbonding_delegations\x12\xc1\x01\n\rRedelegations\x121.cosmos.staking.v1beta1.QueryRedelegationsRequest\x1a2.cosmos.staking.v1beta1.QueryRedelegationsResponse"I\x82\xd3\xe4\x93\x02C\x12A/cosmos/staking/v1beta1/delegators/{delegator_addr}/redelegations\x12\xd0\x01\n\x13DelegatorValidators\x127.cosmos.staking.v1beta1.QueryDelegatorValidatorsRequest\x1a8.cosmos.staking.v1beta1.QueryDelegatorValidatorsResponse"F\x82\xd3\xe4\x93\x02@\x12>/cosmos/staking/v1beta1/delegators/{delegator_addr}/validators\x12\xde\x01\n\x12DelegatorValidator\x126.cosmos.staking.v1beta1.QueryDelegatorValidatorRequest\x1a7.cosmos.staking.v1beta1.QueryDelegatorValidatorResponse"W\x82\xd3\xe4\x93\x02Q\x12O/cosmos/staking/v1beta1/delegators/{delegator_addr}/validators/{validator_addr}\x12\xb3\x01\n\x0eHistoricalInfo\x122.cosmos.staking.v1beta1.QueryHistoricalInfoRequest\x1a3.cosmos.staking.v1beta1.QueryHistoricalInfoResponse"8\x82\xd3\xe4\x93\x022\x120/cosmos/staking/v1beta1/historical_info/{height}\x12\x81\x01\n\x04Pool\x12(.cosmos.staking.v1beta1.QueryPoolRequest\x1a).cosmos.staking.v1beta1.QueryPoolResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/cosmos/staking/v1beta1/pool\x12\x89\x01\n\x06Params\x12*.cosmos.staking.v1beta1.QueryParamsRequest\x1a+.cosmos.staking.v1beta1.QueryParamsResponse"&\x82\xd3\xe4\x93\x02 \x12\x1e/cosmos/staking/v1beta1/paramsB.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')
_QUERYVALIDATORSREQUEST = DESCRIPTOR.message_types_by_name['QueryValidatorsRequest']
_QUERYVALIDATORSRESPONSE = DESCRIPTOR.message_types_by_name['QueryValidatorsResponse']
_QUERYVALIDATORREQUEST = DESCRIPTOR.message_types_by_name['QueryValidatorRequest']
_QUERYVALIDATORRESPONSE = DESCRIPTOR.message_types_by_name['QueryValidatorResponse']
_QUERYVALIDATORDELEGATIONSREQUEST = DESCRIPTOR.message_types_by_name['QueryValidatorDelegationsRequest']
_QUERYVALIDATORDELEGATIONSRESPONSE = DESCRIPTOR.message_types_by_name['QueryValidatorDelegationsResponse']
_QUERYVALIDATORUNBONDINGDELEGATIONSREQUEST = DESCRIPTOR.message_types_by_name['QueryValidatorUnbondingDelegationsRequest']
_QUERYVALIDATORUNBONDINGDELEGATIONSRESPONSE = DESCRIPTOR.message_types_by_name['QueryValidatorUnbondingDelegationsResponse']
_QUERYDELEGATIONREQUEST = DESCRIPTOR.message_types_by_name['QueryDelegationRequest']
_QUERYDELEGATIONRESPONSE = DESCRIPTOR.message_types_by_name['QueryDelegationResponse']
_QUERYUNBONDINGDELEGATIONREQUEST = DESCRIPTOR.message_types_by_name['QueryUnbondingDelegationRequest']
_QUERYUNBONDINGDELEGATIONRESPONSE = DESCRIPTOR.message_types_by_name['QueryUnbondingDelegationResponse']
_QUERYDELEGATORDELEGATIONSREQUEST = DESCRIPTOR.message_types_by_name['QueryDelegatorDelegationsRequest']
_QUERYDELEGATORDELEGATIONSRESPONSE = DESCRIPTOR.message_types_by_name['QueryDelegatorDelegationsResponse']
_QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST = DESCRIPTOR.message_types_by_name['QueryDelegatorUnbondingDelegationsRequest']
_QUERYDELEGATORUNBONDINGDELEGATIONSRESPONSE = DESCRIPTOR.message_types_by_name['QueryDelegatorUnbondingDelegationsResponse']
_QUERYREDELEGATIONSREQUEST = DESCRIPTOR.message_types_by_name['QueryRedelegationsRequest']
_QUERYREDELEGATIONSRESPONSE = DESCRIPTOR.message_types_by_name['QueryRedelegationsResponse']
_QUERYDELEGATORVALIDATORSREQUEST = DESCRIPTOR.message_types_by_name['QueryDelegatorValidatorsRequest']
_QUERYDELEGATORVALIDATORSRESPONSE = DESCRIPTOR.message_types_by_name['QueryDelegatorValidatorsResponse']
_QUERYDELEGATORVALIDATORREQUEST = DESCRIPTOR.message_types_by_name['QueryDelegatorValidatorRequest']
_QUERYDELEGATORVALIDATORRESPONSE = DESCRIPTOR.message_types_by_name['QueryDelegatorValidatorResponse']
_QUERYHISTORICALINFOREQUEST = DESCRIPTOR.message_types_by_name['QueryHistoricalInfoRequest']
_QUERYHISTORICALINFORESPONSE = DESCRIPTOR.message_types_by_name['QueryHistoricalInfoResponse']
_QUERYPOOLREQUEST = DESCRIPTOR.message_types_by_name['QueryPoolRequest']
_QUERYPOOLRESPONSE = DESCRIPTOR.message_types_by_name['QueryPoolResponse']
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
QueryValidatorsRequest = _reflection.GeneratedProtocolMessageType('QueryValidatorsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYVALIDATORSREQUEST, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryValidatorsRequest)
QueryValidatorsResponse = _reflection.GeneratedProtocolMessageType('QueryValidatorsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYVALIDATORSRESPONSE, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryValidatorsResponse)
QueryValidatorRequest = _reflection.GeneratedProtocolMessageType('QueryValidatorRequest', (_message.Message,), {'DESCRIPTOR': _QUERYVALIDATORREQUEST, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryValidatorRequest)
QueryValidatorResponse = _reflection.GeneratedProtocolMessageType('QueryValidatorResponse', (_message.Message,), {'DESCRIPTOR': _QUERYVALIDATORRESPONSE, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryValidatorResponse)
QueryValidatorDelegationsRequest = _reflection.GeneratedProtocolMessageType('QueryValidatorDelegationsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYVALIDATORDELEGATIONSREQUEST, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryValidatorDelegationsRequest)
QueryValidatorDelegationsResponse = _reflection.GeneratedProtocolMessageType('QueryValidatorDelegationsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYVALIDATORDELEGATIONSRESPONSE, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryValidatorDelegationsResponse)
QueryValidatorUnbondingDelegationsRequest = _reflection.GeneratedProtocolMessageType('QueryValidatorUnbondingDelegationsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYVALIDATORUNBONDINGDELEGATIONSREQUEST, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryValidatorUnbondingDelegationsRequest)
QueryValidatorUnbondingDelegationsResponse = _reflection.GeneratedProtocolMessageType('QueryValidatorUnbondingDelegationsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYVALIDATORUNBONDINGDELEGATIONSRESPONSE, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryValidatorUnbondingDelegationsResponse)
QueryDelegationRequest = _reflection.GeneratedProtocolMessageType('QueryDelegationRequest', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATIONREQUEST, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegationRequest)
QueryDelegationResponse = _reflection.GeneratedProtocolMessageType('QueryDelegationResponse', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATIONRESPONSE, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegationResponse)
QueryUnbondingDelegationRequest = _reflection.GeneratedProtocolMessageType('QueryUnbondingDelegationRequest', (_message.Message,), {'DESCRIPTOR': _QUERYUNBONDINGDELEGATIONREQUEST, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryUnbondingDelegationRequest)
QueryUnbondingDelegationResponse = _reflection.GeneratedProtocolMessageType('QueryUnbondingDelegationResponse', (_message.Message,), {'DESCRIPTOR': _QUERYUNBONDINGDELEGATIONRESPONSE, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryUnbondingDelegationResponse)
QueryDelegatorDelegationsRequest = _reflection.GeneratedProtocolMessageType('QueryDelegatorDelegationsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATORDELEGATIONSREQUEST, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegatorDelegationsRequest)
QueryDelegatorDelegationsResponse = _reflection.GeneratedProtocolMessageType('QueryDelegatorDelegationsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATORDELEGATIONSRESPONSE, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegatorDelegationsResponse)
QueryDelegatorUnbondingDelegationsRequest = _reflection.GeneratedProtocolMessageType('QueryDelegatorUnbondingDelegationsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegatorUnbondingDelegationsRequest)
QueryDelegatorUnbondingDelegationsResponse = _reflection.GeneratedProtocolMessageType('QueryDelegatorUnbondingDelegationsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATORUNBONDINGDELEGATIONSRESPONSE, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegatorUnbondingDelegationsResponse)
QueryRedelegationsRequest = _reflection.GeneratedProtocolMessageType('QueryRedelegationsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYREDELEGATIONSREQUEST, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryRedelegationsRequest)
QueryRedelegationsResponse = _reflection.GeneratedProtocolMessageType('QueryRedelegationsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYREDELEGATIONSRESPONSE, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryRedelegationsResponse)
QueryDelegatorValidatorsRequest = _reflection.GeneratedProtocolMessageType('QueryDelegatorValidatorsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATORVALIDATORSREQUEST, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegatorValidatorsRequest)
QueryDelegatorValidatorsResponse = _reflection.GeneratedProtocolMessageType('QueryDelegatorValidatorsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATORVALIDATORSRESPONSE, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegatorValidatorsResponse)
QueryDelegatorValidatorRequest = _reflection.GeneratedProtocolMessageType('QueryDelegatorValidatorRequest', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATORVALIDATORREQUEST, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegatorValidatorRequest)
QueryDelegatorValidatorResponse = _reflection.GeneratedProtocolMessageType('QueryDelegatorValidatorResponse', (_message.Message,), {'DESCRIPTOR': _QUERYDELEGATORVALIDATORRESPONSE, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDelegatorValidatorResponse)
QueryHistoricalInfoRequest = _reflection.GeneratedProtocolMessageType('QueryHistoricalInfoRequest', (_message.Message,), {'DESCRIPTOR': _QUERYHISTORICALINFOREQUEST, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryHistoricalInfoRequest)
QueryHistoricalInfoResponse = _reflection.GeneratedProtocolMessageType('QueryHistoricalInfoResponse', (_message.Message,), {'DESCRIPTOR': _QUERYHISTORICALINFORESPONSE, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryHistoricalInfoResponse)
QueryPoolRequest = _reflection.GeneratedProtocolMessageType('QueryPoolRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPOOLREQUEST, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryPoolRequest)
QueryPoolResponse = _reflection.GeneratedProtocolMessageType('QueryPoolResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPOOLRESPONSE, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryPoolResponse)
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSREQUEST, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsRequest)
QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSRESPONSE, '__module__': 'cosmos.staking.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
    _QUERYVALIDATORSRESPONSE.fields_by_name['validators']._options = None
    _QUERYVALIDATORSRESPONSE.fields_by_name['validators']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYVALIDATORREQUEST.fields_by_name['validator_addr']._options = None
    _QUERYVALIDATORREQUEST.fields_by_name['validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYVALIDATORRESPONSE.fields_by_name['validator']._options = None
    _QUERYVALIDATORRESPONSE.fields_by_name['validator']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYVALIDATORDELEGATIONSREQUEST.fields_by_name['validator_addr']._options = None
    _QUERYVALIDATORDELEGATIONSREQUEST.fields_by_name['validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYVALIDATORDELEGATIONSRESPONSE.fields_by_name['delegation_responses']._options = None
    _QUERYVALIDATORDELEGATIONSRESPONSE.fields_by_name['delegation_responses']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\x13DelegationResponses'
    _QUERYVALIDATORUNBONDINGDELEGATIONSREQUEST.fields_by_name['validator_addr']._options = None
    _QUERYVALIDATORUNBONDINGDELEGATIONSREQUEST.fields_by_name['validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYVALIDATORUNBONDINGDELEGATIONSRESPONSE.fields_by_name['unbonding_responses']._options = None
    _QUERYVALIDATORUNBONDINGDELEGATIONSRESPONSE.fields_by_name['unbonding_responses']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYDELEGATIONREQUEST.fields_by_name['delegator_addr']._options = None
    _QUERYDELEGATIONREQUEST.fields_by_name['delegator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYDELEGATIONREQUEST.fields_by_name['validator_addr']._options = None
    _QUERYDELEGATIONREQUEST.fields_by_name['validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYDELEGATIONREQUEST._options = None
    _QUERYDELEGATIONREQUEST._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYUNBONDINGDELEGATIONREQUEST.fields_by_name['delegator_addr']._options = None
    _QUERYUNBONDINGDELEGATIONREQUEST.fields_by_name['delegator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYUNBONDINGDELEGATIONREQUEST.fields_by_name['validator_addr']._options = None
    _QUERYUNBONDINGDELEGATIONREQUEST.fields_by_name['validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYUNBONDINGDELEGATIONREQUEST._options = None
    _QUERYUNBONDINGDELEGATIONREQUEST._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYUNBONDINGDELEGATIONRESPONSE.fields_by_name['unbond']._options = None
    _QUERYUNBONDINGDELEGATIONRESPONSE.fields_by_name['unbond']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYDELEGATORDELEGATIONSREQUEST.fields_by_name['delegator_addr']._options = None
    _QUERYDELEGATORDELEGATIONSREQUEST.fields_by_name['delegator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYDELEGATORDELEGATIONSREQUEST._options = None
    _QUERYDELEGATORDELEGATIONSREQUEST._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYDELEGATORDELEGATIONSRESPONSE.fields_by_name['delegation_responses']._options = None
    _QUERYDELEGATORDELEGATIONSRESPONSE.fields_by_name['delegation_responses']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST.fields_by_name['delegator_addr']._options = None
    _QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST.fields_by_name['delegator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST._options = None
    _QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYDELEGATORUNBONDINGDELEGATIONSRESPONSE.fields_by_name['unbonding_responses']._options = None
    _QUERYDELEGATORUNBONDINGDELEGATIONSRESPONSE.fields_by_name['unbonding_responses']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYREDELEGATIONSREQUEST.fields_by_name['delegator_addr']._options = None
    _QUERYREDELEGATIONSREQUEST.fields_by_name['delegator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYREDELEGATIONSREQUEST.fields_by_name['src_validator_addr']._options = None
    _QUERYREDELEGATIONSREQUEST.fields_by_name['src_validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYREDELEGATIONSREQUEST.fields_by_name['dst_validator_addr']._options = None
    _QUERYREDELEGATIONSREQUEST.fields_by_name['dst_validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYREDELEGATIONSREQUEST._options = None
    _QUERYREDELEGATIONSREQUEST._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYREDELEGATIONSRESPONSE.fields_by_name['redelegation_responses']._options = None
    _QUERYREDELEGATIONSRESPONSE.fields_by_name['redelegation_responses']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYDELEGATORVALIDATORSREQUEST.fields_by_name['delegator_addr']._options = None
    _QUERYDELEGATORVALIDATORSREQUEST.fields_by_name['delegator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYDELEGATORVALIDATORSREQUEST._options = None
    _QUERYDELEGATORVALIDATORSREQUEST._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYDELEGATORVALIDATORSRESPONSE.fields_by_name['validators']._options = None
    _QUERYDELEGATORVALIDATORSRESPONSE.fields_by_name['validators']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYDELEGATORVALIDATORREQUEST.fields_by_name['delegator_addr']._options = None
    _QUERYDELEGATORVALIDATORREQUEST.fields_by_name['delegator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYDELEGATORVALIDATORREQUEST.fields_by_name['validator_addr']._options = None
    _QUERYDELEGATORVALIDATORREQUEST.fields_by_name['validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYDELEGATORVALIDATORREQUEST._options = None
    _QUERYDELEGATORVALIDATORREQUEST._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _QUERYDELEGATORVALIDATORRESPONSE.fields_by_name['validator']._options = None
    _QUERYDELEGATORVALIDATORRESPONSE.fields_by_name['validator']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYPOOLRESPONSE.fields_by_name['pool']._options = None
    _QUERYPOOLRESPONSE.fields_by_name['pool']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Validators']._options = None
    _QUERY.methods_by_name['Validators']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/cosmos/staking/v1beta1/validators'
    _QUERY.methods_by_name['Validator']._options = None
    _QUERY.methods_by_name['Validator']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/cosmos/staking/v1beta1/validators/{validator_addr}'
    _QUERY.methods_by_name['ValidatorDelegations']._options = None
    _QUERY.methods_by_name['ValidatorDelegations']._serialized_options = b'\x82\xd3\xe4\x93\x02A\x12?/cosmos/staking/v1beta1/validators/{validator_addr}/delegations'
    _QUERY.methods_by_name['ValidatorUnbondingDelegations']._options = None
    _QUERY.methods_by_name['ValidatorUnbondingDelegations']._serialized_options = b'\x82\xd3\xe4\x93\x02K\x12I/cosmos/staking/v1beta1/validators/{validator_addr}/unbonding_delegations'
    _QUERY.methods_by_name['Delegation']._options = None
    _QUERY.methods_by_name['Delegation']._serialized_options = b'\x82\xd3\xe4\x93\x02R\x12P/cosmos/staking/v1beta1/validators/{validator_addr}/delegations/{delegator_addr}'
    _QUERY.methods_by_name['UnbondingDelegation']._options = None
    _QUERY.methods_by_name['UnbondingDelegation']._serialized_options = b'\x82\xd3\xe4\x93\x02g\x12e/cosmos/staking/v1beta1/validators/{validator_addr}/delegations/{delegator_addr}/unbonding_delegation'
    _QUERY.methods_by_name['DelegatorDelegations']._options = None
    _QUERY.methods_by_name['DelegatorDelegations']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/cosmos/staking/v1beta1/delegations/{delegator_addr}'
    _QUERY.methods_by_name['DelegatorUnbondingDelegations']._options = None
    _QUERY.methods_by_name['DelegatorUnbondingDelegations']._serialized_options = b'\x82\xd3\xe4\x93\x02K\x12I/cosmos/staking/v1beta1/delegators/{delegator_addr}/unbonding_delegations'
    _QUERY.methods_by_name['Redelegations']._options = None
    _QUERY.methods_by_name['Redelegations']._serialized_options = b'\x82\xd3\xe4\x93\x02C\x12A/cosmos/staking/v1beta1/delegators/{delegator_addr}/redelegations'
    _QUERY.methods_by_name['DelegatorValidators']._options = None
    _QUERY.methods_by_name['DelegatorValidators']._serialized_options = b'\x82\xd3\xe4\x93\x02@\x12>/cosmos/staking/v1beta1/delegators/{delegator_addr}/validators'
    _QUERY.methods_by_name['DelegatorValidator']._options = None
    _QUERY.methods_by_name['DelegatorValidator']._serialized_options = b'\x82\xd3\xe4\x93\x02Q\x12O/cosmos/staking/v1beta1/delegators/{delegator_addr}/validators/{validator_addr}'
    _QUERY.methods_by_name['HistoricalInfo']._options = None
    _QUERY.methods_by_name['HistoricalInfo']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/cosmos/staking/v1beta1/historical_info/{height}'
    _QUERY.methods_by_name['Pool']._options = None
    _QUERY.methods_by_name['Pool']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/cosmos/staking/v1beta1/pool'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02 \x12\x1e/cosmos/staking/v1beta1/params'
    _QUERYVALIDATORSREQUEST._serialized_start = 223
    _QUERYVALIDATORSREQUEST._serialized_end = 323
    _QUERYVALIDATORSRESPONSE._serialized_start = 326
    _QUERYVALIDATORSRESPONSE._serialized_end = 473
    _QUERYVALIDATORREQUEST._serialized_start = 475
    _QUERYVALIDATORREQUEST._serialized_end = 548
    _QUERYVALIDATORRESPONSE._serialized_start = 550
    _QUERYVALIDATORRESPONSE._serialized_end = 634
    _QUERYVALIDATORDELEGATIONSREQUEST._serialized_start = 637
    _QUERYVALIDATORDELEGATIONSREQUEST._serialized_end = 781
    _QUERYVALIDATORDELEGATIONSRESPONSE._serialized_start = 784
    _QUERYVALIDATORDELEGATIONSRESPONSE._serialized_end = 983
    _QUERYVALIDATORUNBONDINGDELEGATIONSREQUEST._serialized_start = 986
    _QUERYVALIDATORUNBONDINGDELEGATIONSREQUEST._serialized_end = 1139
    _QUERYVALIDATORUNBONDINGDELEGATIONSRESPONSE._serialized_start = 1142
    _QUERYVALIDATORUNBONDINGDELEGATIONSRESPONSE._serialized_end = 1327
    _QUERYDELEGATIONREQUEST._serialized_start = 1330
    _QUERYDELEGATIONREQUEST._serialized_end = 1464
    _QUERYDELEGATIONRESPONSE._serialized_start = 1466
    _QUERYDELEGATIONRESPONSE._serialized_end = 1564
    _QUERYUNBONDINGDELEGATIONREQUEST._serialized_start = 1567
    _QUERYUNBONDINGDELEGATIONREQUEST._serialized_end = 1710
    _QUERYUNBONDINGDELEGATIONRESPONSE._serialized_start = 1712
    _QUERYUNBONDINGDELEGATIONRESPONSE._serialized_end = 1813
    _QUERYDELEGATORDELEGATIONSREQUEST._serialized_start = 1816
    _QUERYDELEGATORDELEGATIONSREQUEST._serialized_end = 1970
    _QUERYDELEGATORDELEGATIONSRESPONSE._serialized_start = 1973
    _QUERYDELEGATORDELEGATIONSRESPONSE._serialized_end = 2149
    _QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST._serialized_start = 2152
    _QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST._serialized_end = 2315
    _QUERYDELEGATORUNBONDINGDELEGATIONSRESPONSE._serialized_start = 2318
    _QUERYDELEGATORUNBONDINGDELEGATIONSRESPONSE._serialized_end = 2503
    _QUERYREDELEGATIONSREQUEST._serialized_start = 2506
    _QUERYREDELEGATIONSREQUEST._serialized_end = 2761
    _QUERYREDELEGATIONSRESPONSE._serialized_start = 2764
    _QUERYREDELEGATIONSRESPONSE._serialized_end = 2937
    _QUERYDELEGATORVALIDATORSREQUEST._serialized_start = 2940
    _QUERYDELEGATORVALIDATORSREQUEST._serialized_end = 3093
    _QUERYDELEGATORVALIDATORSRESPONSE._serialized_start = 3096
    _QUERYDELEGATORVALIDATORSRESPONSE._serialized_end = 3252
    _QUERYDELEGATORVALIDATORREQUEST._serialized_start = 3255
    _QUERYDELEGATORVALIDATORREQUEST._serialized_end = 3397
    _QUERYDELEGATORVALIDATORRESPONSE._serialized_start = 3399
    _QUERYDELEGATORVALIDATORRESPONSE._serialized_end = 3492
    _QUERYHISTORICALINFOREQUEST._serialized_start = 3494
    _QUERYHISTORICALINFOREQUEST._serialized_end = 3538
    _QUERYHISTORICALINFORESPONSE._serialized_start = 3540
    _QUERYHISTORICALINFORESPONSE._serialized_end = 3623
    _QUERYPOOLREQUEST._serialized_start = 3625
    _QUERYPOOLREQUEST._serialized_end = 3643
    _QUERYPOOLRESPONSE._serialized_start = 3645
    _QUERYPOOLRESPONSE._serialized_end = 3714
    _QUERYPARAMSREQUEST._serialized_start = 3716
    _QUERYPARAMSREQUEST._serialized_end = 3736
    _QUERYPARAMSRESPONSE._serialized_start = 3738
    _QUERYPARAMSRESPONSE._serialized_end = 3813
    _QUERY._serialized_start = 3816
    _QUERY._serialized_end = 6610

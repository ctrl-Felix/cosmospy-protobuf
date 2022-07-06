
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.gov.v1 import gov_pb2 as cosmos_dot_gov_dot_v1_dot_gov__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19cosmos/gov/v1/query.proto\x12\rcosmos.gov.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17cosmos/gov/v1/gov.proto\x1a\x19cosmos_proto/cosmos.proto"+\n\x14QueryProposalRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04"B\n\x15QueryProposalResponse\x12)\n\x08proposal\x18\x01 \x01(\x0b2\x17.cosmos.gov.v1.Proposal"\xe1\x01\n\x15QueryProposalsRequest\x126\n\x0fproposal_status\x18\x01 \x01(\x0e2\x1d.cosmos.gov.v1.ProposalStatus\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12+\n\tdepositor\x18\x03 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x04 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x81\x01\n\x16QueryProposalsResponse\x12*\n\tproposals\x18\x01 \x03(\x0b2\x17.cosmos.gov.v1.Proposal\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"P\n\x10QueryVoteRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString"6\n\x11QueryVoteResponse\x12!\n\x04vote\x18\x01 \x01(\x0b2\x13.cosmos.gov.v1.Vote"d\n\x11QueryVotesRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"u\n\x12QueryVotesResponse\x12"\n\x05votes\x18\x01 \x03(\x0b2\x13.cosmos.gov.v1.Vote\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse")\n\x12QueryParamsRequest\x12\x13\n\x0bparams_type\x18\x01 \x01(\t"\xb1\x01\n\x13QueryParamsResponse\x122\n\rvoting_params\x18\x01 \x01(\x0b2\x1b.cosmos.gov.v1.VotingParams\x124\n\x0edeposit_params\x18\x02 \x01(\x0b2\x1c.cosmos.gov.v1.DepositParams\x120\n\x0ctally_params\x18\x03 \x01(\x0b2\x1a.cosmos.gov.v1.TallyParams"W\n\x13QueryDepositRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12+\n\tdepositor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString"?\n\x14QueryDepositResponse\x12\'\n\x07deposit\x18\x01 \x01(\x0b2\x16.cosmos.gov.v1.Deposit"g\n\x14QueryDepositsRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"~\n\x15QueryDepositsResponse\x12(\n\x08deposits\x18\x01 \x03(\x0b2\x16.cosmos.gov.v1.Deposit\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse".\n\x17QueryTallyResultRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04"E\n\x18QueryTallyResultResponse\x12)\n\x05tally\x18\x01 \x01(\x0b2\x1a.cosmos.gov.v1.TallyResult2\xda\x08\n\x05Query\x12\x85\x01\n\x08Proposal\x12#.cosmos.gov.v1.QueryProposalRequest\x1a$.cosmos.gov.v1.QueryProposalResponse".\x82\xd3\xe4\x93\x02(\x12&/cosmos/gov/v1/proposals/{proposal_id}\x12z\n\tProposals\x12$.cosmos.gov.v1.QueryProposalsRequest\x1a%.cosmos.gov.v1.QueryProposalsResponse" \x82\xd3\xe4\x93\x02\x1a\x12\x18/cosmos/gov/v1/proposals\x12\x87\x01\n\x04Vote\x12\x1f.cosmos.gov.v1.QueryVoteRequest\x1a .cosmos.gov.v1.QueryVoteResponse"<\x82\xd3\xe4\x93\x026\x124/cosmos/gov/v1/proposals/{proposal_id}/votes/{voter}\x12\x82\x01\n\x05Votes\x12 .cosmos.gov.v1.QueryVotesRequest\x1a!.cosmos.gov.v1.QueryVotesResponse"4\x82\xd3\xe4\x93\x02.\x12,/cosmos/gov/v1/proposals/{proposal_id}/votes\x12|\n\x06Params\x12!.cosmos.gov.v1.QueryParamsRequest\x1a".cosmos.gov.v1.QueryParamsResponse"+\x82\xd3\xe4\x93\x02%\x12#/cosmos/gov/v1/params/{params_type}\x12\x97\x01\n\x07Deposit\x12".cosmos.gov.v1.QueryDepositRequest\x1a#.cosmos.gov.v1.QueryDepositResponse"C\x82\xd3\xe4\x93\x02=\x12;/cosmos/gov/v1/proposals/{proposal_id}/deposits/{depositor}\x12\x8e\x01\n\x08Deposits\x12#.cosmos.gov.v1.QueryDepositsRequest\x1a$.cosmos.gov.v1.QueryDepositsResponse"7\x82\xd3\xe4\x93\x021\x12//cosmos/gov/v1/proposals/{proposal_id}/deposits\x12\x94\x01\n\x0bTallyResult\x12&.cosmos.gov.v1.QueryTallyResultRequest\x1a\'.cosmos.gov.v1.QueryTallyResultResponse"4\x82\xd3\xe4\x93\x02.\x12,/cosmos/gov/v1/proposals/{proposal_id}/tallyB-Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1b\x06proto3')
_QUERYPROPOSALREQUEST = DESCRIPTOR.message_types_by_name['QueryProposalRequest']
_QUERYPROPOSALRESPONSE = DESCRIPTOR.message_types_by_name['QueryProposalResponse']
_QUERYPROPOSALSREQUEST = DESCRIPTOR.message_types_by_name['QueryProposalsRequest']
_QUERYPROPOSALSRESPONSE = DESCRIPTOR.message_types_by_name['QueryProposalsResponse']
_QUERYVOTEREQUEST = DESCRIPTOR.message_types_by_name['QueryVoteRequest']
_QUERYVOTERESPONSE = DESCRIPTOR.message_types_by_name['QueryVoteResponse']
_QUERYVOTESREQUEST = DESCRIPTOR.message_types_by_name['QueryVotesRequest']
_QUERYVOTESRESPONSE = DESCRIPTOR.message_types_by_name['QueryVotesResponse']
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
_QUERYDEPOSITREQUEST = DESCRIPTOR.message_types_by_name['QueryDepositRequest']
_QUERYDEPOSITRESPONSE = DESCRIPTOR.message_types_by_name['QueryDepositResponse']
_QUERYDEPOSITSREQUEST = DESCRIPTOR.message_types_by_name['QueryDepositsRequest']
_QUERYDEPOSITSRESPONSE = DESCRIPTOR.message_types_by_name['QueryDepositsResponse']
_QUERYTALLYRESULTREQUEST = DESCRIPTOR.message_types_by_name['QueryTallyResultRequest']
_QUERYTALLYRESULTRESPONSE = DESCRIPTOR.message_types_by_name['QueryTallyResultResponse']
QueryProposalRequest = _reflection.GeneratedProtocolMessageType('QueryProposalRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPROPOSALREQUEST, '__module__': 'cosmos.gov.v1.query_pb2'})
_sym_db.RegisterMessage(QueryProposalRequest)
QueryProposalResponse = _reflection.GeneratedProtocolMessageType('QueryProposalResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPROPOSALRESPONSE, '__module__': 'cosmos.gov.v1.query_pb2'})
_sym_db.RegisterMessage(QueryProposalResponse)
QueryProposalsRequest = _reflection.GeneratedProtocolMessageType('QueryProposalsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPROPOSALSREQUEST, '__module__': 'cosmos.gov.v1.query_pb2'})
_sym_db.RegisterMessage(QueryProposalsRequest)
QueryProposalsResponse = _reflection.GeneratedProtocolMessageType('QueryProposalsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPROPOSALSRESPONSE, '__module__': 'cosmos.gov.v1.query_pb2'})
_sym_db.RegisterMessage(QueryProposalsResponse)
QueryVoteRequest = _reflection.GeneratedProtocolMessageType('QueryVoteRequest', (_message.Message,), {'DESCRIPTOR': _QUERYVOTEREQUEST, '__module__': 'cosmos.gov.v1.query_pb2'})
_sym_db.RegisterMessage(QueryVoteRequest)
QueryVoteResponse = _reflection.GeneratedProtocolMessageType('QueryVoteResponse', (_message.Message,), {'DESCRIPTOR': _QUERYVOTERESPONSE, '__module__': 'cosmos.gov.v1.query_pb2'})
_sym_db.RegisterMessage(QueryVoteResponse)
QueryVotesRequest = _reflection.GeneratedProtocolMessageType('QueryVotesRequest', (_message.Message,), {'DESCRIPTOR': _QUERYVOTESREQUEST, '__module__': 'cosmos.gov.v1.query_pb2'})
_sym_db.RegisterMessage(QueryVotesRequest)
QueryVotesResponse = _reflection.GeneratedProtocolMessageType('QueryVotesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYVOTESRESPONSE, '__module__': 'cosmos.gov.v1.query_pb2'})
_sym_db.RegisterMessage(QueryVotesResponse)
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSREQUEST, '__module__': 'cosmos.gov.v1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsRequest)
QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSRESPONSE, '__module__': 'cosmos.gov.v1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsResponse)
QueryDepositRequest = _reflection.GeneratedProtocolMessageType('QueryDepositRequest', (_message.Message,), {'DESCRIPTOR': _QUERYDEPOSITREQUEST, '__module__': 'cosmos.gov.v1.query_pb2'})
_sym_db.RegisterMessage(QueryDepositRequest)
QueryDepositResponse = _reflection.GeneratedProtocolMessageType('QueryDepositResponse', (_message.Message,), {'DESCRIPTOR': _QUERYDEPOSITRESPONSE, '__module__': 'cosmos.gov.v1.query_pb2'})
_sym_db.RegisterMessage(QueryDepositResponse)
QueryDepositsRequest = _reflection.GeneratedProtocolMessageType('QueryDepositsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYDEPOSITSREQUEST, '__module__': 'cosmos.gov.v1.query_pb2'})
_sym_db.RegisterMessage(QueryDepositsRequest)
QueryDepositsResponse = _reflection.GeneratedProtocolMessageType('QueryDepositsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYDEPOSITSRESPONSE, '__module__': 'cosmos.gov.v1.query_pb2'})
_sym_db.RegisterMessage(QueryDepositsResponse)
QueryTallyResultRequest = _reflection.GeneratedProtocolMessageType('QueryTallyResultRequest', (_message.Message,), {'DESCRIPTOR': _QUERYTALLYRESULTREQUEST, '__module__': 'cosmos.gov.v1.query_pb2'})
_sym_db.RegisterMessage(QueryTallyResultRequest)
QueryTallyResultResponse = _reflection.GeneratedProtocolMessageType('QueryTallyResultResponse', (_message.Message,), {'DESCRIPTOR': _QUERYTALLYRESULTRESPONSE, '__module__': 'cosmos.gov.v1.query_pb2'})
_sym_db.RegisterMessage(QueryTallyResultResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1'
    _QUERYPROPOSALSREQUEST.fields_by_name['voter']._options = None
    _QUERYPROPOSALSREQUEST.fields_by_name['voter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYPROPOSALSREQUEST.fields_by_name['depositor']._options = None
    _QUERYPROPOSALSREQUEST.fields_by_name['depositor']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYVOTEREQUEST.fields_by_name['voter']._options = None
    _QUERYVOTEREQUEST.fields_by_name['voter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYDEPOSITREQUEST.fields_by_name['depositor']._options = None
    _QUERYDEPOSITREQUEST.fields_by_name['depositor']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERY.methods_by_name['Proposal']._options = None
    _QUERY.methods_by_name['Proposal']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/cosmos/gov/v1/proposals/{proposal_id}'
    _QUERY.methods_by_name['Proposals']._options = None
    _QUERY.methods_by_name['Proposals']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a\x12\x18/cosmos/gov/v1/proposals'
    _QUERY.methods_by_name['Vote']._options = None
    _QUERY.methods_by_name['Vote']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/cosmos/gov/v1/proposals/{proposal_id}/votes/{voter}'
    _QUERY.methods_by_name['Votes']._options = None
    _QUERY.methods_by_name['Votes']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/cosmos/gov/v1/proposals/{proposal_id}/votes'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/cosmos/gov/v1/params/{params_type}'
    _QUERY.methods_by_name['Deposit']._options = None
    _QUERY.methods_by_name['Deposit']._serialized_options = b'\x82\xd3\xe4\x93\x02=\x12;/cosmos/gov/v1/proposals/{proposal_id}/deposits/{depositor}'
    _QUERY.methods_by_name['Deposits']._options = None
    _QUERY.methods_by_name['Deposits']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//cosmos/gov/v1/proposals/{proposal_id}/deposits'
    _QUERY.methods_by_name['TallyResult']._options = None
    _QUERY.methods_by_name['TallyResult']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/cosmos/gov/v1/proposals/{proposal_id}/tally'
    _QUERYPROPOSALREQUEST._serialized_start = 170
    _QUERYPROPOSALREQUEST._serialized_end = 213
    _QUERYPROPOSALRESPONSE._serialized_start = 215
    _QUERYPROPOSALRESPONSE._serialized_end = 281
    _QUERYPROPOSALSREQUEST._serialized_start = 284
    _QUERYPROPOSALSREQUEST._serialized_end = 509
    _QUERYPROPOSALSRESPONSE._serialized_start = 512
    _QUERYPROPOSALSRESPONSE._serialized_end = 641
    _QUERYVOTEREQUEST._serialized_start = 643
    _QUERYVOTEREQUEST._serialized_end = 723
    _QUERYVOTERESPONSE._serialized_start = 725
    _QUERYVOTERESPONSE._serialized_end = 779
    _QUERYVOTESREQUEST._serialized_start = 781
    _QUERYVOTESREQUEST._serialized_end = 881
    _QUERYVOTESRESPONSE._serialized_start = 883
    _QUERYVOTESRESPONSE._serialized_end = 1000
    _QUERYPARAMSREQUEST._serialized_start = 1002
    _QUERYPARAMSREQUEST._serialized_end = 1043
    _QUERYPARAMSRESPONSE._serialized_start = 1046
    _QUERYPARAMSRESPONSE._serialized_end = 1223
    _QUERYDEPOSITREQUEST._serialized_start = 1225
    _QUERYDEPOSITREQUEST._serialized_end = 1312
    _QUERYDEPOSITRESPONSE._serialized_start = 1314
    _QUERYDEPOSITRESPONSE._serialized_end = 1377
    _QUERYDEPOSITSREQUEST._serialized_start = 1379
    _QUERYDEPOSITSREQUEST._serialized_end = 1482
    _QUERYDEPOSITSRESPONSE._serialized_start = 1484
    _QUERYDEPOSITSRESPONSE._serialized_end = 1610
    _QUERYTALLYRESULTREQUEST._serialized_start = 1612
    _QUERYTALLYRESULTREQUEST._serialized_end = 1658
    _QUERYTALLYRESULTRESPONSE._serialized_start = 1660
    _QUERYTALLYRESULTRESPONSE._serialized_end = 1729
    _QUERY._serialized_start = 1732
    _QUERY._serialized_end = 2846

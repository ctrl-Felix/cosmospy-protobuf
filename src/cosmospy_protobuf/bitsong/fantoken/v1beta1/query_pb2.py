
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....bitsong.fantoken.v1beta1 import fantoken_pb2 as bitsong_dot_fantoken_dot_v1beta1_dot_fantoken__pb2
from ....bitsong.fantoken.v1beta1 import params_pb2 as bitsong_dot_fantoken_dot_v1beta1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$bitsong/fantoken/v1beta1/query.proto\x12\x18bitsong.fantoken.v1beta1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\'bitsong/fantoken/v1beta1/fantoken.proto\x1a%bitsong/fantoken/v1beta1/params.proto"%\n\x14QueryFanTokenRequest\x12\r\n\x05denom\x18\x01 \x01(\t"M\n\x15QueryFanTokenResponse\x124\n\x08fantoken\x18\x01 \x01(\x0b2".bitsong.fantoken.v1beta1.FanToken"f\n\x15QueryFanTokensRequest\x12\x11\n\tauthority\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8c\x01\n\x16QueryFanTokensResponse\x125\n\tfantokens\x18\x01 \x03(\x0b2".bitsong.fantoken.v1beta1.FanToken\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x14\n\x12QueryParamsRequest"M\n\x13QueryParamsResponse\x126\n\x06params\x18\x01 \x01(\x0b2 .bitsong.fantoken.v1beta1.ParamsB\x04\xc8\xde\x1f\x002\xd6\x03\n\x05Query\x12\x9c\x01\n\x08FanToken\x12..bitsong.fantoken.v1beta1.QueryFanTokenRequest\x1a/.bitsong.fantoken.v1beta1.QueryFanTokenResponse"/\x82\xd3\xe4\x93\x02)\x12\'/bitsong/fantoken/v1beta1/denom/{denom}\x12\x9b\x01\n\tFanTokens\x12/.bitsong.fantoken.v1beta1.QueryFanTokensRequest\x1a0.bitsong.fantoken.v1beta1.QueryFanTokensResponse"+\x82\xd3\xe4\x93\x02%\x12#/bitsong/fantoken/v1beta1/fantokens\x12\x8f\x01\n\x06Params\x12,.bitsong.fantoken.v1beta1.QueryParamsRequest\x1a-.bitsong.fantoken.v1beta1.QueryParamsResponse"(\x82\xd3\xe4\x93\x02"\x12 /bitsong/fantoken/v1beta1/paramsB8Z6github.com/bitsongofficial/go-bitsong/x/fantoken/typesb\x06proto3')
_QUERYFANTOKENREQUEST = DESCRIPTOR.message_types_by_name['QueryFanTokenRequest']
_QUERYFANTOKENRESPONSE = DESCRIPTOR.message_types_by_name['QueryFanTokenResponse']
_QUERYFANTOKENSREQUEST = DESCRIPTOR.message_types_by_name['QueryFanTokensRequest']
_QUERYFANTOKENSRESPONSE = DESCRIPTOR.message_types_by_name['QueryFanTokensResponse']
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
QueryFanTokenRequest = _reflection.GeneratedProtocolMessageType('QueryFanTokenRequest', (_message.Message,), {'DESCRIPTOR': _QUERYFANTOKENREQUEST, '__module__': 'bitsong.fantoken.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryFanTokenRequest)
QueryFanTokenResponse = _reflection.GeneratedProtocolMessageType('QueryFanTokenResponse', (_message.Message,), {'DESCRIPTOR': _QUERYFANTOKENRESPONSE, '__module__': 'bitsong.fantoken.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryFanTokenResponse)
QueryFanTokensRequest = _reflection.GeneratedProtocolMessageType('QueryFanTokensRequest', (_message.Message,), {'DESCRIPTOR': _QUERYFANTOKENSREQUEST, '__module__': 'bitsong.fantoken.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryFanTokensRequest)
QueryFanTokensResponse = _reflection.GeneratedProtocolMessageType('QueryFanTokensResponse', (_message.Message,), {'DESCRIPTOR': _QUERYFANTOKENSRESPONSE, '__module__': 'bitsong.fantoken.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryFanTokensResponse)
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSREQUEST, '__module__': 'bitsong.fantoken.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsRequest)
QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSRESPONSE, '__module__': 'bitsong.fantoken.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/bitsongofficial/go-bitsong/x/fantoken/types'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['FanToken']._options = None
    _QUERY.methods_by_name['FanToken']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/bitsong/fantoken/v1beta1/denom/{denom}"
    _QUERY.methods_by_name['FanTokens']._options = None
    _QUERY.methods_by_name['FanTokens']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/bitsong/fantoken/v1beta1/fantokens'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /bitsong/fantoken/v1beta1/params'
    _QUERYFANTOKENREQUEST._serialized_start = 274
    _QUERYFANTOKENREQUEST._serialized_end = 311
    _QUERYFANTOKENRESPONSE._serialized_start = 313
    _QUERYFANTOKENRESPONSE._serialized_end = 390
    _QUERYFANTOKENSREQUEST._serialized_start = 392
    _QUERYFANTOKENSREQUEST._serialized_end = 494
    _QUERYFANTOKENSRESPONSE._serialized_start = 497
    _QUERYFANTOKENSRESPONSE._serialized_end = 637
    _QUERYPARAMSREQUEST._serialized_start = 639
    _QUERYPARAMSREQUEST._serialized_end = 659
    _QUERYPARAMSRESPONSE._serialized_start = 661
    _QUERYPARAMSRESPONSE._serialized_end = 738
    _QUERY._serialized_start = 741
    _QUERY._serialized_end = 1211

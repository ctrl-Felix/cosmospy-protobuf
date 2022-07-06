
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....osmosis.txfees.v1beta1 import feetoken_pb2 as osmosis_dot_txfees_dot_v1beta1_dot_feetoken__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"osmosis/txfees/v1beta1/query.proto\x12\x16osmosis.txfees.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a%osmosis/txfees/v1beta1/feetoken.proto"\x17\n\x15QueryFeeTokensRequest"i\n\x16QueryFeeTokensResponse\x12O\n\nfee_tokens\x18\x01 \x03(\x0b2 .osmosis.txfees.v1beta1.FeeTokenB\x19\xf2\xde\x1f\x11yaml:"fee_tokens"\xc8\xde\x1f\x00"=\n\x1aQueryDenomSpotPriceRequest\x12\x1f\n\x05denom\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"denom""\x9a\x01\n\x1bQueryDenomSpotPriceResponse\x12"\n\x06poolID\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12W\n\nspot_price\x18\x02 \x01(\tBC\xf2\xde\x1f\x11yaml:"spot_price"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00":\n\x17QueryDenomPoolIdRequest\x12\x1f\n\x05denom\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"denom"">\n\x18QueryDenomPoolIdResponse\x12"\n\x06poolID\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id""\x17\n\x15QueryBaseDenomRequest"C\n\x16QueryBaseDenomResponse\x12)\n\nbase_denom\x18\x01 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"base_denom"2\x94\x05\n\x05Query\x12\x96\x01\n\tFeeTokens\x12-.osmosis.txfees.v1beta1.QueryFeeTokensRequest\x1a..osmosis.txfees.v1beta1.QueryFeeTokensResponse"*\x82\xd3\xe4\x93\x02$\x12"/osmosis/txfees/v1beta1/fee_tokens\x12\xae\x01\n\x0eDenomSpotPrice\x122.osmosis.txfees.v1beta1.QueryDenomSpotPriceRequest\x1a3.osmosis.txfees.v1beta1.QueryDenomSpotPriceResponse"3\x82\xd3\xe4\x93\x02-\x12+/osmosis/txfees/v1beta1/spot_price_by_denom\x12\xa7\x01\n\x0bDenomPoolId\x12/.osmosis.txfees.v1beta1.QueryDenomPoolIdRequest\x1a0.osmosis.txfees.v1beta1.QueryDenomPoolIdResponse"5\x82\xd3\xe4\x93\x02/\x12-/osmosis/txfees/v1beta1/denom_pool_id/{denom}\x12\x96\x01\n\tBaseDenom\x12-.osmosis.txfees.v1beta1.QueryBaseDenomRequest\x1a..osmosis.txfees.v1beta1.QueryBaseDenomResponse"*\x82\xd3\xe4\x93\x02$\x12"/osmosis/txfees/v1beta1/base_denomB3Z1github.com/osmosis-labs/osmosis/v7/x/txfees/typesb\x06proto3')
_QUERYFEETOKENSREQUEST = DESCRIPTOR.message_types_by_name['QueryFeeTokensRequest']
_QUERYFEETOKENSRESPONSE = DESCRIPTOR.message_types_by_name['QueryFeeTokensResponse']
_QUERYDENOMSPOTPRICEREQUEST = DESCRIPTOR.message_types_by_name['QueryDenomSpotPriceRequest']
_QUERYDENOMSPOTPRICERESPONSE = DESCRIPTOR.message_types_by_name['QueryDenomSpotPriceResponse']
_QUERYDENOMPOOLIDREQUEST = DESCRIPTOR.message_types_by_name['QueryDenomPoolIdRequest']
_QUERYDENOMPOOLIDRESPONSE = DESCRIPTOR.message_types_by_name['QueryDenomPoolIdResponse']
_QUERYBASEDENOMREQUEST = DESCRIPTOR.message_types_by_name['QueryBaseDenomRequest']
_QUERYBASEDENOMRESPONSE = DESCRIPTOR.message_types_by_name['QueryBaseDenomResponse']
QueryFeeTokensRequest = _reflection.GeneratedProtocolMessageType('QueryFeeTokensRequest', (_message.Message,), {'DESCRIPTOR': _QUERYFEETOKENSREQUEST, '__module__': 'osmosis.txfees.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryFeeTokensRequest)
QueryFeeTokensResponse = _reflection.GeneratedProtocolMessageType('QueryFeeTokensResponse', (_message.Message,), {'DESCRIPTOR': _QUERYFEETOKENSRESPONSE, '__module__': 'osmosis.txfees.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryFeeTokensResponse)
QueryDenomSpotPriceRequest = _reflection.GeneratedProtocolMessageType('QueryDenomSpotPriceRequest', (_message.Message,), {'DESCRIPTOR': _QUERYDENOMSPOTPRICEREQUEST, '__module__': 'osmosis.txfees.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDenomSpotPriceRequest)
QueryDenomSpotPriceResponse = _reflection.GeneratedProtocolMessageType('QueryDenomSpotPriceResponse', (_message.Message,), {'DESCRIPTOR': _QUERYDENOMSPOTPRICERESPONSE, '__module__': 'osmosis.txfees.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDenomSpotPriceResponse)
QueryDenomPoolIdRequest = _reflection.GeneratedProtocolMessageType('QueryDenomPoolIdRequest', (_message.Message,), {'DESCRIPTOR': _QUERYDENOMPOOLIDREQUEST, '__module__': 'osmosis.txfees.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDenomPoolIdRequest)
QueryDenomPoolIdResponse = _reflection.GeneratedProtocolMessageType('QueryDenomPoolIdResponse', (_message.Message,), {'DESCRIPTOR': _QUERYDENOMPOOLIDRESPONSE, '__module__': 'osmosis.txfees.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDenomPoolIdResponse)
QueryBaseDenomRequest = _reflection.GeneratedProtocolMessageType('QueryBaseDenomRequest', (_message.Message,), {'DESCRIPTOR': _QUERYBASEDENOMREQUEST, '__module__': 'osmosis.txfees.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryBaseDenomRequest)
QueryBaseDenomResponse = _reflection.GeneratedProtocolMessageType('QueryBaseDenomResponse', (_message.Message,), {'DESCRIPTOR': _QUERYBASEDENOMRESPONSE, '__module__': 'osmosis.txfees.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryBaseDenomResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/osmosis-labs/osmosis/v7/x/txfees/types'
    _QUERYFEETOKENSRESPONSE.fields_by_name['fee_tokens']._options = None
    _QUERYFEETOKENSRESPONSE.fields_by_name['fee_tokens']._serialized_options = b'\xf2\xde\x1f\x11yaml:"fee_tokens"\xc8\xde\x1f\x00'
    _QUERYDENOMSPOTPRICEREQUEST.fields_by_name['denom']._options = None
    _QUERYDENOMSPOTPRICEREQUEST.fields_by_name['denom']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"denom"'
    _QUERYDENOMSPOTPRICERESPONSE.fields_by_name['poolID']._options = None
    _QUERYDENOMSPOTPRICERESPONSE.fields_by_name['poolID']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _QUERYDENOMSPOTPRICERESPONSE.fields_by_name['spot_price']._options = None
    _QUERYDENOMSPOTPRICERESPONSE.fields_by_name['spot_price']._serialized_options = b'\xf2\xde\x1f\x11yaml:"spot_price"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _QUERYDENOMPOOLIDREQUEST.fields_by_name['denom']._options = None
    _QUERYDENOMPOOLIDREQUEST.fields_by_name['denom']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"denom"'
    _QUERYDENOMPOOLIDRESPONSE.fields_by_name['poolID']._options = None
    _QUERYDENOMPOOLIDRESPONSE.fields_by_name['poolID']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _QUERYBASEDENOMRESPONSE.fields_by_name['base_denom']._options = None
    _QUERYBASEDENOMRESPONSE.fields_by_name['base_denom']._serialized_options = b'\xf2\xde\x1f\x11yaml:"base_denom"'
    _QUERY.methods_by_name['FeeTokens']._options = None
    _QUERY.methods_by_name['FeeTokens']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/osmosis/txfees/v1beta1/fee_tokens'
    _QUERY.methods_by_name['DenomSpotPrice']._options = None
    _QUERY.methods_by_name['DenomSpotPrice']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/osmosis/txfees/v1beta1/spot_price_by_denom'
    _QUERY.methods_by_name['DenomPoolId']._options = None
    _QUERY.methods_by_name['DenomPoolId']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/osmosis/txfees/v1beta1/denom_pool_id/{denom}'
    _QUERY.methods_by_name['BaseDenom']._options = None
    _QUERY.methods_by_name['BaseDenom']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/osmosis/txfees/v1beta1/base_denom'
    _QUERYFEETOKENSREQUEST._serialized_start = 185
    _QUERYFEETOKENSREQUEST._serialized_end = 208
    _QUERYFEETOKENSRESPONSE._serialized_start = 210
    _QUERYFEETOKENSRESPONSE._serialized_end = 315
    _QUERYDENOMSPOTPRICEREQUEST._serialized_start = 317
    _QUERYDENOMSPOTPRICEREQUEST._serialized_end = 378
    _QUERYDENOMSPOTPRICERESPONSE._serialized_start = 381
    _QUERYDENOMSPOTPRICERESPONSE._serialized_end = 535
    _QUERYDENOMPOOLIDREQUEST._serialized_start = 537
    _QUERYDENOMPOOLIDREQUEST._serialized_end = 595
    _QUERYDENOMPOOLIDRESPONSE._serialized_start = 597
    _QUERYDENOMPOOLIDRESPONSE._serialized_end = 659
    _QUERYBASEDENOMREQUEST._serialized_start = 661
    _QUERYBASEDENOMREQUEST._serialized_end = 684
    _QUERYBASEDENOMRESPONSE._serialized_start = 686
    _QUERYBASEDENOMRESPONSE._serialized_end = 753
    _QUERY._serialized_start = 756
    _QUERY._serialized_end = 1416

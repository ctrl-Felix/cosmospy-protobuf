
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....osmosis.gamm.v1beta1 import tx_pb2 as osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n osmosis/gamm/v1beta1/query.proto\x12\x14osmosis.gamm.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1dosmosis/gamm/v1beta1/tx.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto"6\n\x10QueryPoolRequest\x12"\n\x06poolId\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id""B\n\x11QueryPoolResponse\x12-\n\x04pool\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyB\t\xca\xb4-\x05PoolI"O\n\x11QueryPoolsRequest\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x81\x01\n\x12QueryPoolsResponse\x12.\n\x05pools\x18\x01 \x03(\x0b2\x14.google.protobuf.AnyB\t\xca\xb4-\x05PoolI\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x16\n\x14QueryNumPoolsRequest"?\n\x15QueryNumPoolsResponse\x12&\n\x08numPools\x18\x01 \x01(\x04B\x14\xf2\xde\x1f\x10yaml:"num_pools""<\n\x16QueryPoolParamsRequest\x12"\n\x06poolId\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id""?\n\x17QueryPoolParamsResponse\x12$\n\x06params\x18\x01 \x01(\x0b2\x14.google.protobuf.Any"D\n\x1eQueryTotalPoolLiquidityRequest\x12"\n\x06poolId\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id""\x95\x01\n\x1fQueryTotalPoolLiquidityResponse\x12r\n\tliquidity\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBD\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x10yaml:"liquidity"\xc8\xde\x1f\x00"=\n\x17QueryTotalSharesRequest\x12"\n\x06poolId\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id""g\n\x18QueryTotalSharesResponse\x12K\n\x0btotalShares\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x1b\xf2\xde\x1f\x13yaml:"total_shares"\xc8\xde\x1f\x00"\xbe\x01\n\x15QuerySpotPriceRequest\x12"\n\x06poolId\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x125\n\x10base_asset_denom\x18\x02 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:"base_asset_denom"\x127\n\x11quote_asset_denom\x18\x03 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"quote_asset_denom"J\x04\x08\x04\x10\x05R\x0bwithSwapFee"B\n\x16QuerySpotPriceResponse\x12(\n\tspotPrice\x18\x01 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"spot_price""\xdc\x01\n\x1dQuerySwapExactAmountInRequest\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12"\n\x06poolId\x18\x02 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12$\n\x07tokenIn\x18\x03 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"token_in"\x12N\n\x06routes\x18\x04 \x03(\x0b2\'.osmosis.gamm.v1beta1.SwapAmountInRouteB\x15\xf2\xde\x1f\ryaml:"routes"\xc8\xde\x1f\x00"\x83\x01\n\x1eQuerySwapExactAmountInResponse\x12a\n\x0etokenOutAmount\x18\x01 \x01(\tBI\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:"token_out_amount"\xc8\xde\x1f\x00"\xe0\x01\n\x1eQuerySwapExactAmountOutRequest\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12"\n\x06poolId\x18\x02 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12O\n\x06routes\x18\x03 \x03(\x0b2(.osmosis.gamm.v1beta1.SwapAmountOutRouteB\x15\xf2\xde\x1f\ryaml:"routes"\xc8\xde\x1f\x00\x12&\n\x08tokenOut\x18\x04 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"token_out""\x82\x01\n\x1fQuerySwapExactAmountOutResponse\x12_\n\rtokenInAmount\x18\x01 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"token_in_amount"\xc8\xde\x1f\x00"\x1c\n\x1aQueryTotalLiquidityRequest"\x91\x01\n\x1bQueryTotalLiquidityResponse\x12r\n\tliquidity\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBD\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x10yaml:"liquidity"\xc8\xde\x1f\x002\x98\r\n\x05Query\x12\x7f\n\x05Pools\x12\'.osmosis.gamm.v1beta1.QueryPoolsRequest\x1a(.osmosis.gamm.v1beta1.QueryPoolsResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/osmosis/gamm/v1beta1/pools\x12\x8c\x01\n\x08NumPools\x12*.osmosis.gamm.v1beta1.QueryNumPoolsRequest\x1a+.osmosis.gamm.v1beta1.QueryNumPoolsResponse"\'\x82\xd3\xe4\x93\x02!\x12\x1f/osmosis/gamm/v1beta1/num_pools\x12\xa4\x01\n\x0eTotalLiquidity\x120.osmosis.gamm.v1beta1.QueryTotalLiquidityRequest\x1a1.osmosis.gamm.v1beta1.QueryTotalLiquidityResponse"-\x82\xd3\xe4\x93\x02\'\x12%/osmosis/gamm/v1beta1/total_liquidity\x12\x85\x01\n\x04Pool\x12&.osmosis.gamm.v1beta1.QueryPoolRequest\x1a\'.osmosis.gamm.v1beta1.QueryPoolResponse",\x82\xd3\xe4\x93\x02&\x12$/osmosis/gamm/v1beta1/pools/{poolId}\x12\x9e\x01\n\nPoolParams\x12,.osmosis.gamm.v1beta1.QueryPoolParamsRequest\x1a-.osmosis.gamm.v1beta1.QueryPoolParamsResponse"3\x82\xd3\xe4\x93\x02-\x12+/osmosis/gamm/v1beta1/pools/{poolId}/params\x12\xc4\x01\n\x12TotalPoolLiquidity\x124.osmosis.gamm.v1beta1.QueryTotalPoolLiquidityRequest\x1a5.osmosis.gamm.v1beta1.QueryTotalPoolLiquidityResponse"A\x82\xd3\xe4\x93\x02;\x129/osmosis/gamm/v1beta1/pools/{poolId}/total_pool_liquidity\x12\xa7\x01\n\x0bTotalShares\x12-.osmosis.gamm.v1beta1.QueryTotalSharesRequest\x1a..osmosis.gamm.v1beta1.QueryTotalSharesResponse"9\x82\xd3\xe4\x93\x023\x121/osmosis/gamm/v1beta1/pools/{poolId}/total_shares\x12\x9b\x01\n\tSpotPrice\x12+.osmosis.gamm.v1beta1.QuerySpotPriceRequest\x1a,.osmosis.gamm.v1beta1.QuerySpotPriceResponse"3\x82\xd3\xe4\x93\x02-\x12+/osmosis/gamm/v1beta1/pools/{poolId}/prices\x12\xcc\x01\n\x19EstimateSwapExactAmountIn\x123.osmosis.gamm.v1beta1.QuerySwapExactAmountInRequest\x1a4.osmosis.gamm.v1beta1.QuerySwapExactAmountInResponse"D\x82\xd3\xe4\x93\x02>\x12</osmosis/gamm/v1beta1/{poolId}/estimate/swap_exact_amount_in\x12\xd0\x01\n\x1aEstimateSwapExactAmountOut\x124.osmosis.gamm.v1beta1.QuerySwapExactAmountOutRequest\x1a5.osmosis.gamm.v1beta1.QuerySwapExactAmountOutResponse"E\x82\xd3\xe4\x93\x02?\x12=/osmosis/gamm/v1beta1/{poolId}/estimate/swap_exact_amount_outB1Z/github.com/osmosis-labs/osmosis/v7/x/gamm/typesb\x06proto3')
_QUERYPOOLREQUEST = DESCRIPTOR.message_types_by_name['QueryPoolRequest']
_QUERYPOOLRESPONSE = DESCRIPTOR.message_types_by_name['QueryPoolResponse']
_QUERYPOOLSREQUEST = DESCRIPTOR.message_types_by_name['QueryPoolsRequest']
_QUERYPOOLSRESPONSE = DESCRIPTOR.message_types_by_name['QueryPoolsResponse']
_QUERYNUMPOOLSREQUEST = DESCRIPTOR.message_types_by_name['QueryNumPoolsRequest']
_QUERYNUMPOOLSRESPONSE = DESCRIPTOR.message_types_by_name['QueryNumPoolsResponse']
_QUERYPOOLPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryPoolParamsRequest']
_QUERYPOOLPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryPoolParamsResponse']
_QUERYTOTALPOOLLIQUIDITYREQUEST = DESCRIPTOR.message_types_by_name['QueryTotalPoolLiquidityRequest']
_QUERYTOTALPOOLLIQUIDITYRESPONSE = DESCRIPTOR.message_types_by_name['QueryTotalPoolLiquidityResponse']
_QUERYTOTALSHARESREQUEST = DESCRIPTOR.message_types_by_name['QueryTotalSharesRequest']
_QUERYTOTALSHARESRESPONSE = DESCRIPTOR.message_types_by_name['QueryTotalSharesResponse']
_QUERYSPOTPRICEREQUEST = DESCRIPTOR.message_types_by_name['QuerySpotPriceRequest']
_QUERYSPOTPRICERESPONSE = DESCRIPTOR.message_types_by_name['QuerySpotPriceResponse']
_QUERYSWAPEXACTAMOUNTINREQUEST = DESCRIPTOR.message_types_by_name['QuerySwapExactAmountInRequest']
_QUERYSWAPEXACTAMOUNTINRESPONSE = DESCRIPTOR.message_types_by_name['QuerySwapExactAmountInResponse']
_QUERYSWAPEXACTAMOUNTOUTREQUEST = DESCRIPTOR.message_types_by_name['QuerySwapExactAmountOutRequest']
_QUERYSWAPEXACTAMOUNTOUTRESPONSE = DESCRIPTOR.message_types_by_name['QuerySwapExactAmountOutResponse']
_QUERYTOTALLIQUIDITYREQUEST = DESCRIPTOR.message_types_by_name['QueryTotalLiquidityRequest']
_QUERYTOTALLIQUIDITYRESPONSE = DESCRIPTOR.message_types_by_name['QueryTotalLiquidityResponse']
QueryPoolRequest = _reflection.GeneratedProtocolMessageType('QueryPoolRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPOOLREQUEST, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryPoolRequest)
QueryPoolResponse = _reflection.GeneratedProtocolMessageType('QueryPoolResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPOOLRESPONSE, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryPoolResponse)
QueryPoolsRequest = _reflection.GeneratedProtocolMessageType('QueryPoolsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPOOLSREQUEST, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryPoolsRequest)
QueryPoolsResponse = _reflection.GeneratedProtocolMessageType('QueryPoolsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPOOLSRESPONSE, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryPoolsResponse)
QueryNumPoolsRequest = _reflection.GeneratedProtocolMessageType('QueryNumPoolsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYNUMPOOLSREQUEST, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryNumPoolsRequest)
QueryNumPoolsResponse = _reflection.GeneratedProtocolMessageType('QueryNumPoolsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYNUMPOOLSRESPONSE, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryNumPoolsResponse)
QueryPoolParamsRequest = _reflection.GeneratedProtocolMessageType('QueryPoolParamsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPOOLPARAMSREQUEST, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryPoolParamsRequest)
QueryPoolParamsResponse = _reflection.GeneratedProtocolMessageType('QueryPoolParamsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPOOLPARAMSRESPONSE, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryPoolParamsResponse)
QueryTotalPoolLiquidityRequest = _reflection.GeneratedProtocolMessageType('QueryTotalPoolLiquidityRequest', (_message.Message,), {'DESCRIPTOR': _QUERYTOTALPOOLLIQUIDITYREQUEST, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryTotalPoolLiquidityRequest)
QueryTotalPoolLiquidityResponse = _reflection.GeneratedProtocolMessageType('QueryTotalPoolLiquidityResponse', (_message.Message,), {'DESCRIPTOR': _QUERYTOTALPOOLLIQUIDITYRESPONSE, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryTotalPoolLiquidityResponse)
QueryTotalSharesRequest = _reflection.GeneratedProtocolMessageType('QueryTotalSharesRequest', (_message.Message,), {'DESCRIPTOR': _QUERYTOTALSHARESREQUEST, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryTotalSharesRequest)
QueryTotalSharesResponse = _reflection.GeneratedProtocolMessageType('QueryTotalSharesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYTOTALSHARESRESPONSE, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryTotalSharesResponse)
QuerySpotPriceRequest = _reflection.GeneratedProtocolMessageType('QuerySpotPriceRequest', (_message.Message,), {'DESCRIPTOR': _QUERYSPOTPRICEREQUEST, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QuerySpotPriceRequest)
QuerySpotPriceResponse = _reflection.GeneratedProtocolMessageType('QuerySpotPriceResponse', (_message.Message,), {'DESCRIPTOR': _QUERYSPOTPRICERESPONSE, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QuerySpotPriceResponse)
QuerySwapExactAmountInRequest = _reflection.GeneratedProtocolMessageType('QuerySwapExactAmountInRequest', (_message.Message,), {'DESCRIPTOR': _QUERYSWAPEXACTAMOUNTINREQUEST, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QuerySwapExactAmountInRequest)
QuerySwapExactAmountInResponse = _reflection.GeneratedProtocolMessageType('QuerySwapExactAmountInResponse', (_message.Message,), {'DESCRIPTOR': _QUERYSWAPEXACTAMOUNTINRESPONSE, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QuerySwapExactAmountInResponse)
QuerySwapExactAmountOutRequest = _reflection.GeneratedProtocolMessageType('QuerySwapExactAmountOutRequest', (_message.Message,), {'DESCRIPTOR': _QUERYSWAPEXACTAMOUNTOUTREQUEST, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QuerySwapExactAmountOutRequest)
QuerySwapExactAmountOutResponse = _reflection.GeneratedProtocolMessageType('QuerySwapExactAmountOutResponse', (_message.Message,), {'DESCRIPTOR': _QUERYSWAPEXACTAMOUNTOUTRESPONSE, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QuerySwapExactAmountOutResponse)
QueryTotalLiquidityRequest = _reflection.GeneratedProtocolMessageType('QueryTotalLiquidityRequest', (_message.Message,), {'DESCRIPTOR': _QUERYTOTALLIQUIDITYREQUEST, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryTotalLiquidityRequest)
QueryTotalLiquidityResponse = _reflection.GeneratedProtocolMessageType('QueryTotalLiquidityResponse', (_message.Message,), {'DESCRIPTOR': _QUERYTOTALLIQUIDITYRESPONSE, '__module__': 'osmosis.gamm.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryTotalLiquidityResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z/github.com/osmosis-labs/osmosis/v7/x/gamm/types'
    _QUERYPOOLREQUEST.fields_by_name['poolId']._options = None
    _QUERYPOOLREQUEST.fields_by_name['poolId']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _QUERYPOOLRESPONSE.fields_by_name['pool']._options = None
    _QUERYPOOLRESPONSE.fields_by_name['pool']._serialized_options = b'\xca\xb4-\x05PoolI'
    _QUERYPOOLSRESPONSE.fields_by_name['pools']._options = None
    _QUERYPOOLSRESPONSE.fields_by_name['pools']._serialized_options = b'\xca\xb4-\x05PoolI'
    _QUERYNUMPOOLSRESPONSE.fields_by_name['numPools']._options = None
    _QUERYNUMPOOLSRESPONSE.fields_by_name['numPools']._serialized_options = b'\xf2\xde\x1f\x10yaml:"num_pools"'
    _QUERYPOOLPARAMSREQUEST.fields_by_name['poolId']._options = None
    _QUERYPOOLPARAMSREQUEST.fields_by_name['poolId']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _QUERYTOTALPOOLLIQUIDITYREQUEST.fields_by_name['poolId']._options = None
    _QUERYTOTALPOOLLIQUIDITYREQUEST.fields_by_name['poolId']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _QUERYTOTALPOOLLIQUIDITYRESPONSE.fields_by_name['liquidity']._options = None
    _QUERYTOTALPOOLLIQUIDITYRESPONSE.fields_by_name['liquidity']._serialized_options = b'\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x10yaml:"liquidity"\xc8\xde\x1f\x00'
    _QUERYTOTALSHARESREQUEST.fields_by_name['poolId']._options = None
    _QUERYTOTALSHARESREQUEST.fields_by_name['poolId']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _QUERYTOTALSHARESRESPONSE.fields_by_name['totalShares']._options = None
    _QUERYTOTALSHARESRESPONSE.fields_by_name['totalShares']._serialized_options = b'\xf2\xde\x1f\x13yaml:"total_shares"\xc8\xde\x1f\x00'
    _QUERYSPOTPRICEREQUEST.fields_by_name['poolId']._options = None
    _QUERYSPOTPRICEREQUEST.fields_by_name['poolId']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _QUERYSPOTPRICEREQUEST.fields_by_name['base_asset_denom']._options = None
    _QUERYSPOTPRICEREQUEST.fields_by_name['base_asset_denom']._serialized_options = b'\xf2\xde\x1f\x17yaml:"base_asset_denom"'
    _QUERYSPOTPRICEREQUEST.fields_by_name['quote_asset_denom']._options = None
    _QUERYSPOTPRICEREQUEST.fields_by_name['quote_asset_denom']._serialized_options = b'\xf2\xde\x1f\x18yaml:"quote_asset_denom"'
    _QUERYSPOTPRICERESPONSE.fields_by_name['spotPrice']._options = None
    _QUERYSPOTPRICERESPONSE.fields_by_name['spotPrice']._serialized_options = b'\xf2\xde\x1f\x11yaml:"spot_price"'
    _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['sender']._options = None
    _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['poolId']._options = None
    _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['poolId']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['tokenIn']._options = None
    _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['tokenIn']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"token_in"'
    _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['routes']._options = None
    _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['routes']._serialized_options = b'\xf2\xde\x1f\ryaml:"routes"\xc8\xde\x1f\x00'
    _QUERYSWAPEXACTAMOUNTINRESPONSE.fields_by_name['tokenOutAmount']._options = None
    _QUERYSWAPEXACTAMOUNTINRESPONSE.fields_by_name['tokenOutAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:"token_out_amount"\xc8\xde\x1f\x00'
    _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['sender']._options = None
    _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['poolId']._options = None
    _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['poolId']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['routes']._options = None
    _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['routes']._serialized_options = b'\xf2\xde\x1f\ryaml:"routes"\xc8\xde\x1f\x00'
    _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['tokenOut']._options = None
    _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['tokenOut']._serialized_options = b'\xf2\xde\x1f\x10yaml:"token_out"'
    _QUERYSWAPEXACTAMOUNTOUTRESPONSE.fields_by_name['tokenInAmount']._options = None
    _QUERYSWAPEXACTAMOUNTOUTRESPONSE.fields_by_name['tokenInAmount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"token_in_amount"\xc8\xde\x1f\x00'
    _QUERYTOTALLIQUIDITYRESPONSE.fields_by_name['liquidity']._options = None
    _QUERYTOTALLIQUIDITYRESPONSE.fields_by_name['liquidity']._serialized_options = b'\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x10yaml:"liquidity"\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Pools']._options = None
    _QUERY.methods_by_name['Pools']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/osmosis/gamm/v1beta1/pools'
    _QUERY.methods_by_name['NumPools']._options = None
    _QUERY.methods_by_name['NumPools']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/osmosis/gamm/v1beta1/num_pools'
    _QUERY.methods_by_name['TotalLiquidity']._options = None
    _QUERY.methods_by_name['TotalLiquidity']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/osmosis/gamm/v1beta1/total_liquidity"
    _QUERY.methods_by_name['Pool']._options = None
    _QUERY.methods_by_name['Pool']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/osmosis/gamm/v1beta1/pools/{poolId}'
    _QUERY.methods_by_name['PoolParams']._options = None
    _QUERY.methods_by_name['PoolParams']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/osmosis/gamm/v1beta1/pools/{poolId}/params'
    _QUERY.methods_by_name['TotalPoolLiquidity']._options = None
    _QUERY.methods_by_name['TotalPoolLiquidity']._serialized_options = b'\x82\xd3\xe4\x93\x02;\x129/osmosis/gamm/v1beta1/pools/{poolId}/total_pool_liquidity'
    _QUERY.methods_by_name['TotalShares']._options = None
    _QUERY.methods_by_name['TotalShares']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/osmosis/gamm/v1beta1/pools/{poolId}/total_shares'
    _QUERY.methods_by_name['SpotPrice']._options = None
    _QUERY.methods_by_name['SpotPrice']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/osmosis/gamm/v1beta1/pools/{poolId}/prices'
    _QUERY.methods_by_name['EstimateSwapExactAmountIn']._options = None
    _QUERY.methods_by_name['EstimateSwapExactAmountIn']._serialized_options = b'\x82\xd3\xe4\x93\x02>\x12</osmosis/gamm/v1beta1/{poolId}/estimate/swap_exact_amount_in'
    _QUERY.methods_by_name['EstimateSwapExactAmountOut']._options = None
    _QUERY.methods_by_name['EstimateSwapExactAmountOut']._serialized_options = b'\x82\xd3\xe4\x93\x02?\x12=/osmosis/gamm/v1beta1/{poolId}/estimate/swap_exact_amount_out'
    _QUERYPOOLREQUEST._serialized_start = 271
    _QUERYPOOLREQUEST._serialized_end = 325
    _QUERYPOOLRESPONSE._serialized_start = 327
    _QUERYPOOLRESPONSE._serialized_end = 393
    _QUERYPOOLSREQUEST._serialized_start = 395
    _QUERYPOOLSREQUEST._serialized_end = 474
    _QUERYPOOLSRESPONSE._serialized_start = 477
    _QUERYPOOLSRESPONSE._serialized_end = 606
    _QUERYNUMPOOLSREQUEST._serialized_start = 608
    _QUERYNUMPOOLSREQUEST._serialized_end = 630
    _QUERYNUMPOOLSRESPONSE._serialized_start = 632
    _QUERYNUMPOOLSRESPONSE._serialized_end = 695
    _QUERYPOOLPARAMSREQUEST._serialized_start = 697
    _QUERYPOOLPARAMSREQUEST._serialized_end = 757
    _QUERYPOOLPARAMSRESPONSE._serialized_start = 759
    _QUERYPOOLPARAMSRESPONSE._serialized_end = 822
    _QUERYTOTALPOOLLIQUIDITYREQUEST._serialized_start = 824
    _QUERYTOTALPOOLLIQUIDITYREQUEST._serialized_end = 892
    _QUERYTOTALPOOLLIQUIDITYRESPONSE._serialized_start = 895
    _QUERYTOTALPOOLLIQUIDITYRESPONSE._serialized_end = 1044
    _QUERYTOTALSHARESREQUEST._serialized_start = 1046
    _QUERYTOTALSHARESREQUEST._serialized_end = 1107
    _QUERYTOTALSHARESRESPONSE._serialized_start = 1109
    _QUERYTOTALSHARESRESPONSE._serialized_end = 1212
    _QUERYSPOTPRICEREQUEST._serialized_start = 1215
    _QUERYSPOTPRICEREQUEST._serialized_end = 1405
    _QUERYSPOTPRICERESPONSE._serialized_start = 1407
    _QUERYSPOTPRICERESPONSE._serialized_end = 1473
    _QUERYSWAPEXACTAMOUNTINREQUEST._serialized_start = 1476
    _QUERYSWAPEXACTAMOUNTINREQUEST._serialized_end = 1696
    _QUERYSWAPEXACTAMOUNTINRESPONSE._serialized_start = 1699
    _QUERYSWAPEXACTAMOUNTINRESPONSE._serialized_end = 1830
    _QUERYSWAPEXACTAMOUNTOUTREQUEST._serialized_start = 1833
    _QUERYSWAPEXACTAMOUNTOUTREQUEST._serialized_end = 2057
    _QUERYSWAPEXACTAMOUNTOUTRESPONSE._serialized_start = 2060
    _QUERYSWAPEXACTAMOUNTOUTRESPONSE._serialized_end = 2190
    _QUERYTOTALLIQUIDITYREQUEST._serialized_start = 2192
    _QUERYTOTALLIQUIDITYREQUEST._serialized_end = 2220
    _QUERYTOTALLIQUIDITYRESPONSE._serialized_start = 2223
    _QUERYTOTALLIQUIDITYRESPONSE._serialized_end = 2368
    _QUERY._serialized_start = 2371
    _QUERY._serialized_end = 4059

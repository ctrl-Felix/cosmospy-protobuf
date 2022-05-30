
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....umee.leverage.v1 import leverage_pb2 as umee_dot_leverage_dot_v1_dot_leverage__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cumee/leverage/v1/query.proto\x12\x1cumeenetwork.umee.leverage.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fumee/leverage/v1/leverage.proto\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x17\n\x15QueryRegisteredTokens",\n\x1bQueryAvailableBorrowRequest\x12\r\n\x05denom\x18\x01 \x01(\t"^\n\x1cQueryAvailableBorrowResponse\x12>\n\x06amount\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00"&\n\x15QueryBorrowAPYRequest\x12\r\n\x05denom\x18\x01 \x01(\t"U\n\x16QueryBorrowAPYResponse\x12;\n\x03APY\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"$\n\x13QueryLendAPYRequest\x12\r\n\x05denom\x18\x01 \x01(\t"S\n\x14QueryLendAPYResponse\x12;\n\x03APY\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"\'\n\x16QueryMarketSizeRequest\x12\r\n\x05denom\x18\x01 \x01(\t"b\n\x17QueryMarketSizeResponse\x12G\n\x0fmarket_size_usd\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00",\n\x1bQueryTokenMarketSizeRequest\x12\r\n\x05denom\x18\x01 \x01(\t"c\n\x1cQueryTokenMarketSizeResponse\x12C\n\x0bmarket_size\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00"\\\n\x1dQueryRegisteredTokensResponse\x12;\n\x08registry\x18\x01 \x03(\x0b2#.umeenetwork.umee.leverage.v1.TokenB\x04\xc8\xde\x1f\x00"\x14\n\x12QueryParamsRequest"Q\n\x13QueryParamsResponse\x12:\n\x06params\x18\x01 \x01(\x0b2$.umeenetwork.umee.leverage.v1.ParamsB\x04\xc8\xde\x1f\x00"6\n\x14QueryBorrowedRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"v\n\x15QueryBorrowedResponse\x12]\n\x08borrowed\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins";\n\x19QueryBorrowedValueRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"d\n\x1aQueryBorrowedValueResponse\x12F\n\x0eborrowed_value\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"=\n\x1bQueryCollateralValueRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"h\n\x1cQueryCollateralValueResponse\x12H\n\x10collateral_value\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"4\n\x12QueryLoanedRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"r\n\x13QueryLoanedResponse\x12[\n\x06loaned\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"9\n\x17QueryLoanedValueRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"`\n\x18QueryLoanedValueResponse\x12D\n\x0cloaned_value\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"*\n\x19QueryReserveAmountRequest\x12\r\n\x05denom\x18\x01 \x01(\t"\\\n\x1aQueryReserveAmountResponse\x12>\n\x06amount\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00"?\n\x1dQueryCollateralSettingRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"1\n\x1eQueryCollateralSettingResponse\x12\x0f\n\x07enabled\x18\x01 \x01(\x08"8\n\x16QueryCollateralRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"z\n\x17QueryCollateralResponse\x12_\n\ncollateral\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins")\n\x18QueryExchangeRateRequest\x12\r\n\x05denom\x18\x01 \x01(\t"b\n\x19QueryExchangeRateResponse\x12E\n\rexchange_rate\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"*\n\x17QueryBorrowLimitRequest\x12\x0f\n\x07address\x18\x01 \x01(\t"`\n\x18QueryBorrowLimitResponse\x12D\n\x0cborrow_limit\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"3\n QueryLiquidationThresholdRequest\x12\x0f\n\x07address\x18\x01 \x01(\t"r\n!QueryLiquidationThresholdResponse\x12M\n\x15liquidation_threshold\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00" \n\x1eQueryLiquidationTargetsRequest"2\n\x1fQueryLiquidationTargetsResponse\x12\x0f\n\x07targets\x18\x01 \x03(\t"*\n\x19QueryMarketSummaryRequest\x12\r\n\x05denom\x18\x01 \x01(\t"\xaf\x04\n\x1aQueryMarketSummaryResponse\x12\x14\n\x0csymbol_denom\x18\x01 \x01(\t\x12\x10\n\x08exponent\x18\x02 \x01(\r\x12D\n\x0coracle_price\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x01\x12L\n\x14uToken_exchange_rate\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12@\n\x08lend_APY\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12B\n\nborrow_APY\x18\x06 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12C\n\x0bmarket_size\x18\x07 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12H\n\x10available_borrow\x18\x08 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12@\n\x08reserved\x18\t \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x002\xed\x1a\n\x05Query\x12\xb1\x01\n\x10RegisteredTokens\x123.umeenetwork.umee.leverage.v1.QueryRegisteredTokens\x1a;.umeenetwork.umee.leverage.v1.QueryRegisteredTokensResponse"+\x82\xd3\xe4\x93\x02%\x12#/umee/leverage/v1/registered_tokens\x12\x8f\x01\n\x06Params\x120.umeenetwork.umee.leverage.v1.QueryParamsRequest\x1a1.umeenetwork.umee.leverage.v1.QueryParamsResponse" \x82\xd3\xe4\x93\x02\x1a\x12\x18/umee/leverage/v1/params\x12\x97\x01\n\x08Borrowed\x122.umeenetwork.umee.leverage.v1.QueryBorrowedRequest\x1a3.umeenetwork.umee.leverage.v1.QueryBorrowedResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/umee/leverage/v1/borrowed\x12\xac\x01\n\rBorrowedValue\x127.umeenetwork.umee.leverage.v1.QueryBorrowedValueRequest\x1a8.umeenetwork.umee.leverage.v1.QueryBorrowedValueResponse"(\x82\xd3\xe4\x93\x02"\x12 /umee/leverage/v1/borrowed_value\x12\x8f\x01\n\x06Loaned\x120.umeenetwork.umee.leverage.v1.QueryLoanedRequest\x1a1.umeenetwork.umee.leverage.v1.QueryLoanedResponse" \x82\xd3\xe4\x93\x02\x1a\x12\x18/umee/leverage/v1/loaned\x12\xa4\x01\n\x0bLoanedValue\x125.umeenetwork.umee.leverage.v1.QueryLoanedValueRequest\x1a6.umeenetwork.umee.leverage.v1.QueryLoanedValueResponse"&\x82\xd3\xe4\x93\x02 \x12\x1e/umee/leverage/v1/loaned_value\x12\xb4\x01\n\x0fAvailableBorrow\x129.umeenetwork.umee.leverage.v1.QueryAvailableBorrowRequest\x1a:.umeenetwork.umee.leverage.v1.QueryAvailableBorrowResponse"*\x82\xd3\xe4\x93\x02$\x12"/umee/leverage/v1/available_borrow\x12\x9c\x01\n\tBorrowAPY\x123.umeenetwork.umee.leverage.v1.QueryBorrowAPYRequest\x1a4.umeenetwork.umee.leverage.v1.QueryBorrowAPYResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/umee/leverage/v1/borrow_apy\x12\x94\x01\n\x07LendAPY\x121.umeenetwork.umee.leverage.v1.QueryLendAPYRequest\x1a2.umeenetwork.umee.leverage.v1.QueryLendAPYResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/umee/leverage/v1/lend_apy\x12\xa0\x01\n\nMarketSize\x124.umeenetwork.umee.leverage.v1.QueryMarketSizeRequest\x1a5.umeenetwork.umee.leverage.v1.QueryMarketSizeResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/umee/leverage/v1/market_size\x12\xb5\x01\n\x0fTokenMarketSize\x129.umeenetwork.umee.leverage.v1.QueryTokenMarketSizeRequest\x1a:.umeenetwork.umee.leverage.v1.QueryTokenMarketSizeResponse"+\x82\xd3\xe4\x93\x02%\x12#/umee/leverage/v1/token_market_size\x12\xac\x01\n\rReserveAmount\x127.umeenetwork.umee.leverage.v1.QueryReserveAmountRequest\x1a8.umeenetwork.umee.leverage.v1.QueryReserveAmountResponse"(\x82\xd3\xe4\x93\x02"\x12 /umee/leverage/v1/reserve_amount\x12\xbc\x01\n\x11CollateralSetting\x12;.umeenetwork.umee.leverage.v1.QueryCollateralSettingRequest\x1a<.umeenetwork.umee.leverage.v1.QueryCollateralSettingResponse",\x82\xd3\xe4\x93\x02&\x12$/umee/leverage/v1/collateral_setting\x12\x9f\x01\n\nCollateral\x124.umeenetwork.umee.leverage.v1.QueryCollateralRequest\x1a5.umeenetwork.umee.leverage.v1.QueryCollateralResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/umee/leverage/v1/collateral\x12\xb4\x01\n\x0fCollateralValue\x129.umeenetwork.umee.leverage.v1.QueryCollateralValueRequest\x1a:.umeenetwork.umee.leverage.v1.QueryCollateralValueResponse"*\x82\xd3\xe4\x93\x02$\x12"/umee/leverage/v1/collateral_value\x12\xa8\x01\n\x0cExchangeRate\x126.umeenetwork.umee.leverage.v1.QueryExchangeRateRequest\x1a7.umeenetwork.umee.leverage.v1.QueryExchangeRateResponse"\'\x82\xd3\xe4\x93\x02!\x12\x1f/umee/leverage/v1/exchange_rate\x12\xa4\x01\n\x0bBorrowLimit\x125.umeenetwork.umee.leverage.v1.QueryBorrowLimitRequest\x1a6.umeenetwork.umee.leverage.v1.QueryBorrowLimitResponse"&\x82\xd3\xe4\x93\x02 \x12\x1e/umee/leverage/v1/borrow_limit\x12\xc8\x01\n\x14LiquidationThreshold\x12>.umeenetwork.umee.leverage.v1.QueryLiquidationThresholdRequest\x1a?.umeenetwork.umee.leverage.v1.QueryLiquidationThresholdResponse"/\x82\xd3\xe4\x93\x02)\x12\'/umee/leverage/v1/liquidation_threshold\x12\xc0\x01\n\x12LiquidationTargets\x12<.umeenetwork.umee.leverage.v1.QueryLiquidationTargetsRequest\x1a=.umeenetwork.umee.leverage.v1.QueryLiquidationTargetsResponse"-\x82\xd3\xe4\x93\x02\'\x12%/umee/leverage/v1/liquidation_targets\x12\xac\x01\n\rMarketSummary\x127.umeenetwork.umee.leverage.v1.QueryMarketSummaryRequest\x1a8.umeenetwork.umee.leverage.v1.QueryMarketSummaryResponse"(\x82\xd3\xe4\x93\x02"\x12 /umee/leverage/v1/market_summaryB2Z0github.com/umee-network/umee/v2/x/leverage/typesb\x06proto3')
_QUERYREGISTEREDTOKENS = DESCRIPTOR.message_types_by_name['QueryRegisteredTokens']
_QUERYAVAILABLEBORROWREQUEST = DESCRIPTOR.message_types_by_name['QueryAvailableBorrowRequest']
_QUERYAVAILABLEBORROWRESPONSE = DESCRIPTOR.message_types_by_name['QueryAvailableBorrowResponse']
_QUERYBORROWAPYREQUEST = DESCRIPTOR.message_types_by_name['QueryBorrowAPYRequest']
_QUERYBORROWAPYRESPONSE = DESCRIPTOR.message_types_by_name['QueryBorrowAPYResponse']
_QUERYLENDAPYREQUEST = DESCRIPTOR.message_types_by_name['QueryLendAPYRequest']
_QUERYLENDAPYRESPONSE = DESCRIPTOR.message_types_by_name['QueryLendAPYResponse']
_QUERYMARKETSIZEREQUEST = DESCRIPTOR.message_types_by_name['QueryMarketSizeRequest']
_QUERYMARKETSIZERESPONSE = DESCRIPTOR.message_types_by_name['QueryMarketSizeResponse']
_QUERYTOKENMARKETSIZEREQUEST = DESCRIPTOR.message_types_by_name['QueryTokenMarketSizeRequest']
_QUERYTOKENMARKETSIZERESPONSE = DESCRIPTOR.message_types_by_name['QueryTokenMarketSizeResponse']
_QUERYREGISTEREDTOKENSRESPONSE = DESCRIPTOR.message_types_by_name['QueryRegisteredTokensResponse']
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
_QUERYBORROWEDREQUEST = DESCRIPTOR.message_types_by_name['QueryBorrowedRequest']
_QUERYBORROWEDRESPONSE = DESCRIPTOR.message_types_by_name['QueryBorrowedResponse']
_QUERYBORROWEDVALUEREQUEST = DESCRIPTOR.message_types_by_name['QueryBorrowedValueRequest']
_QUERYBORROWEDVALUERESPONSE = DESCRIPTOR.message_types_by_name['QueryBorrowedValueResponse']
_QUERYCOLLATERALVALUEREQUEST = DESCRIPTOR.message_types_by_name['QueryCollateralValueRequest']
_QUERYCOLLATERALVALUERESPONSE = DESCRIPTOR.message_types_by_name['QueryCollateralValueResponse']
_QUERYLOANEDREQUEST = DESCRIPTOR.message_types_by_name['QueryLoanedRequest']
_QUERYLOANEDRESPONSE = DESCRIPTOR.message_types_by_name['QueryLoanedResponse']
_QUERYLOANEDVALUEREQUEST = DESCRIPTOR.message_types_by_name['QueryLoanedValueRequest']
_QUERYLOANEDVALUERESPONSE = DESCRIPTOR.message_types_by_name['QueryLoanedValueResponse']
_QUERYRESERVEAMOUNTREQUEST = DESCRIPTOR.message_types_by_name['QueryReserveAmountRequest']
_QUERYRESERVEAMOUNTRESPONSE = DESCRIPTOR.message_types_by_name['QueryReserveAmountResponse']
_QUERYCOLLATERALSETTINGREQUEST = DESCRIPTOR.message_types_by_name['QueryCollateralSettingRequest']
_QUERYCOLLATERALSETTINGRESPONSE = DESCRIPTOR.message_types_by_name['QueryCollateralSettingResponse']
_QUERYCOLLATERALREQUEST = DESCRIPTOR.message_types_by_name['QueryCollateralRequest']
_QUERYCOLLATERALRESPONSE = DESCRIPTOR.message_types_by_name['QueryCollateralResponse']
_QUERYEXCHANGERATEREQUEST = DESCRIPTOR.message_types_by_name['QueryExchangeRateRequest']
_QUERYEXCHANGERATERESPONSE = DESCRIPTOR.message_types_by_name['QueryExchangeRateResponse']
_QUERYBORROWLIMITREQUEST = DESCRIPTOR.message_types_by_name['QueryBorrowLimitRequest']
_QUERYBORROWLIMITRESPONSE = DESCRIPTOR.message_types_by_name['QueryBorrowLimitResponse']
_QUERYLIQUIDATIONTHRESHOLDREQUEST = DESCRIPTOR.message_types_by_name['QueryLiquidationThresholdRequest']
_QUERYLIQUIDATIONTHRESHOLDRESPONSE = DESCRIPTOR.message_types_by_name['QueryLiquidationThresholdResponse']
_QUERYLIQUIDATIONTARGETSREQUEST = DESCRIPTOR.message_types_by_name['QueryLiquidationTargetsRequest']
_QUERYLIQUIDATIONTARGETSRESPONSE = DESCRIPTOR.message_types_by_name['QueryLiquidationTargetsResponse']
_QUERYMARKETSUMMARYREQUEST = DESCRIPTOR.message_types_by_name['QueryMarketSummaryRequest']
_QUERYMARKETSUMMARYRESPONSE = DESCRIPTOR.message_types_by_name['QueryMarketSummaryResponse']
QueryRegisteredTokens = _reflection.GeneratedProtocolMessageType('QueryRegisteredTokens', (_message.Message,), {'DESCRIPTOR': _QUERYREGISTEREDTOKENS, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryRegisteredTokens)
QueryAvailableBorrowRequest = _reflection.GeneratedProtocolMessageType('QueryAvailableBorrowRequest', (_message.Message,), {'DESCRIPTOR': _QUERYAVAILABLEBORROWREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryAvailableBorrowRequest)
QueryAvailableBorrowResponse = _reflection.GeneratedProtocolMessageType('QueryAvailableBorrowResponse', (_message.Message,), {'DESCRIPTOR': _QUERYAVAILABLEBORROWRESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryAvailableBorrowResponse)
QueryBorrowAPYRequest = _reflection.GeneratedProtocolMessageType('QueryBorrowAPYRequest', (_message.Message,), {'DESCRIPTOR': _QUERYBORROWAPYREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryBorrowAPYRequest)
QueryBorrowAPYResponse = _reflection.GeneratedProtocolMessageType('QueryBorrowAPYResponse', (_message.Message,), {'DESCRIPTOR': _QUERYBORROWAPYRESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryBorrowAPYResponse)
QueryLendAPYRequest = _reflection.GeneratedProtocolMessageType('QueryLendAPYRequest', (_message.Message,), {'DESCRIPTOR': _QUERYLENDAPYREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryLendAPYRequest)
QueryLendAPYResponse = _reflection.GeneratedProtocolMessageType('QueryLendAPYResponse', (_message.Message,), {'DESCRIPTOR': _QUERYLENDAPYRESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryLendAPYResponse)
QueryMarketSizeRequest = _reflection.GeneratedProtocolMessageType('QueryMarketSizeRequest', (_message.Message,), {'DESCRIPTOR': _QUERYMARKETSIZEREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryMarketSizeRequest)
QueryMarketSizeResponse = _reflection.GeneratedProtocolMessageType('QueryMarketSizeResponse', (_message.Message,), {'DESCRIPTOR': _QUERYMARKETSIZERESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryMarketSizeResponse)
QueryTokenMarketSizeRequest = _reflection.GeneratedProtocolMessageType('QueryTokenMarketSizeRequest', (_message.Message,), {'DESCRIPTOR': _QUERYTOKENMARKETSIZEREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryTokenMarketSizeRequest)
QueryTokenMarketSizeResponse = _reflection.GeneratedProtocolMessageType('QueryTokenMarketSizeResponse', (_message.Message,), {'DESCRIPTOR': _QUERYTOKENMARKETSIZERESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryTokenMarketSizeResponse)
QueryRegisteredTokensResponse = _reflection.GeneratedProtocolMessageType('QueryRegisteredTokensResponse', (_message.Message,), {'DESCRIPTOR': _QUERYREGISTEREDTOKENSRESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryRegisteredTokensResponse)
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsRequest)
QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSRESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsResponse)
QueryBorrowedRequest = _reflection.GeneratedProtocolMessageType('QueryBorrowedRequest', (_message.Message,), {'DESCRIPTOR': _QUERYBORROWEDREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryBorrowedRequest)
QueryBorrowedResponse = _reflection.GeneratedProtocolMessageType('QueryBorrowedResponse', (_message.Message,), {'DESCRIPTOR': _QUERYBORROWEDRESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryBorrowedResponse)
QueryBorrowedValueRequest = _reflection.GeneratedProtocolMessageType('QueryBorrowedValueRequest', (_message.Message,), {'DESCRIPTOR': _QUERYBORROWEDVALUEREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryBorrowedValueRequest)
QueryBorrowedValueResponse = _reflection.GeneratedProtocolMessageType('QueryBorrowedValueResponse', (_message.Message,), {'DESCRIPTOR': _QUERYBORROWEDVALUERESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryBorrowedValueResponse)
QueryCollateralValueRequest = _reflection.GeneratedProtocolMessageType('QueryCollateralValueRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCOLLATERALVALUEREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryCollateralValueRequest)
QueryCollateralValueResponse = _reflection.GeneratedProtocolMessageType('QueryCollateralValueResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCOLLATERALVALUERESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryCollateralValueResponse)
QueryLoanedRequest = _reflection.GeneratedProtocolMessageType('QueryLoanedRequest', (_message.Message,), {'DESCRIPTOR': _QUERYLOANEDREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryLoanedRequest)
QueryLoanedResponse = _reflection.GeneratedProtocolMessageType('QueryLoanedResponse', (_message.Message,), {'DESCRIPTOR': _QUERYLOANEDRESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryLoanedResponse)
QueryLoanedValueRequest = _reflection.GeneratedProtocolMessageType('QueryLoanedValueRequest', (_message.Message,), {'DESCRIPTOR': _QUERYLOANEDVALUEREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryLoanedValueRequest)
QueryLoanedValueResponse = _reflection.GeneratedProtocolMessageType('QueryLoanedValueResponse', (_message.Message,), {'DESCRIPTOR': _QUERYLOANEDVALUERESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryLoanedValueResponse)
QueryReserveAmountRequest = _reflection.GeneratedProtocolMessageType('QueryReserveAmountRequest', (_message.Message,), {'DESCRIPTOR': _QUERYRESERVEAMOUNTREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryReserveAmountRequest)
QueryReserveAmountResponse = _reflection.GeneratedProtocolMessageType('QueryReserveAmountResponse', (_message.Message,), {'DESCRIPTOR': _QUERYRESERVEAMOUNTRESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryReserveAmountResponse)
QueryCollateralSettingRequest = _reflection.GeneratedProtocolMessageType('QueryCollateralSettingRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCOLLATERALSETTINGREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryCollateralSettingRequest)
QueryCollateralSettingResponse = _reflection.GeneratedProtocolMessageType('QueryCollateralSettingResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCOLLATERALSETTINGRESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryCollateralSettingResponse)
QueryCollateralRequest = _reflection.GeneratedProtocolMessageType('QueryCollateralRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCOLLATERALREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryCollateralRequest)
QueryCollateralResponse = _reflection.GeneratedProtocolMessageType('QueryCollateralResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCOLLATERALRESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryCollateralResponse)
QueryExchangeRateRequest = _reflection.GeneratedProtocolMessageType('QueryExchangeRateRequest', (_message.Message,), {'DESCRIPTOR': _QUERYEXCHANGERATEREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryExchangeRateRequest)
QueryExchangeRateResponse = _reflection.GeneratedProtocolMessageType('QueryExchangeRateResponse', (_message.Message,), {'DESCRIPTOR': _QUERYEXCHANGERATERESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryExchangeRateResponse)
QueryBorrowLimitRequest = _reflection.GeneratedProtocolMessageType('QueryBorrowLimitRequest', (_message.Message,), {'DESCRIPTOR': _QUERYBORROWLIMITREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryBorrowLimitRequest)
QueryBorrowLimitResponse = _reflection.GeneratedProtocolMessageType('QueryBorrowLimitResponse', (_message.Message,), {'DESCRIPTOR': _QUERYBORROWLIMITRESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryBorrowLimitResponse)
QueryLiquidationThresholdRequest = _reflection.GeneratedProtocolMessageType('QueryLiquidationThresholdRequest', (_message.Message,), {'DESCRIPTOR': _QUERYLIQUIDATIONTHRESHOLDREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryLiquidationThresholdRequest)
QueryLiquidationThresholdResponse = _reflection.GeneratedProtocolMessageType('QueryLiquidationThresholdResponse', (_message.Message,), {'DESCRIPTOR': _QUERYLIQUIDATIONTHRESHOLDRESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryLiquidationThresholdResponse)
QueryLiquidationTargetsRequest = _reflection.GeneratedProtocolMessageType('QueryLiquidationTargetsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYLIQUIDATIONTARGETSREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryLiquidationTargetsRequest)
QueryLiquidationTargetsResponse = _reflection.GeneratedProtocolMessageType('QueryLiquidationTargetsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYLIQUIDATIONTARGETSRESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryLiquidationTargetsResponse)
QueryMarketSummaryRequest = _reflection.GeneratedProtocolMessageType('QueryMarketSummaryRequest', (_message.Message,), {'DESCRIPTOR': _QUERYMARKETSUMMARYREQUEST, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryMarketSummaryRequest)
QueryMarketSummaryResponse = _reflection.GeneratedProtocolMessageType('QueryMarketSummaryResponse', (_message.Message,), {'DESCRIPTOR': _QUERYMARKETSUMMARYRESPONSE, '__module__': 'umee.leverage.v1.query_pb2'})
_sym_db.RegisterMessage(QueryMarketSummaryResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/umee-network/umee/v2/x/leverage/types'
    _QUERYAVAILABLEBORROWRESPONSE.fields_by_name['amount']._options = None
    _QUERYAVAILABLEBORROWRESPONSE.fields_by_name['amount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _QUERYBORROWAPYRESPONSE.fields_by_name['APY']._options = None
    _QUERYBORROWAPYRESPONSE.fields_by_name['APY']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _QUERYLENDAPYRESPONSE.fields_by_name['APY']._options = None
    _QUERYLENDAPYRESPONSE.fields_by_name['APY']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _QUERYMARKETSIZERESPONSE.fields_by_name['market_size_usd']._options = None
    _QUERYMARKETSIZERESPONSE.fields_by_name['market_size_usd']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _QUERYTOKENMARKETSIZERESPONSE.fields_by_name['market_size']._options = None
    _QUERYTOKENMARKETSIZERESPONSE.fields_by_name['market_size']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _QUERYREGISTEREDTOKENSRESPONSE.fields_by_name['registry']._options = None
    _QUERYREGISTEREDTOKENSRESPONSE.fields_by_name['registry']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYBORROWEDRESPONSE.fields_by_name['borrowed']._options = None
    _QUERYBORROWEDRESPONSE.fields_by_name['borrowed']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYBORROWEDVALUERESPONSE.fields_by_name['borrowed_value']._options = None
    _QUERYBORROWEDVALUERESPONSE.fields_by_name['borrowed_value']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _QUERYCOLLATERALVALUERESPONSE.fields_by_name['collateral_value']._options = None
    _QUERYCOLLATERALVALUERESPONSE.fields_by_name['collateral_value']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _QUERYLOANEDRESPONSE.fields_by_name['loaned']._options = None
    _QUERYLOANEDRESPONSE.fields_by_name['loaned']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYLOANEDVALUERESPONSE.fields_by_name['loaned_value']._options = None
    _QUERYLOANEDVALUERESPONSE.fields_by_name['loaned_value']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _QUERYRESERVEAMOUNTRESPONSE.fields_by_name['amount']._options = None
    _QUERYRESERVEAMOUNTRESPONSE.fields_by_name['amount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _QUERYCOLLATERALRESPONSE.fields_by_name['collateral']._options = None
    _QUERYCOLLATERALRESPONSE.fields_by_name['collateral']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYEXCHANGERATERESPONSE.fields_by_name['exchange_rate']._options = None
    _QUERYEXCHANGERATERESPONSE.fields_by_name['exchange_rate']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _QUERYBORROWLIMITRESPONSE.fields_by_name['borrow_limit']._options = None
    _QUERYBORROWLIMITRESPONSE.fields_by_name['borrow_limit']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _QUERYLIQUIDATIONTHRESHOLDRESPONSE.fields_by_name['liquidation_threshold']._options = None
    _QUERYLIQUIDATIONTHRESHOLDRESPONSE.fields_by_name['liquidation_threshold']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _QUERYMARKETSUMMARYRESPONSE.fields_by_name['oracle_price']._options = None
    _QUERYMARKETSUMMARYRESPONSE.fields_by_name['oracle_price']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x01'
    _QUERYMARKETSUMMARYRESPONSE.fields_by_name['uToken_exchange_rate']._options = None
    _QUERYMARKETSUMMARYRESPONSE.fields_by_name['uToken_exchange_rate']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _QUERYMARKETSUMMARYRESPONSE.fields_by_name['lend_APY']._options = None
    _QUERYMARKETSUMMARYRESPONSE.fields_by_name['lend_APY']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _QUERYMARKETSUMMARYRESPONSE.fields_by_name['borrow_APY']._options = None
    _QUERYMARKETSUMMARYRESPONSE.fields_by_name['borrow_APY']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _QUERYMARKETSUMMARYRESPONSE.fields_by_name['market_size']._options = None
    _QUERYMARKETSUMMARYRESPONSE.fields_by_name['market_size']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _QUERYMARKETSUMMARYRESPONSE.fields_by_name['available_borrow']._options = None
    _QUERYMARKETSUMMARYRESPONSE.fields_by_name['available_borrow']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _QUERYMARKETSUMMARYRESPONSE.fields_by_name['reserved']._options = None
    _QUERYMARKETSUMMARYRESPONSE.fields_by_name['reserved']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['RegisteredTokens']._options = None
    _QUERY.methods_by_name['RegisteredTokens']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/umee/leverage/v1/registered_tokens'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a\x12\x18/umee/leverage/v1/params'
    _QUERY.methods_by_name['Borrowed']._options = None
    _QUERY.methods_by_name['Borrowed']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/umee/leverage/v1/borrowed'
    _QUERY.methods_by_name['BorrowedValue']._options = None
    _QUERY.methods_by_name['BorrowedValue']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /umee/leverage/v1/borrowed_value'
    _QUERY.methods_by_name['Loaned']._options = None
    _QUERY.methods_by_name['Loaned']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a\x12\x18/umee/leverage/v1/loaned'
    _QUERY.methods_by_name['LoanedValue']._options = None
    _QUERY.methods_by_name['LoanedValue']._serialized_options = b'\x82\xd3\xe4\x93\x02 \x12\x1e/umee/leverage/v1/loaned_value'
    _QUERY.methods_by_name['AvailableBorrow']._options = None
    _QUERY.methods_by_name['AvailableBorrow']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/umee/leverage/v1/available_borrow'
    _QUERY.methods_by_name['BorrowAPY']._options = None
    _QUERY.methods_by_name['BorrowAPY']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/umee/leverage/v1/borrow_apy'
    _QUERY.methods_by_name['LendAPY']._options = None
    _QUERY.methods_by_name['LendAPY']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/umee/leverage/v1/lend_apy'
    _QUERY.methods_by_name['MarketSize']._options = None
    _QUERY.methods_by_name['MarketSize']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/umee/leverage/v1/market_size'
    _QUERY.methods_by_name['TokenMarketSize']._options = None
    _QUERY.methods_by_name['TokenMarketSize']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/umee/leverage/v1/token_market_size'
    _QUERY.methods_by_name['ReserveAmount']._options = None
    _QUERY.methods_by_name['ReserveAmount']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /umee/leverage/v1/reserve_amount'
    _QUERY.methods_by_name['CollateralSetting']._options = None
    _QUERY.methods_by_name['CollateralSetting']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/umee/leverage/v1/collateral_setting'
    _QUERY.methods_by_name['Collateral']._options = None
    _QUERY.methods_by_name['Collateral']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/umee/leverage/v1/collateral'
    _QUERY.methods_by_name['CollateralValue']._options = None
    _QUERY.methods_by_name['CollateralValue']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/umee/leverage/v1/collateral_value'
    _QUERY.methods_by_name['ExchangeRate']._options = None
    _QUERY.methods_by_name['ExchangeRate']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/umee/leverage/v1/exchange_rate'
    _QUERY.methods_by_name['BorrowLimit']._options = None
    _QUERY.methods_by_name['BorrowLimit']._serialized_options = b'\x82\xd3\xe4\x93\x02 \x12\x1e/umee/leverage/v1/borrow_limit'
    _QUERY.methods_by_name['LiquidationThreshold']._options = None
    _QUERY.methods_by_name['LiquidationThreshold']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/umee/leverage/v1/liquidation_threshold"
    _QUERY.methods_by_name['LiquidationTargets']._options = None
    _QUERY.methods_by_name['LiquidationTargets']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/umee/leverage/v1/liquidation_targets"
    _QUERY.methods_by_name['MarketSummary']._options = None
    _QUERY.methods_by_name['MarketSummary']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /umee/leverage/v1/market_summary'
    _QUERYREGISTEREDTOKENS._serialized_start = 179
    _QUERYREGISTEREDTOKENS._serialized_end = 202
    _QUERYAVAILABLEBORROWREQUEST._serialized_start = 204
    _QUERYAVAILABLEBORROWREQUEST._serialized_end = 248
    _QUERYAVAILABLEBORROWRESPONSE._serialized_start = 250
    _QUERYAVAILABLEBORROWRESPONSE._serialized_end = 344
    _QUERYBORROWAPYREQUEST._serialized_start = 346
    _QUERYBORROWAPYREQUEST._serialized_end = 384
    _QUERYBORROWAPYRESPONSE._serialized_start = 386
    _QUERYBORROWAPYRESPONSE._serialized_end = 471
    _QUERYLENDAPYREQUEST._serialized_start = 473
    _QUERYLENDAPYREQUEST._serialized_end = 509
    _QUERYLENDAPYRESPONSE._serialized_start = 511
    _QUERYLENDAPYRESPONSE._serialized_end = 594
    _QUERYMARKETSIZEREQUEST._serialized_start = 596
    _QUERYMARKETSIZEREQUEST._serialized_end = 635
    _QUERYMARKETSIZERESPONSE._serialized_start = 637
    _QUERYMARKETSIZERESPONSE._serialized_end = 735
    _QUERYTOKENMARKETSIZEREQUEST._serialized_start = 737
    _QUERYTOKENMARKETSIZEREQUEST._serialized_end = 781
    _QUERYTOKENMARKETSIZERESPONSE._serialized_start = 783
    _QUERYTOKENMARKETSIZERESPONSE._serialized_end = 882
    _QUERYREGISTEREDTOKENSRESPONSE._serialized_start = 884
    _QUERYREGISTEREDTOKENSRESPONSE._serialized_end = 976
    _QUERYPARAMSREQUEST._serialized_start = 978
    _QUERYPARAMSREQUEST._serialized_end = 998
    _QUERYPARAMSRESPONSE._serialized_start = 1000
    _QUERYPARAMSRESPONSE._serialized_end = 1081
    _QUERYBORROWEDREQUEST._serialized_start = 1083
    _QUERYBORROWEDREQUEST._serialized_end = 1137
    _QUERYBORROWEDRESPONSE._serialized_start = 1139
    _QUERYBORROWEDRESPONSE._serialized_end = 1257
    _QUERYBORROWEDVALUEREQUEST._serialized_start = 1259
    _QUERYBORROWEDVALUEREQUEST._serialized_end = 1318
    _QUERYBORROWEDVALUERESPONSE._serialized_start = 1320
    _QUERYBORROWEDVALUERESPONSE._serialized_end = 1420
    _QUERYCOLLATERALVALUEREQUEST._serialized_start = 1422
    _QUERYCOLLATERALVALUEREQUEST._serialized_end = 1483
    _QUERYCOLLATERALVALUERESPONSE._serialized_start = 1485
    _QUERYCOLLATERALVALUERESPONSE._serialized_end = 1589
    _QUERYLOANEDREQUEST._serialized_start = 1591
    _QUERYLOANEDREQUEST._serialized_end = 1643
    _QUERYLOANEDRESPONSE._serialized_start = 1645
    _QUERYLOANEDRESPONSE._serialized_end = 1759
    _QUERYLOANEDVALUEREQUEST._serialized_start = 1761
    _QUERYLOANEDVALUEREQUEST._serialized_end = 1818
    _QUERYLOANEDVALUERESPONSE._serialized_start = 1820
    _QUERYLOANEDVALUERESPONSE._serialized_end = 1916
    _QUERYRESERVEAMOUNTREQUEST._serialized_start = 1918
    _QUERYRESERVEAMOUNTREQUEST._serialized_end = 1960
    _QUERYRESERVEAMOUNTRESPONSE._serialized_start = 1962
    _QUERYRESERVEAMOUNTRESPONSE._serialized_end = 2054
    _QUERYCOLLATERALSETTINGREQUEST._serialized_start = 2056
    _QUERYCOLLATERALSETTINGREQUEST._serialized_end = 2119
    _QUERYCOLLATERALSETTINGRESPONSE._serialized_start = 2121
    _QUERYCOLLATERALSETTINGRESPONSE._serialized_end = 2170
    _QUERYCOLLATERALREQUEST._serialized_start = 2172
    _QUERYCOLLATERALREQUEST._serialized_end = 2228
    _QUERYCOLLATERALRESPONSE._serialized_start = 2230
    _QUERYCOLLATERALRESPONSE._serialized_end = 2352
    _QUERYEXCHANGERATEREQUEST._serialized_start = 2354
    _QUERYEXCHANGERATEREQUEST._serialized_end = 2395
    _QUERYEXCHANGERATERESPONSE._serialized_start = 2397
    _QUERYEXCHANGERATERESPONSE._serialized_end = 2495
    _QUERYBORROWLIMITREQUEST._serialized_start = 2497
    _QUERYBORROWLIMITREQUEST._serialized_end = 2539
    _QUERYBORROWLIMITRESPONSE._serialized_start = 2541
    _QUERYBORROWLIMITRESPONSE._serialized_end = 2637
    _QUERYLIQUIDATIONTHRESHOLDREQUEST._serialized_start = 2639
    _QUERYLIQUIDATIONTHRESHOLDREQUEST._serialized_end = 2690
    _QUERYLIQUIDATIONTHRESHOLDRESPONSE._serialized_start = 2692
    _QUERYLIQUIDATIONTHRESHOLDRESPONSE._serialized_end = 2806
    _QUERYLIQUIDATIONTARGETSREQUEST._serialized_start = 2808
    _QUERYLIQUIDATIONTARGETSREQUEST._serialized_end = 2840
    _QUERYLIQUIDATIONTARGETSRESPONSE._serialized_start = 2842
    _QUERYLIQUIDATIONTARGETSRESPONSE._serialized_end = 2892
    _QUERYMARKETSUMMARYREQUEST._serialized_start = 2894
    _QUERYMARKETSUMMARYREQUEST._serialized_end = 2936
    _QUERYMARKETSUMMARYRESPONSE._serialized_start = 2939
    _QUERYMARKETSUMMARYRESPONSE._serialized_end = 3498
    _QUERY._serialized_start = 3501
    _QUERY._serialized_end = 6938

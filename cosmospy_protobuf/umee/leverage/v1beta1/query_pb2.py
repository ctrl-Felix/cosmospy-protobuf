
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....umee.leverage.v1beta1 import leverage_pb2 as umee_dot_leverage_dot_v1beta1_dot_leverage__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!umee/leverage/v1beta1/query.proto\x12!umeenetwork.umee.leverage.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a$umee/leverage/v1beta1/leverage.proto\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x17\n\x15QueryRegisteredTokens",\n\x1bQueryAvailableBorrowRequest\x12\r\n\x05denom\x18\x01 \x01(\t"^\n\x1cQueryAvailableBorrowResponse\x12>\n\x06amount\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00"&\n\x15QueryBorrowAPYRequest\x12\r\n\x05denom\x18\x01 \x01(\t"U\n\x16QueryBorrowAPYResponse\x12;\n\x03APY\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"$\n\x13QueryLendAPYRequest\x12\r\n\x05denom\x18\x01 \x01(\t"S\n\x14QueryLendAPYResponse\x12;\n\x03APY\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"\'\n\x16QueryMarketSizeRequest\x12\r\n\x05denom\x18\x01 \x01(\t"b\n\x17QueryMarketSizeResponse\x12G\n\x0fmarket_size_usd\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00",\n\x1bQueryTokenMarketSizeRequest\x12\r\n\x05denom\x18\x01 \x01(\t"c\n\x1cQueryTokenMarketSizeResponse\x12C\n\x0bmarket_size\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00"a\n\x1dQueryRegisteredTokensResponse\x12@\n\x08registry\x18\x01 \x03(\x0b2(.umeenetwork.umee.leverage.v1beta1.TokenB\x04\xc8\xde\x1f\x00"\x14\n\x12QueryParamsRequest"V\n\x13QueryParamsResponse\x12?\n\x06params\x18\x01 \x01(\x0b2).umeenetwork.umee.leverage.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"6\n\x14QueryBorrowedRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"v\n\x15QueryBorrowedResponse\x12]\n\x08borrowed\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins";\n\x19QueryBorrowedValueRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"d\n\x1aQueryBorrowedValueResponse\x12F\n\x0eborrowed_value\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"=\n\x1bQueryCollateralValueRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"h\n\x1cQueryCollateralValueResponse\x12H\n\x10collateral_value\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"4\n\x12QueryLoanedRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"r\n\x13QueryLoanedResponse\x12[\n\x06loaned\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"9\n\x17QueryLoanedValueRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"`\n\x18QueryLoanedValueResponse\x12D\n\x0cloaned_value\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"*\n\x19QueryReserveAmountRequest\x12\r\n\x05denom\x18\x01 \x01(\t"\\\n\x1aQueryReserveAmountResponse\x12>\n\x06amount\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00"?\n\x1dQueryCollateralSettingRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"1\n\x1eQueryCollateralSettingResponse\x12\x0f\n\x07enabled\x18\x01 \x01(\x08"8\n\x16QueryCollateralRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"z\n\x17QueryCollateralResponse\x12_\n\ncollateral\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins")\n\x18QueryExchangeRateRequest\x12\r\n\x05denom\x18\x01 \x01(\t"b\n\x19QueryExchangeRateResponse\x12E\n\rexchange_rate\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"*\n\x17QueryBorrowLimitRequest\x12\x0f\n\x07address\x18\x01 \x01(\t"`\n\x18QueryBorrowLimitResponse\x12D\n\x0cborrow_limit\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"/\n\x1cQueryLiquidationLimitRequest\x12\x0f\n\x07address\x18\x01 \x01(\t"j\n\x1dQueryLiquidationLimitResponse\x12I\n\x11liquidation_limit\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00" \n\x1eQueryLiquidationTargetsRequest"2\n\x1fQueryLiquidationTargetsResponse\x12\x0f\n\x07targets\x18\x01 \x03(\t"*\n\x19QueryMarketSummaryRequest\x12\r\n\x05denom\x18\x01 \x01(\t"\xaf\x04\n\x1aQueryMarketSummaryResponse\x12\x14\n\x0csymbol_denom\x18\x01 \x01(\t\x12\x10\n\x08exponent\x18\x02 \x01(\r\x12D\n\x0coracle_price\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x01\x12L\n\x14uToken_exchange_rate\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12@\n\x08lend_APY\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12B\n\nborrow_APY\x18\x06 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12C\n\x0bmarket_size\x18\x07 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12H\n\x10available_borrow\x18\x08 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12@\n\x08reserved\x18\t \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x002\x84\x1d\n\x05Query\x12\xc0\x01\n\x10RegisteredTokens\x128.umeenetwork.umee.leverage.v1beta1.QueryRegisteredTokens\x1a@.umeenetwork.umee.leverage.v1beta1.QueryRegisteredTokensResponse"0\x82\xd3\xe4\x93\x02*\x12(/umee/leverage/v1beta1/registered_tokens\x12\x9e\x01\n\x06Params\x125.umeenetwork.umee.leverage.v1beta1.QueryParamsRequest\x1a6.umeenetwork.umee.leverage.v1beta1.QueryParamsResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/umee/leverage/v1beta1/params\x12\xa6\x01\n\x08Borrowed\x127.umeenetwork.umee.leverage.v1beta1.QueryBorrowedRequest\x1a8.umeenetwork.umee.leverage.v1beta1.QueryBorrowedResponse"\'\x82\xd3\xe4\x93\x02!\x12\x1f/umee/leverage/v1beta1/borrowed\x12\xbb\x01\n\rBorrowedValue\x12<.umeenetwork.umee.leverage.v1beta1.QueryBorrowedValueRequest\x1a=.umeenetwork.umee.leverage.v1beta1.QueryBorrowedValueResponse"-\x82\xd3\xe4\x93\x02\'\x12%/umee/leverage/v1beta1/borrowed_value\x12\x9e\x01\n\x06Loaned\x125.umeenetwork.umee.leverage.v1beta1.QueryLoanedRequest\x1a6.umeenetwork.umee.leverage.v1beta1.QueryLoanedResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/umee/leverage/v1beta1/loaned\x12\xb3\x01\n\x0bLoanedValue\x12:.umeenetwork.umee.leverage.v1beta1.QueryLoanedValueRequest\x1a;.umeenetwork.umee.leverage.v1beta1.QueryLoanedValueResponse"+\x82\xd3\xe4\x93\x02%\x12#/umee/leverage/v1beta1/loaned_value\x12\xc3\x01\n\x0fAvailableBorrow\x12>.umeenetwork.umee.leverage.v1beta1.QueryAvailableBorrowRequest\x1a?.umeenetwork.umee.leverage.v1beta1.QueryAvailableBorrowResponse"/\x82\xd3\xe4\x93\x02)\x12\'/umee/leverage/v1beta1/available_borrow\x12\xab\x01\n\tBorrowAPY\x128.umeenetwork.umee.leverage.v1beta1.QueryBorrowAPYRequest\x1a9.umeenetwork.umee.leverage.v1beta1.QueryBorrowAPYResponse")\x82\xd3\xe4\x93\x02#\x12!/umee/leverage/v1beta1/borrow_apy\x12\xa3\x01\n\x07LendAPY\x126.umeenetwork.umee.leverage.v1beta1.QueryLendAPYRequest\x1a7.umeenetwork.umee.leverage.v1beta1.QueryLendAPYResponse"\'\x82\xd3\xe4\x93\x02!\x12\x1f/umee/leverage/v1beta1/lend_apy\x12\xaf\x01\n\nMarketSize\x129.umeenetwork.umee.leverage.v1beta1.QueryMarketSizeRequest\x1a:.umeenetwork.umee.leverage.v1beta1.QueryMarketSizeResponse"*\x82\xd3\xe4\x93\x02$\x12"/umee/leverage/v1beta1/market_size\x12\xc4\x01\n\x0fTokenMarketSize\x12>.umeenetwork.umee.leverage.v1beta1.QueryTokenMarketSizeRequest\x1a?.umeenetwork.umee.leverage.v1beta1.QueryTokenMarketSizeResponse"0\x82\xd3\xe4\x93\x02*\x12(/umee/leverage/v1beta1/token_market_size\x12\xbb\x01\n\rReserveAmount\x12<.umeenetwork.umee.leverage.v1beta1.QueryReserveAmountRequest\x1a=.umeenetwork.umee.leverage.v1beta1.QueryReserveAmountResponse"-\x82\xd3\xe4\x93\x02\'\x12%/umee/leverage/v1beta1/reserve_amount\x12\xcb\x01\n\x11CollateralSetting\x12@.umeenetwork.umee.leverage.v1beta1.QueryCollateralSettingRequest\x1aA.umeenetwork.umee.leverage.v1beta1.QueryCollateralSettingResponse"1\x82\xd3\xe4\x93\x02+\x12)/umee/leverage/v1beta1/collateral_setting\x12\xae\x01\n\nCollateral\x129.umeenetwork.umee.leverage.v1beta1.QueryCollateralRequest\x1a:.umeenetwork.umee.leverage.v1beta1.QueryCollateralResponse")\x82\xd3\xe4\x93\x02#\x12!/umee/leverage/v1beta1/collateral\x12\xc3\x01\n\x0fCollateralValue\x12>.umeenetwork.umee.leverage.v1beta1.QueryCollateralValueRequest\x1a?.umeenetwork.umee.leverage.v1beta1.QueryCollateralValueResponse"/\x82\xd3\xe4\x93\x02)\x12\'/umee/leverage/v1beta1/collateral_value\x12\xb7\x01\n\x0cExchangeRate\x12;.umeenetwork.umee.leverage.v1beta1.QueryExchangeRateRequest\x1a<.umeenetwork.umee.leverage.v1beta1.QueryExchangeRateResponse",\x82\xd3\xe4\x93\x02&\x12$/umee/leverage/v1beta1/exchange_rate\x12\xb3\x01\n\x0bBorrowLimit\x12:.umeenetwork.umee.leverage.v1beta1.QueryBorrowLimitRequest\x1a;.umeenetwork.umee.leverage.v1beta1.QueryBorrowLimitResponse"+\x82\xd3\xe4\x93\x02%\x12#/umee/leverage/v1beta1/borrow_limit\x12\xc7\x01\n\x10LiquidationLimit\x12?.umeenetwork.umee.leverage.v1beta1.QueryLiquidationLimitRequest\x1a@.umeenetwork.umee.leverage.v1beta1.QueryLiquidationLimitResponse"0\x82\xd3\xe4\x93\x02*\x12(/umee/leverage/v1beta1/liquidation_limit\x12\xcf\x01\n\x12LiquidationTargets\x12A.umeenetwork.umee.leverage.v1beta1.QueryLiquidationTargetsRequest\x1aB.umeenetwork.umee.leverage.v1beta1.QueryLiquidationTargetsResponse"2\x82\xd3\xe4\x93\x02,\x12*/umee/leverage/v1beta1/liquidation_targets\x12\xb6\x01\n\rMarketSummary\x12<.umeenetwork.umee.leverage.v1beta1.QueryMarketSummaryRequest\x1a=.umeenetwork.umee.leverage.v1beta1.QueryMarketSummaryResponse"(\x82\xd3\xe4\x93\x02"\x12 /umee/leverage/v1/market_summaryB2Z0github.com/umee-network/umee/v2/x/leverage/typesb\x06proto3')
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
_QUERYLIQUIDATIONLIMITREQUEST = DESCRIPTOR.message_types_by_name['QueryLiquidationLimitRequest']
_QUERYLIQUIDATIONLIMITRESPONSE = DESCRIPTOR.message_types_by_name['QueryLiquidationLimitResponse']
_QUERYLIQUIDATIONTARGETSREQUEST = DESCRIPTOR.message_types_by_name['QueryLiquidationTargetsRequest']
_QUERYLIQUIDATIONTARGETSRESPONSE = DESCRIPTOR.message_types_by_name['QueryLiquidationTargetsResponse']
_QUERYMARKETSUMMARYREQUEST = DESCRIPTOR.message_types_by_name['QueryMarketSummaryRequest']
_QUERYMARKETSUMMARYRESPONSE = DESCRIPTOR.message_types_by_name['QueryMarketSummaryResponse']
QueryRegisteredTokens = _reflection.GeneratedProtocolMessageType('QueryRegisteredTokens', (_message.Message,), {'DESCRIPTOR': _QUERYREGISTEREDTOKENS, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryRegisteredTokens)
QueryAvailableBorrowRequest = _reflection.GeneratedProtocolMessageType('QueryAvailableBorrowRequest', (_message.Message,), {'DESCRIPTOR': _QUERYAVAILABLEBORROWREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryAvailableBorrowRequest)
QueryAvailableBorrowResponse = _reflection.GeneratedProtocolMessageType('QueryAvailableBorrowResponse', (_message.Message,), {'DESCRIPTOR': _QUERYAVAILABLEBORROWRESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryAvailableBorrowResponse)
QueryBorrowAPYRequest = _reflection.GeneratedProtocolMessageType('QueryBorrowAPYRequest', (_message.Message,), {'DESCRIPTOR': _QUERYBORROWAPYREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryBorrowAPYRequest)
QueryBorrowAPYResponse = _reflection.GeneratedProtocolMessageType('QueryBorrowAPYResponse', (_message.Message,), {'DESCRIPTOR': _QUERYBORROWAPYRESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryBorrowAPYResponse)
QueryLendAPYRequest = _reflection.GeneratedProtocolMessageType('QueryLendAPYRequest', (_message.Message,), {'DESCRIPTOR': _QUERYLENDAPYREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryLendAPYRequest)
QueryLendAPYResponse = _reflection.GeneratedProtocolMessageType('QueryLendAPYResponse', (_message.Message,), {'DESCRIPTOR': _QUERYLENDAPYRESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryLendAPYResponse)
QueryMarketSizeRequest = _reflection.GeneratedProtocolMessageType('QueryMarketSizeRequest', (_message.Message,), {'DESCRIPTOR': _QUERYMARKETSIZEREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryMarketSizeRequest)
QueryMarketSizeResponse = _reflection.GeneratedProtocolMessageType('QueryMarketSizeResponse', (_message.Message,), {'DESCRIPTOR': _QUERYMARKETSIZERESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryMarketSizeResponse)
QueryTokenMarketSizeRequest = _reflection.GeneratedProtocolMessageType('QueryTokenMarketSizeRequest', (_message.Message,), {'DESCRIPTOR': _QUERYTOKENMARKETSIZEREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryTokenMarketSizeRequest)
QueryTokenMarketSizeResponse = _reflection.GeneratedProtocolMessageType('QueryTokenMarketSizeResponse', (_message.Message,), {'DESCRIPTOR': _QUERYTOKENMARKETSIZERESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryTokenMarketSizeResponse)
QueryRegisteredTokensResponse = _reflection.GeneratedProtocolMessageType('QueryRegisteredTokensResponse', (_message.Message,), {'DESCRIPTOR': _QUERYREGISTEREDTOKENSRESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryRegisteredTokensResponse)
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsRequest)
QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSRESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsResponse)
QueryBorrowedRequest = _reflection.GeneratedProtocolMessageType('QueryBorrowedRequest', (_message.Message,), {'DESCRIPTOR': _QUERYBORROWEDREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryBorrowedRequest)
QueryBorrowedResponse = _reflection.GeneratedProtocolMessageType('QueryBorrowedResponse', (_message.Message,), {'DESCRIPTOR': _QUERYBORROWEDRESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryBorrowedResponse)
QueryBorrowedValueRequest = _reflection.GeneratedProtocolMessageType('QueryBorrowedValueRequest', (_message.Message,), {'DESCRIPTOR': _QUERYBORROWEDVALUEREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryBorrowedValueRequest)
QueryBorrowedValueResponse = _reflection.GeneratedProtocolMessageType('QueryBorrowedValueResponse', (_message.Message,), {'DESCRIPTOR': _QUERYBORROWEDVALUERESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryBorrowedValueResponse)
QueryCollateralValueRequest = _reflection.GeneratedProtocolMessageType('QueryCollateralValueRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCOLLATERALVALUEREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryCollateralValueRequest)
QueryCollateralValueResponse = _reflection.GeneratedProtocolMessageType('QueryCollateralValueResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCOLLATERALVALUERESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryCollateralValueResponse)
QueryLoanedRequest = _reflection.GeneratedProtocolMessageType('QueryLoanedRequest', (_message.Message,), {'DESCRIPTOR': _QUERYLOANEDREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryLoanedRequest)
QueryLoanedResponse = _reflection.GeneratedProtocolMessageType('QueryLoanedResponse', (_message.Message,), {'DESCRIPTOR': _QUERYLOANEDRESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryLoanedResponse)
QueryLoanedValueRequest = _reflection.GeneratedProtocolMessageType('QueryLoanedValueRequest', (_message.Message,), {'DESCRIPTOR': _QUERYLOANEDVALUEREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryLoanedValueRequest)
QueryLoanedValueResponse = _reflection.GeneratedProtocolMessageType('QueryLoanedValueResponse', (_message.Message,), {'DESCRIPTOR': _QUERYLOANEDVALUERESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryLoanedValueResponse)
QueryReserveAmountRequest = _reflection.GeneratedProtocolMessageType('QueryReserveAmountRequest', (_message.Message,), {'DESCRIPTOR': _QUERYRESERVEAMOUNTREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryReserveAmountRequest)
QueryReserveAmountResponse = _reflection.GeneratedProtocolMessageType('QueryReserveAmountResponse', (_message.Message,), {'DESCRIPTOR': _QUERYRESERVEAMOUNTRESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryReserveAmountResponse)
QueryCollateralSettingRequest = _reflection.GeneratedProtocolMessageType('QueryCollateralSettingRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCOLLATERALSETTINGREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryCollateralSettingRequest)
QueryCollateralSettingResponse = _reflection.GeneratedProtocolMessageType('QueryCollateralSettingResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCOLLATERALSETTINGRESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryCollateralSettingResponse)
QueryCollateralRequest = _reflection.GeneratedProtocolMessageType('QueryCollateralRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCOLLATERALREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryCollateralRequest)
QueryCollateralResponse = _reflection.GeneratedProtocolMessageType('QueryCollateralResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCOLLATERALRESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryCollateralResponse)
QueryExchangeRateRequest = _reflection.GeneratedProtocolMessageType('QueryExchangeRateRequest', (_message.Message,), {'DESCRIPTOR': _QUERYEXCHANGERATEREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryExchangeRateRequest)
QueryExchangeRateResponse = _reflection.GeneratedProtocolMessageType('QueryExchangeRateResponse', (_message.Message,), {'DESCRIPTOR': _QUERYEXCHANGERATERESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryExchangeRateResponse)
QueryBorrowLimitRequest = _reflection.GeneratedProtocolMessageType('QueryBorrowLimitRequest', (_message.Message,), {'DESCRIPTOR': _QUERYBORROWLIMITREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryBorrowLimitRequest)
QueryBorrowLimitResponse = _reflection.GeneratedProtocolMessageType('QueryBorrowLimitResponse', (_message.Message,), {'DESCRIPTOR': _QUERYBORROWLIMITRESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryBorrowLimitResponse)
QueryLiquidationLimitRequest = _reflection.GeneratedProtocolMessageType('QueryLiquidationLimitRequest', (_message.Message,), {'DESCRIPTOR': _QUERYLIQUIDATIONLIMITREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryLiquidationLimitRequest)
QueryLiquidationLimitResponse = _reflection.GeneratedProtocolMessageType('QueryLiquidationLimitResponse', (_message.Message,), {'DESCRIPTOR': _QUERYLIQUIDATIONLIMITRESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryLiquidationLimitResponse)
QueryLiquidationTargetsRequest = _reflection.GeneratedProtocolMessageType('QueryLiquidationTargetsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYLIQUIDATIONTARGETSREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryLiquidationTargetsRequest)
QueryLiquidationTargetsResponse = _reflection.GeneratedProtocolMessageType('QueryLiquidationTargetsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYLIQUIDATIONTARGETSRESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryLiquidationTargetsResponse)
QueryMarketSummaryRequest = _reflection.GeneratedProtocolMessageType('QueryMarketSummaryRequest', (_message.Message,), {'DESCRIPTOR': _QUERYMARKETSUMMARYREQUEST, '__module__': 'umee.leverage.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryMarketSummaryRequest)
QueryMarketSummaryResponse = _reflection.GeneratedProtocolMessageType('QueryMarketSummaryResponse', (_message.Message,), {'DESCRIPTOR': _QUERYMARKETSUMMARYRESPONSE, '__module__': 'umee.leverage.v1beta1.query_pb2'})
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
    _QUERYLIQUIDATIONLIMITRESPONSE.fields_by_name['liquidation_limit']._options = None
    _QUERYLIQUIDATIONLIMITRESPONSE.fields_by_name['liquidation_limit']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
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
    _QUERY.methods_by_name['RegisteredTokens']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/umee/leverage/v1beta1/registered_tokens'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/umee/leverage/v1beta1/params'
    _QUERY.methods_by_name['Borrowed']._options = None
    _QUERY.methods_by_name['Borrowed']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/umee/leverage/v1beta1/borrowed'
    _QUERY.methods_by_name['BorrowedValue']._options = None
    _QUERY.methods_by_name['BorrowedValue']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/umee/leverage/v1beta1/borrowed_value"
    _QUERY.methods_by_name['Loaned']._options = None
    _QUERY.methods_by_name['Loaned']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/umee/leverage/v1beta1/loaned'
    _QUERY.methods_by_name['LoanedValue']._options = None
    _QUERY.methods_by_name['LoanedValue']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/umee/leverage/v1beta1/loaned_value'
    _QUERY.methods_by_name['AvailableBorrow']._options = None
    _QUERY.methods_by_name['AvailableBorrow']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/umee/leverage/v1beta1/available_borrow"
    _QUERY.methods_by_name['BorrowAPY']._options = None
    _QUERY.methods_by_name['BorrowAPY']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/umee/leverage/v1beta1/borrow_apy'
    _QUERY.methods_by_name['LendAPY']._options = None
    _QUERY.methods_by_name['LendAPY']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/umee/leverage/v1beta1/lend_apy'
    _QUERY.methods_by_name['MarketSize']._options = None
    _QUERY.methods_by_name['MarketSize']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/umee/leverage/v1beta1/market_size'
    _QUERY.methods_by_name['TokenMarketSize']._options = None
    _QUERY.methods_by_name['TokenMarketSize']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/umee/leverage/v1beta1/token_market_size'
    _QUERY.methods_by_name['ReserveAmount']._options = None
    _QUERY.methods_by_name['ReserveAmount']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/umee/leverage/v1beta1/reserve_amount"
    _QUERY.methods_by_name['CollateralSetting']._options = None
    _QUERY.methods_by_name['CollateralSetting']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/umee/leverage/v1beta1/collateral_setting'
    _QUERY.methods_by_name['Collateral']._options = None
    _QUERY.methods_by_name['Collateral']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/umee/leverage/v1beta1/collateral'
    _QUERY.methods_by_name['CollateralValue']._options = None
    _QUERY.methods_by_name['CollateralValue']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/umee/leverage/v1beta1/collateral_value"
    _QUERY.methods_by_name['ExchangeRate']._options = None
    _QUERY.methods_by_name['ExchangeRate']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/umee/leverage/v1beta1/exchange_rate'
    _QUERY.methods_by_name['BorrowLimit']._options = None
    _QUERY.methods_by_name['BorrowLimit']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/umee/leverage/v1beta1/borrow_limit'
    _QUERY.methods_by_name['LiquidationLimit']._options = None
    _QUERY.methods_by_name['LiquidationLimit']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/umee/leverage/v1beta1/liquidation_limit'
    _QUERY.methods_by_name['LiquidationTargets']._options = None
    _QUERY.methods_by_name['LiquidationTargets']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/umee/leverage/v1beta1/liquidation_targets'
    _QUERY.methods_by_name['MarketSummary']._options = None
    _QUERY.methods_by_name['MarketSummary']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /umee/leverage/v1/market_summary'
    _QUERYREGISTEREDTOKENS._serialized_start = 194
    _QUERYREGISTEREDTOKENS._serialized_end = 217
    _QUERYAVAILABLEBORROWREQUEST._serialized_start = 219
    _QUERYAVAILABLEBORROWREQUEST._serialized_end = 263
    _QUERYAVAILABLEBORROWRESPONSE._serialized_start = 265
    _QUERYAVAILABLEBORROWRESPONSE._serialized_end = 359
    _QUERYBORROWAPYREQUEST._serialized_start = 361
    _QUERYBORROWAPYREQUEST._serialized_end = 399
    _QUERYBORROWAPYRESPONSE._serialized_start = 401
    _QUERYBORROWAPYRESPONSE._serialized_end = 486
    _QUERYLENDAPYREQUEST._serialized_start = 488
    _QUERYLENDAPYREQUEST._serialized_end = 524
    _QUERYLENDAPYRESPONSE._serialized_start = 526
    _QUERYLENDAPYRESPONSE._serialized_end = 609
    _QUERYMARKETSIZEREQUEST._serialized_start = 611
    _QUERYMARKETSIZEREQUEST._serialized_end = 650
    _QUERYMARKETSIZERESPONSE._serialized_start = 652
    _QUERYMARKETSIZERESPONSE._serialized_end = 750
    _QUERYTOKENMARKETSIZEREQUEST._serialized_start = 752
    _QUERYTOKENMARKETSIZEREQUEST._serialized_end = 796
    _QUERYTOKENMARKETSIZERESPONSE._serialized_start = 798
    _QUERYTOKENMARKETSIZERESPONSE._serialized_end = 897
    _QUERYREGISTEREDTOKENSRESPONSE._serialized_start = 899
    _QUERYREGISTEREDTOKENSRESPONSE._serialized_end = 996
    _QUERYPARAMSREQUEST._serialized_start = 998
    _QUERYPARAMSREQUEST._serialized_end = 1018
    _QUERYPARAMSRESPONSE._serialized_start = 1020
    _QUERYPARAMSRESPONSE._serialized_end = 1106
    _QUERYBORROWEDREQUEST._serialized_start = 1108
    _QUERYBORROWEDREQUEST._serialized_end = 1162
    _QUERYBORROWEDRESPONSE._serialized_start = 1164
    _QUERYBORROWEDRESPONSE._serialized_end = 1282
    _QUERYBORROWEDVALUEREQUEST._serialized_start = 1284
    _QUERYBORROWEDVALUEREQUEST._serialized_end = 1343
    _QUERYBORROWEDVALUERESPONSE._serialized_start = 1345
    _QUERYBORROWEDVALUERESPONSE._serialized_end = 1445
    _QUERYCOLLATERALVALUEREQUEST._serialized_start = 1447
    _QUERYCOLLATERALVALUEREQUEST._serialized_end = 1508
    _QUERYCOLLATERALVALUERESPONSE._serialized_start = 1510
    _QUERYCOLLATERALVALUERESPONSE._serialized_end = 1614
    _QUERYLOANEDREQUEST._serialized_start = 1616
    _QUERYLOANEDREQUEST._serialized_end = 1668
    _QUERYLOANEDRESPONSE._serialized_start = 1670
    _QUERYLOANEDRESPONSE._serialized_end = 1784
    _QUERYLOANEDVALUEREQUEST._serialized_start = 1786
    _QUERYLOANEDVALUEREQUEST._serialized_end = 1843
    _QUERYLOANEDVALUERESPONSE._serialized_start = 1845
    _QUERYLOANEDVALUERESPONSE._serialized_end = 1941
    _QUERYRESERVEAMOUNTREQUEST._serialized_start = 1943
    _QUERYRESERVEAMOUNTREQUEST._serialized_end = 1985
    _QUERYRESERVEAMOUNTRESPONSE._serialized_start = 1987
    _QUERYRESERVEAMOUNTRESPONSE._serialized_end = 2079
    _QUERYCOLLATERALSETTINGREQUEST._serialized_start = 2081
    _QUERYCOLLATERALSETTINGREQUEST._serialized_end = 2144
    _QUERYCOLLATERALSETTINGRESPONSE._serialized_start = 2146
    _QUERYCOLLATERALSETTINGRESPONSE._serialized_end = 2195
    _QUERYCOLLATERALREQUEST._serialized_start = 2197
    _QUERYCOLLATERALREQUEST._serialized_end = 2253
    _QUERYCOLLATERALRESPONSE._serialized_start = 2255
    _QUERYCOLLATERALRESPONSE._serialized_end = 2377
    _QUERYEXCHANGERATEREQUEST._serialized_start = 2379
    _QUERYEXCHANGERATEREQUEST._serialized_end = 2420
    _QUERYEXCHANGERATERESPONSE._serialized_start = 2422
    _QUERYEXCHANGERATERESPONSE._serialized_end = 2520
    _QUERYBORROWLIMITREQUEST._serialized_start = 2522
    _QUERYBORROWLIMITREQUEST._serialized_end = 2564
    _QUERYBORROWLIMITRESPONSE._serialized_start = 2566
    _QUERYBORROWLIMITRESPONSE._serialized_end = 2662
    _QUERYLIQUIDATIONLIMITREQUEST._serialized_start = 2664
    _QUERYLIQUIDATIONLIMITREQUEST._serialized_end = 2711
    _QUERYLIQUIDATIONLIMITRESPONSE._serialized_start = 2713
    _QUERYLIQUIDATIONLIMITRESPONSE._serialized_end = 2819
    _QUERYLIQUIDATIONTARGETSREQUEST._serialized_start = 2821
    _QUERYLIQUIDATIONTARGETSREQUEST._serialized_end = 2853
    _QUERYLIQUIDATIONTARGETSRESPONSE._serialized_start = 2855
    _QUERYLIQUIDATIONTARGETSRESPONSE._serialized_end = 2905
    _QUERYMARKETSUMMARYREQUEST._serialized_start = 2907
    _QUERYMARKETSUMMARYREQUEST._serialized_end = 2949
    _QUERYMARKETSUMMARYRESPONSE._serialized_start = 2952
    _QUERYMARKETSUMMARYRESPONSE._serialized_end = 3511
    _QUERY._serialized_start = 3514
    _QUERY._serialized_end = 7230


'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....umee.leverage.v1beta1 import query_pb2 as umee_dot_leverage_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.RegisteredTokens = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/RegisteredTokens', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryRegisteredTokens.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryRegisteredTokensResponse.FromString)
        self.Params = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/Params', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString)
        self.Borrowed = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/Borrowed', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowedRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowedResponse.FromString)
        self.BorrowedValue = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/BorrowedValue', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowedValueRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowedValueResponse.FromString)
        self.Loaned = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/Loaned', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLoanedRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLoanedResponse.FromString)
        self.LoanedValue = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/LoanedValue', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLoanedValueRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLoanedValueResponse.FromString)
        self.AvailableBorrow = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/AvailableBorrow', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryAvailableBorrowRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryAvailableBorrowResponse.FromString)
        self.BorrowAPY = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/BorrowAPY', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowAPYRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowAPYResponse.FromString)
        self.LendAPY = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/LendAPY', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLendAPYRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLendAPYResponse.FromString)
        self.MarketSize = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/MarketSize', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryMarketSizeRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryMarketSizeResponse.FromString)
        self.TokenMarketSize = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/TokenMarketSize', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryTokenMarketSizeRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryTokenMarketSizeResponse.FromString)
        self.ReserveAmount = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/ReserveAmount', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryReserveAmountRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryReserveAmountResponse.FromString)
        self.CollateralSetting = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/CollateralSetting', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralSettingRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralSettingResponse.FromString)
        self.Collateral = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/Collateral', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralResponse.FromString)
        self.CollateralValue = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/CollateralValue', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralValueRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralValueResponse.FromString)
        self.ExchangeRate = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/ExchangeRate', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryExchangeRateRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryExchangeRateResponse.FromString)
        self.BorrowLimit = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/BorrowLimit', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowLimitRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowLimitResponse.FromString)
        self.LiquidationLimit = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/LiquidationLimit', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLiquidationLimitRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLiquidationLimitResponse.FromString)
        self.LiquidationTargets = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/LiquidationTargets', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLiquidationTargetsRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLiquidationTargetsResponse.FromString)
        self.MarketSummary = channel.unary_unary('/umeenetwork.umee.leverage.v1beta1.Query/MarketSummary', request_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryMarketSummaryRequest.SerializeToString, response_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryMarketSummaryResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service.\n    '

    def RegisteredTokens(self, request, context):
        'RegisteredTokens queries for all the registered tokens.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        'Params queries the parameters of the x/leverage module.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Borrowed(self, request, context):
        'Borrowed queries for the borrowed amount of a user by token denomination.\n        If the denomination is not supplied, the total for each borrowed token is\n        returned.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BorrowedValue(self, request, context):
        'BorrowedValue queries for the usd value of the borrowed amount of a user\n        by token denomination.  If the denomination is not supplied, the sum across\n        all borrowed tokens is returned.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Loaned(self, request, context):
        'Loaned queries for the amount of tokens loaned by a user by denomination.\n        If the denomination is not supplied, the total for each loaned token is\n        returned.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoanedValue(self, request, context):
        'LoanedValue queries for the USD value loaned by a user by token\n        denomination. If the denomination is not supplied, the sum across all\n        loaned tokens is returned.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AvailableBorrow(self, request, context):
        'AvailableBorrow queries for the available amount to borrow of a specified denomination.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BorrowAPY(self, request, context):
        'BorrowAPY queries for the borrow APY of a specified denomination.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LendAPY(self, request, context):
        'LendAPY queries for the lend APY of a specified denomination.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MarketSize(self, request, context):
        'MarketSize queries for the Market Size in USD of a specified denomination, which\n        is the USD value of total tokens loaned by all users plus borrow interest owed\n        by all users.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TokenMarketSize(self, request, context):
        'TokenMarketSize queries for the Market Size in base tokens of a specified denomination,\n        which is the total tokens loaned by all users plus borrow interest owed by all users.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReserveAmount(self, request, context):
        'ReserveAmount queries for the amount reserved of a specified denomination.\n        If the token is not valid, the reserved amount is zero.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CollateralSetting(self, request, context):
        "CollateralSetting queries a borrower's collateral setting (enabled or disabled)\n        for a specified uToken denomination.\n        "
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Collateral(self, request, context):
        "Collateral queries the collateral amount of a user by token denomination.\n        If the denomination is not supplied, all of the user's collateral tokens\n        are returned.\n        "
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CollateralValue(self, request, context):
        "CollateralValue queries for the total USD value of a user's collateral, or\n        the USD value held as a given base asset's associated uToken denomination.\n        "
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExchangeRate(self, request, context):
        'ExchangeRate queries the uToken exchange rate of a given uToken denomination.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BorrowLimit(self, request, context):
        'BorrowLimit queries the borrow limit in USD of a given borrower.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LiquidationLimit(self, request, context):
        'LiquidationLimit queries the limit in USD above which a given borrower is eligible for liquidation.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LiquidationTargets(self, request, context):
        'LiquidationTargets queries a list of all borrower addresses eligible for liquidation.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MarketSummary(self, request, context):
        "MarketSummary queries a base asset's current borrowing and lending conditions.\n        "
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'RegisteredTokens': grpc.unary_unary_rpc_method_handler(servicer.RegisteredTokens, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryRegisteredTokens.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryRegisteredTokensResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'Borrowed': grpc.unary_unary_rpc_method_handler(servicer.Borrowed, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowedRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowedResponse.SerializeToString), 'BorrowedValue': grpc.unary_unary_rpc_method_handler(servicer.BorrowedValue, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowedValueRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowedValueResponse.SerializeToString), 'Loaned': grpc.unary_unary_rpc_method_handler(servicer.Loaned, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLoanedRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLoanedResponse.SerializeToString), 'LoanedValue': grpc.unary_unary_rpc_method_handler(servicer.LoanedValue, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLoanedValueRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLoanedValueResponse.SerializeToString), 'AvailableBorrow': grpc.unary_unary_rpc_method_handler(servicer.AvailableBorrow, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryAvailableBorrowRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryAvailableBorrowResponse.SerializeToString), 'BorrowAPY': grpc.unary_unary_rpc_method_handler(servicer.BorrowAPY, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowAPYRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowAPYResponse.SerializeToString), 'LendAPY': grpc.unary_unary_rpc_method_handler(servicer.LendAPY, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLendAPYRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLendAPYResponse.SerializeToString), 'MarketSize': grpc.unary_unary_rpc_method_handler(servicer.MarketSize, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryMarketSizeRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryMarketSizeResponse.SerializeToString), 'TokenMarketSize': grpc.unary_unary_rpc_method_handler(servicer.TokenMarketSize, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryTokenMarketSizeRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryTokenMarketSizeResponse.SerializeToString), 'ReserveAmount': grpc.unary_unary_rpc_method_handler(servicer.ReserveAmount, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryReserveAmountRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryReserveAmountResponse.SerializeToString), 'CollateralSetting': grpc.unary_unary_rpc_method_handler(servicer.CollateralSetting, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralSettingRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralSettingResponse.SerializeToString), 'Collateral': grpc.unary_unary_rpc_method_handler(servicer.Collateral, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralResponse.SerializeToString), 'CollateralValue': grpc.unary_unary_rpc_method_handler(servicer.CollateralValue, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralValueRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralValueResponse.SerializeToString), 'ExchangeRate': grpc.unary_unary_rpc_method_handler(servicer.ExchangeRate, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryExchangeRateRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryExchangeRateResponse.SerializeToString), 'BorrowLimit': grpc.unary_unary_rpc_method_handler(servicer.BorrowLimit, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowLimitRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowLimitResponse.SerializeToString), 'LiquidationLimit': grpc.unary_unary_rpc_method_handler(servicer.LiquidationLimit, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLiquidationLimitRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLiquidationLimitResponse.SerializeToString), 'LiquidationTargets': grpc.unary_unary_rpc_method_handler(servicer.LiquidationTargets, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLiquidationTargetsRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLiquidationTargetsResponse.SerializeToString), 'MarketSummary': grpc.unary_unary_rpc_method_handler(servicer.MarketSummary, request_deserializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryMarketSummaryRequest.FromString, response_serializer=umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryMarketSummaryResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('umeenetwork.umee.leverage.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service.\n    '

    @staticmethod
    def RegisteredTokens(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/RegisteredTokens', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryRegisteredTokens.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryRegisteredTokensResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/Params', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Borrowed(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/Borrowed', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowedRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowedResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BorrowedValue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/BorrowedValue', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowedValueRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowedValueResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Loaned(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/Loaned', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLoanedRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLoanedResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoanedValue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/LoanedValue', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLoanedValueRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLoanedValueResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AvailableBorrow(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/AvailableBorrow', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryAvailableBorrowRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryAvailableBorrowResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BorrowAPY(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/BorrowAPY', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowAPYRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowAPYResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LendAPY(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/LendAPY', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLendAPYRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLendAPYResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MarketSize(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/MarketSize', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryMarketSizeRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryMarketSizeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TokenMarketSize(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/TokenMarketSize', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryTokenMarketSizeRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryTokenMarketSizeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReserveAmount(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/ReserveAmount', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryReserveAmountRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryReserveAmountResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CollateralSetting(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/CollateralSetting', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralSettingRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralSettingResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Collateral(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/Collateral', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CollateralValue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/CollateralValue', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralValueRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryCollateralValueResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExchangeRate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/ExchangeRate', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryExchangeRateRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryExchangeRateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BorrowLimit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/BorrowLimit', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowLimitRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryBorrowLimitResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LiquidationLimit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/LiquidationLimit', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLiquidationLimitRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLiquidationLimitResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LiquidationTargets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/LiquidationTargets', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLiquidationTargetsRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryLiquidationTargetsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MarketSummary(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/umeenetwork.umee.leverage.v1beta1.Query/MarketSummary', umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryMarketSummaryRequest.SerializeToString, umee_dot_leverage_dot_v1beta1_dot_query__pb2.QueryMarketSummaryResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

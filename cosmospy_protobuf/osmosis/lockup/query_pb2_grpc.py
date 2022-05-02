
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ...osmosis.lockup import query_pb2 as osmosis_dot_lockup_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.ModuleBalance = channel.unary_unary('/osmosis.lockup.Query/ModuleBalance', request_serializer=osmosis_dot_lockup_dot_query__pb2.ModuleBalanceRequest.SerializeToString, response_deserializer=osmosis_dot_lockup_dot_query__pb2.ModuleBalanceResponse.FromString)
        self.ModuleLockedAmount = channel.unary_unary('/osmosis.lockup.Query/ModuleLockedAmount', request_serializer=osmosis_dot_lockup_dot_query__pb2.ModuleLockedAmountRequest.SerializeToString, response_deserializer=osmosis_dot_lockup_dot_query__pb2.ModuleLockedAmountResponse.FromString)
        self.AccountUnlockableCoins = channel.unary_unary('/osmosis.lockup.Query/AccountUnlockableCoins', request_serializer=osmosis_dot_lockup_dot_query__pb2.AccountUnlockableCoinsRequest.SerializeToString, response_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountUnlockableCoinsResponse.FromString)
        self.AccountUnlockingCoins = channel.unary_unary('/osmosis.lockup.Query/AccountUnlockingCoins', request_serializer=osmosis_dot_lockup_dot_query__pb2.AccountUnlockingCoinsRequest.SerializeToString, response_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountUnlockingCoinsResponse.FromString)
        self.AccountLockedCoins = channel.unary_unary('/osmosis.lockup.Query/AccountLockedCoins', request_serializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedCoinsRequest.SerializeToString, response_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedCoinsResponse.FromString)
        self.AccountLockedPastTime = channel.unary_unary('/osmosis.lockup.Query/AccountLockedPastTime', request_serializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeRequest.SerializeToString, response_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeResponse.FromString)
        self.AccountLockedPastTimeNotUnlockingOnly = channel.unary_unary('/osmosis.lockup.Query/AccountLockedPastTimeNotUnlockingOnly', request_serializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeNotUnlockingOnlyRequest.SerializeToString, response_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeNotUnlockingOnlyResponse.FromString)
        self.AccountUnlockedBeforeTime = channel.unary_unary('/osmosis.lockup.Query/AccountUnlockedBeforeTime', request_serializer=osmosis_dot_lockup_dot_query__pb2.AccountUnlockedBeforeTimeRequest.SerializeToString, response_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountUnlockedBeforeTimeResponse.FromString)
        self.AccountLockedPastTimeDenom = channel.unary_unary('/osmosis.lockup.Query/AccountLockedPastTimeDenom', request_serializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeDenomRequest.SerializeToString, response_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeDenomResponse.FromString)
        self.LockedDenom = channel.unary_unary('/osmosis.lockup.Query/LockedDenom', request_serializer=osmosis_dot_lockup_dot_query__pb2.LockedDenomRequest.SerializeToString, response_deserializer=osmosis_dot_lockup_dot_query__pb2.LockedDenomResponse.FromString)
        self.LockedByID = channel.unary_unary('/osmosis.lockup.Query/LockedByID', request_serializer=osmosis_dot_lockup_dot_query__pb2.LockedRequest.SerializeToString, response_deserializer=osmosis_dot_lockup_dot_query__pb2.LockedResponse.FromString)
        self.SyntheticLockupsByLockupID = channel.unary_unary('/osmosis.lockup.Query/SyntheticLockupsByLockupID', request_serializer=osmosis_dot_lockup_dot_query__pb2.SyntheticLockupsByLockupIDRequest.SerializeToString, response_deserializer=osmosis_dot_lockup_dot_query__pb2.SyntheticLockupsByLockupIDResponse.FromString)
        self.AccountLockedLongerDuration = channel.unary_unary('/osmosis.lockup.Query/AccountLockedLongerDuration', request_serializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationRequest.SerializeToString, response_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationResponse.FromString)
        self.AccountLockedDuration = channel.unary_unary('/osmosis.lockup.Query/AccountLockedDuration', request_serializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedDurationRequest.SerializeToString, response_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedDurationResponse.FromString)
        self.AccountLockedLongerDurationNotUnlockingOnly = channel.unary_unary('/osmosis.lockup.Query/AccountLockedLongerDurationNotUnlockingOnly', request_serializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationNotUnlockingOnlyRequest.SerializeToString, response_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationNotUnlockingOnlyResponse.FromString)
        self.AccountLockedLongerDurationDenom = channel.unary_unary('/osmosis.lockup.Query/AccountLockedLongerDurationDenom', request_serializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationDenomRequest.SerializeToString, response_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationDenomResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service.\n    '

    def ModuleBalance(self, request, context):
        'Return full balance of the module\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModuleLockedAmount(self, request, context):
        'Return locked balance of the module\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountUnlockableCoins(self, request, context):
        'Returns unlockable coins which are not withdrawn yet\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountUnlockingCoins(self, request, context):
        'Returns unlocking coins\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountLockedCoins(self, request, context):
        "Return a locked coins that can't be withdrawn\n        "
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountLockedPastTime(self, request, context):
        'Returns locked records of an account with unlock time beyond timestamp\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountLockedPastTimeNotUnlockingOnly(self, request, context):
        'Returns locked records of an account with unlock time beyond timestamp\n        excluding tokens started unlocking\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountUnlockedBeforeTime(self, request, context):
        'Returns unlocked records with unlock time before timestamp\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountLockedPastTimeDenom(self, request, context):
        'Returns lock records by address, timestamp, denom\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LockedDenom(self, request, context):
        'Returns total locked per denom with longer past given time\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LockedByID(self, request, context):
        'Returns lock record by id\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SyntheticLockupsByLockupID(self, request, context):
        'Returns synthetic lockups by native lockup id\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountLockedLongerDuration(self, request, context):
        'Returns account locked records with longer duration\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountLockedDuration(self, request, context):
        'Returns account locked records with a specific duration\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountLockedLongerDurationNotUnlockingOnly(self, request, context):
        'Returns account locked records with longer duration excluding tokens\n        started unlocking\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountLockedLongerDurationDenom(self, request, context):
        "Returns account's locked records for a denom with longer duration\n        "
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'ModuleBalance': grpc.unary_unary_rpc_method_handler(servicer.ModuleBalance, request_deserializer=osmosis_dot_lockup_dot_query__pb2.ModuleBalanceRequest.FromString, response_serializer=osmosis_dot_lockup_dot_query__pb2.ModuleBalanceResponse.SerializeToString), 'ModuleLockedAmount': grpc.unary_unary_rpc_method_handler(servicer.ModuleLockedAmount, request_deserializer=osmosis_dot_lockup_dot_query__pb2.ModuleLockedAmountRequest.FromString, response_serializer=osmosis_dot_lockup_dot_query__pb2.ModuleLockedAmountResponse.SerializeToString), 'AccountUnlockableCoins': grpc.unary_unary_rpc_method_handler(servicer.AccountUnlockableCoins, request_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountUnlockableCoinsRequest.FromString, response_serializer=osmosis_dot_lockup_dot_query__pb2.AccountUnlockableCoinsResponse.SerializeToString), 'AccountUnlockingCoins': grpc.unary_unary_rpc_method_handler(servicer.AccountUnlockingCoins, request_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountUnlockingCoinsRequest.FromString, response_serializer=osmosis_dot_lockup_dot_query__pb2.AccountUnlockingCoinsResponse.SerializeToString), 'AccountLockedCoins': grpc.unary_unary_rpc_method_handler(servicer.AccountLockedCoins, request_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedCoinsRequest.FromString, response_serializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedCoinsResponse.SerializeToString), 'AccountLockedPastTime': grpc.unary_unary_rpc_method_handler(servicer.AccountLockedPastTime, request_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeRequest.FromString, response_serializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeResponse.SerializeToString), 'AccountLockedPastTimeNotUnlockingOnly': grpc.unary_unary_rpc_method_handler(servicer.AccountLockedPastTimeNotUnlockingOnly, request_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeNotUnlockingOnlyRequest.FromString, response_serializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeNotUnlockingOnlyResponse.SerializeToString), 'AccountUnlockedBeforeTime': grpc.unary_unary_rpc_method_handler(servicer.AccountUnlockedBeforeTime, request_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountUnlockedBeforeTimeRequest.FromString, response_serializer=osmosis_dot_lockup_dot_query__pb2.AccountUnlockedBeforeTimeResponse.SerializeToString), 'AccountLockedPastTimeDenom': grpc.unary_unary_rpc_method_handler(servicer.AccountLockedPastTimeDenom, request_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeDenomRequest.FromString, response_serializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeDenomResponse.SerializeToString), 'LockedDenom': grpc.unary_unary_rpc_method_handler(servicer.LockedDenom, request_deserializer=osmosis_dot_lockup_dot_query__pb2.LockedDenomRequest.FromString, response_serializer=osmosis_dot_lockup_dot_query__pb2.LockedDenomResponse.SerializeToString), 'LockedByID': grpc.unary_unary_rpc_method_handler(servicer.LockedByID, request_deserializer=osmosis_dot_lockup_dot_query__pb2.LockedRequest.FromString, response_serializer=osmosis_dot_lockup_dot_query__pb2.LockedResponse.SerializeToString), 'SyntheticLockupsByLockupID': grpc.unary_unary_rpc_method_handler(servicer.SyntheticLockupsByLockupID, request_deserializer=osmosis_dot_lockup_dot_query__pb2.SyntheticLockupsByLockupIDRequest.FromString, response_serializer=osmosis_dot_lockup_dot_query__pb2.SyntheticLockupsByLockupIDResponse.SerializeToString), 'AccountLockedLongerDuration': grpc.unary_unary_rpc_method_handler(servicer.AccountLockedLongerDuration, request_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationRequest.FromString, response_serializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationResponse.SerializeToString), 'AccountLockedDuration': grpc.unary_unary_rpc_method_handler(servicer.AccountLockedDuration, request_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedDurationRequest.FromString, response_serializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedDurationResponse.SerializeToString), 'AccountLockedLongerDurationNotUnlockingOnly': grpc.unary_unary_rpc_method_handler(servicer.AccountLockedLongerDurationNotUnlockingOnly, request_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationNotUnlockingOnlyRequest.FromString, response_serializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationNotUnlockingOnlyResponse.SerializeToString), 'AccountLockedLongerDurationDenom': grpc.unary_unary_rpc_method_handler(servicer.AccountLockedLongerDurationDenom, request_deserializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationDenomRequest.FromString, response_serializer=osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationDenomResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.lockup.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service.\n    '

    @staticmethod
    def ModuleBalance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.lockup.Query/ModuleBalance', osmosis_dot_lockup_dot_query__pb2.ModuleBalanceRequest.SerializeToString, osmosis_dot_lockup_dot_query__pb2.ModuleBalanceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModuleLockedAmount(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.lockup.Query/ModuleLockedAmount', osmosis_dot_lockup_dot_query__pb2.ModuleLockedAmountRequest.SerializeToString, osmosis_dot_lockup_dot_query__pb2.ModuleLockedAmountResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AccountUnlockableCoins(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.lockup.Query/AccountUnlockableCoins', osmosis_dot_lockup_dot_query__pb2.AccountUnlockableCoinsRequest.SerializeToString, osmosis_dot_lockup_dot_query__pb2.AccountUnlockableCoinsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AccountUnlockingCoins(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.lockup.Query/AccountUnlockingCoins', osmosis_dot_lockup_dot_query__pb2.AccountUnlockingCoinsRequest.SerializeToString, osmosis_dot_lockup_dot_query__pb2.AccountUnlockingCoinsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AccountLockedCoins(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.lockup.Query/AccountLockedCoins', osmosis_dot_lockup_dot_query__pb2.AccountLockedCoinsRequest.SerializeToString, osmosis_dot_lockup_dot_query__pb2.AccountLockedCoinsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AccountLockedPastTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.lockup.Query/AccountLockedPastTime', osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeRequest.SerializeToString, osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AccountLockedPastTimeNotUnlockingOnly(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.lockup.Query/AccountLockedPastTimeNotUnlockingOnly', osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeNotUnlockingOnlyRequest.SerializeToString, osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeNotUnlockingOnlyResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AccountUnlockedBeforeTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.lockup.Query/AccountUnlockedBeforeTime', osmosis_dot_lockup_dot_query__pb2.AccountUnlockedBeforeTimeRequest.SerializeToString, osmosis_dot_lockup_dot_query__pb2.AccountUnlockedBeforeTimeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AccountLockedPastTimeDenom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.lockup.Query/AccountLockedPastTimeDenom', osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeDenomRequest.SerializeToString, osmosis_dot_lockup_dot_query__pb2.AccountLockedPastTimeDenomResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LockedDenom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.lockup.Query/LockedDenom', osmosis_dot_lockup_dot_query__pb2.LockedDenomRequest.SerializeToString, osmosis_dot_lockup_dot_query__pb2.LockedDenomResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LockedByID(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.lockup.Query/LockedByID', osmosis_dot_lockup_dot_query__pb2.LockedRequest.SerializeToString, osmosis_dot_lockup_dot_query__pb2.LockedResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SyntheticLockupsByLockupID(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.lockup.Query/SyntheticLockupsByLockupID', osmosis_dot_lockup_dot_query__pb2.SyntheticLockupsByLockupIDRequest.SerializeToString, osmosis_dot_lockup_dot_query__pb2.SyntheticLockupsByLockupIDResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AccountLockedLongerDuration(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.lockup.Query/AccountLockedLongerDuration', osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationRequest.SerializeToString, osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AccountLockedDuration(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.lockup.Query/AccountLockedDuration', osmosis_dot_lockup_dot_query__pb2.AccountLockedDurationRequest.SerializeToString, osmosis_dot_lockup_dot_query__pb2.AccountLockedDurationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AccountLockedLongerDurationNotUnlockingOnly(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.lockup.Query/AccountLockedLongerDurationNotUnlockingOnly', osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationNotUnlockingOnlyRequest.SerializeToString, osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationNotUnlockingOnlyResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AccountLockedLongerDurationDenom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.lockup.Query/AccountLockedLongerDurationDenom', osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationDenomRequest.SerializeToString, osmosis_dot_lockup_dot_query__pb2.AccountLockedLongerDurationDenomResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

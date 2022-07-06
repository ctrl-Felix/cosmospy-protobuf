
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....akash.market.v1beta2 import bid_pb2 as akash_dot_market_dot_v1beta2_dot_bid__pb2
from ....akash.market.v1beta2 import lease_pb2 as akash_dot_market_dot_v1beta2_dot_lease__pb2

class MsgStub(object):
    'Msg defines the market Msg service\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.CreateBid = channel.unary_unary('/akash.market.v1beta2.Msg/CreateBid', request_serializer=akash_dot_market_dot_v1beta2_dot_bid__pb2.MsgCreateBid.SerializeToString, response_deserializer=akash_dot_market_dot_v1beta2_dot_bid__pb2.MsgCreateBidResponse.FromString)
        self.CloseBid = channel.unary_unary('/akash.market.v1beta2.Msg/CloseBid', request_serializer=akash_dot_market_dot_v1beta2_dot_bid__pb2.MsgCloseBid.SerializeToString, response_deserializer=akash_dot_market_dot_v1beta2_dot_bid__pb2.MsgCloseBidResponse.FromString)
        self.WithdrawLease = channel.unary_unary('/akash.market.v1beta2.Msg/WithdrawLease', request_serializer=akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgWithdrawLease.SerializeToString, response_deserializer=akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgWithdrawLeaseResponse.FromString)
        self.CreateLease = channel.unary_unary('/akash.market.v1beta2.Msg/CreateLease', request_serializer=akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgCreateLease.SerializeToString, response_deserializer=akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgCreateLeaseResponse.FromString)
        self.CloseLease = channel.unary_unary('/akash.market.v1beta2.Msg/CloseLease', request_serializer=akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgCloseLease.SerializeToString, response_deserializer=akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgCloseLeaseResponse.FromString)

class MsgServicer(object):
    'Msg defines the market Msg service\n    '

    def CreateBid(self, request, context):
        'CreateBid defines a method to create a bid given proper inputs.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseBid(self, request, context):
        'CloseBid defines a method to close a bid given proper inputs.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WithdrawLease(self, request, context):
        'WithdrawLease withdraws accrued funds from the lease payment\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateLease(self, request, context):
        'CreateLease creates a new lease\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseLease(self, request, context):
        'CloseLease defines a method to close an order given proper inputs.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateBid': grpc.unary_unary_rpc_method_handler(servicer.CreateBid, request_deserializer=akash_dot_market_dot_v1beta2_dot_bid__pb2.MsgCreateBid.FromString, response_serializer=akash_dot_market_dot_v1beta2_dot_bid__pb2.MsgCreateBidResponse.SerializeToString), 'CloseBid': grpc.unary_unary_rpc_method_handler(servicer.CloseBid, request_deserializer=akash_dot_market_dot_v1beta2_dot_bid__pb2.MsgCloseBid.FromString, response_serializer=akash_dot_market_dot_v1beta2_dot_bid__pb2.MsgCloseBidResponse.SerializeToString), 'WithdrawLease': grpc.unary_unary_rpc_method_handler(servicer.WithdrawLease, request_deserializer=akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgWithdrawLease.FromString, response_serializer=akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgWithdrawLeaseResponse.SerializeToString), 'CreateLease': grpc.unary_unary_rpc_method_handler(servicer.CreateLease, request_deserializer=akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgCreateLease.FromString, response_serializer=akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgCreateLeaseResponse.SerializeToString), 'CloseLease': grpc.unary_unary_rpc_method_handler(servicer.CloseLease, request_deserializer=akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgCloseLease.FromString, response_serializer=akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgCloseLeaseResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('akash.market.v1beta2.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Msg(object):
    'Msg defines the market Msg service\n    '

    @staticmethod
    def CreateBid(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.market.v1beta2.Msg/CreateBid', akash_dot_market_dot_v1beta2_dot_bid__pb2.MsgCreateBid.SerializeToString, akash_dot_market_dot_v1beta2_dot_bid__pb2.MsgCreateBidResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseBid(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.market.v1beta2.Msg/CloseBid', akash_dot_market_dot_v1beta2_dot_bid__pb2.MsgCloseBid.SerializeToString, akash_dot_market_dot_v1beta2_dot_bid__pb2.MsgCloseBidResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WithdrawLease(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.market.v1beta2.Msg/WithdrawLease', akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgWithdrawLease.SerializeToString, akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgWithdrawLeaseResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateLease(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.market.v1beta2.Msg/CreateLease', akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgCreateLease.SerializeToString, akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgCreateLeaseResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseLease(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.market.v1beta2.Msg/CloseLease', akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgCloseLease.SerializeToString, akash_dot_market_dot_v1beta2_dot_lease__pb2.MsgCloseLeaseResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

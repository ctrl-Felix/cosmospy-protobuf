
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....akash.cert.v1beta2 import query_pb2 as akash_dot_cert_dot_v1beta2_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Certificates = channel.unary_unary('/akash.cert.v1beta2.Query/Certificates', request_serializer=akash_dot_cert_dot_v1beta2_dot_query__pb2.QueryCertificatesRequest.SerializeToString, response_deserializer=akash_dot_cert_dot_v1beta2_dot_query__pb2.QueryCertificatesResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service\n    '

    def Certificates(self, request, context):
        'Certificates queries certificates\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Certificates': grpc.unary_unary_rpc_method_handler(servicer.Certificates, request_deserializer=akash_dot_cert_dot_v1beta2_dot_query__pb2.QueryCertificatesRequest.FromString, response_serializer=akash_dot_cert_dot_v1beta2_dot_query__pb2.QueryCertificatesResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('akash.cert.v1beta2.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service\n    '

    @staticmethod
    def Certificates(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/akash.cert.v1beta2.Query/Certificates', akash_dot_cert_dot_v1beta2_dot_query__pb2.QueryCertificatesRequest.SerializeToString, akash_dot_cert_dot_v1beta2_dot_query__pb2.QueryCertificatesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

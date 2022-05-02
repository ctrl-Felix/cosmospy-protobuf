import grpc
import cosmospy_protobuf.cosmos.bank.v1beta1.query_pb2_grpc as query_pb2_grpc
import cosmospy_protobuf.cosmos.bank.v1beta1.query_pb2 as query_pb2
host = "osmosis.strange.love"
port = "9090"

c = grpc.insecure_channel('{}:{}'.format(host, port))
stub = query_pb2_grpc.QueryStub(c)


r = stub.AllBalances(query_pb2.QueryAllBalancesRequest(address="osmo15hzhcvgs2ljfng6unghvr5l32prwqdyq4aguxn"))
print(r.balances)
import cosmospy_protobuf.cosmos.staking.v1beta1.query_pb2 as query_pb2
import cosmospy_protobuf.cosmos.staking.v1beta1.query_pb2_grpc as query_pb2_grpc
import grpc

host = "evmos.strange.love"
port = 9090


class Staking:
    def __init__(self, c: grpc.Channel = grpc.insecure_channel(f"{host}:{port}")):
        self.stub = query_pb2_grpc.QueryStub(c)
        self._assets = {}

    @property
    def bonded(self):
        """Return bonded and unbonded funds"""
        r = self.stub.Pool(query_pb2.QueryPoolRequest())
        return {
            'bonded': int(r.pool.bonded_tokens),
            'unbonded': int(r.pool.not_bonded_tokens)
        }


print(Staking().bonded)

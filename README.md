# Cosmos Protobuf
This repository compains the whole cosmos protobuf files compiled for python and ready to use with grpc. Please use the according .proto file as documentation for each python file.

## Installation

You can install this package directly from the repository by using:
```
python -m pip install git+https://github.com/ctrl-Felix/cosmospy-protobuf.git
```

## Usage

The following code snippet will query the balances for the address ``osmo15hzhcvgs2ljfng6unghvr5l32prwqdyq4aguxn``. The according query.proto file in the bank subdirectory contains the Request and the Response for this request. The details for the response are defined in ``QueryAllBalancesResponse``. It contains the balances and pagination attribute which can be accessed as shown in the example below.  

```python
import grpc
import cosmospy_protobuf.cosmos.bank.v1beta1.query_pb2_grpc as query_pb2_grpc
import cosmospy_protobuf.cosmos.bank.v1beta1.query_pb2 as query_pb2

host = "osmosis.strange.love"
port = "9090"

c = grpc.insecure_channel(f'{host}:{port}')
stub = query_pb2_grpc.QueryStub(c)

r = stub.AllBalances(query_pb2.QueryAllBalancesRequest(address="osmo15hzhcvgs2ljfng6unghvr5l32prwqdyq4aguxn"))
print(r.balances)

```

## Compile the Protobuf files

The files are compield using the ``grpc_tools.protoc`` command from the [grpcio-tools](https://pypi.org/project/grpcio-tools/) library.
To compile a .proto file use following command:
```
python -m grpc_tools.protoc -I <absolute path to project root> --python_out=. --grpc_python_out=. <absolute path to .proto file>
```

After compiling all the files with protoc you need to fix the imports by using [protoletariat](https://github.com/cpcloud/protoletariat)

Note:
* The --grpc_python_out=. is only needed when compiling a query.proto file as these define the actual grpc query
* To compile the whole project it is favorable to match all proto files by using `*.proto` instead of each individual file. You can also match the whole folders to compile multiple folders at the same time. Not that the folders might contain sub-folders.
# Cosmos Protobuf
This repository compains the whole cosmos protobuf files compiled for python and ready to use with grpc. Please use the according .proto file as documentation for each python file.

This is a build in progress and only a rudimentary state right now. However I hope this helps every python developer who struggles to use grpc and protobuf. To get the example below running clone this code and create a new file in the root of this repository.

## Usage

The following code snippet will query the balances for the address ``osmo15hzhcvgs2ljfng6unghvr5l32prwqdyq4aguxn``. The according query.proto file in the bank subdirectory contains the Request and the Response for this request. This is also the place where you can see that you will get two values. First the balances which we will print below as well as the pagination which could then be accessed through ``r.pagination`` 
```python
import grpc
import cosmos.bank.v1beta1.query_pb2_grpc as query_pb2_grpc
import cosmos.bank.v1beta1.query_pb2 as query_pb2
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
Note:
* The --grpc_python_out=. is only needed when compiling a query.proto file as these define the actual grpc query
* To compile the whole project it is favorable to match all proto files by using `*.proto` instead of each individual file. You can also match the whole folders to compile multiple folders at the same time. Not that the folders might contain sub-folders.
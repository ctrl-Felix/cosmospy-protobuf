
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.params.v1beta1 import params_pb2 as cosmos_dot_params_dot_v1beta1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!cosmos/params/v1beta1/query.proto\x12\x15cosmos.params.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a"cosmos/params/v1beta1/params.proto"3\n\x12QueryParamsRequest\x12\x10\n\x08subspace\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t"N\n\x13QueryParamsResponse\x127\n\x05param\x18\x01 \x01(\x0b2".cosmos.params.v1beta1.ParamChangeB\x04\xc8\xde\x1f\x00"\x17\n\x15QuerySubspacesRequest"L\n\x16QuerySubspacesResponse\x122\n\tsubspaces\x18\x01 \x03(\x0b2\x1f.cosmos.params.v1beta1.Subspace"*\n\x08Subspace\x12\x10\n\x08subspace\x18\x01 \x01(\t\x12\x0c\n\x04keys\x18\x02 \x03(\t2\xa5\x02\n\x05Query\x12\x86\x01\n\x06Params\x12).cosmos.params.v1beta1.QueryParamsRequest\x1a*.cosmos.params.v1beta1.QueryParamsResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/params/v1beta1/params\x12\x92\x01\n\tSubspaces\x12,.cosmos.params.v1beta1.QuerySubspacesRequest\x1a-.cosmos.params.v1beta1.QuerySubspacesResponse"(\x82\xd3\xe4\x93\x02"\x12 /cosmos/params/v1beta1/subspacesB6Z4github.com/cosmos/cosmos-sdk/x/params/types/proposalb\x06proto3')
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
_QUERYSUBSPACESREQUEST = DESCRIPTOR.message_types_by_name['QuerySubspacesRequest']
_QUERYSUBSPACESRESPONSE = DESCRIPTOR.message_types_by_name['QuerySubspacesResponse']
_SUBSPACE = DESCRIPTOR.message_types_by_name['Subspace']
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSREQUEST, '__module__': 'cosmos.params.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsRequest)
QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSRESPONSE, '__module__': 'cosmos.params.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsResponse)
QuerySubspacesRequest = _reflection.GeneratedProtocolMessageType('QuerySubspacesRequest', (_message.Message,), {'DESCRIPTOR': _QUERYSUBSPACESREQUEST, '__module__': 'cosmos.params.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QuerySubspacesRequest)
QuerySubspacesResponse = _reflection.GeneratedProtocolMessageType('QuerySubspacesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYSUBSPACESRESPONSE, '__module__': 'cosmos.params.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QuerySubspacesResponse)
Subspace = _reflection.GeneratedProtocolMessageType('Subspace', (_message.Message,), {'DESCRIPTOR': _SUBSPACE, '__module__': 'cosmos.params.v1beta1.query_pb2'})
_sym_db.RegisterMessage(Subspace)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4github.com/cosmos/cosmos-sdk/x/params/types/proposal'
    _QUERYPARAMSRESPONSE.fields_by_name['param']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['param']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/params/v1beta1/params'
    _QUERY.methods_by_name['Subspaces']._options = None
    _QUERY.methods_by_name['Subspaces']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /cosmos/params/v1beta1/subspaces'
    _QUERYPARAMSREQUEST._serialized_start = 148
    _QUERYPARAMSREQUEST._serialized_end = 199
    _QUERYPARAMSRESPONSE._serialized_start = 201
    _QUERYPARAMSRESPONSE._serialized_end = 279
    _QUERYSUBSPACESREQUEST._serialized_start = 281
    _QUERYSUBSPACESREQUEST._serialized_end = 304
    _QUERYSUBSPACESRESPONSE._serialized_start = 306
    _QUERYSUBSPACESRESPONSE._serialized_end = 382
    _SUBSPACE._serialized_start = 384
    _SUBSPACE._serialized_end = 426
    _QUERY._serialized_start = 429
    _QUERY._serialized_end = 722

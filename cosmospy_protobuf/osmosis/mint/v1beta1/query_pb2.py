
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....osmosis.mint.v1beta1 import mint_pb2 as osmosis_dot_mint_dot_v1beta1_dot_mint__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n osmosis/mint/v1beta1/query.proto\x12\x14osmosis.mint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fosmosis/mint/v1beta1/mint.proto"\x14\n\x12QueryParamsRequest"I\n\x13QueryParamsResponse\x122\n\x06params\x18\x01 \x01(\x0b2\x1c.osmosis.mint.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"\x1d\n\x1bQueryEpochProvisionsRequest"h\n\x1cQueryEpochProvisionsResponse\x12H\n\x10epoch_provisions\x18\x01 \x01(\x0cB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x002\xb8\x02\n\x05Query\x12\x83\x01\n\x06Params\x12(.osmosis.mint.v1beta1.QueryParamsRequest\x1a).osmosis.mint.v1beta1.QueryParamsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/osmosis/mint/v1beta1/params\x12\xa8\x01\n\x0fEpochProvisions\x121.osmosis.mint.v1beta1.QueryEpochProvisionsRequest\x1a2.osmosis.mint.v1beta1.QueryEpochProvisionsResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/mint/v1beta1/epoch_provisionsB1Z/github.com/osmosis-labs/osmosis/v7/x/mint/typesb\x06proto3')
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
_QUERYEPOCHPROVISIONSREQUEST = DESCRIPTOR.message_types_by_name['QueryEpochProvisionsRequest']
_QUERYEPOCHPROVISIONSRESPONSE = DESCRIPTOR.message_types_by_name['QueryEpochProvisionsResponse']
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSREQUEST, '__module__': 'osmosis.mint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsRequest)
QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSRESPONSE, '__module__': 'osmosis.mint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsResponse)
QueryEpochProvisionsRequest = _reflection.GeneratedProtocolMessageType('QueryEpochProvisionsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYEPOCHPROVISIONSREQUEST, '__module__': 'osmosis.mint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryEpochProvisionsRequest)
QueryEpochProvisionsResponse = _reflection.GeneratedProtocolMessageType('QueryEpochProvisionsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYEPOCHPROVISIONSRESPONSE, '__module__': 'osmosis.mint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryEpochProvisionsResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z/github.com/osmosis-labs/osmosis/v7/x/mint/types'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYEPOCHPROVISIONSRESPONSE.fields_by_name['epoch_provisions']._options = None
    _QUERYEPOCHPROVISIONSRESPONSE.fields_by_name['epoch_provisions']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/osmosis/mint/v1beta1/params'
    _QUERY.methods_by_name['EpochProvisions']._options = None
    _QUERY.methods_by_name['EpochProvisions']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/mint/v1beta1/epoch_provisions'
    _QUERYPARAMSREQUEST._serialized_start = 143
    _QUERYPARAMSREQUEST._serialized_end = 163
    _QUERYPARAMSRESPONSE._serialized_start = 165
    _QUERYPARAMSRESPONSE._serialized_end = 238
    _QUERYEPOCHPROVISIONSREQUEST._serialized_start = 240
    _QUERYEPOCHPROVISIONSREQUEST._serialized_end = 269
    _QUERYEPOCHPROVISIONSRESPONSE._serialized_start = 271
    _QUERYEPOCHPROVISIONSRESPONSE._serialized_end = 375
    _QUERY._serialized_start = 378
    _QUERY._serialized_end = 690

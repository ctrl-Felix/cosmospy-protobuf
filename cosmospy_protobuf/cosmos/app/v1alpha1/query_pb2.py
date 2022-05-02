
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.app.v1alpha1 import config_pb2 as cosmos_dot_app_dot_v1alpha1_dot_config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/app/v1alpha1/query.proto\x12\x13cosmos.app.v1alpha1\x1a cosmos/app/v1alpha1/config.proto"\x14\n\x12QueryConfigRequest"B\n\x13QueryConfigResponse\x12+\n\x06config\x18\x01 \x01(\x0b2\x1b.cosmos.app.v1alpha1.Config2f\n\x05Query\x12]\n\x06Config\x12\'.cosmos.app.v1alpha1.QueryConfigRequest\x1a(.cosmos.app.v1alpha1.QueryConfigResponse"\x00b\x06proto3')
_QUERYCONFIGREQUEST = DESCRIPTOR.message_types_by_name['QueryConfigRequest']
_QUERYCONFIGRESPONSE = DESCRIPTOR.message_types_by_name['QueryConfigResponse']
QueryConfigRequest = _reflection.GeneratedProtocolMessageType('QueryConfigRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCONFIGREQUEST, '__module__': 'cosmos.app.v1alpha1.query_pb2'})
_sym_db.RegisterMessage(QueryConfigRequest)
QueryConfigResponse = _reflection.GeneratedProtocolMessageType('QueryConfigResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCONFIGRESPONSE, '__module__': 'cosmos.app.v1alpha1.query_pb2'})
_sym_db.RegisterMessage(QueryConfigResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _QUERYCONFIGREQUEST._serialized_start = 90
    _QUERYCONFIGREQUEST._serialized_end = 110
    _QUERYCONFIGRESPONSE._serialized_start = 112
    _QUERYCONFIGRESPONSE._serialized_end = 178
    _QUERY._serialized_start = 180
    _QUERY._serialized_end = 282

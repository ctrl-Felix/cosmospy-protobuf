
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....akash.provider.v1beta2 import provider_pb2 as akash_dot_provider_dot_v1beta2_dot_provider__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"akash/provider/v1beta2/query.proto\x12\x16akash.provider.v1beta2\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a%akash/provider/v1beta2/provider.proto"S\n\x15QueryProvidersRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x9d\x01\n\x16QueryProvidersResponse\x12F\n\tproviders\x18\x01 \x03(\x0b2 .akash.provider.v1beta2.ProviderB\x11\xc8\xde\x1f\x00\xaa\xdf\x1f\tProviders\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"%\n\x14QueryProviderRequest\x12\r\n\x05owner\x18\x01 \x01(\t"Q\n\x15QueryProviderResponse\x128\n\x08provider\x18\x01 \x01(\x0b2 .akash.provider.v1beta2.ProviderB\x04\xc8\xde\x1f\x002\xbc\x02\n\x05Query\x12\x95\x01\n\tProviders\x12-.akash.provider.v1beta2.QueryProvidersRequest\x1a..akash.provider.v1beta2.QueryProvidersResponse")\x82\xd3\xe4\x93\x02#\x12!/akash/provider/v1beta2/providers\x12\x9a\x01\n\x08Provider\x12,.akash.provider.v1beta2.QueryProviderRequest\x1a-.akash.provider.v1beta2.QueryProviderResponse"1\x82\xd3\xe4\x93\x02+\x12)/akash/provider/v1beta2/providers/{owner}B2Z0github.com/ovrclk/akash/x/provider/types/v1beta2b\x06proto3')
_QUERYPROVIDERSREQUEST = DESCRIPTOR.message_types_by_name['QueryProvidersRequest']
_QUERYPROVIDERSRESPONSE = DESCRIPTOR.message_types_by_name['QueryProvidersResponse']
_QUERYPROVIDERREQUEST = DESCRIPTOR.message_types_by_name['QueryProviderRequest']
_QUERYPROVIDERRESPONSE = DESCRIPTOR.message_types_by_name['QueryProviderResponse']
QueryProvidersRequest = _reflection.GeneratedProtocolMessageType('QueryProvidersRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPROVIDERSREQUEST, '__module__': 'akash.provider.v1beta2.query_pb2'})
_sym_db.RegisterMessage(QueryProvidersRequest)
QueryProvidersResponse = _reflection.GeneratedProtocolMessageType('QueryProvidersResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPROVIDERSRESPONSE, '__module__': 'akash.provider.v1beta2.query_pb2'})
_sym_db.RegisterMessage(QueryProvidersResponse)
QueryProviderRequest = _reflection.GeneratedProtocolMessageType('QueryProviderRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPROVIDERREQUEST, '__module__': 'akash.provider.v1beta2.query_pb2'})
_sym_db.RegisterMessage(QueryProviderRequest)
QueryProviderResponse = _reflection.GeneratedProtocolMessageType('QueryProviderResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPROVIDERRESPONSE, '__module__': 'akash.provider.v1beta2.query_pb2'})
_sym_db.RegisterMessage(QueryProviderResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/ovrclk/akash/x/provider/types/v1beta2'
    _QUERYPROVIDERSRESPONSE.fields_by_name['providers']._options = None
    _QUERYPROVIDERSRESPONSE.fields_by_name['providers']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\tProviders'
    _QUERYPROVIDERRESPONSE.fields_by_name['provider']._options = None
    _QUERYPROVIDERRESPONSE.fields_by_name['provider']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Providers']._options = None
    _QUERY.methods_by_name['Providers']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/akash/provider/v1beta2/providers'
    _QUERY.methods_by_name['Provider']._options = None
    _QUERY.methods_by_name['Provider']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/akash/provider/v1beta2/providers/{owner}'
    _QUERYPROVIDERSREQUEST._serialized_start = 197
    _QUERYPROVIDERSREQUEST._serialized_end = 280
    _QUERYPROVIDERSRESPONSE._serialized_start = 283
    _QUERYPROVIDERSRESPONSE._serialized_end = 440
    _QUERYPROVIDERREQUEST._serialized_start = 442
    _QUERYPROVIDERREQUEST._serialized_end = 479
    _QUERYPROVIDERRESPONSE._serialized_start = 481
    _QUERYPROVIDERRESPONSE._serialized_end = 562
    _QUERY._serialized_start = 565
    _QUERY._serialized_end = 881

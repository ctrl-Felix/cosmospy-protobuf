
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....cosmos.authz.v1beta1 import authz_pb2 as cosmos_dot_authz_dot_v1beta1_dot_authz__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/authz/v1beta1/query.proto\x12\x14cosmos.authz.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a cosmos/authz/v1beta1/authz.proto\x1a\x19cosmos_proto/cosmos.proto"\xbc\x01\n\x12QueryGrantsRequest\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x14\n\x0cmsg_type_url\x18\x03 \x01(\t\x12:\n\npagination\x18\x04 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x7f\n\x13QueryGrantsResponse\x12+\n\x06grants\x18\x01 \x03(\x0b2\x1b.cosmos.authz.v1beta1.Grant\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x82\x01\n\x19QueryGranterGrantsRequest\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x93\x01\n\x1aQueryGranterGrantsResponse\x128\n\x06grants\x18\x01 \x03(\x0b2(.cosmos.authz.v1beta1.GrantAuthorization\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x82\x01\n\x19QueryGranteeGrantsRequest\x12)\n\x07grantee\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x93\x01\n\x1aQueryGranteeGrantsResponse\x128\n\x06grants\x18\x01 \x03(\x0b2(.cosmos.authz.v1beta1.GrantAuthorization\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse2\xe7\x03\n\x05Query\x12\x83\x01\n\x06Grants\x12(.cosmos.authz.v1beta1.QueryGrantsRequest\x1a).cosmos.authz.v1beta1.QueryGrantsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/cosmos/authz/v1beta1/grants\x12\xaa\x01\n\rGranterGrants\x12/.cosmos.authz.v1beta1.QueryGranterGrantsRequest\x1a0.cosmos.authz.v1beta1.QueryGranterGrantsResponse"6\x82\xd3\xe4\x93\x020\x12./cosmos/authz/v1beta1/grants/granter/{granter}\x12\xaa\x01\n\rGranteeGrants\x12/.cosmos.authz.v1beta1.QueryGranteeGrantsRequest\x1a0.cosmos.authz.v1beta1.QueryGranteeGrantsResponse"6\x82\xd3\xe4\x93\x020\x12./cosmos/authz/v1beta1/grants/grantee/{grantee}B&Z$github.com/cosmos/cosmos-sdk/x/authzb\x06proto3')
_QUERYGRANTSREQUEST = DESCRIPTOR.message_types_by_name['QueryGrantsRequest']
_QUERYGRANTSRESPONSE = DESCRIPTOR.message_types_by_name['QueryGrantsResponse']
_QUERYGRANTERGRANTSREQUEST = DESCRIPTOR.message_types_by_name['QueryGranterGrantsRequest']
_QUERYGRANTERGRANTSRESPONSE = DESCRIPTOR.message_types_by_name['QueryGranterGrantsResponse']
_QUERYGRANTEEGRANTSREQUEST = DESCRIPTOR.message_types_by_name['QueryGranteeGrantsRequest']
_QUERYGRANTEEGRANTSRESPONSE = DESCRIPTOR.message_types_by_name['QueryGranteeGrantsResponse']
QueryGrantsRequest = _reflection.GeneratedProtocolMessageType('QueryGrantsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYGRANTSREQUEST, '__module__': 'cosmos.authz.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryGrantsRequest)
QueryGrantsResponse = _reflection.GeneratedProtocolMessageType('QueryGrantsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYGRANTSRESPONSE, '__module__': 'cosmos.authz.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryGrantsResponse)
QueryGranterGrantsRequest = _reflection.GeneratedProtocolMessageType('QueryGranterGrantsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYGRANTERGRANTSREQUEST, '__module__': 'cosmos.authz.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryGranterGrantsRequest)
QueryGranterGrantsResponse = _reflection.GeneratedProtocolMessageType('QueryGranterGrantsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYGRANTERGRANTSRESPONSE, '__module__': 'cosmos.authz.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryGranterGrantsResponse)
QueryGranteeGrantsRequest = _reflection.GeneratedProtocolMessageType('QueryGranteeGrantsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYGRANTEEGRANTSREQUEST, '__module__': 'cosmos.authz.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryGranteeGrantsRequest)
QueryGranteeGrantsResponse = _reflection.GeneratedProtocolMessageType('QueryGranteeGrantsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYGRANTEEGRANTSRESPONSE, '__module__': 'cosmos.authz.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryGranteeGrantsResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/authz'
    _QUERYGRANTSREQUEST.fields_by_name['granter']._options = None
    _QUERYGRANTSREQUEST.fields_by_name['granter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYGRANTSREQUEST.fields_by_name['grantee']._options = None
    _QUERYGRANTSREQUEST.fields_by_name['grantee']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYGRANTERGRANTSREQUEST.fields_by_name['granter']._options = None
    _QUERYGRANTERGRANTSREQUEST.fields_by_name['granter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYGRANTEEGRANTSREQUEST.fields_by_name['grantee']._options = None
    _QUERYGRANTEEGRANTSREQUEST.fields_by_name['grantee']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERY.methods_by_name['Grants']._options = None
    _QUERY.methods_by_name['Grants']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/cosmos/authz/v1beta1/grants'
    _QUERY.methods_by_name['GranterGrants']._options = None
    _QUERY.methods_by_name['GranterGrants']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./cosmos/authz/v1beta1/grants/granter/{granter}'
    _QUERY.methods_by_name['GranteeGrants']._options = None
    _QUERY.methods_by_name['GranteeGrants']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./cosmos/authz/v1beta1/grants/grantee/{grantee}'
    _QUERYGRANTSREQUEST._serialized_start = 194
    _QUERYGRANTSREQUEST._serialized_end = 382
    _QUERYGRANTSRESPONSE._serialized_start = 384
    _QUERYGRANTSRESPONSE._serialized_end = 511
    _QUERYGRANTERGRANTSREQUEST._serialized_start = 514
    _QUERYGRANTERGRANTSREQUEST._serialized_end = 644
    _QUERYGRANTERGRANTSRESPONSE._serialized_start = 647
    _QUERYGRANTERGRANTSRESPONSE._serialized_end = 794
    _QUERYGRANTEEGRANTSREQUEST._serialized_start = 797
    _QUERYGRANTEEGRANTSREQUEST._serialized_end = 927
    _QUERYGRANTEEGRANTSRESPONSE._serialized_start = 930
    _QUERYGRANTEEGRANTSRESPONSE._serialized_end = 1077
    _QUERY._serialized_start = 1080
    _QUERY._serialized_end = 1567

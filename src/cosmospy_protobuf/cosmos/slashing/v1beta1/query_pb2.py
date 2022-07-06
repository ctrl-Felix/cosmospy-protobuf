
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.slashing.v1beta1 import slashing_pb2 as cosmos_dot_slashing_dot_v1beta1_dot_slashing__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#cosmos/slashing/v1beta1/query.proto\x12\x17cosmos.slashing.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a&cosmos/slashing/v1beta1/slashing.proto\x1a\x19cosmos_proto/cosmos.proto"\x14\n\x12QueryParamsRequest"L\n\x13QueryParamsResponse\x125\n\x06params\x18\x01 \x01(\x0b2\x1f.cosmos.slashing.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"I\n\x17QuerySigningInfoRequest\x12.\n\x0ccons_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString"i\n\x18QuerySigningInfoResponse\x12M\n\x10val_signing_info\x18\x01 \x01(\x0b2-.cosmos.slashing.v1beta1.ValidatorSigningInfoB\x04\xc8\xde\x1f\x00"V\n\x18QuerySigningInfosRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x9b\x01\n\x19QuerySigningInfosResponse\x12A\n\x04info\x18\x01 \x03(\x0b2-.cosmos.slashing.v1beta1.ValidatorSigningInfoB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse2\xf2\x03\n\x05Query\x12\x8c\x01\n\x06Params\x12+.cosmos.slashing.v1beta1.QueryParamsRequest\x1a,.cosmos.slashing.v1beta1.QueryParamsResponse"\'\x82\xd3\xe4\x93\x02!\x12\x1f/cosmos/slashing/v1beta1/params\x12\xb1\x01\n\x0bSigningInfo\x120.cosmos.slashing.v1beta1.QuerySigningInfoRequest\x1a1.cosmos.slashing.v1beta1.QuerySigningInfoResponse"=\x82\xd3\xe4\x93\x027\x125/cosmos/slashing/v1beta1/signing_infos/{cons_address}\x12\xa5\x01\n\x0cSigningInfos\x121.cosmos.slashing.v1beta1.QuerySigningInfosRequest\x1a2.cosmos.slashing.v1beta1.QuerySigningInfosResponse".\x82\xd3\xe4\x93\x02(\x12&/cosmos/slashing/v1beta1/signing_infosB/Z-github.com/cosmos/cosmos-sdk/x/slashing/typesb\x06proto3')
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
_QUERYSIGNINGINFOREQUEST = DESCRIPTOR.message_types_by_name['QuerySigningInfoRequest']
_QUERYSIGNINGINFORESPONSE = DESCRIPTOR.message_types_by_name['QuerySigningInfoResponse']
_QUERYSIGNINGINFOSREQUEST = DESCRIPTOR.message_types_by_name['QuerySigningInfosRequest']
_QUERYSIGNINGINFOSRESPONSE = DESCRIPTOR.message_types_by_name['QuerySigningInfosResponse']
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSREQUEST, '__module__': 'cosmos.slashing.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsRequest)
QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSRESPONSE, '__module__': 'cosmos.slashing.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsResponse)
QuerySigningInfoRequest = _reflection.GeneratedProtocolMessageType('QuerySigningInfoRequest', (_message.Message,), {'DESCRIPTOR': _QUERYSIGNINGINFOREQUEST, '__module__': 'cosmos.slashing.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QuerySigningInfoRequest)
QuerySigningInfoResponse = _reflection.GeneratedProtocolMessageType('QuerySigningInfoResponse', (_message.Message,), {'DESCRIPTOR': _QUERYSIGNINGINFORESPONSE, '__module__': 'cosmos.slashing.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QuerySigningInfoResponse)
QuerySigningInfosRequest = _reflection.GeneratedProtocolMessageType('QuerySigningInfosRequest', (_message.Message,), {'DESCRIPTOR': _QUERYSIGNINGINFOSREQUEST, '__module__': 'cosmos.slashing.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QuerySigningInfosRequest)
QuerySigningInfosResponse = _reflection.GeneratedProtocolMessageType('QuerySigningInfosResponse', (_message.Message,), {'DESCRIPTOR': _QUERYSIGNINGINFOSRESPONSE, '__module__': 'cosmos.slashing.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QuerySigningInfosResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/slashing/types'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYSIGNINGINFOREQUEST.fields_by_name['cons_address']._options = None
    _QUERYSIGNINGINFOREQUEST.fields_by_name['cons_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYSIGNINGINFORESPONSE.fields_by_name['val_signing_info']._options = None
    _QUERYSIGNINGINFORESPONSE.fields_by_name['val_signing_info']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYSIGNINGINFOSRESPONSE.fields_by_name['info']._options = None
    _QUERYSIGNINGINFOSRESPONSE.fields_by_name['info']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/cosmos/slashing/v1beta1/params'
    _QUERY.methods_by_name['SigningInfo']._options = None
    _QUERY.methods_by_name['SigningInfo']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/cosmos/slashing/v1beta1/signing_infos/{cons_address}'
    _QUERY.methods_by_name['SigningInfos']._options = None
    _QUERY.methods_by_name['SigningInfos']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/cosmos/slashing/v1beta1/signing_infos'
    _QUERYPARAMSREQUEST._serialized_start = 227
    _QUERYPARAMSREQUEST._serialized_end = 247
    _QUERYPARAMSRESPONSE._serialized_start = 249
    _QUERYPARAMSRESPONSE._serialized_end = 325
    _QUERYSIGNINGINFOREQUEST._serialized_start = 327
    _QUERYSIGNINGINFOREQUEST._serialized_end = 400
    _QUERYSIGNINGINFORESPONSE._serialized_start = 402
    _QUERYSIGNINGINFORESPONSE._serialized_end = 507
    _QUERYSIGNINGINFOSREQUEST._serialized_start = 509
    _QUERYSIGNINGINFOSREQUEST._serialized_end = 595
    _QUERYSIGNINGINFOSRESPONSE._serialized_start = 598
    _QUERYSIGNINGINFOSRESPONSE._serialized_end = 753
    _QUERY._serialized_start = 756
    _QUERY._serialized_end = 1254

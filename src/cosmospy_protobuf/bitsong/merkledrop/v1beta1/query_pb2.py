
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....bitsong.merkledrop.v1beta1 import merkledrop_pb2 as bitsong_dot_merkledrop_dot_v1beta1_dot_merkledrop__pb2
from ....bitsong.merkledrop.v1beta1 import params_pb2 as bitsong_dot_merkledrop_dot_v1beta1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&bitsong/merkledrop/v1beta1/query.proto\x12\x1abitsong.merkledrop.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a+bitsong/merkledrop/v1beta1/merkledrop.proto\x1a\'bitsong/merkledrop/v1beta1/params.proto"$\n\x16QueryMerkledropRequest\x12\n\n\x02id\x18\x01 \x01(\x04"[\n\x17QueryMerkledropResponse\x12@\n\nmerkledrop\x18\x01 \x01(\x0b2&.bitsong.merkledrop.v1beta1.MerkledropB\x04\xc8\xde\x1f\x00"5\n\x18QueryIndexClaimedRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\r\n\x05index\x18\x02 \x01(\x04"F\n\x19QueryIndexClaimedResponse\x12)\n\nis_claimed\x18\x01 \x01(\x08B\x15\xf2\xde\x1f\x11yaml:"is_claimed""\x14\n\x12QueryParamsRequest"O\n\x13QueryParamsResponse\x128\n\x06params\x18\x01 \x01(\x0b2".bitsong.merkledrop.v1beta1.ParamsB\x04\xc8\xde\x1f\x002\x97\x04\n\x05Query\x12\xab\x01\n\nMerkledrop\x122.bitsong.merkledrop.v1beta1.QueryMerkledropRequest\x1a3.bitsong.merkledrop.v1beta1.QueryMerkledropResponse"4\x82\xd3\xe4\x93\x02.\x12,/bitsong/merkledrop/v1beta1/markledrops/{id}\x12\xc7\x01\n\x0cIndexClaimed\x124.bitsong.merkledrop.v1beta1.QueryIndexClaimedRequest\x1a5.bitsong.merkledrop.v1beta1.QueryIndexClaimedResponse"J\x82\xd3\xe4\x93\x02D\x12B/bitsong/merkledrop/v1beta1/markledrops/{id}/index_claimed/{index}\x12\x95\x01\n\x06Params\x12..bitsong.merkledrop.v1beta1.QueryParamsRequest\x1a/.bitsong.merkledrop.v1beta1.QueryParamsResponse"*\x82\xd3\xe4\x93\x02$\x12"/bitsong/merkledrop/v1beta1/paramsB>Z8github.com/bitsongofficial/go-bitsong/x/merkledrop/types\xc8\xe1\x1e\x00b\x06proto3')
_QUERYMERKLEDROPREQUEST = DESCRIPTOR.message_types_by_name['QueryMerkledropRequest']
_QUERYMERKLEDROPRESPONSE = DESCRIPTOR.message_types_by_name['QueryMerkledropResponse']
_QUERYINDEXCLAIMEDREQUEST = DESCRIPTOR.message_types_by_name['QueryIndexClaimedRequest']
_QUERYINDEXCLAIMEDRESPONSE = DESCRIPTOR.message_types_by_name['QueryIndexClaimedResponse']
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
QueryMerkledropRequest = _reflection.GeneratedProtocolMessageType('QueryMerkledropRequest', (_message.Message,), {'DESCRIPTOR': _QUERYMERKLEDROPREQUEST, '__module__': 'bitsong.merkledrop.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryMerkledropRequest)
QueryMerkledropResponse = _reflection.GeneratedProtocolMessageType('QueryMerkledropResponse', (_message.Message,), {'DESCRIPTOR': _QUERYMERKLEDROPRESPONSE, '__module__': 'bitsong.merkledrop.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryMerkledropResponse)
QueryIndexClaimedRequest = _reflection.GeneratedProtocolMessageType('QueryIndexClaimedRequest', (_message.Message,), {'DESCRIPTOR': _QUERYINDEXCLAIMEDREQUEST, '__module__': 'bitsong.merkledrop.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryIndexClaimedRequest)
QueryIndexClaimedResponse = _reflection.GeneratedProtocolMessageType('QueryIndexClaimedResponse', (_message.Message,), {'DESCRIPTOR': _QUERYINDEXCLAIMEDRESPONSE, '__module__': 'bitsong.merkledrop.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryIndexClaimedResponse)
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSREQUEST, '__module__': 'bitsong.merkledrop.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsRequest)
QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSRESPONSE, '__module__': 'bitsong.merkledrop.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/bitsongofficial/go-bitsong/x/merkledrop/types\xc8\xe1\x1e\x00'
    _QUERYMERKLEDROPRESPONSE.fields_by_name['merkledrop']._options = None
    _QUERYMERKLEDROPRESPONSE.fields_by_name['merkledrop']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYINDEXCLAIMEDRESPONSE.fields_by_name['is_claimed']._options = None
    _QUERYINDEXCLAIMEDRESPONSE.fields_by_name['is_claimed']._serialized_options = b'\xf2\xde\x1f\x11yaml:"is_claimed"'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Merkledrop']._options = None
    _QUERY.methods_by_name['Merkledrop']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/bitsong/merkledrop/v1beta1/markledrops/{id}'
    _QUERY.methods_by_name['IndexClaimed']._options = None
    _QUERY.methods_by_name['IndexClaimed']._serialized_options = b'\x82\xd3\xe4\x93\x02D\x12B/bitsong/merkledrop/v1beta1/markledrops/{id}/index_claimed/{index}'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/bitsong/merkledrop/v1beta1/params'
    _QUERYMERKLEDROPREQUEST._serialized_start = 240
    _QUERYMERKLEDROPREQUEST._serialized_end = 276
    _QUERYMERKLEDROPRESPONSE._serialized_start = 278
    _QUERYMERKLEDROPRESPONSE._serialized_end = 369
    _QUERYINDEXCLAIMEDREQUEST._serialized_start = 371
    _QUERYINDEXCLAIMEDREQUEST._serialized_end = 424
    _QUERYINDEXCLAIMEDRESPONSE._serialized_start = 426
    _QUERYINDEXCLAIMEDRESPONSE._serialized_end = 496
    _QUERYPARAMSREQUEST._serialized_start = 498
    _QUERYPARAMSREQUEST._serialized_end = 518
    _QUERYPARAMSRESPONSE._serialized_start = 520
    _QUERYPARAMSRESPONSE._serialized_end = 599
    _QUERY._serialized_start = 602
    _QUERY._serialized_end = 1137

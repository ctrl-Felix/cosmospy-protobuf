
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos.authz.v1beta1 import authz_pb2 as cosmos_dot_authz_dot_v1beta1_dot_authz__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dcosmos/authz/v1beta1/tx.proto\x12\x14cosmos.authz.v1beta1\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a cosmos/authz/v1beta1/authz.proto\x1a\x17cosmos/msg/v1/msg.proto"\xa0\x01\n\x08MsgGrant\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x120\n\x05grant\x18\x03 \x01(\x0b2\x1b.cosmos.authz.v1beta1.GrantB\x04\xc8\xde\x1f\x00:\x0c\x82\xe7\xb0*\x07granter""\n\x0fMsgExecResponse\x12\x0f\n\x07results\x18\x01 \x03(\x0c"\x88\x01\n\x07MsgExec\x12)\n\x07grantee\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12D\n\x04msgs\x18\x02 \x03(\x0b2\x14.google.protobuf.AnyB \xca\xb4-\x1csdk.Msg, authz.Authorization:\x0c\x82\xe7\xb0*\x07grantee"\x12\n\x10MsgGrantResponse"\x85\x01\n\tMsgRevoke\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x14\n\x0cmsg_type_url\x18\x03 \x01(\t:\x0c\x82\xe7\xb0*\x07granter"\x13\n\x11MsgRevokeResponse2\xf8\x01\n\x03Msg\x12O\n\x05Grant\x12\x1e.cosmos.authz.v1beta1.MsgGrant\x1a&.cosmos.authz.v1beta1.MsgGrantResponse\x12L\n\x04Exec\x12\x1d.cosmos.authz.v1beta1.MsgExec\x1a%.cosmos.authz.v1beta1.MsgExecResponse\x12R\n\x06Revoke\x12\x1f.cosmos.authz.v1beta1.MsgRevoke\x1a\'.cosmos.authz.v1beta1.MsgRevokeResponseB*Z$github.com/cosmos/cosmos-sdk/x/authz\xc8\xe1\x1e\x00b\x06proto3')
_MSGGRANT = DESCRIPTOR.message_types_by_name['MsgGrant']
_MSGEXECRESPONSE = DESCRIPTOR.message_types_by_name['MsgExecResponse']
_MSGEXEC = DESCRIPTOR.message_types_by_name['MsgExec']
_MSGGRANTRESPONSE = DESCRIPTOR.message_types_by_name['MsgGrantResponse']
_MSGREVOKE = DESCRIPTOR.message_types_by_name['MsgRevoke']
_MSGREVOKERESPONSE = DESCRIPTOR.message_types_by_name['MsgRevokeResponse']
MsgGrant = _reflection.GeneratedProtocolMessageType('MsgGrant', (_message.Message,), {'DESCRIPTOR': _MSGGRANT, '__module__': 'cosmos.authz.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgGrant)
MsgExecResponse = _reflection.GeneratedProtocolMessageType('MsgExecResponse', (_message.Message,), {'DESCRIPTOR': _MSGEXECRESPONSE, '__module__': 'cosmos.authz.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgExecResponse)
MsgExec = _reflection.GeneratedProtocolMessageType('MsgExec', (_message.Message,), {'DESCRIPTOR': _MSGEXEC, '__module__': 'cosmos.authz.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgExec)
MsgGrantResponse = _reflection.GeneratedProtocolMessageType('MsgGrantResponse', (_message.Message,), {'DESCRIPTOR': _MSGGRANTRESPONSE, '__module__': 'cosmos.authz.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgGrantResponse)
MsgRevoke = _reflection.GeneratedProtocolMessageType('MsgRevoke', (_message.Message,), {'DESCRIPTOR': _MSGREVOKE, '__module__': 'cosmos.authz.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgRevoke)
MsgRevokeResponse = _reflection.GeneratedProtocolMessageType('MsgRevokeResponse', (_message.Message,), {'DESCRIPTOR': _MSGREVOKERESPONSE, '__module__': 'cosmos.authz.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgRevokeResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/authz\xc8\xe1\x1e\x00'
    _MSGGRANT.fields_by_name['granter']._options = None
    _MSGGRANT.fields_by_name['granter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGGRANT.fields_by_name['grantee']._options = None
    _MSGGRANT.fields_by_name['grantee']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGGRANT.fields_by_name['grant']._options = None
    _MSGGRANT.fields_by_name['grant']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGGRANT._options = None
    _MSGGRANT._serialized_options = b'\x82\xe7\xb0*\x07granter'
    _MSGEXEC.fields_by_name['grantee']._options = None
    _MSGEXEC.fields_by_name['grantee']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGEXEC.fields_by_name['msgs']._options = None
    _MSGEXEC.fields_by_name['msgs']._serialized_options = b'\xca\xb4-\x1csdk.Msg, authz.Authorization'
    _MSGEXEC._options = None
    _MSGEXEC._serialized_options = b'\x82\xe7\xb0*\x07grantee'
    _MSGREVOKE.fields_by_name['granter']._options = None
    _MSGREVOKE.fields_by_name['granter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGREVOKE.fields_by_name['grantee']._options = None
    _MSGREVOKE.fields_by_name['grantee']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGREVOKE._options = None
    _MSGREVOKE._serialized_options = b'\x82\xe7\xb0*\x07granter'
    _MSGGRANT._serialized_start = 191
    _MSGGRANT._serialized_end = 351
    _MSGEXECRESPONSE._serialized_start = 353
    _MSGEXECRESPONSE._serialized_end = 387
    _MSGEXEC._serialized_start = 390
    _MSGEXEC._serialized_end = 526
    _MSGGRANTRESPONSE._serialized_start = 528
    _MSGGRANTRESPONSE._serialized_end = 546
    _MSGREVOKE._serialized_start = 549
    _MSGREVOKE._serialized_end = 682
    _MSGREVOKERESPONSE._serialized_start = 684
    _MSGREVOKERESPONSE._serialized_end = 703
    _MSG._serialized_start = 706
    _MSG._serialized_end = 954

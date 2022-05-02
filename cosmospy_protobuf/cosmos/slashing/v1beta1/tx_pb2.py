
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/slashing/v1beta1/tx.proto\x12\x17cosmos.slashing.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x17cosmos/msg/v1/msg.proto"e\n\tMsgUnjail\x12;\n\x0evalidator_addr\x18\x01 \x01(\tB#\xd2\xb4-\x14cosmos.AddressString\xea\xde\x1f\x07address:\x1b\x82\xe7\xb0*\x0evalidator_addr\x88\xa0\x1f\x00\x98\xa0\x1f\x01"\x13\n\x11MsgUnjailResponse2_\n\x03Msg\x12X\n\x06Unjail\x12".cosmos.slashing.v1beta1.MsgUnjail\x1a*.cosmos.slashing.v1beta1.MsgUnjailResponseB3Z-github.com/cosmos/cosmos-sdk/x/slashing/types\xa8\xe2\x1e\x01b\x06proto3')
_MSGUNJAIL = DESCRIPTOR.message_types_by_name['MsgUnjail']
_MSGUNJAILRESPONSE = DESCRIPTOR.message_types_by_name['MsgUnjailResponse']
MsgUnjail = _reflection.GeneratedProtocolMessageType('MsgUnjail', (_message.Message,), {'DESCRIPTOR': _MSGUNJAIL, '__module__': 'cosmos.slashing.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgUnjail)
MsgUnjailResponse = _reflection.GeneratedProtocolMessageType('MsgUnjailResponse', (_message.Message,), {'DESCRIPTOR': _MSGUNJAILRESPONSE, '__module__': 'cosmos.slashing.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgUnjailResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/slashing/types\xa8\xe2\x1e\x01'
    _MSGUNJAIL.fields_by_name['validator_addr']._options = None
    _MSGUNJAIL.fields_by_name['validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString\xea\xde\x1f\x07address'
    _MSGUNJAIL._options = None
    _MSGUNJAIL._serialized_options = b'\x82\xe7\xb0*\x0evalidator_addr\x88\xa0\x1f\x00\x98\xa0\x1f\x01'
    _MSGUNJAIL._serialized_start = 135
    _MSGUNJAIL._serialized_end = 236
    _MSGUNJAILRESPONSE._serialized_start = 238
    _MSGUNJAILRESPONSE._serialized_end = 257
    _MSG._serialized_start = 259
    _MSG._serialized_end = 354

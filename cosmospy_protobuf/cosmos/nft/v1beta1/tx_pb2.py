
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bcosmos/nft/v1beta1/tx.proto\x12\x12cosmos.nft.v1beta1\x1a\x17cosmos/msg/v1/msg.proto"V\n\x07MsgSend\x12\x10\n\x08class_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0e\n\x06sender\x18\x03 \x01(\t\x12\x10\n\x08receiver\x18\x04 \x01(\t:\x0b\x82\xe7\xb0*\x06sender"\x11\n\x0fMsgSendResponse2O\n\x03Msg\x12H\n\x04Send\x12\x1b.cosmos.nft.v1beta1.MsgSend\x1a#.cosmos.nft.v1beta1.MsgSendResponseB$Z"github.com/cosmos/cosmos-sdk/x/nftb\x06proto3')
_MSGSEND = DESCRIPTOR.message_types_by_name['MsgSend']
_MSGSENDRESPONSE = DESCRIPTOR.message_types_by_name['MsgSendResponse']
MsgSend = _reflection.GeneratedProtocolMessageType('MsgSend', (_message.Message,), {'DESCRIPTOR': _MSGSEND, '__module__': 'cosmos.nft.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgSend)
MsgSendResponse = _reflection.GeneratedProtocolMessageType('MsgSendResponse', (_message.Message,), {'DESCRIPTOR': _MSGSENDRESPONSE, '__module__': 'cosmos.nft.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgSendResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z"github.com/cosmos/cosmos-sdk/x/nft'
    _MSGSEND._options = None
    _MSGSEND._serialized_options = b'\x82\xe7\xb0*\x06sender'
    _MSGSEND._serialized_start = 76
    _MSGSEND._serialized_end = 162
    _MSGSENDRESPONSE._serialized_start = 164
    _MSGSENDRESPONSE._serialized_end = 181
    _MSG._serialized_start = 183
    _MSG._serialized_end = 262

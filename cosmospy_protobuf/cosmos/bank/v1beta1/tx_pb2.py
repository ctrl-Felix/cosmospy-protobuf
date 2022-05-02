
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ccosmos/bank/v1beta1/tx.proto\x12\x13cosmos.bank.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1ecosmos/bank/v1beta1/bank.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x17cosmos/msg/v1/msg.proto"\xdf\x01\n\x07MsgSend\x12.\n\x0cfrom_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12,\n\nto_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12[\n\x06amount\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x19\x82\xe7\xb0*\x0cfrom_address\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x11\n\x0fMsgSendResponse"\x85\x01\n\x0cMsgMultiSend\x120\n\x06inputs\x18\x01 \x03(\x0b2\x1a.cosmos.bank.v1beta1.InputB\x04\xc8\xde\x1f\x00\x122\n\x07outputs\x18\x02 \x03(\x0b2\x1b.cosmos.bank.v1beta1.OutputB\x04\xc8\xde\x1f\x00:\x0f\x82\xe7\xb0*\x06inputs\xe8\xa0\x1f\x00"\x16\n\x14MsgMultiSendResponse2\xac\x01\n\x03Msg\x12J\n\x04Send\x12\x1c.cosmos.bank.v1beta1.MsgSend\x1a$.cosmos.bank.v1beta1.MsgSendResponse\x12Y\n\tMultiSend\x12!.cosmos.bank.v1beta1.MsgMultiSend\x1a).cosmos.bank.v1beta1.MsgMultiSendResponseB+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3')
_MSGSEND = DESCRIPTOR.message_types_by_name['MsgSend']
_MSGSENDRESPONSE = DESCRIPTOR.message_types_by_name['MsgSendResponse']
_MSGMULTISEND = DESCRIPTOR.message_types_by_name['MsgMultiSend']
_MSGMULTISENDRESPONSE = DESCRIPTOR.message_types_by_name['MsgMultiSendResponse']
MsgSend = _reflection.GeneratedProtocolMessageType('MsgSend', (_message.Message,), {'DESCRIPTOR': _MSGSEND, '__module__': 'cosmos.bank.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgSend)
MsgSendResponse = _reflection.GeneratedProtocolMessageType('MsgSendResponse', (_message.Message,), {'DESCRIPTOR': _MSGSENDRESPONSE, '__module__': 'cosmos.bank.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgSendResponse)
MsgMultiSend = _reflection.GeneratedProtocolMessageType('MsgMultiSend', (_message.Message,), {'DESCRIPTOR': _MSGMULTISEND, '__module__': 'cosmos.bank.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgMultiSend)
MsgMultiSendResponse = _reflection.GeneratedProtocolMessageType('MsgMultiSendResponse', (_message.Message,), {'DESCRIPTOR': _MSGMULTISENDRESPONSE, '__module__': 'cosmos.bank.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgMultiSendResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
    _MSGSEND.fields_by_name['from_address']._options = None
    _MSGSEND.fields_by_name['from_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGSEND.fields_by_name['to_address']._options = None
    _MSGSEND.fields_by_name['to_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGSEND.fields_by_name['amount']._options = None
    _MSGSEND.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGSEND._options = None
    _MSGSEND._serialized_options = b'\x82\xe7\xb0*\x0cfrom_address\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGMULTISEND.fields_by_name['inputs']._options = None
    _MSGMULTISEND.fields_by_name['inputs']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGMULTISEND.fields_by_name['outputs']._options = None
    _MSGMULTISEND.fields_by_name['outputs']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGMULTISEND._options = None
    _MSGMULTISEND._serialized_options = b'\x82\xe7\xb0*\x06inputs\xe8\xa0\x1f\x00'
    _MSGSEND._serialized_start = 192
    _MSGSEND._serialized_end = 415
    _MSGSENDRESPONSE._serialized_start = 417
    _MSGSENDRESPONSE._serialized_end = 434
    _MSGMULTISEND._serialized_start = 437
    _MSGMULTISEND._serialized_end = 570
    _MSGMULTISENDRESPONSE._serialized_start = 572
    _MSGMULTISENDRESPONSE._serialized_end = 594
    _MSG._serialized_start = 597
    _MSG._serialized_end = 769

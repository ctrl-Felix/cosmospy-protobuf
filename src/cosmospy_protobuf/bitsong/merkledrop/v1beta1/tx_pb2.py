
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#bitsong/merkledrop/v1beta1/tx.proto\x12\x1abitsong.merkledrop.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xcb\x01\n\tMsgCreate\x12\r\n\x05owner\x18\x01 \x01(\t\x12+\n\x0bmerkle_root\x18\x02 \x01(\tB\x16\xf2\xde\x1f\x12yaml:"merkle_root"\x12\x14\n\x0cstart_height\x18\x03 \x01(\x03\x12\x12\n\nend_height\x18\x04 \x01(\x03\x12X\n\x04coin\x18\x05 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\xc8\xde\x1f\x00".\n\x11MsgCreateResponse\x12\r\n\x05owner\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04"\x90\x01\n\x08MsgClaim\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x15\n\rmerkledrop_id\x18\x02 \x01(\x04\x12\r\n\x05index\x18\x03 \x01(\x04\x12>\n\x06amount\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x0e\n\x06proofs\x18\x05 \x03(\t"m\n\x10MsgClaimResponse\x12\n\n\x02id\x18\x01 \x01(\x04\x12\r\n\x05index\x18\x02 \x01(\x04\x12>\n\x06amount\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x002\xc2\x01\n\x03Msg\x12^\n\x06Create\x12%.bitsong.merkledrop.v1beta1.MsgCreate\x1a-.bitsong.merkledrop.v1beta1.MsgCreateResponse\x12[\n\x05Claim\x12$.bitsong.merkledrop.v1beta1.MsgClaim\x1a,.bitsong.merkledrop.v1beta1.MsgClaimResponseB>Z8github.com/bitsongofficial/go-bitsong/x/merkledrop/types\xc8\xe1\x1e\x00b\x06proto3')
_MSGCREATE = DESCRIPTOR.message_types_by_name['MsgCreate']
_MSGCREATERESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateResponse']
_MSGCLAIM = DESCRIPTOR.message_types_by_name['MsgClaim']
_MSGCLAIMRESPONSE = DESCRIPTOR.message_types_by_name['MsgClaimResponse']
MsgCreate = _reflection.GeneratedProtocolMessageType('MsgCreate', (_message.Message,), {'DESCRIPTOR': _MSGCREATE, '__module__': 'bitsong.merkledrop.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreate)
MsgCreateResponse = _reflection.GeneratedProtocolMessageType('MsgCreateResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATERESPONSE, '__module__': 'bitsong.merkledrop.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateResponse)
MsgClaim = _reflection.GeneratedProtocolMessageType('MsgClaim', (_message.Message,), {'DESCRIPTOR': _MSGCLAIM, '__module__': 'bitsong.merkledrop.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgClaim)
MsgClaimResponse = _reflection.GeneratedProtocolMessageType('MsgClaimResponse', (_message.Message,), {'DESCRIPTOR': _MSGCLAIMRESPONSE, '__module__': 'bitsong.merkledrop.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgClaimResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/bitsongofficial/go-bitsong/x/merkledrop/types\xc8\xe1\x1e\x00'
    _MSGCREATE.fields_by_name['merkle_root']._options = None
    _MSGCREATE.fields_by_name['merkle_root']._serialized_options = b'\xf2\xde\x1f\x12yaml:"merkle_root"'
    _MSGCREATE.fields_by_name['coin']._options = None
    _MSGCREATE.fields_by_name['coin']._serialized_options = b"\xda\xde\x1f'github.com/cosmos/cosmos-sdk/types.Coin\xc8\xde\x1f\x00"
    _MSGCLAIM.fields_by_name['amount']._options = None
    _MSGCLAIM.fields_by_name['amount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _MSGCLAIMRESPONSE.fields_by_name['amount']._options = None
    _MSGCLAIMRESPONSE.fields_by_name['amount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _MSGCREATE._serialized_start = 155
    _MSGCREATE._serialized_end = 358
    _MSGCREATERESPONSE._serialized_start = 360
    _MSGCREATERESPONSE._serialized_end = 406
    _MSGCLAIM._serialized_start = 409
    _MSGCLAIM._serialized_end = 553
    _MSGCLAIMRESPONSE._serialized_start = 555
    _MSGCLAIMRESPONSE._serialized_end = 664
    _MSG._serialized_start = 667
    _MSG._serialized_end = 861

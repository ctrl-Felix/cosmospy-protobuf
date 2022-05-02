
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.vesting.v1beta1 import vesting_pb2 as cosmos_dot_vesting_dot_v1beta1_dot_vesting__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/vesting/v1beta1/tx.proto\x12\x16cosmos.vesting.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x19cosmos_proto/cosmos.proto\x1a$cosmos/vesting/v1beta1/vesting.proto\x1a\x17cosmos/msg/v1/msg.proto"\x8e\x02\n\x17MsgCreateVestingAccount\x12.\n\x0cfrom_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12,\n\nto_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12[\n\x06amount\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x10\n\x08end_time\x18\x04 \x01(\x03\x12\x0f\n\x07delayed\x18\x05 \x01(\x08:\x15\x82\xe7\xb0*\x0cfrom_address\xe8\xa0\x1f\x01"!\n\x1fMsgCreateVestingAccountResponse"\xde\x01\n\x1fMsgCreatePermanentLockedAccount\x12-\n\x0cfrom_address\x18\x01 \x01(\tB\x17\xf2\xde\x1f\x13yaml:"from_address"\x12)\n\nto_address\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"to_address"\x12[\n\x06amount\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x04\xe8\xa0\x1f\x01")\n\'MsgCreatePermanentLockedAccountResponse"\xb5\x01\n\x1fMsgCreatePeriodicVestingAccount\x12\x14\n\x0cfrom_address\x18\x01 \x01(\t\x12\x12\n\nto_address\x18\x02 \x01(\t\x12\x12\n\nstart_time\x18\x03 \x01(\x03\x12=\n\x0fvesting_periods\x18\x04 \x03(\x0b2\x1e.cosmos.vesting.v1beta1.PeriodB\x04\xc8\xde\x1f\x00:\x15\x82\xe7\xb0*\x0cfrom_address\xe8\xa0\x1f\x00")\n\'MsgCreatePeriodicVestingAccountResponse2\xbe\x03\n\x03Msg\x12\x80\x01\n\x14CreateVestingAccount\x12/.cosmos.vesting.v1beta1.MsgCreateVestingAccount\x1a7.cosmos.vesting.v1beta1.MsgCreateVestingAccountResponse\x12\x98\x01\n\x1cCreatePermanentLockedAccount\x127.cosmos.vesting.v1beta1.MsgCreatePermanentLockedAccount\x1a?.cosmos.vesting.v1beta1.MsgCreatePermanentLockedAccountResponse\x12\x98\x01\n\x1cCreatePeriodicVestingAccount\x127.cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccount\x1a?.cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccountResponseB3Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/typesb\x06proto3')
_MSGCREATEVESTINGACCOUNT = DESCRIPTOR.message_types_by_name['MsgCreateVestingAccount']
_MSGCREATEVESTINGACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateVestingAccountResponse']
_MSGCREATEPERMANENTLOCKEDACCOUNT = DESCRIPTOR.message_types_by_name['MsgCreatePermanentLockedAccount']
_MSGCREATEPERMANENTLOCKEDACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['MsgCreatePermanentLockedAccountResponse']
_MSGCREATEPERIODICVESTINGACCOUNT = DESCRIPTOR.message_types_by_name['MsgCreatePeriodicVestingAccount']
_MSGCREATEPERIODICVESTINGACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['MsgCreatePeriodicVestingAccountResponse']
MsgCreateVestingAccount = _reflection.GeneratedProtocolMessageType('MsgCreateVestingAccount', (_message.Message,), {'DESCRIPTOR': _MSGCREATEVESTINGACCOUNT, '__module__': 'cosmos.vesting.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateVestingAccount)
MsgCreateVestingAccountResponse = _reflection.GeneratedProtocolMessageType('MsgCreateVestingAccountResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATEVESTINGACCOUNTRESPONSE, '__module__': 'cosmos.vesting.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateVestingAccountResponse)
MsgCreatePermanentLockedAccount = _reflection.GeneratedProtocolMessageType('MsgCreatePermanentLockedAccount', (_message.Message,), {'DESCRIPTOR': _MSGCREATEPERMANENTLOCKEDACCOUNT, '__module__': 'cosmos.vesting.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreatePermanentLockedAccount)
MsgCreatePermanentLockedAccountResponse = _reflection.GeneratedProtocolMessageType('MsgCreatePermanentLockedAccountResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATEPERMANENTLOCKEDACCOUNTRESPONSE, '__module__': 'cosmos.vesting.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreatePermanentLockedAccountResponse)
MsgCreatePeriodicVestingAccount = _reflection.GeneratedProtocolMessageType('MsgCreatePeriodicVestingAccount', (_message.Message,), {'DESCRIPTOR': _MSGCREATEPERIODICVESTINGACCOUNT, '__module__': 'cosmos.vesting.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreatePeriodicVestingAccount)
MsgCreatePeriodicVestingAccountResponse = _reflection.GeneratedProtocolMessageType('MsgCreatePeriodicVestingAccountResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATEPERIODICVESTINGACCOUNTRESPONSE, '__module__': 'cosmos.vesting.v1beta1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreatePeriodicVestingAccountResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/types'
    _MSGCREATEVESTINGACCOUNT.fields_by_name['from_address']._options = None
    _MSGCREATEVESTINGACCOUNT.fields_by_name['from_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGCREATEVESTINGACCOUNT.fields_by_name['to_address']._options = None
    _MSGCREATEVESTINGACCOUNT.fields_by_name['to_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGCREATEVESTINGACCOUNT.fields_by_name['amount']._options = None
    _MSGCREATEVESTINGACCOUNT.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGCREATEVESTINGACCOUNT._options = None
    _MSGCREATEVESTINGACCOUNT._serialized_options = b'\x82\xe7\xb0*\x0cfrom_address\xe8\xa0\x1f\x01'
    _MSGCREATEPERMANENTLOCKEDACCOUNT.fields_by_name['from_address']._options = None
    _MSGCREATEPERMANENTLOCKEDACCOUNT.fields_by_name['from_address']._serialized_options = b'\xf2\xde\x1f\x13yaml:"from_address"'
    _MSGCREATEPERMANENTLOCKEDACCOUNT.fields_by_name['to_address']._options = None
    _MSGCREATEPERMANENTLOCKEDACCOUNT.fields_by_name['to_address']._serialized_options = b'\xf2\xde\x1f\x11yaml:"to_address"'
    _MSGCREATEPERMANENTLOCKEDACCOUNT.fields_by_name['amount']._options = None
    _MSGCREATEPERMANENTLOCKEDACCOUNT.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGCREATEPERMANENTLOCKEDACCOUNT._options = None
    _MSGCREATEPERMANENTLOCKEDACCOUNT._serialized_options = b'\xe8\xa0\x1f\x01'
    _MSGCREATEPERIODICVESTINGACCOUNT.fields_by_name['vesting_periods']._options = None
    _MSGCREATEPERIODICVESTINGACCOUNT.fields_by_name['vesting_periods']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCREATEPERIODICVESTINGACCOUNT._options = None
    _MSGCREATEPERIODICVESTINGACCOUNT._serialized_options = b'\x82\xe7\xb0*\x0cfrom_address\xe8\xa0\x1f\x00'
    _MSGCREATEVESTINGACCOUNT._serialized_start = 204
    _MSGCREATEVESTINGACCOUNT._serialized_end = 474
    _MSGCREATEVESTINGACCOUNTRESPONSE._serialized_start = 476
    _MSGCREATEVESTINGACCOUNTRESPONSE._serialized_end = 509
    _MSGCREATEPERMANENTLOCKEDACCOUNT._serialized_start = 512
    _MSGCREATEPERMANENTLOCKEDACCOUNT._serialized_end = 734
    _MSGCREATEPERMANENTLOCKEDACCOUNTRESPONSE._serialized_start = 736
    _MSGCREATEPERMANENTLOCKEDACCOUNTRESPONSE._serialized_end = 777
    _MSGCREATEPERIODICVESTINGACCOUNT._serialized_start = 780
    _MSGCREATEPERIODICVESTINGACCOUNT._serialized_end = 961
    _MSGCREATEPERIODICVESTINGACCOUNTRESPONSE._serialized_start = 963
    _MSGCREATEPERIODICVESTINGACCOUNTRESPONSE._serialized_end = 1004
    _MSG._serialized_start = 1007
    _MSG._serialized_end = 1453


'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.auth.v1beta1 import auth_pb2 as cosmos_dot_auth_dot_v1beta1_dot_auth__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/vesting/v1beta1/vesting.proto\x12\x16cosmos.vesting.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1ecosmos/auth/v1beta1/auth.proto"\xa2\x03\n\x12BaseVestingAccount\x12<\n\x0cbase_account\x18\x01 \x01(\x0b2 .cosmos.auth.v1beta1.BaseAccountB\x04\xd0\xde\x1f\x01\x12e\n\x10original_vesting\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12c\n\x0edelegated_free\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12f\n\x11delegated_vesting\x18\x04 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x10\n\x08end_time\x18\x05 \x01(\x03:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00"\x88\x01\n\x18ContinuousVestingAccount\x12N\n\x14base_vesting_account\x18\x01 \x01(\x0b2*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01\x12\x12\n\nstart_time\x18\x02 \x01(\x03:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00"q\n\x15DelayedVestingAccount\x12N\n\x14base_vesting_account\x18\x01 \x01(\x0b2*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00"{\n\x06Period\x12\x0e\n\x06length\x18\x01 \x01(\x03\x12[\n\x06amount\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x04\x98\xa0\x1f\x00"\xc5\x01\n\x16PeriodicVestingAccount\x12N\n\x14base_vesting_account\x18\x01 \x01(\x0b2*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01\x12\x12\n\nstart_time\x18\x02 \x01(\x03\x12=\n\x0fvesting_periods\x18\x03 \x03(\x0b2\x1e.cosmos.vesting.v1beta1.PeriodB\x04\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00"r\n\x16PermanentLockedAccount\x12N\n\x14base_vesting_account\x18\x01 \x01(\x0b2*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00B3Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/typesb\x06proto3')
_BASEVESTINGACCOUNT = DESCRIPTOR.message_types_by_name['BaseVestingAccount']
_CONTINUOUSVESTINGACCOUNT = DESCRIPTOR.message_types_by_name['ContinuousVestingAccount']
_DELAYEDVESTINGACCOUNT = DESCRIPTOR.message_types_by_name['DelayedVestingAccount']
_PERIOD = DESCRIPTOR.message_types_by_name['Period']
_PERIODICVESTINGACCOUNT = DESCRIPTOR.message_types_by_name['PeriodicVestingAccount']
_PERMANENTLOCKEDACCOUNT = DESCRIPTOR.message_types_by_name['PermanentLockedAccount']
BaseVestingAccount = _reflection.GeneratedProtocolMessageType('BaseVestingAccount', (_message.Message,), {'DESCRIPTOR': _BASEVESTINGACCOUNT, '__module__': 'cosmos.vesting.v1beta1.vesting_pb2'})
_sym_db.RegisterMessage(BaseVestingAccount)
ContinuousVestingAccount = _reflection.GeneratedProtocolMessageType('ContinuousVestingAccount', (_message.Message,), {'DESCRIPTOR': _CONTINUOUSVESTINGACCOUNT, '__module__': 'cosmos.vesting.v1beta1.vesting_pb2'})
_sym_db.RegisterMessage(ContinuousVestingAccount)
DelayedVestingAccount = _reflection.GeneratedProtocolMessageType('DelayedVestingAccount', (_message.Message,), {'DESCRIPTOR': _DELAYEDVESTINGACCOUNT, '__module__': 'cosmos.vesting.v1beta1.vesting_pb2'})
_sym_db.RegisterMessage(DelayedVestingAccount)
Period = _reflection.GeneratedProtocolMessageType('Period', (_message.Message,), {'DESCRIPTOR': _PERIOD, '__module__': 'cosmos.vesting.v1beta1.vesting_pb2'})
_sym_db.RegisterMessage(Period)
PeriodicVestingAccount = _reflection.GeneratedProtocolMessageType('PeriodicVestingAccount', (_message.Message,), {'DESCRIPTOR': _PERIODICVESTINGACCOUNT, '__module__': 'cosmos.vesting.v1beta1.vesting_pb2'})
_sym_db.RegisterMessage(PeriodicVestingAccount)
PermanentLockedAccount = _reflection.GeneratedProtocolMessageType('PermanentLockedAccount', (_message.Message,), {'DESCRIPTOR': _PERMANENTLOCKEDACCOUNT, '__module__': 'cosmos.vesting.v1beta1.vesting_pb2'})
_sym_db.RegisterMessage(PermanentLockedAccount)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/types'
    _BASEVESTINGACCOUNT.fields_by_name['base_account']._options = None
    _BASEVESTINGACCOUNT.fields_by_name['base_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _BASEVESTINGACCOUNT.fields_by_name['original_vesting']._options = None
    _BASEVESTINGACCOUNT.fields_by_name['original_vesting']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _BASEVESTINGACCOUNT.fields_by_name['delegated_free']._options = None
    _BASEVESTINGACCOUNT.fields_by_name['delegated_free']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _BASEVESTINGACCOUNT.fields_by_name['delegated_vesting']._options = None
    _BASEVESTINGACCOUNT.fields_by_name['delegated_vesting']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _BASEVESTINGACCOUNT._options = None
    _BASEVESTINGACCOUNT._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _CONTINUOUSVESTINGACCOUNT.fields_by_name['base_vesting_account']._options = None
    _CONTINUOUSVESTINGACCOUNT.fields_by_name['base_vesting_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _CONTINUOUSVESTINGACCOUNT._options = None
    _CONTINUOUSVESTINGACCOUNT._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _DELAYEDVESTINGACCOUNT.fields_by_name['base_vesting_account']._options = None
    _DELAYEDVESTINGACCOUNT.fields_by_name['base_vesting_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _DELAYEDVESTINGACCOUNT._options = None
    _DELAYEDVESTINGACCOUNT._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _PERIOD.fields_by_name['amount']._options = None
    _PERIOD.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _PERIOD._options = None
    _PERIOD._serialized_options = b'\x98\xa0\x1f\x00'
    _PERIODICVESTINGACCOUNT.fields_by_name['base_vesting_account']._options = None
    _PERIODICVESTINGACCOUNT.fields_by_name['base_vesting_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _PERIODICVESTINGACCOUNT.fields_by_name['vesting_periods']._options = None
    _PERIODICVESTINGACCOUNT.fields_by_name['vesting_periods']._serialized_options = b'\xc8\xde\x1f\x00'
    _PERIODICVESTINGACCOUNT._options = None
    _PERIODICVESTINGACCOUNT._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _PERMANENTLOCKEDACCOUNT.fields_by_name['base_vesting_account']._options = None
    _PERMANENTLOCKEDACCOUNT.fields_by_name['base_vesting_account']._serialized_options = b'\xd0\xde\x1f\x01'
    _PERMANENTLOCKEDACCOUNT._options = None
    _PERMANENTLOCKEDACCOUNT._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _BASEVESTINGACCOUNT._serialized_start = 151
    _BASEVESTINGACCOUNT._serialized_end = 569
    _CONTINUOUSVESTINGACCOUNT._serialized_start = 572
    _CONTINUOUSVESTINGACCOUNT._serialized_end = 708
    _DELAYEDVESTINGACCOUNT._serialized_start = 710
    _DELAYEDVESTINGACCOUNT._serialized_end = 823
    _PERIOD._serialized_start = 825
    _PERIOD._serialized_end = 948
    _PERIODICVESTINGACCOUNT._serialized_start = 951
    _PERIODICVESTINGACCOUNT._serialized_end = 1148
    _PERMANENTLOCKEDACCOUNT._serialized_start = 1150
    _PERMANENTLOCKEDACCOUNT._serialized_end = 1264

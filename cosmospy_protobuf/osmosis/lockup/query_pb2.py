
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ...google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ...osmosis.lockup import lock_pb2 as osmosis_dot_lockup_dot_lock__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aosmosis/lockup/query.proto\x12\x0eosmosis.lockup\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x19osmosis/lockup/lock.proto"\x16\n\x14ModuleBalanceRequest"s\n\x15ModuleBalanceResponse\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\x1b\n\x19ModuleLockedAmountRequest"x\n\x1aModuleLockedAmountResponse\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"@\n\x1dAccountUnlockableCoinsRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner""|\n\x1eAccountUnlockableCoinsResponse\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"?\n\x1cAccountUnlockingCoinsRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner""{\n\x1dAccountUnlockingCoinsResponse\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"<\n\x19AccountLockedCoinsRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner""x\n\x1aAccountLockedCoinsResponse\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\x8c\x01\n\x1cAccountLockedPastTimeRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12K\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1c\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp""P\n\x1dAccountLockedPastTimeResponse\x12/\n\x05locks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00"\x9c\x01\n,AccountLockedPastTimeNotUnlockingOnlyRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12K\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1c\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp""`\n-AccountLockedPastTimeNotUnlockingOnlyResponse\x12/\n\x05locks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00"\x90\x01\n AccountUnlockedBeforeTimeRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12K\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1c\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp""T\n!AccountUnlockedBeforeTimeResponse\x12/\n\x05locks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00"\xa0\x01\n!AccountLockedPastTimeDenomRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12K\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1c\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"\x12\r\n\x05denom\x18\x03 \x01(\t"U\n"AccountLockedPastTimeDenomResponse\x12/\n\x05locks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00"m\n\x12LockedDenomRequest\x12\r\n\x05denom\x18\x01 \x01(\t\x12H\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x1b\x98\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration""f\n\x13LockedDenomResponse\x12O\n\x06amount\x18\x01 \x01(\tB?\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\ryaml:"amount"\xc8\xde\x1f\x00" \n\rLockedRequest\x12\x0f\n\x07lock_id\x18\x01 \x01(\x04":\n\x0eLockedResponse\x12(\n\x04lock\x18\x01 \x01(\x0b2\x1a.osmosis.lockup.PeriodLock"4\n!SyntheticLockupsByLockupIDRequest\x12\x0f\n\x07lock_id\x18\x01 \x01(\x04"b\n"SyntheticLockupsByLockupIDResponse\x12<\n\x0fsynthetic_locks\x18\x01 \x03(\x0b2\x1d.osmosis.lockup.SyntheticLockB\x04\xc8\xde\x1f\x00"\x8f\x01\n"AccountLockedLongerDurationRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12H\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x1b\x98\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration""V\n#AccountLockedLongerDurationResponse\x12/\n\x05locks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00"\x89\x01\n\x1cAccountLockedDurationRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12H\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x1b\x98\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration""P\n\x1dAccountLockedDurationResponse\x12/\n\x05locks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00"\x9f\x01\n2AccountLockedLongerDurationNotUnlockingOnlyRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12H\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x1b\x98\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration""f\n3AccountLockedLongerDurationNotUnlockingOnlyResponse\x12/\n\x05locks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00"\xa3\x01\n\'AccountLockedLongerDurationDenomRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12H\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x1b\x98\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration"\x12\r\n\x05denom\x18\x03 \x01(\t"[\n(AccountLockedLongerDurationDenomResponse\x12/\n\x05locks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x002\x81\x18\n\x05Query\x12\x8c\x01\n\rModuleBalance\x12$.osmosis.lockup.ModuleBalanceRequest\x1a%.osmosis.lockup.ModuleBalanceResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/lockup/v1beta1/module_balance\x12\xa1\x01\n\x12ModuleLockedAmount\x12).osmosis.lockup.ModuleLockedAmountRequest\x1a*.osmosis.lockup.ModuleLockedAmountResponse"4\x82\xd3\xe4\x93\x02.\x12,/osmosis/lockup/v1beta1/module_locked_amount\x12\xb9\x01\n\x16AccountUnlockableCoins\x12-.osmosis.lockup.AccountUnlockableCoinsRequest\x1a..osmosis.lockup.AccountUnlockableCoinsResponse"@\x82\xd3\xe4\x93\x02:\x128/osmosis/lockup/v1beta1/account_unlockable_coins/{owner}\x12\xb5\x01\n\x15AccountUnlockingCoins\x12,.osmosis.lockup.AccountUnlockingCoinsRequest\x1a-.osmosis.lockup.AccountUnlockingCoinsResponse"?\x82\xd3\xe4\x93\x029\x127/osmosis/lockup/v1beta1/account_unlocking_coins/{owner}\x12\xa9\x01\n\x12AccountLockedCoins\x12).osmosis.lockup.AccountLockedCoinsRequest\x1a*.osmosis.lockup.AccountLockedCoinsResponse"<\x82\xd3\xe4\x93\x026\x124/osmosis/lockup/v1beta1/account_locked_coins/{owner}\x12\xb5\x01\n\x15AccountLockedPastTime\x12,.osmosis.lockup.AccountLockedPastTimeRequest\x1a-.osmosis.lockup.AccountLockedPastTimeResponse"?\x82\xd3\xe4\x93\x029\x127/osmosis/lockup/v1beta1/account_locked_pasttime/{owner}\x12\xf8\x01\n%AccountLockedPastTimeNotUnlockingOnly\x12<.osmosis.lockup.AccountLockedPastTimeNotUnlockingOnlyRequest\x1a=.osmosis.lockup.AccountLockedPastTimeNotUnlockingOnlyResponse"R\x82\xd3\xe4\x93\x02L\x12J/osmosis/lockup/v1beta1/account_locked_pasttime_not_unlocking_only/{owner}\x12\xc6\x01\n\x19AccountUnlockedBeforeTime\x120.osmosis.lockup.AccountUnlockedBeforeTimeRequest\x1a1.osmosis.lockup.AccountUnlockedBeforeTimeResponse"D\x82\xd3\xe4\x93\x02>\x12</osmosis/lockup/v1beta1/account_unlocked_before_time/{owner}\x12\xca\x01\n\x1aAccountLockedPastTimeDenom\x121.osmosis.lockup.AccountLockedPastTimeDenomRequest\x1a2.osmosis.lockup.AccountLockedPastTimeDenomResponse"E\x82\xd3\xe4\x93\x02?\x12=/osmosis/lockup/v1beta1/account_locked_pasttime_denom/{owner}\x12\x84\x01\n\x0bLockedDenom\x12".osmosis.lockup.LockedDenomRequest\x1a#.osmosis.lockup.LockedDenomResponse",\x82\xd3\xe4\x93\x02&\x12$/osmosis/lockup/v1beta1/locked_denom\x12\x83\x01\n\nLockedByID\x12\x1d.osmosis.lockup.LockedRequest\x1a\x1e.osmosis.lockup.LockedResponse"6\x82\xd3\xe4\x93\x020\x12./osmosis/lockup/v1beta1/locked_by_id/{lock_id}\x12\xcb\x01\n\x1aSyntheticLockupsByLockupID\x121.osmosis.lockup.SyntheticLockupsByLockupIDRequest\x1a2.osmosis.lockup.SyntheticLockupsByLockupIDResponse"F\x82\xd3\xe4\x93\x02@\x12>/osmosis/lockup/v1beta1/synthetic_lockups_by_lock_id/{lock_id}\x12\xce\x01\n\x1bAccountLockedLongerDuration\x122.osmosis.lockup.AccountLockedLongerDurationRequest\x1a3.osmosis.lockup.AccountLockedLongerDurationResponse"F\x82\xd3\xe4\x93\x02@\x12>/osmosis/lockup/v1beta1/account_locked_longer_duration/{owner}\x12\xb5\x01\n\x15AccountLockedDuration\x12,.osmosis.lockup.AccountLockedDurationRequest\x1a-.osmosis.lockup.AccountLockedDurationResponse"?\x82\xd3\xe4\x93\x029\x127/osmosis/lockup/v1beta1/account_locked_duration/{owner}\x12\x91\x02\n+AccountLockedLongerDurationNotUnlockingOnly\x12B.osmosis.lockup.AccountLockedLongerDurationNotUnlockingOnlyRequest\x1aC.osmosis.lockup.AccountLockedLongerDurationNotUnlockingOnlyResponse"Y\x82\xd3\xe4\x93\x02S\x12Q/osmosis/lockup/v1beta1/account_locked_longer_duration_not_unlocking_only/{owner}\x12\xe3\x01\n AccountLockedLongerDurationDenom\x127.osmosis.lockup.AccountLockedLongerDurationDenomRequest\x1a8.osmosis.lockup.AccountLockedLongerDurationDenomResponse"L\x82\xd3\xe4\x93\x02F\x12D/osmosis/lockup/v1beta1/account_locked_longer_duration_denom/{owner}B3Z1github.com/osmosis-labs/osmosis/v7/x/lockup/typesb\x06proto3')
_MODULEBALANCEREQUEST = DESCRIPTOR.message_types_by_name['ModuleBalanceRequest']
_MODULEBALANCERESPONSE = DESCRIPTOR.message_types_by_name['ModuleBalanceResponse']
_MODULELOCKEDAMOUNTREQUEST = DESCRIPTOR.message_types_by_name['ModuleLockedAmountRequest']
_MODULELOCKEDAMOUNTRESPONSE = DESCRIPTOR.message_types_by_name['ModuleLockedAmountResponse']
_ACCOUNTUNLOCKABLECOINSREQUEST = DESCRIPTOR.message_types_by_name['AccountUnlockableCoinsRequest']
_ACCOUNTUNLOCKABLECOINSRESPONSE = DESCRIPTOR.message_types_by_name['AccountUnlockableCoinsResponse']
_ACCOUNTUNLOCKINGCOINSREQUEST = DESCRIPTOR.message_types_by_name['AccountUnlockingCoinsRequest']
_ACCOUNTUNLOCKINGCOINSRESPONSE = DESCRIPTOR.message_types_by_name['AccountUnlockingCoinsResponse']
_ACCOUNTLOCKEDCOINSREQUEST = DESCRIPTOR.message_types_by_name['AccountLockedCoinsRequest']
_ACCOUNTLOCKEDCOINSRESPONSE = DESCRIPTOR.message_types_by_name['AccountLockedCoinsResponse']
_ACCOUNTLOCKEDPASTTIMEREQUEST = DESCRIPTOR.message_types_by_name['AccountLockedPastTimeRequest']
_ACCOUNTLOCKEDPASTTIMERESPONSE = DESCRIPTOR.message_types_by_name['AccountLockedPastTimeResponse']
_ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYREQUEST = DESCRIPTOR.message_types_by_name['AccountLockedPastTimeNotUnlockingOnlyRequest']
_ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYRESPONSE = DESCRIPTOR.message_types_by_name['AccountLockedPastTimeNotUnlockingOnlyResponse']
_ACCOUNTUNLOCKEDBEFORETIMEREQUEST = DESCRIPTOR.message_types_by_name['AccountUnlockedBeforeTimeRequest']
_ACCOUNTUNLOCKEDBEFORETIMERESPONSE = DESCRIPTOR.message_types_by_name['AccountUnlockedBeforeTimeResponse']
_ACCOUNTLOCKEDPASTTIMEDENOMREQUEST = DESCRIPTOR.message_types_by_name['AccountLockedPastTimeDenomRequest']
_ACCOUNTLOCKEDPASTTIMEDENOMRESPONSE = DESCRIPTOR.message_types_by_name['AccountLockedPastTimeDenomResponse']
_LOCKEDDENOMREQUEST = DESCRIPTOR.message_types_by_name['LockedDenomRequest']
_LOCKEDDENOMRESPONSE = DESCRIPTOR.message_types_by_name['LockedDenomResponse']
_LOCKEDREQUEST = DESCRIPTOR.message_types_by_name['LockedRequest']
_LOCKEDRESPONSE = DESCRIPTOR.message_types_by_name['LockedResponse']
_SYNTHETICLOCKUPSBYLOCKUPIDREQUEST = DESCRIPTOR.message_types_by_name['SyntheticLockupsByLockupIDRequest']
_SYNTHETICLOCKUPSBYLOCKUPIDRESPONSE = DESCRIPTOR.message_types_by_name['SyntheticLockupsByLockupIDResponse']
_ACCOUNTLOCKEDLONGERDURATIONREQUEST = DESCRIPTOR.message_types_by_name['AccountLockedLongerDurationRequest']
_ACCOUNTLOCKEDLONGERDURATIONRESPONSE = DESCRIPTOR.message_types_by_name['AccountLockedLongerDurationResponse']
_ACCOUNTLOCKEDDURATIONREQUEST = DESCRIPTOR.message_types_by_name['AccountLockedDurationRequest']
_ACCOUNTLOCKEDDURATIONRESPONSE = DESCRIPTOR.message_types_by_name['AccountLockedDurationResponse']
_ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYREQUEST = DESCRIPTOR.message_types_by_name['AccountLockedLongerDurationNotUnlockingOnlyRequest']
_ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYRESPONSE = DESCRIPTOR.message_types_by_name['AccountLockedLongerDurationNotUnlockingOnlyResponse']
_ACCOUNTLOCKEDLONGERDURATIONDENOMREQUEST = DESCRIPTOR.message_types_by_name['AccountLockedLongerDurationDenomRequest']
_ACCOUNTLOCKEDLONGERDURATIONDENOMRESPONSE = DESCRIPTOR.message_types_by_name['AccountLockedLongerDurationDenomResponse']
ModuleBalanceRequest = _reflection.GeneratedProtocolMessageType('ModuleBalanceRequest', (_message.Message,), {'DESCRIPTOR': _MODULEBALANCEREQUEST, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(ModuleBalanceRequest)
ModuleBalanceResponse = _reflection.GeneratedProtocolMessageType('ModuleBalanceResponse', (_message.Message,), {'DESCRIPTOR': _MODULEBALANCERESPONSE, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(ModuleBalanceResponse)
ModuleLockedAmountRequest = _reflection.GeneratedProtocolMessageType('ModuleLockedAmountRequest', (_message.Message,), {'DESCRIPTOR': _MODULELOCKEDAMOUNTREQUEST, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(ModuleLockedAmountRequest)
ModuleLockedAmountResponse = _reflection.GeneratedProtocolMessageType('ModuleLockedAmountResponse', (_message.Message,), {'DESCRIPTOR': _MODULELOCKEDAMOUNTRESPONSE, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(ModuleLockedAmountResponse)
AccountUnlockableCoinsRequest = _reflection.GeneratedProtocolMessageType('AccountUnlockableCoinsRequest', (_message.Message,), {'DESCRIPTOR': _ACCOUNTUNLOCKABLECOINSREQUEST, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountUnlockableCoinsRequest)
AccountUnlockableCoinsResponse = _reflection.GeneratedProtocolMessageType('AccountUnlockableCoinsResponse', (_message.Message,), {'DESCRIPTOR': _ACCOUNTUNLOCKABLECOINSRESPONSE, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountUnlockableCoinsResponse)
AccountUnlockingCoinsRequest = _reflection.GeneratedProtocolMessageType('AccountUnlockingCoinsRequest', (_message.Message,), {'DESCRIPTOR': _ACCOUNTUNLOCKINGCOINSREQUEST, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountUnlockingCoinsRequest)
AccountUnlockingCoinsResponse = _reflection.GeneratedProtocolMessageType('AccountUnlockingCoinsResponse', (_message.Message,), {'DESCRIPTOR': _ACCOUNTUNLOCKINGCOINSRESPONSE, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountUnlockingCoinsResponse)
AccountLockedCoinsRequest = _reflection.GeneratedProtocolMessageType('AccountLockedCoinsRequest', (_message.Message,), {'DESCRIPTOR': _ACCOUNTLOCKEDCOINSREQUEST, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountLockedCoinsRequest)
AccountLockedCoinsResponse = _reflection.GeneratedProtocolMessageType('AccountLockedCoinsResponse', (_message.Message,), {'DESCRIPTOR': _ACCOUNTLOCKEDCOINSRESPONSE, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountLockedCoinsResponse)
AccountLockedPastTimeRequest = _reflection.GeneratedProtocolMessageType('AccountLockedPastTimeRequest', (_message.Message,), {'DESCRIPTOR': _ACCOUNTLOCKEDPASTTIMEREQUEST, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountLockedPastTimeRequest)
AccountLockedPastTimeResponse = _reflection.GeneratedProtocolMessageType('AccountLockedPastTimeResponse', (_message.Message,), {'DESCRIPTOR': _ACCOUNTLOCKEDPASTTIMERESPONSE, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountLockedPastTimeResponse)
AccountLockedPastTimeNotUnlockingOnlyRequest = _reflection.GeneratedProtocolMessageType('AccountLockedPastTimeNotUnlockingOnlyRequest', (_message.Message,), {'DESCRIPTOR': _ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYREQUEST, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountLockedPastTimeNotUnlockingOnlyRequest)
AccountLockedPastTimeNotUnlockingOnlyResponse = _reflection.GeneratedProtocolMessageType('AccountLockedPastTimeNotUnlockingOnlyResponse', (_message.Message,), {'DESCRIPTOR': _ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYRESPONSE, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountLockedPastTimeNotUnlockingOnlyResponse)
AccountUnlockedBeforeTimeRequest = _reflection.GeneratedProtocolMessageType('AccountUnlockedBeforeTimeRequest', (_message.Message,), {'DESCRIPTOR': _ACCOUNTUNLOCKEDBEFORETIMEREQUEST, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountUnlockedBeforeTimeRequest)
AccountUnlockedBeforeTimeResponse = _reflection.GeneratedProtocolMessageType('AccountUnlockedBeforeTimeResponse', (_message.Message,), {'DESCRIPTOR': _ACCOUNTUNLOCKEDBEFORETIMERESPONSE, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountUnlockedBeforeTimeResponse)
AccountLockedPastTimeDenomRequest = _reflection.GeneratedProtocolMessageType('AccountLockedPastTimeDenomRequest', (_message.Message,), {'DESCRIPTOR': _ACCOUNTLOCKEDPASTTIMEDENOMREQUEST, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountLockedPastTimeDenomRequest)
AccountLockedPastTimeDenomResponse = _reflection.GeneratedProtocolMessageType('AccountLockedPastTimeDenomResponse', (_message.Message,), {'DESCRIPTOR': _ACCOUNTLOCKEDPASTTIMEDENOMRESPONSE, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountLockedPastTimeDenomResponse)
LockedDenomRequest = _reflection.GeneratedProtocolMessageType('LockedDenomRequest', (_message.Message,), {'DESCRIPTOR': _LOCKEDDENOMREQUEST, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(LockedDenomRequest)
LockedDenomResponse = _reflection.GeneratedProtocolMessageType('LockedDenomResponse', (_message.Message,), {'DESCRIPTOR': _LOCKEDDENOMRESPONSE, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(LockedDenomResponse)
LockedRequest = _reflection.GeneratedProtocolMessageType('LockedRequest', (_message.Message,), {'DESCRIPTOR': _LOCKEDREQUEST, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(LockedRequest)
LockedResponse = _reflection.GeneratedProtocolMessageType('LockedResponse', (_message.Message,), {'DESCRIPTOR': _LOCKEDRESPONSE, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(LockedResponse)
SyntheticLockupsByLockupIDRequest = _reflection.GeneratedProtocolMessageType('SyntheticLockupsByLockupIDRequest', (_message.Message,), {'DESCRIPTOR': _SYNTHETICLOCKUPSBYLOCKUPIDREQUEST, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(SyntheticLockupsByLockupIDRequest)
SyntheticLockupsByLockupIDResponse = _reflection.GeneratedProtocolMessageType('SyntheticLockupsByLockupIDResponse', (_message.Message,), {'DESCRIPTOR': _SYNTHETICLOCKUPSBYLOCKUPIDRESPONSE, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(SyntheticLockupsByLockupIDResponse)
AccountLockedLongerDurationRequest = _reflection.GeneratedProtocolMessageType('AccountLockedLongerDurationRequest', (_message.Message,), {'DESCRIPTOR': _ACCOUNTLOCKEDLONGERDURATIONREQUEST, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountLockedLongerDurationRequest)
AccountLockedLongerDurationResponse = _reflection.GeneratedProtocolMessageType('AccountLockedLongerDurationResponse', (_message.Message,), {'DESCRIPTOR': _ACCOUNTLOCKEDLONGERDURATIONRESPONSE, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountLockedLongerDurationResponse)
AccountLockedDurationRequest = _reflection.GeneratedProtocolMessageType('AccountLockedDurationRequest', (_message.Message,), {'DESCRIPTOR': _ACCOUNTLOCKEDDURATIONREQUEST, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountLockedDurationRequest)
AccountLockedDurationResponse = _reflection.GeneratedProtocolMessageType('AccountLockedDurationResponse', (_message.Message,), {'DESCRIPTOR': _ACCOUNTLOCKEDDURATIONRESPONSE, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountLockedDurationResponse)
AccountLockedLongerDurationNotUnlockingOnlyRequest = _reflection.GeneratedProtocolMessageType('AccountLockedLongerDurationNotUnlockingOnlyRequest', (_message.Message,), {'DESCRIPTOR': _ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYREQUEST, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountLockedLongerDurationNotUnlockingOnlyRequest)
AccountLockedLongerDurationNotUnlockingOnlyResponse = _reflection.GeneratedProtocolMessageType('AccountLockedLongerDurationNotUnlockingOnlyResponse', (_message.Message,), {'DESCRIPTOR': _ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYRESPONSE, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountLockedLongerDurationNotUnlockingOnlyResponse)
AccountLockedLongerDurationDenomRequest = _reflection.GeneratedProtocolMessageType('AccountLockedLongerDurationDenomRequest', (_message.Message,), {'DESCRIPTOR': _ACCOUNTLOCKEDLONGERDURATIONDENOMREQUEST, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountLockedLongerDurationDenomRequest)
AccountLockedLongerDurationDenomResponse = _reflection.GeneratedProtocolMessageType('AccountLockedLongerDurationDenomResponse', (_message.Message,), {'DESCRIPTOR': _ACCOUNTLOCKEDLONGERDURATIONDENOMRESPONSE, '__module__': 'osmosis.lockup.query_pb2'})
_sym_db.RegisterMessage(AccountLockedLongerDurationDenomResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/osmosis-labs/osmosis/v7/x/lockup/types'
    _MODULEBALANCERESPONSE.fields_by_name['coins']._options = None
    _MODULEBALANCERESPONSE.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MODULELOCKEDAMOUNTRESPONSE.fields_by_name['coins']._options = None
    _MODULELOCKEDAMOUNTRESPONSE.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _ACCOUNTUNLOCKABLECOINSREQUEST.fields_by_name['owner']._options = None
    _ACCOUNTUNLOCKABLECOINSREQUEST.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _ACCOUNTUNLOCKABLECOINSRESPONSE.fields_by_name['coins']._options = None
    _ACCOUNTUNLOCKABLECOINSRESPONSE.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _ACCOUNTUNLOCKINGCOINSREQUEST.fields_by_name['owner']._options = None
    _ACCOUNTUNLOCKINGCOINSREQUEST.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _ACCOUNTUNLOCKINGCOINSRESPONSE.fields_by_name['coins']._options = None
    _ACCOUNTUNLOCKINGCOINSRESPONSE.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _ACCOUNTLOCKEDCOINSREQUEST.fields_by_name['owner']._options = None
    _ACCOUNTLOCKEDCOINSREQUEST.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _ACCOUNTLOCKEDCOINSRESPONSE.fields_by_name['coins']._options = None
    _ACCOUNTLOCKEDCOINSRESPONSE.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _ACCOUNTLOCKEDPASTTIMEREQUEST.fields_by_name['owner']._options = None
    _ACCOUNTLOCKEDPASTTIMEREQUEST.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _ACCOUNTLOCKEDPASTTIMEREQUEST.fields_by_name['timestamp']._options = None
    _ACCOUNTLOCKEDPASTTIMEREQUEST.fields_by_name['timestamp']._serialized_options = b'\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"'
    _ACCOUNTLOCKEDPASTTIMERESPONSE.fields_by_name['locks']._options = None
    _ACCOUNTLOCKEDPASTTIMERESPONSE.fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYREQUEST.fields_by_name['owner']._options = None
    _ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYREQUEST.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYREQUEST.fields_by_name['timestamp']._options = None
    _ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYREQUEST.fields_by_name['timestamp']._serialized_options = b'\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"'
    _ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYRESPONSE.fields_by_name['locks']._options = None
    _ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYRESPONSE.fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _ACCOUNTUNLOCKEDBEFORETIMEREQUEST.fields_by_name['owner']._options = None
    _ACCOUNTUNLOCKEDBEFORETIMEREQUEST.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _ACCOUNTUNLOCKEDBEFORETIMEREQUEST.fields_by_name['timestamp']._options = None
    _ACCOUNTUNLOCKEDBEFORETIMEREQUEST.fields_by_name['timestamp']._serialized_options = b'\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"'
    _ACCOUNTUNLOCKEDBEFORETIMERESPONSE.fields_by_name['locks']._options = None
    _ACCOUNTUNLOCKEDBEFORETIMERESPONSE.fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _ACCOUNTLOCKEDPASTTIMEDENOMREQUEST.fields_by_name['owner']._options = None
    _ACCOUNTLOCKEDPASTTIMEDENOMREQUEST.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _ACCOUNTLOCKEDPASTTIMEDENOMREQUEST.fields_by_name['timestamp']._options = None
    _ACCOUNTLOCKEDPASTTIMEDENOMREQUEST.fields_by_name['timestamp']._serialized_options = b'\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"'
    _ACCOUNTLOCKEDPASTTIMEDENOMRESPONSE.fields_by_name['locks']._options = None
    _ACCOUNTLOCKEDPASTTIMEDENOMRESPONSE.fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _LOCKEDDENOMREQUEST.fields_by_name['duration']._options = None
    _LOCKEDDENOMREQUEST.fields_by_name['duration']._serialized_options = b'\x98\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration"'
    _LOCKEDDENOMRESPONSE.fields_by_name['amount']._options = None
    _LOCKEDDENOMRESPONSE.fields_by_name['amount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\ryaml:"amount"\xc8\xde\x1f\x00'
    _SYNTHETICLOCKUPSBYLOCKUPIDRESPONSE.fields_by_name['synthetic_locks']._options = None
    _SYNTHETICLOCKUPSBYLOCKUPIDRESPONSE.fields_by_name['synthetic_locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _ACCOUNTLOCKEDLONGERDURATIONREQUEST.fields_by_name['owner']._options = None
    _ACCOUNTLOCKEDLONGERDURATIONREQUEST.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _ACCOUNTLOCKEDLONGERDURATIONREQUEST.fields_by_name['duration']._options = None
    _ACCOUNTLOCKEDLONGERDURATIONREQUEST.fields_by_name['duration']._serialized_options = b'\x98\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration"'
    _ACCOUNTLOCKEDLONGERDURATIONRESPONSE.fields_by_name['locks']._options = None
    _ACCOUNTLOCKEDLONGERDURATIONRESPONSE.fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _ACCOUNTLOCKEDDURATIONREQUEST.fields_by_name['owner']._options = None
    _ACCOUNTLOCKEDDURATIONREQUEST.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _ACCOUNTLOCKEDDURATIONREQUEST.fields_by_name['duration']._options = None
    _ACCOUNTLOCKEDDURATIONREQUEST.fields_by_name['duration']._serialized_options = b'\x98\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration"'
    _ACCOUNTLOCKEDDURATIONRESPONSE.fields_by_name['locks']._options = None
    _ACCOUNTLOCKEDDURATIONRESPONSE.fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYREQUEST.fields_by_name['owner']._options = None
    _ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYREQUEST.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYREQUEST.fields_by_name['duration']._options = None
    _ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYREQUEST.fields_by_name['duration']._serialized_options = b'\x98\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration"'
    _ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYRESPONSE.fields_by_name['locks']._options = None
    _ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYRESPONSE.fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _ACCOUNTLOCKEDLONGERDURATIONDENOMREQUEST.fields_by_name['owner']._options = None
    _ACCOUNTLOCKEDLONGERDURATIONDENOMREQUEST.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _ACCOUNTLOCKEDLONGERDURATIONDENOMREQUEST.fields_by_name['duration']._options = None
    _ACCOUNTLOCKEDLONGERDURATIONDENOMREQUEST.fields_by_name['duration']._serialized_options = b'\x98\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration"'
    _ACCOUNTLOCKEDLONGERDURATIONDENOMRESPONSE.fields_by_name['locks']._options = None
    _ACCOUNTLOCKEDLONGERDURATIONDENOMRESPONSE.fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['ModuleBalance']._options = None
    _QUERY.methods_by_name['ModuleBalance']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/lockup/v1beta1/module_balance'
    _QUERY.methods_by_name['ModuleLockedAmount']._options = None
    _QUERY.methods_by_name['ModuleLockedAmount']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/osmosis/lockup/v1beta1/module_locked_amount'
    _QUERY.methods_by_name['AccountUnlockableCoins']._options = None
    _QUERY.methods_by_name['AccountUnlockableCoins']._serialized_options = b'\x82\xd3\xe4\x93\x02:\x128/osmosis/lockup/v1beta1/account_unlockable_coins/{owner}'
    _QUERY.methods_by_name['AccountUnlockingCoins']._options = None
    _QUERY.methods_by_name['AccountUnlockingCoins']._serialized_options = b'\x82\xd3\xe4\x93\x029\x127/osmosis/lockup/v1beta1/account_unlocking_coins/{owner}'
    _QUERY.methods_by_name['AccountLockedCoins']._options = None
    _QUERY.methods_by_name['AccountLockedCoins']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/osmosis/lockup/v1beta1/account_locked_coins/{owner}'
    _QUERY.methods_by_name['AccountLockedPastTime']._options = None
    _QUERY.methods_by_name['AccountLockedPastTime']._serialized_options = b'\x82\xd3\xe4\x93\x029\x127/osmosis/lockup/v1beta1/account_locked_pasttime/{owner}'
    _QUERY.methods_by_name['AccountLockedPastTimeNotUnlockingOnly']._options = None
    _QUERY.methods_by_name['AccountLockedPastTimeNotUnlockingOnly']._serialized_options = b'\x82\xd3\xe4\x93\x02L\x12J/osmosis/lockup/v1beta1/account_locked_pasttime_not_unlocking_only/{owner}'
    _QUERY.methods_by_name['AccountUnlockedBeforeTime']._options = None
    _QUERY.methods_by_name['AccountUnlockedBeforeTime']._serialized_options = b'\x82\xd3\xe4\x93\x02>\x12</osmosis/lockup/v1beta1/account_unlocked_before_time/{owner}'
    _QUERY.methods_by_name['AccountLockedPastTimeDenom']._options = None
    _QUERY.methods_by_name['AccountLockedPastTimeDenom']._serialized_options = b'\x82\xd3\xe4\x93\x02?\x12=/osmosis/lockup/v1beta1/account_locked_pasttime_denom/{owner}'
    _QUERY.methods_by_name['LockedDenom']._options = None
    _QUERY.methods_by_name['LockedDenom']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/osmosis/lockup/v1beta1/locked_denom'
    _QUERY.methods_by_name['LockedByID']._options = None
    _QUERY.methods_by_name['LockedByID']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./osmosis/lockup/v1beta1/locked_by_id/{lock_id}'
    _QUERY.methods_by_name['SyntheticLockupsByLockupID']._options = None
    _QUERY.methods_by_name['SyntheticLockupsByLockupID']._serialized_options = b'\x82\xd3\xe4\x93\x02@\x12>/osmosis/lockup/v1beta1/synthetic_lockups_by_lock_id/{lock_id}'
    _QUERY.methods_by_name['AccountLockedLongerDuration']._options = None
    _QUERY.methods_by_name['AccountLockedLongerDuration']._serialized_options = b'\x82\xd3\xe4\x93\x02@\x12>/osmosis/lockup/v1beta1/account_locked_longer_duration/{owner}'
    _QUERY.methods_by_name['AccountLockedDuration']._options = None
    _QUERY.methods_by_name['AccountLockedDuration']._serialized_options = b'\x82\xd3\xe4\x93\x029\x127/osmosis/lockup/v1beta1/account_locked_duration/{owner}'
    _QUERY.methods_by_name['AccountLockedLongerDurationNotUnlockingOnly']._options = None
    _QUERY.methods_by_name['AccountLockedLongerDurationNotUnlockingOnly']._serialized_options = b'\x82\xd3\xe4\x93\x02S\x12Q/osmosis/lockup/v1beta1/account_locked_longer_duration_not_unlocking_only/{owner}'
    _QUERY.methods_by_name['AccountLockedLongerDurationDenom']._options = None
    _QUERY.methods_by_name['AccountLockedLongerDurationDenom']._serialized_options = b'\x82\xd3\xe4\x93\x02F\x12D/osmosis/lockup/v1beta1/account_locked_longer_duration_denom/{owner}'
    _MODULEBALANCEREQUEST._serialized_start = 222
    _MODULEBALANCEREQUEST._serialized_end = 244
    _MODULEBALANCERESPONSE._serialized_start = 246
    _MODULEBALANCERESPONSE._serialized_end = 361
    _MODULELOCKEDAMOUNTREQUEST._serialized_start = 363
    _MODULELOCKEDAMOUNTREQUEST._serialized_end = 390
    _MODULELOCKEDAMOUNTRESPONSE._serialized_start = 392
    _MODULELOCKEDAMOUNTRESPONSE._serialized_end = 512
    _ACCOUNTUNLOCKABLECOINSREQUEST._serialized_start = 514
    _ACCOUNTUNLOCKABLECOINSREQUEST._serialized_end = 578
    _ACCOUNTUNLOCKABLECOINSRESPONSE._serialized_start = 580
    _ACCOUNTUNLOCKABLECOINSRESPONSE._serialized_end = 704
    _ACCOUNTUNLOCKINGCOINSREQUEST._serialized_start = 706
    _ACCOUNTUNLOCKINGCOINSREQUEST._serialized_end = 769
    _ACCOUNTUNLOCKINGCOINSRESPONSE._serialized_start = 771
    _ACCOUNTUNLOCKINGCOINSRESPONSE._serialized_end = 894
    _ACCOUNTLOCKEDCOINSREQUEST._serialized_start = 896
    _ACCOUNTLOCKEDCOINSREQUEST._serialized_end = 956
    _ACCOUNTLOCKEDCOINSRESPONSE._serialized_start = 958
    _ACCOUNTLOCKEDCOINSRESPONSE._serialized_end = 1078
    _ACCOUNTLOCKEDPASTTIMEREQUEST._serialized_start = 1081
    _ACCOUNTLOCKEDPASTTIMEREQUEST._serialized_end = 1221
    _ACCOUNTLOCKEDPASTTIMERESPONSE._serialized_start = 1223
    _ACCOUNTLOCKEDPASTTIMERESPONSE._serialized_end = 1303
    _ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYREQUEST._serialized_start = 1306
    _ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYREQUEST._serialized_end = 1462
    _ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYRESPONSE._serialized_start = 1464
    _ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYRESPONSE._serialized_end = 1560
    _ACCOUNTUNLOCKEDBEFORETIMEREQUEST._serialized_start = 1563
    _ACCOUNTUNLOCKEDBEFORETIMEREQUEST._serialized_end = 1707
    _ACCOUNTUNLOCKEDBEFORETIMERESPONSE._serialized_start = 1709
    _ACCOUNTUNLOCKEDBEFORETIMERESPONSE._serialized_end = 1793
    _ACCOUNTLOCKEDPASTTIMEDENOMREQUEST._serialized_start = 1796
    _ACCOUNTLOCKEDPASTTIMEDENOMREQUEST._serialized_end = 1956
    _ACCOUNTLOCKEDPASTTIMEDENOMRESPONSE._serialized_start = 1958
    _ACCOUNTLOCKEDPASTTIMEDENOMRESPONSE._serialized_end = 2043
    _LOCKEDDENOMREQUEST._serialized_start = 2045
    _LOCKEDDENOMREQUEST._serialized_end = 2154
    _LOCKEDDENOMRESPONSE._serialized_start = 2156
    _LOCKEDDENOMRESPONSE._serialized_end = 2258
    _LOCKEDREQUEST._serialized_start = 2260
    _LOCKEDREQUEST._serialized_end = 2292
    _LOCKEDRESPONSE._serialized_start = 2294
    _LOCKEDRESPONSE._serialized_end = 2352
    _SYNTHETICLOCKUPSBYLOCKUPIDREQUEST._serialized_start = 2354
    _SYNTHETICLOCKUPSBYLOCKUPIDREQUEST._serialized_end = 2406
    _SYNTHETICLOCKUPSBYLOCKUPIDRESPONSE._serialized_start = 2408
    _SYNTHETICLOCKUPSBYLOCKUPIDRESPONSE._serialized_end = 2506
    _ACCOUNTLOCKEDLONGERDURATIONREQUEST._serialized_start = 2509
    _ACCOUNTLOCKEDLONGERDURATIONREQUEST._serialized_end = 2652
    _ACCOUNTLOCKEDLONGERDURATIONRESPONSE._serialized_start = 2654
    _ACCOUNTLOCKEDLONGERDURATIONRESPONSE._serialized_end = 2740
    _ACCOUNTLOCKEDDURATIONREQUEST._serialized_start = 2743
    _ACCOUNTLOCKEDDURATIONREQUEST._serialized_end = 2880
    _ACCOUNTLOCKEDDURATIONRESPONSE._serialized_start = 2882
    _ACCOUNTLOCKEDDURATIONRESPONSE._serialized_end = 2962
    _ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYREQUEST._serialized_start = 2965
    _ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYREQUEST._serialized_end = 3124
    _ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYRESPONSE._serialized_start = 3126
    _ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYRESPONSE._serialized_end = 3228
    _ACCOUNTLOCKEDLONGERDURATIONDENOMREQUEST._serialized_start = 3231
    _ACCOUNTLOCKEDLONGERDURATIONDENOMREQUEST._serialized_end = 3394
    _ACCOUNTLOCKEDLONGERDURATIONDENOMRESPONSE._serialized_start = 3396
    _ACCOUNTLOCKEDLONGERDURATIONDENOMRESPONSE._serialized_end = 3487
    _QUERY._serialized_start = 3490
    _QUERY._serialized_end = 6563

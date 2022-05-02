
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ...cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ...osmosis.lockup import lock_pb2 as osmosis_dot_lockup_dot_lock__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eosmosis/incentives/gauge.proto\x12\x12osmosis.incentives\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x19osmosis/lockup/lock.proto"\xae\x03\n\x05Gauge\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x14\n\x0cis_perpetual\x18\x02 \x01(\x08\x12;\n\rdistribute_to\x18\x03 \x01(\x0b2\x1e.osmosis.lockup.QueryConditionB\x04\xc8\xde\x1f\x00\x12Z\n\x05coins\x18\x04 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12M\n\nstart_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1d\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x11yaml:"start_time"\x12\x1c\n\x14num_epochs_paid_over\x18\x06 \x01(\x04\x12\x15\n\rfilled_epochs\x18\x07 \x01(\x04\x12f\n\x11distributed_coins\x18\x08 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"u\n\x15LockableDurationsInfo\x12\\\n\x12lockable_durations\x18\x01 \x03(\x0b2\x19.google.protobuf.DurationB%\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x19yaml:"lockable_durations"B7Z5github.com/osmosis-labs/osmosis/v7/x/incentives/typesb\x06proto3')
_GAUGE = DESCRIPTOR.message_types_by_name['Gauge']
_LOCKABLEDURATIONSINFO = DESCRIPTOR.message_types_by_name['LockableDurationsInfo']
Gauge = _reflection.GeneratedProtocolMessageType('Gauge', (_message.Message,), {'DESCRIPTOR': _GAUGE, '__module__': 'osmosis.incentives.gauge_pb2'})
_sym_db.RegisterMessage(Gauge)
LockableDurationsInfo = _reflection.GeneratedProtocolMessageType('LockableDurationsInfo', (_message.Message,), {'DESCRIPTOR': _LOCKABLEDURATIONSINFO, '__module__': 'osmosis.incentives.gauge_pb2'})
_sym_db.RegisterMessage(LockableDurationsInfo)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/osmosis-labs/osmosis/v7/x/incentives/types'
    _GAUGE.fields_by_name['distribute_to']._options = None
    _GAUGE.fields_by_name['distribute_to']._serialized_options = b'\xc8\xde\x1f\x00'
    _GAUGE.fields_by_name['coins']._options = None
    _GAUGE.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _GAUGE.fields_by_name['start_time']._options = None
    _GAUGE.fields_by_name['start_time']._serialized_options = b'\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x11yaml:"start_time"'
    _GAUGE.fields_by_name['distributed_coins']._options = None
    _GAUGE.fields_by_name['distributed_coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _LOCKABLEDURATIONSINFO.fields_by_name['lockable_durations']._options = None
    _LOCKABLEDURATIONSINFO.fields_by_name['lockable_durations']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x19yaml:"lockable_durations"'
    _GAUGE._serialized_start = 201
    _GAUGE._serialized_end = 631
    _LOCKABLEDURATIONSINFO._serialized_start = 633
    _LOCKABLEDURATIONSINFO._serialized_end = 750

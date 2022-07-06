
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ...cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ...osmosis.incentives import gauge_pb2 as osmosis_dot_incentives_dot_gauge__pb2
from ...osmosis.lockup import lock_pb2 as osmosis_dot_lockup_dot_lock__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bosmosis/incentives/tx.proto\x12\x12osmosis.incentives\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1eosmosis/incentives/gauge.proto\x1a\x19osmosis/lockup/lock.proto"\xcc\x02\n\x0eMsgCreateGauge\x12\x14\n\x0cis_perpetual\x18\x01 \x01(\x08\x12\x1f\n\x05owner\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12;\n\rdistribute_to\x18\x03 \x01(\x0b2\x1e.osmosis.lockup.QueryConditionB\x04\xc8\xde\x1f\x00\x12Z\n\x05coins\x18\x04 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12L\n\nstart_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1c\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"\x12\x1c\n\x14num_epochs_paid_over\x18\x06 \x01(\x04"\x18\n\x16MsgCreateGaugeResponse"\xa0\x01\n\rMsgAddToGauge\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12\x10\n\x08gauge_id\x18\x02 \x01(\x04\x12\\\n\x07rewards\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\x17\n\x15MsgAddToGaugeResponse2\xc0\x01\n\x03Msg\x12]\n\x0bCreateGauge\x12".osmosis.incentives.MsgCreateGauge\x1a*.osmosis.incentives.MsgCreateGaugeResponse\x12Z\n\nAddToGauge\x12!.osmosis.incentives.MsgAddToGauge\x1a).osmosis.incentives.MsgAddToGaugeResponseB7Z5github.com/osmosis-labs/osmosis/v7/x/incentives/typesb\x06proto3')
_MSGCREATEGAUGE = DESCRIPTOR.message_types_by_name['MsgCreateGauge']
_MSGCREATEGAUGERESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateGaugeResponse']
_MSGADDTOGAUGE = DESCRIPTOR.message_types_by_name['MsgAddToGauge']
_MSGADDTOGAUGERESPONSE = DESCRIPTOR.message_types_by_name['MsgAddToGaugeResponse']
MsgCreateGauge = _reflection.GeneratedProtocolMessageType('MsgCreateGauge', (_message.Message,), {'DESCRIPTOR': _MSGCREATEGAUGE, '__module__': 'osmosis.incentives.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateGauge)
MsgCreateGaugeResponse = _reflection.GeneratedProtocolMessageType('MsgCreateGaugeResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATEGAUGERESPONSE, '__module__': 'osmosis.incentives.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateGaugeResponse)
MsgAddToGauge = _reflection.GeneratedProtocolMessageType('MsgAddToGauge', (_message.Message,), {'DESCRIPTOR': _MSGADDTOGAUGE, '__module__': 'osmosis.incentives.tx_pb2'})
_sym_db.RegisterMessage(MsgAddToGauge)
MsgAddToGaugeResponse = _reflection.GeneratedProtocolMessageType('MsgAddToGaugeResponse', (_message.Message,), {'DESCRIPTOR': _MSGADDTOGAUGERESPONSE, '__module__': 'osmosis.incentives.tx_pb2'})
_sym_db.RegisterMessage(MsgAddToGaugeResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/osmosis-labs/osmosis/v7/x/incentives/types'
    _MSGCREATEGAUGE.fields_by_name['owner']._options = None
    _MSGCREATEGAUGE.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGCREATEGAUGE.fields_by_name['distribute_to']._options = None
    _MSGCREATEGAUGE.fields_by_name['distribute_to']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCREATEGAUGE.fields_by_name['coins']._options = None
    _MSGCREATEGAUGE.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGCREATEGAUGE.fields_by_name['start_time']._options = None
    _MSGCREATEGAUGE.fields_by_name['start_time']._serialized_options = b'\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"'
    _MSGADDTOGAUGE.fields_by_name['owner']._options = None
    _MSGADDTOGAUGE.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGADDTOGAUGE.fields_by_name['rewards']._options = None
    _MSGADDTOGAUGE.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGCREATEGAUGE._serialized_start = 198
    _MSGCREATEGAUGE._serialized_end = 530
    _MSGCREATEGAUGERESPONSE._serialized_start = 532
    _MSGCREATEGAUGERESPONSE._serialized_end = 556
    _MSGADDTOGAUGE._serialized_start = 559
    _MSGADDTOGAUGE._serialized_end = 719
    _MSGADDTOGAUGERESPONSE._serialized_start = 721
    _MSGADDTOGAUGERESPONSE._serialized_end = 744
    _MSG._serialized_start = 747
    _MSG._serialized_end = 939

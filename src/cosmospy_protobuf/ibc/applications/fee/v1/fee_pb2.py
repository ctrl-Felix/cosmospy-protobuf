
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!ibc/applications/fee/v1/fee.proto\x12\x17ibc.applications.fee.v1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a!ibc/core/channel/v1/channel.proto"\xdf\x02\n\x03Fee\x12p\n\x08recv_fee\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBC\xf2\xde\x1f\x0fyaml:"recv_fee"\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12n\n\x07ack_fee\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBB\xf2\xde\x1f\x0eyaml:"ack_fee"\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12v\n\x0btimeout_fee\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBF\xf2\xde\x1f\x12yaml:"timeout_fee"\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\x81\x01\n\tPacketFee\x12/\n\x03fee\x18\x01 \x01(\x0b2\x1c.ibc.applications.fee.v1.FeeB\x04\xc8\xde\x1f\x00\x121\n\x0erefund_address\x18\x02 \x01(\tB\x19\xf2\xde\x1f\x15yaml:"refund_address"\x12\x10\n\x08relayers\x18\x03 \x03(\t"a\n\nPacketFees\x12S\n\x0bpacket_fees\x18\x01 \x03(\x0b2".ibc.applications.fee.v1.PacketFeeB\x1a\xf2\xde\x1f\x12yaml:"packet_fees"\xc8\xde\x1f\x00"\xb7\x01\n\x14IdentifiedPacketFees\x12J\n\tpacket_id\x18\x01 \x01(\x0b2\x1d.ibc.core.channel.v1.PacketIdB\x18\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"packet_id"\x12S\n\x0bpacket_fees\x18\x02 \x03(\x0b2".ibc.applications.fee.v1.PacketFeeB\x1a\xf2\xde\x1f\x12yaml:"packet_fees"\xc8\xde\x1f\x00B7Z5github.com/cosmos/ibc-go/v3/modules/apps/29-fee/typesb\x06proto3')
_FEE = DESCRIPTOR.message_types_by_name['Fee']
_PACKETFEE = DESCRIPTOR.message_types_by_name['PacketFee']
_PACKETFEES = DESCRIPTOR.message_types_by_name['PacketFees']
_IDENTIFIEDPACKETFEES = DESCRIPTOR.message_types_by_name['IdentifiedPacketFees']
Fee = _reflection.GeneratedProtocolMessageType('Fee', (_message.Message,), {'DESCRIPTOR': _FEE, '__module__': 'ibc.applications.fee.v1.fee_pb2'})
_sym_db.RegisterMessage(Fee)
PacketFee = _reflection.GeneratedProtocolMessageType('PacketFee', (_message.Message,), {'DESCRIPTOR': _PACKETFEE, '__module__': 'ibc.applications.fee.v1.fee_pb2'})
_sym_db.RegisterMessage(PacketFee)
PacketFees = _reflection.GeneratedProtocolMessageType('PacketFees', (_message.Message,), {'DESCRIPTOR': _PACKETFEES, '__module__': 'ibc.applications.fee.v1.fee_pb2'})
_sym_db.RegisterMessage(PacketFees)
IdentifiedPacketFees = _reflection.GeneratedProtocolMessageType('IdentifiedPacketFees', (_message.Message,), {'DESCRIPTOR': _IDENTIFIEDPACKETFEES, '__module__': 'ibc.applications.fee.v1.fee_pb2'})
_sym_db.RegisterMessage(IdentifiedPacketFees)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/cosmos/ibc-go/v3/modules/apps/29-fee/types'
    _FEE.fields_by_name['recv_fee']._options = None
    _FEE.fields_by_name['recv_fee']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"recv_fee"\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _FEE.fields_by_name['ack_fee']._options = None
    _FEE.fields_by_name['ack_fee']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"ack_fee"\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _FEE.fields_by_name['timeout_fee']._options = None
    _FEE.fields_by_name['timeout_fee']._serialized_options = b'\xf2\xde\x1f\x12yaml:"timeout_fee"\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _PACKETFEE.fields_by_name['fee']._options = None
    _PACKETFEE.fields_by_name['fee']._serialized_options = b'\xc8\xde\x1f\x00'
    _PACKETFEE.fields_by_name['refund_address']._options = None
    _PACKETFEE.fields_by_name['refund_address']._serialized_options = b'\xf2\xde\x1f\x15yaml:"refund_address"'
    _PACKETFEES.fields_by_name['packet_fees']._options = None
    _PACKETFEES.fields_by_name['packet_fees']._serialized_options = b'\xf2\xde\x1f\x12yaml:"packet_fees"\xc8\xde\x1f\x00'
    _IDENTIFIEDPACKETFEES.fields_by_name['packet_id']._options = None
    _IDENTIFIEDPACKETFEES.fields_by_name['packet_id']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"packet_id"'
    _IDENTIFIEDPACKETFEES.fields_by_name['packet_fees']._options = None
    _IDENTIFIEDPACKETFEES.fields_by_name['packet_fees']._serialized_options = b'\xf2\xde\x1f\x12yaml:"packet_fees"\xc8\xde\x1f\x00'
    _FEE._serialized_start = 152
    _FEE._serialized_end = 503
    _PACKETFEE._serialized_start = 506
    _PACKETFEE._serialized_end = 635
    _PACKETFEES._serialized_start = 637
    _PACKETFEES._serialized_end = 734
    _IDENTIFIEDPACKETFEES._serialized_start = 737
    _IDENTIFIEDPACKETFEES._serialized_end = 920


'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from .....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from .....ibc.applications.fee.v1 import fee_pb2 as ibc_dot_applications_dot_fee_dot_v1_dot_fee__pb2
from .....ibc.applications.fee.v1 import genesis_pb2 as ibc_dot_applications_dot_fee_dot_v1_dot_genesis__pb2
from .....ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#ibc/applications/fee/v1/query.proto\x12\x17ibc.applications.fee.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a!ibc/applications/fee/v1/fee.proto\x1a%ibc/applications/fee/v1/genesis.proto\x1a!ibc/core/channel/v1/channel.proto"s\n\x1fQueryIncentivizedPacketsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest\x12\x14\n\x0cquery_height\x18\x02 \x01(\x04"u\n QueryIncentivizedPacketsResponse\x12Q\n\x14incentivized_packets\x18\x01 \x03(\x0b2-.ibc.applications.fee.v1.IdentifiedPacketFeesB\x04\xc8\xde\x1f\x00"n\n\x1eQueryIncentivizedPacketRequest\x126\n\tpacket_id\x18\x01 \x01(\x0b2\x1d.ibc.core.channel.v1.PacketIdB\x04\xc8\xde\x1f\x00\x12\x14\n\x0cquery_height\x18\x02 \x01(\x04"s\n\x1fQueryIncentivizedPacketResponse\x12P\n\x13incentivized_packet\x18\x01 \x01(\x0b2-.ibc.applications.fee.v1.IdentifiedPacketFeesB\x04\xc8\xde\x1f\x00"\xa2\x01\n)QueryIncentivizedPacketsForChannelRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest\x12\x0f\n\x07port_id\x18\x02 \x01(\t\x12\x12\n\nchannel_id\x18\x03 \x01(\t\x12\x14\n\x0cquery_height\x18\x04 \x01(\x04"y\n*QueryIncentivizedPacketsForChannelResponse\x12K\n\x14incentivized_packets\x18\x01 \x03(\x0b2-.ibc.applications.fee.v1.IdentifiedPacketFees"S\n\x19QueryTotalRecvFeesRequest\x126\n\tpacket_id\x18\x01 \x01(\x0b2\x1d.ibc.core.channel.v1.PacketIdB\x04\xc8\xde\x1f\x00"\x90\x01\n\x1aQueryTotalRecvFeesResponse\x12r\n\trecv_fees\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBD\xf2\xde\x1f\x10yaml:"recv_fees"\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"R\n\x18QueryTotalAckFeesRequest\x126\n\tpacket_id\x18\x01 \x01(\x0b2\x1d.ibc.core.channel.v1.PacketIdB\x04\xc8\xde\x1f\x00"\x8d\x01\n\x19QueryTotalAckFeesResponse\x12p\n\x08ack_fees\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBC\xf2\xde\x1f\x0fyaml:"ack_fees"\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"V\n\x1cQueryTotalTimeoutFeesRequest\x126\n\tpacket_id\x18\x01 \x01(\x0b2\x1d.ibc.core.channel.v1.PacketIdB\x04\xc8\xde\x1f\x00"\x99\x01\n\x1dQueryTotalTimeoutFeesResponse\x12x\n\x0ctimeout_fees\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBG\xf2\xde\x1f\x13yaml:"timeout_fees"\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\x81\x01\n\x1fQueryCounterpartyAddressRequest\x12)\n\nchannel_id\x18\x01 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id"\x123\n\x0frelayer_address\x18\x02 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"relayer_address""a\n QueryCounterpartyAddressResponse\x12=\n\x14counterparty_address\x18\x01 \x01(\tB\x1f\xf2\xde\x1f\x1byaml:"counterparty_address""r\n\x1eQueryFeeEnabledChannelsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest\x12\x14\n\x0cquery_height\x18\x02 \x01(\x04"\x90\x01\n\x1fQueryFeeEnabledChannelsResponse\x12m\n\x14fee_enabled_channels\x18\x01 \x03(\x0b2*.ibc.applications.fee.v1.FeeEnabledChannelB#\xf2\xde\x1f\x1byaml:"fee_enabled_channels"\xc8\xde\x1f\x00"o\n\x1dQueryFeeEnabledChannelRequest\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"port_id"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id""M\n\x1eQueryFeeEnabledChannelResponse\x12+\n\x0bfee_enabled\x18\x01 \x01(\x08B\x16\xf2\xde\x1f\x12yaml:"fee_enabled"2\xae\x10\n\x05Query\x12\xb9\x01\n\x13IncentivizedPackets\x128.ibc.applications.fee.v1.QueryIncentivizedPacketsRequest\x1a9.ibc.applications.fee.v1.QueryIncentivizedPacketsResponse"-\x82\xd3\xe4\x93\x02\'\x12%/ibc/apps/fee/v1/incentivized_packets\x12\x8c\x02\n\x12IncentivizedPacket\x127.ibc.applications.fee.v1.QueryIncentivizedPacketRequest\x1a8.ibc.applications.fee.v1.QueryIncentivizedPacketResponse"\x82\x01\x82\xd3\xe4\x93\x02|\x12z/ibc/apps/fee/v1/incentivized_packet/port/{packet_id.port_id}/channel/{packet_id.channel_id}/sequence/{packet_id.sequence}\x12\xfb\x01\n\x1dIncentivizedPacketsForChannel\x12B.ibc.applications.fee.v1.QueryIncentivizedPacketsForChannelRequest\x1aC.ibc.applications.fee.v1.QueryIncentivizedPacketsForChannelResponse"Q\x82\xd3\xe4\x93\x02K\x12I/ibc/apps/fee/v1/incentivized_packets/port/{port_id}/channel/{channel_id}\x12\xf8\x01\n\rTotalRecvFees\x122.ibc.applications.fee.v1.QueryTotalRecvFeesRequest\x1a3.ibc.applications.fee.v1.QueryTotalRecvFeesResponse"~\x82\xd3\xe4\x93\x02x\x12v/ibc/apps/fee/v1/total_recv_fees/port/{packet_id.port_id}/channel/{packet_id.channel_id}/sequence/{packet_id.sequence}\x12\xf4\x01\n\x0cTotalAckFees\x121.ibc.applications.fee.v1.QueryTotalAckFeesRequest\x1a2.ibc.applications.fee.v1.QueryTotalAckFeesResponse"}\x82\xd3\xe4\x93\x02w\x12u/ibc/apps/fee/v1/total_ack_fees/port/{packet_id.port_id}/channel/{packet_id.channel_id}/sequence/{packet_id.sequence}\x12\x85\x02\n\x10TotalTimeoutFees\x125.ibc.applications.fee.v1.QueryTotalTimeoutFeesRequest\x1a6.ibc.applications.fee.v1.QueryTotalTimeoutFeesResponse"\x81\x01\x82\xd3\xe4\x93\x02{\x12y/ibc/apps/fee/v1/total_timeout_fees/port/{packet_id.port_id}/channel/{packet_id.channel_id}/sequence/{packet_id.sequence}\x12\xe0\x01\n\x13CounterpartyAddress\x128.ibc.applications.fee.v1.QueryCounterpartyAddressRequest\x1a9.ibc.applications.fee.v1.QueryCounterpartyAddressResponse"T\x82\xd3\xe4\x93\x02N\x12L/ibc/apps/fee/v1/counterparty_address/{relayer_address}/channel/{channel_id}\x12\xad\x01\n\x12FeeEnabledChannels\x127.ibc.applications.fee.v1.QueryFeeEnabledChannelsRequest\x1a8.ibc.applications.fee.v1.QueryFeeEnabledChannelsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/ibc/apps/fee/v1/fee_enabled\x12\xce\x01\n\x11FeeEnabledChannel\x126.ibc.applications.fee.v1.QueryFeeEnabledChannelRequest\x1a7.ibc.applications.fee.v1.QueryFeeEnabledChannelResponse"H\x82\xd3\xe4\x93\x02B\x12@/ibc/apps/fee/v1/fee_enabled/port/{port_id}/channel/{channel_id}B7Z5github.com/cosmos/ibc-go/v3/modules/apps/29-fee/typesb\x06proto3')
_QUERYINCENTIVIZEDPACKETSREQUEST = DESCRIPTOR.message_types_by_name['QueryIncentivizedPacketsRequest']
_QUERYINCENTIVIZEDPACKETSRESPONSE = DESCRIPTOR.message_types_by_name['QueryIncentivizedPacketsResponse']
_QUERYINCENTIVIZEDPACKETREQUEST = DESCRIPTOR.message_types_by_name['QueryIncentivizedPacketRequest']
_QUERYINCENTIVIZEDPACKETRESPONSE = DESCRIPTOR.message_types_by_name['QueryIncentivizedPacketResponse']
_QUERYINCENTIVIZEDPACKETSFORCHANNELREQUEST = DESCRIPTOR.message_types_by_name['QueryIncentivizedPacketsForChannelRequest']
_QUERYINCENTIVIZEDPACKETSFORCHANNELRESPONSE = DESCRIPTOR.message_types_by_name['QueryIncentivizedPacketsForChannelResponse']
_QUERYTOTALRECVFEESREQUEST = DESCRIPTOR.message_types_by_name['QueryTotalRecvFeesRequest']
_QUERYTOTALRECVFEESRESPONSE = DESCRIPTOR.message_types_by_name['QueryTotalRecvFeesResponse']
_QUERYTOTALACKFEESREQUEST = DESCRIPTOR.message_types_by_name['QueryTotalAckFeesRequest']
_QUERYTOTALACKFEESRESPONSE = DESCRIPTOR.message_types_by_name['QueryTotalAckFeesResponse']
_QUERYTOTALTIMEOUTFEESREQUEST = DESCRIPTOR.message_types_by_name['QueryTotalTimeoutFeesRequest']
_QUERYTOTALTIMEOUTFEESRESPONSE = DESCRIPTOR.message_types_by_name['QueryTotalTimeoutFeesResponse']
_QUERYCOUNTERPARTYADDRESSREQUEST = DESCRIPTOR.message_types_by_name['QueryCounterpartyAddressRequest']
_QUERYCOUNTERPARTYADDRESSRESPONSE = DESCRIPTOR.message_types_by_name['QueryCounterpartyAddressResponse']
_QUERYFEEENABLEDCHANNELSREQUEST = DESCRIPTOR.message_types_by_name['QueryFeeEnabledChannelsRequest']
_QUERYFEEENABLEDCHANNELSRESPONSE = DESCRIPTOR.message_types_by_name['QueryFeeEnabledChannelsResponse']
_QUERYFEEENABLEDCHANNELREQUEST = DESCRIPTOR.message_types_by_name['QueryFeeEnabledChannelRequest']
_QUERYFEEENABLEDCHANNELRESPONSE = DESCRIPTOR.message_types_by_name['QueryFeeEnabledChannelResponse']
QueryIncentivizedPacketsRequest = _reflection.GeneratedProtocolMessageType('QueryIncentivizedPacketsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYINCENTIVIZEDPACKETSREQUEST, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryIncentivizedPacketsRequest)
QueryIncentivizedPacketsResponse = _reflection.GeneratedProtocolMessageType('QueryIncentivizedPacketsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYINCENTIVIZEDPACKETSRESPONSE, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryIncentivizedPacketsResponse)
QueryIncentivizedPacketRequest = _reflection.GeneratedProtocolMessageType('QueryIncentivizedPacketRequest', (_message.Message,), {'DESCRIPTOR': _QUERYINCENTIVIZEDPACKETREQUEST, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryIncentivizedPacketRequest)
QueryIncentivizedPacketResponse = _reflection.GeneratedProtocolMessageType('QueryIncentivizedPacketResponse', (_message.Message,), {'DESCRIPTOR': _QUERYINCENTIVIZEDPACKETRESPONSE, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryIncentivizedPacketResponse)
QueryIncentivizedPacketsForChannelRequest = _reflection.GeneratedProtocolMessageType('QueryIncentivizedPacketsForChannelRequest', (_message.Message,), {'DESCRIPTOR': _QUERYINCENTIVIZEDPACKETSFORCHANNELREQUEST, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryIncentivizedPacketsForChannelRequest)
QueryIncentivizedPacketsForChannelResponse = _reflection.GeneratedProtocolMessageType('QueryIncentivizedPacketsForChannelResponse', (_message.Message,), {'DESCRIPTOR': _QUERYINCENTIVIZEDPACKETSFORCHANNELRESPONSE, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryIncentivizedPacketsForChannelResponse)
QueryTotalRecvFeesRequest = _reflection.GeneratedProtocolMessageType('QueryTotalRecvFeesRequest', (_message.Message,), {'DESCRIPTOR': _QUERYTOTALRECVFEESREQUEST, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryTotalRecvFeesRequest)
QueryTotalRecvFeesResponse = _reflection.GeneratedProtocolMessageType('QueryTotalRecvFeesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYTOTALRECVFEESRESPONSE, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryTotalRecvFeesResponse)
QueryTotalAckFeesRequest = _reflection.GeneratedProtocolMessageType('QueryTotalAckFeesRequest', (_message.Message,), {'DESCRIPTOR': _QUERYTOTALACKFEESREQUEST, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryTotalAckFeesRequest)
QueryTotalAckFeesResponse = _reflection.GeneratedProtocolMessageType('QueryTotalAckFeesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYTOTALACKFEESRESPONSE, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryTotalAckFeesResponse)
QueryTotalTimeoutFeesRequest = _reflection.GeneratedProtocolMessageType('QueryTotalTimeoutFeesRequest', (_message.Message,), {'DESCRIPTOR': _QUERYTOTALTIMEOUTFEESREQUEST, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryTotalTimeoutFeesRequest)
QueryTotalTimeoutFeesResponse = _reflection.GeneratedProtocolMessageType('QueryTotalTimeoutFeesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYTOTALTIMEOUTFEESRESPONSE, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryTotalTimeoutFeesResponse)
QueryCounterpartyAddressRequest = _reflection.GeneratedProtocolMessageType('QueryCounterpartyAddressRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCOUNTERPARTYADDRESSREQUEST, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryCounterpartyAddressRequest)
QueryCounterpartyAddressResponse = _reflection.GeneratedProtocolMessageType('QueryCounterpartyAddressResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCOUNTERPARTYADDRESSRESPONSE, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryCounterpartyAddressResponse)
QueryFeeEnabledChannelsRequest = _reflection.GeneratedProtocolMessageType('QueryFeeEnabledChannelsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYFEEENABLEDCHANNELSREQUEST, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryFeeEnabledChannelsRequest)
QueryFeeEnabledChannelsResponse = _reflection.GeneratedProtocolMessageType('QueryFeeEnabledChannelsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYFEEENABLEDCHANNELSRESPONSE, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryFeeEnabledChannelsResponse)
QueryFeeEnabledChannelRequest = _reflection.GeneratedProtocolMessageType('QueryFeeEnabledChannelRequest', (_message.Message,), {'DESCRIPTOR': _QUERYFEEENABLEDCHANNELREQUEST, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryFeeEnabledChannelRequest)
QueryFeeEnabledChannelResponse = _reflection.GeneratedProtocolMessageType('QueryFeeEnabledChannelResponse', (_message.Message,), {'DESCRIPTOR': _QUERYFEEENABLEDCHANNELRESPONSE, '__module__': 'ibc.applications.fee.v1.query_pb2'})
_sym_db.RegisterMessage(QueryFeeEnabledChannelResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/cosmos/ibc-go/v3/modules/apps/29-fee/types'
    _QUERYINCENTIVIZEDPACKETSRESPONSE.fields_by_name['incentivized_packets']._options = None
    _QUERYINCENTIVIZEDPACKETSRESPONSE.fields_by_name['incentivized_packets']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYINCENTIVIZEDPACKETREQUEST.fields_by_name['packet_id']._options = None
    _QUERYINCENTIVIZEDPACKETREQUEST.fields_by_name['packet_id']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYINCENTIVIZEDPACKETRESPONSE.fields_by_name['incentivized_packet']._options = None
    _QUERYINCENTIVIZEDPACKETRESPONSE.fields_by_name['incentivized_packet']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYTOTALRECVFEESREQUEST.fields_by_name['packet_id']._options = None
    _QUERYTOTALRECVFEESREQUEST.fields_by_name['packet_id']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYTOTALRECVFEESRESPONSE.fields_by_name['recv_fees']._options = None
    _QUERYTOTALRECVFEESRESPONSE.fields_by_name['recv_fees']._serialized_options = b'\xf2\xde\x1f\x10yaml:"recv_fees"\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYTOTALACKFEESREQUEST.fields_by_name['packet_id']._options = None
    _QUERYTOTALACKFEESREQUEST.fields_by_name['packet_id']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYTOTALACKFEESRESPONSE.fields_by_name['ack_fees']._options = None
    _QUERYTOTALACKFEESRESPONSE.fields_by_name['ack_fees']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"ack_fees"\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYTOTALTIMEOUTFEESREQUEST.fields_by_name['packet_id']._options = None
    _QUERYTOTALTIMEOUTFEESREQUEST.fields_by_name['packet_id']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYTOTALTIMEOUTFEESRESPONSE.fields_by_name['timeout_fees']._options = None
    _QUERYTOTALTIMEOUTFEESRESPONSE.fields_by_name['timeout_fees']._serialized_options = b'\xf2\xde\x1f\x13yaml:"timeout_fees"\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYCOUNTERPARTYADDRESSREQUEST.fields_by_name['channel_id']._options = None
    _QUERYCOUNTERPARTYADDRESSREQUEST.fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _QUERYCOUNTERPARTYADDRESSREQUEST.fields_by_name['relayer_address']._options = None
    _QUERYCOUNTERPARTYADDRESSREQUEST.fields_by_name['relayer_address']._serialized_options = b'\xf2\xde\x1f\x16yaml:"relayer_address"'
    _QUERYCOUNTERPARTYADDRESSRESPONSE.fields_by_name['counterparty_address']._options = None
    _QUERYCOUNTERPARTYADDRESSRESPONSE.fields_by_name['counterparty_address']._serialized_options = b'\xf2\xde\x1f\x1byaml:"counterparty_address"'
    _QUERYFEEENABLEDCHANNELSRESPONSE.fields_by_name['fee_enabled_channels']._options = None
    _QUERYFEEENABLEDCHANNELSRESPONSE.fields_by_name['fee_enabled_channels']._serialized_options = b'\xf2\xde\x1f\x1byaml:"fee_enabled_channels"\xc8\xde\x1f\x00'
    _QUERYFEEENABLEDCHANNELREQUEST.fields_by_name['port_id']._options = None
    _QUERYFEEENABLEDCHANNELREQUEST.fields_by_name['port_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"port_id"'
    _QUERYFEEENABLEDCHANNELREQUEST.fields_by_name['channel_id']._options = None
    _QUERYFEEENABLEDCHANNELREQUEST.fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _QUERYFEEENABLEDCHANNELRESPONSE.fields_by_name['fee_enabled']._options = None
    _QUERYFEEENABLEDCHANNELRESPONSE.fields_by_name['fee_enabled']._serialized_options = b'\xf2\xde\x1f\x12yaml:"fee_enabled"'
    _QUERY.methods_by_name['IncentivizedPackets']._options = None
    _QUERY.methods_by_name['IncentivizedPackets']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/ibc/apps/fee/v1/incentivized_packets"
    _QUERY.methods_by_name['IncentivizedPacket']._options = None
    _QUERY.methods_by_name['IncentivizedPacket']._serialized_options = b'\x82\xd3\xe4\x93\x02|\x12z/ibc/apps/fee/v1/incentivized_packet/port/{packet_id.port_id}/channel/{packet_id.channel_id}/sequence/{packet_id.sequence}'
    _QUERY.methods_by_name['IncentivizedPacketsForChannel']._options = None
    _QUERY.methods_by_name['IncentivizedPacketsForChannel']._serialized_options = b'\x82\xd3\xe4\x93\x02K\x12I/ibc/apps/fee/v1/incentivized_packets/port/{port_id}/channel/{channel_id}'
    _QUERY.methods_by_name['TotalRecvFees']._options = None
    _QUERY.methods_by_name['TotalRecvFees']._serialized_options = b'\x82\xd3\xe4\x93\x02x\x12v/ibc/apps/fee/v1/total_recv_fees/port/{packet_id.port_id}/channel/{packet_id.channel_id}/sequence/{packet_id.sequence}'
    _QUERY.methods_by_name['TotalAckFees']._options = None
    _QUERY.methods_by_name['TotalAckFees']._serialized_options = b'\x82\xd3\xe4\x93\x02w\x12u/ibc/apps/fee/v1/total_ack_fees/port/{packet_id.port_id}/channel/{packet_id.channel_id}/sequence/{packet_id.sequence}'
    _QUERY.methods_by_name['TotalTimeoutFees']._options = None
    _QUERY.methods_by_name['TotalTimeoutFees']._serialized_options = b'\x82\xd3\xe4\x93\x02{\x12y/ibc/apps/fee/v1/total_timeout_fees/port/{packet_id.port_id}/channel/{packet_id.channel_id}/sequence/{packet_id.sequence}'
    _QUERY.methods_by_name['CounterpartyAddress']._options = None
    _QUERY.methods_by_name['CounterpartyAddress']._serialized_options = b'\x82\xd3\xe4\x93\x02N\x12L/ibc/apps/fee/v1/counterparty_address/{relayer_address}/channel/{channel_id}'
    _QUERY.methods_by_name['FeeEnabledChannels']._options = None
    _QUERY.methods_by_name['FeeEnabledChannels']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/ibc/apps/fee/v1/fee_enabled'
    _QUERY.methods_by_name['FeeEnabledChannel']._options = None
    _QUERY.methods_by_name['FeeEnabledChannel']._serialized_options = b'\x82\xd3\xe4\x93\x02B\x12@/ibc/apps/fee/v1/fee_enabled/port/{port_id}/channel/{channel_id}'
    _QUERYINCENTIVIZEDPACKETSREQUEST._serialized_start = 301
    _QUERYINCENTIVIZEDPACKETSREQUEST._serialized_end = 416
    _QUERYINCENTIVIZEDPACKETSRESPONSE._serialized_start = 418
    _QUERYINCENTIVIZEDPACKETSRESPONSE._serialized_end = 535
    _QUERYINCENTIVIZEDPACKETREQUEST._serialized_start = 537
    _QUERYINCENTIVIZEDPACKETREQUEST._serialized_end = 647
    _QUERYINCENTIVIZEDPACKETRESPONSE._serialized_start = 649
    _QUERYINCENTIVIZEDPACKETRESPONSE._serialized_end = 764
    _QUERYINCENTIVIZEDPACKETSFORCHANNELREQUEST._serialized_start = 767
    _QUERYINCENTIVIZEDPACKETSFORCHANNELREQUEST._serialized_end = 929
    _QUERYINCENTIVIZEDPACKETSFORCHANNELRESPONSE._serialized_start = 931
    _QUERYINCENTIVIZEDPACKETSFORCHANNELRESPONSE._serialized_end = 1052
    _QUERYTOTALRECVFEESREQUEST._serialized_start = 1054
    _QUERYTOTALRECVFEESREQUEST._serialized_end = 1137
    _QUERYTOTALRECVFEESRESPONSE._serialized_start = 1140
    _QUERYTOTALRECVFEESRESPONSE._serialized_end = 1284
    _QUERYTOTALACKFEESREQUEST._serialized_start = 1286
    _QUERYTOTALACKFEESREQUEST._serialized_end = 1368
    _QUERYTOTALACKFEESRESPONSE._serialized_start = 1371
    _QUERYTOTALACKFEESRESPONSE._serialized_end = 1512
    _QUERYTOTALTIMEOUTFEESREQUEST._serialized_start = 1514
    _QUERYTOTALTIMEOUTFEESREQUEST._serialized_end = 1600
    _QUERYTOTALTIMEOUTFEESRESPONSE._serialized_start = 1603
    _QUERYTOTALTIMEOUTFEESRESPONSE._serialized_end = 1756
    _QUERYCOUNTERPARTYADDRESSREQUEST._serialized_start = 1759
    _QUERYCOUNTERPARTYADDRESSREQUEST._serialized_end = 1888
    _QUERYCOUNTERPARTYADDRESSRESPONSE._serialized_start = 1890
    _QUERYCOUNTERPARTYADDRESSRESPONSE._serialized_end = 1987
    _QUERYFEEENABLEDCHANNELSREQUEST._serialized_start = 1989
    _QUERYFEEENABLEDCHANNELSREQUEST._serialized_end = 2103
    _QUERYFEEENABLEDCHANNELSRESPONSE._serialized_start = 2106
    _QUERYFEEENABLEDCHANNELSRESPONSE._serialized_end = 2250
    _QUERYFEEENABLEDCHANNELREQUEST._serialized_start = 2252
    _QUERYFEEENABLEDCHANNELREQUEST._serialized_end = 2363
    _QUERYFEEENABLEDCHANNELRESPONSE._serialized_start = 2365
    _QUERYFEEENABLEDCHANNELRESPONSE._serialized_end = 2442
    _QUERY._serialized_start = 2445
    _QUERY._serialized_end = 4539

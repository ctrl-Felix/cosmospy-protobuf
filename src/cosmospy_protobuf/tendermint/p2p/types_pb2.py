
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1atendermint/p2p/types.proto\x12\x0etendermint.p2p\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto"C\n\x0fProtocolVersion\x12\x14\n\x03p2p\x18\x01 \x01(\x04B\x07\xe2\xde\x1f\x03P2P\x12\r\n\x05block\x18\x02 \x01(\x04\x12\x0b\n\x03app\x18\x03 \x01(\x04"\xf6\x01\n\x08NodeInfo\x12?\n\x10protocol_version\x18\x01 \x01(\x0b2\x1f.tendermint.p2p.ProtocolVersionB\x04\xc8\xde\x1f\x00\x12\x1b\n\x07node_id\x18\x02 \x01(\tB\n\xe2\xde\x1f\x06NodeID\x12\x13\n\x0blisten_addr\x18\x03 \x01(\t\x12\x0f\n\x07network\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x10\n\x08channels\x18\x06 \x01(\x0c\x12\x0f\n\x07moniker\x18\x07 \x01(\t\x122\n\x05other\x18\x08 \x01(\x0b2\x1d.tendermint.p2p.NodeInfoOtherB\x04\xc8\xde\x1f\x00"F\n\rNodeInfoOther\x12\x10\n\x08tx_index\x18\x01 \x01(\t\x12#\n\x0brpc_address\x18\x02 \x01(\tB\x0e\xe2\xde\x1f\nRPCAddress"\x8f\x01\n\x08PeerInfo\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xe2\xde\x1f\x02ID\x125\n\x0caddress_info\x18\x02 \x03(\x0b2\x1f.tendermint.p2p.PeerAddressInfo\x128\n\x0elast_connected\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01"\xb3\x01\n\x0fPeerAddressInfo\x12\x0f\n\x07address\x18\x01 \x01(\t\x12;\n\x11last_dial_success\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\x12;\n\x11last_dial_failure\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\x12\x15\n\rdial_failures\x18\x04 \x01(\rB7Z5github.com/tendermint/tendermint/proto/tendermint/p2pb\x06proto3')
_PROTOCOLVERSION = DESCRIPTOR.message_types_by_name['ProtocolVersion']
_NODEINFO = DESCRIPTOR.message_types_by_name['NodeInfo']
_NODEINFOOTHER = DESCRIPTOR.message_types_by_name['NodeInfoOther']
_PEERINFO = DESCRIPTOR.message_types_by_name['PeerInfo']
_PEERADDRESSINFO = DESCRIPTOR.message_types_by_name['PeerAddressInfo']
ProtocolVersion = _reflection.GeneratedProtocolMessageType('ProtocolVersion', (_message.Message,), {'DESCRIPTOR': _PROTOCOLVERSION, '__module__': 'tendermint.p2p.types_pb2'})
_sym_db.RegisterMessage(ProtocolVersion)
NodeInfo = _reflection.GeneratedProtocolMessageType('NodeInfo', (_message.Message,), {'DESCRIPTOR': _NODEINFO, '__module__': 'tendermint.p2p.types_pb2'})
_sym_db.RegisterMessage(NodeInfo)
NodeInfoOther = _reflection.GeneratedProtocolMessageType('NodeInfoOther', (_message.Message,), {'DESCRIPTOR': _NODEINFOOTHER, '__module__': 'tendermint.p2p.types_pb2'})
_sym_db.RegisterMessage(NodeInfoOther)
PeerInfo = _reflection.GeneratedProtocolMessageType('PeerInfo', (_message.Message,), {'DESCRIPTOR': _PEERINFO, '__module__': 'tendermint.p2p.types_pb2'})
_sym_db.RegisterMessage(PeerInfo)
PeerAddressInfo = _reflection.GeneratedProtocolMessageType('PeerAddressInfo', (_message.Message,), {'DESCRIPTOR': _PEERADDRESSINFO, '__module__': 'tendermint.p2p.types_pb2'})
_sym_db.RegisterMessage(PeerAddressInfo)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/tendermint/tendermint/proto/tendermint/p2p'
    _PROTOCOLVERSION.fields_by_name['p2p']._options = None
    _PROTOCOLVERSION.fields_by_name['p2p']._serialized_options = b'\xe2\xde\x1f\x03P2P'
    _NODEINFO.fields_by_name['protocol_version']._options = None
    _NODEINFO.fields_by_name['protocol_version']._serialized_options = b'\xc8\xde\x1f\x00'
    _NODEINFO.fields_by_name['node_id']._options = None
    _NODEINFO.fields_by_name['node_id']._serialized_options = b'\xe2\xde\x1f\x06NodeID'
    _NODEINFO.fields_by_name['other']._options = None
    _NODEINFO.fields_by_name['other']._serialized_options = b'\xc8\xde\x1f\x00'
    _NODEINFOOTHER.fields_by_name['rpc_address']._options = None
    _NODEINFOOTHER.fields_by_name['rpc_address']._serialized_options = b'\xe2\xde\x1f\nRPCAddress'
    _PEERINFO.fields_by_name['id']._options = None
    _PEERINFO.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _PEERINFO.fields_by_name['last_connected']._options = None
    _PEERINFO.fields_by_name['last_connected']._serialized_options = b'\x90\xdf\x1f\x01'
    _PEERADDRESSINFO.fields_by_name['last_dial_success']._options = None
    _PEERADDRESSINFO.fields_by_name['last_dial_success']._serialized_options = b'\x90\xdf\x1f\x01'
    _PEERADDRESSINFO.fields_by_name['last_dial_failure']._options = None
    _PEERADDRESSINFO.fields_by_name['last_dial_failure']._serialized_options = b'\x90\xdf\x1f\x01'
    _PROTOCOLVERSION._serialized_start = 101
    _PROTOCOLVERSION._serialized_end = 168
    _NODEINFO._serialized_start = 171
    _NODEINFO._serialized_end = 417
    _NODEINFOOTHER._serialized_start = 419
    _NODEINFOOTHER._serialized_end = 489
    _PEERINFO._serialized_start = 492
    _PEERINFO._serialized_end = 635
    _PEERADDRESSINFO._serialized_start = 638
    _PEERADDRESSINFO._serialized_end = 817


'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.market.v1beta2 import order_pb2 as akash_dot_market_dot_v1beta2_dot_order__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eakash/market/v1beta2/bid.proto\x12\x14akash.market.v1beta2\x1a\x14gogoproto/gogo.proto\x1a akash/market/v1beta2/order.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xb8\x02\n\x0cMsgCreateBid\x12T\n\x05order\x18\x01 \x01(\x0b2\x1d.akash.market.v1beta2.OrderIDB&\xe2\xde\x1f\x05Order\xc8\xde\x1f\x00\xea\xde\x1f\x05order\xf2\xde\x1f\x0cyaml:"order"\x121\n\x08provider\x18\x02 \x01(\tB\x1f\xea\xde\x1f\x08provider\xf2\xde\x1f\x0fyaml:"provider"\x12J\n\x05price\x18\x03 \x01(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB\x1d\xc8\xde\x1f\x00\xea\xde\x1f\x05price\xf2\xde\x1f\x0cyaml:"price"\x12M\n\x07deposit\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB!\xc8\xde\x1f\x00\xea\xde\x1f\x07deposit\xf2\xde\x1f\x0eyaml:"deposit":\x04\xe8\xa0\x1f\x00"\x16\n\x14MsgCreateBidResponse"b\n\x0bMsgCloseBid\x12M\n\x06bid_id\x18\x01 \x01(\x0b2\x1b.akash.market.v1beta2.BidIDB \xe2\xde\x1f\x05BidID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id":\x04\xe8\xa0\x1f\x00"\x15\n\x13MsgCloseBidResponse"\xfb\x01\n\x05BidID\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12-\n\x04dseq\x18\x02 \x01(\x04B\x1f\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"\x12-\n\x04gseq\x18\x03 \x01(\rB\x1f\xe2\xde\x1f\x04GSeq\xea\xde\x1f\x04gseq\xf2\xde\x1f\x0byaml:"gseq"\x12-\n\x04oseq\x18\x04 \x01(\rB\x1f\xe2\xde\x1f\x04OSeq\xea\xde\x1f\x04oseq\xf2\xde\x1f\x0byaml:"oseq"\x121\n\x08provider\x18\x05 \x01(\tB\x1f\xea\xde\x1f\x08provider\xf2\xde\x1f\x0fyaml:"provider":\x08\xe8\xa0\x1f\x00\x98\xa0\x1f\x00"\x9f\x03\n\x03Bid\x12M\n\x06bid_id\x18\x01 \x01(\x0b2\x1b.akash.market.v1beta2.BidIDB \xe2\xde\x1f\x05BidID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"\x12I\n\x05state\x18\x02 \x01(\x0e2\x1f.akash.market.v1beta2.Bid.StateB\x19\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"\x12J\n\x05price\x18\x03 \x01(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB\x1d\xc8\xde\x1f\x00\xea\xde\x1f\x05price\xf2\xde\x1f\x0cyaml:"price"\x12\x12\n\ncreated_at\x18\x04 \x01(\x03"\x93\x01\n\x05State\x12 \n\x07invalid\x10\x00\x1a\x13\x8a\x9d \x0fBidStateInvalid\x12\x15\n\x04open\x10\x01\x1a\x0b\x8a\x9d \x07BidOpen\x12\x19\n\x06active\x10\x02\x1a\r\x8a\x9d \tBidActive\x12\x15\n\x04lost\x10\x03\x1a\x0b\x8a\x9d \x07BidLost\x12\x19\n\x06closed\x10\x04\x1a\r\x8a\x9d \tBidClosed\x1a\x04\x88\xa3\x1e\x00:\x08\xe8\xa0\x1f\x00\x98\xa0\x1f\x00"\xa6\x02\n\nBidFilters\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12-\n\x04dseq\x18\x02 \x01(\x04B\x1f\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"\x12-\n\x04gseq\x18\x03 \x01(\rB\x1f\xe2\xde\x1f\x04GSeq\xea\xde\x1f\x04gseq\xf2\xde\x1f\x0byaml:"gseq"\x12-\n\x04oseq\x18\x04 \x01(\rB\x1f\xe2\xde\x1f\x04OSeq\xea\xde\x1f\x04oseq\xf2\xde\x1f\x0byaml:"oseq"\x121\n\x08provider\x18\x05 \x01(\tB\x1f\xea\xde\x1f\x08provider\xf2\xde\x1f\x0fyaml:"provider"\x12(\n\x05state\x18\x06 \x01(\tB\x19\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state":\x04\xe8\xa0\x1f\x00B0Z.github.com/ovrclk/akash/x/market/types/v1beta2b\x06proto3')
_MSGCREATEBID = DESCRIPTOR.message_types_by_name['MsgCreateBid']
_MSGCREATEBIDRESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateBidResponse']
_MSGCLOSEBID = DESCRIPTOR.message_types_by_name['MsgCloseBid']
_MSGCLOSEBIDRESPONSE = DESCRIPTOR.message_types_by_name['MsgCloseBidResponse']
_BIDID = DESCRIPTOR.message_types_by_name['BidID']
_BID = DESCRIPTOR.message_types_by_name['Bid']
_BIDFILTERS = DESCRIPTOR.message_types_by_name['BidFilters']
_BID_STATE = _BID.enum_types_by_name['State']
MsgCreateBid = _reflection.GeneratedProtocolMessageType('MsgCreateBid', (_message.Message,), {'DESCRIPTOR': _MSGCREATEBID, '__module__': 'akash.market.v1beta2.bid_pb2'})
_sym_db.RegisterMessage(MsgCreateBid)
MsgCreateBidResponse = _reflection.GeneratedProtocolMessageType('MsgCreateBidResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATEBIDRESPONSE, '__module__': 'akash.market.v1beta2.bid_pb2'})
_sym_db.RegisterMessage(MsgCreateBidResponse)
MsgCloseBid = _reflection.GeneratedProtocolMessageType('MsgCloseBid', (_message.Message,), {'DESCRIPTOR': _MSGCLOSEBID, '__module__': 'akash.market.v1beta2.bid_pb2'})
_sym_db.RegisterMessage(MsgCloseBid)
MsgCloseBidResponse = _reflection.GeneratedProtocolMessageType('MsgCloseBidResponse', (_message.Message,), {'DESCRIPTOR': _MSGCLOSEBIDRESPONSE, '__module__': 'akash.market.v1beta2.bid_pb2'})
_sym_db.RegisterMessage(MsgCloseBidResponse)
BidID = _reflection.GeneratedProtocolMessageType('BidID', (_message.Message,), {'DESCRIPTOR': _BIDID, '__module__': 'akash.market.v1beta2.bid_pb2'})
_sym_db.RegisterMessage(BidID)
Bid = _reflection.GeneratedProtocolMessageType('Bid', (_message.Message,), {'DESCRIPTOR': _BID, '__module__': 'akash.market.v1beta2.bid_pb2'})
_sym_db.RegisterMessage(Bid)
BidFilters = _reflection.GeneratedProtocolMessageType('BidFilters', (_message.Message,), {'DESCRIPTOR': _BIDFILTERS, '__module__': 'akash.market.v1beta2.bid_pb2'})
_sym_db.RegisterMessage(BidFilters)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z.github.com/ovrclk/akash/x/market/types/v1beta2'
    _MSGCREATEBID.fields_by_name['order']._options = None
    _MSGCREATEBID.fields_by_name['order']._serialized_options = b'\xe2\xde\x1f\x05Order\xc8\xde\x1f\x00\xea\xde\x1f\x05order\xf2\xde\x1f\x0cyaml:"order"'
    _MSGCREATEBID.fields_by_name['provider']._options = None
    _MSGCREATEBID.fields_by_name['provider']._serialized_options = b'\xea\xde\x1f\x08provider\xf2\xde\x1f\x0fyaml:"provider"'
    _MSGCREATEBID.fields_by_name['price']._options = None
    _MSGCREATEBID.fields_by_name['price']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x05price\xf2\xde\x1f\x0cyaml:"price"'
    _MSGCREATEBID.fields_by_name['deposit']._options = None
    _MSGCREATEBID.fields_by_name['deposit']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x07deposit\xf2\xde\x1f\x0eyaml:"deposit"'
    _MSGCREATEBID._options = None
    _MSGCREATEBID._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGCLOSEBID.fields_by_name['bid_id']._options = None
    _MSGCLOSEBID.fields_by_name['bid_id']._serialized_options = b'\xe2\xde\x1f\x05BidID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGCLOSEBID._options = None
    _MSGCLOSEBID._serialized_options = b'\xe8\xa0\x1f\x00'
    _BIDID.fields_by_name['owner']._options = None
    _BIDID.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _BIDID.fields_by_name['dseq']._options = None
    _BIDID.fields_by_name['dseq']._serialized_options = b'\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"'
    _BIDID.fields_by_name['gseq']._options = None
    _BIDID.fields_by_name['gseq']._serialized_options = b'\xe2\xde\x1f\x04GSeq\xea\xde\x1f\x04gseq\xf2\xde\x1f\x0byaml:"gseq"'
    _BIDID.fields_by_name['oseq']._options = None
    _BIDID.fields_by_name['oseq']._serialized_options = b'\xe2\xde\x1f\x04OSeq\xea\xde\x1f\x04oseq\xf2\xde\x1f\x0byaml:"oseq"'
    _BIDID.fields_by_name['provider']._options = None
    _BIDID.fields_by_name['provider']._serialized_options = b'\xea\xde\x1f\x08provider\xf2\xde\x1f\x0fyaml:"provider"'
    _BIDID._options = None
    _BIDID._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x00'
    _BID_STATE._options = None
    _BID_STATE._serialized_options = b'\x88\xa3\x1e\x00'
    _BID_STATE.values_by_name['invalid']._options = None
    _BID_STATE.values_by_name['invalid']._serialized_options = b'\x8a\x9d \x0fBidStateInvalid'
    _BID_STATE.values_by_name['open']._options = None
    _BID_STATE.values_by_name['open']._serialized_options = b'\x8a\x9d \x07BidOpen'
    _BID_STATE.values_by_name['active']._options = None
    _BID_STATE.values_by_name['active']._serialized_options = b'\x8a\x9d \tBidActive'
    _BID_STATE.values_by_name['lost']._options = None
    _BID_STATE.values_by_name['lost']._serialized_options = b'\x8a\x9d \x07BidLost'
    _BID_STATE.values_by_name['closed']._options = None
    _BID_STATE.values_by_name['closed']._serialized_options = b'\x8a\x9d \tBidClosed'
    _BID.fields_by_name['bid_id']._options = None
    _BID.fields_by_name['bid_id']._serialized_options = b'\xe2\xde\x1f\x05BidID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _BID.fields_by_name['state']._options = None
    _BID.fields_by_name['state']._serialized_options = b'\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"'
    _BID.fields_by_name['price']._options = None
    _BID.fields_by_name['price']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x05price\xf2\xde\x1f\x0cyaml:"price"'
    _BID._options = None
    _BID._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x00'
    _BIDFILTERS.fields_by_name['owner']._options = None
    _BIDFILTERS.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _BIDFILTERS.fields_by_name['dseq']._options = None
    _BIDFILTERS.fields_by_name['dseq']._serialized_options = b'\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"'
    _BIDFILTERS.fields_by_name['gseq']._options = None
    _BIDFILTERS.fields_by_name['gseq']._serialized_options = b'\xe2\xde\x1f\x04GSeq\xea\xde\x1f\x04gseq\xf2\xde\x1f\x0byaml:"gseq"'
    _BIDFILTERS.fields_by_name['oseq']._options = None
    _BIDFILTERS.fields_by_name['oseq']._serialized_options = b'\xe2\xde\x1f\x04OSeq\xea\xde\x1f\x04oseq\xf2\xde\x1f\x0byaml:"oseq"'
    _BIDFILTERS.fields_by_name['provider']._options = None
    _BIDFILTERS.fields_by_name['provider']._serialized_options = b'\xea\xde\x1f\x08provider\xf2\xde\x1f\x0fyaml:"provider"'
    _BIDFILTERS.fields_by_name['state']._options = None
    _BIDFILTERS.fields_by_name['state']._serialized_options = b'\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"'
    _BIDFILTERS._options = None
    _BIDFILTERS._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGCREATEBID._serialized_start = 145
    _MSGCREATEBID._serialized_end = 457
    _MSGCREATEBIDRESPONSE._serialized_start = 459
    _MSGCREATEBIDRESPONSE._serialized_end = 481
    _MSGCLOSEBID._serialized_start = 483
    _MSGCLOSEBID._serialized_end = 581
    _MSGCLOSEBIDRESPONSE._serialized_start = 583
    _MSGCLOSEBIDRESPONSE._serialized_end = 604
    _BIDID._serialized_start = 607
    _BIDID._serialized_end = 858
    _BID._serialized_start = 861
    _BID._serialized_end = 1276
    _BID_STATE._serialized_start = 1119
    _BID_STATE._serialized_end = 1266
    _BIDFILTERS._serialized_start = 1279
    _BIDFILTERS._serialized_end = 1573

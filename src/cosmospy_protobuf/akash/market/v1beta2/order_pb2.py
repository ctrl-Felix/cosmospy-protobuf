
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.deployment.v1beta2 import groupspec_pb2 as akash_dot_deployment_dot_v1beta2_dot_groupspec__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n akash/market/v1beta2/order.proto\x12\x14akash.market.v1beta2\x1a\x14gogoproto/gogo.proto\x1a(akash/deployment/v1beta2/groupspec.proto"\xca\x01\n\x07OrderID\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12-\n\x04dseq\x18\x02 \x01(\x04B\x1f\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"\x12-\n\x04gseq\x18\x03 \x01(\rB\x1f\xe2\xde\x1f\x04GSeq\xea\xde\x1f\x04gseq\xf2\xde\x1f\x0byaml:"gseq"\x12-\n\x04oseq\x18\x04 \x01(\rB\x1f\xe2\xde\x1f\x04OSeq\xea\xde\x1f\x04oseq\xf2\xde\x1f\x0byaml:"oseq":\x08\xe8\xa0\x1f\x00\x98\xa0\x1f\x00"\x9e\x03\n\x05Order\x12S\n\x08order_id\x18\x01 \x01(\x0b2\x1d.akash.market.v1beta2.OrderIDB"\xe2\xde\x1f\x07OrderID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"\x12K\n\x05state\x18\x02 \x01(\x0e2!.akash.market.v1beta2.Order.StateB\x19\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"\x12N\n\x04spec\x18\x03 \x01(\x0b2#.akash.deployment.v1beta2.GroupSpecB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04spec\xf2\xde\x1f\x0byaml:"spec"\x12\x12\n\ncreated_at\x18\x04 \x01(\x03"\x84\x01\n\x05State\x12"\n\x07invalid\x10\x00\x1a\x15\x8a\x9d \x11OrderStateInvalid\x12\x17\n\x04open\x10\x01\x1a\r\x8a\x9d \tOrderOpen\x12\x1b\n\x06active\x10\x02\x1a\x0f\x8a\x9d \x0bOrderActive\x12\x1b\n\x06closed\x10\x03\x1a\x0f\x8a\x9d \x0bOrderClosed\x1a\x04\x88\xa3\x1e\x00:\x08\xe8\xa0\x1f\x00\x98\xa0\x1f\x00"\xf5\x01\n\x0cOrderFilters\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12-\n\x04dseq\x18\x02 \x01(\x04B\x1f\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"\x12-\n\x04gseq\x18\x03 \x01(\rB\x1f\xe2\xde\x1f\x04GSeq\xea\xde\x1f\x04gseq\xf2\xde\x1f\x0byaml:"gseq"\x12-\n\x04oseq\x18\x04 \x01(\rB\x1f\xe2\xde\x1f\x04OSeq\xea\xde\x1f\x04oseq\xf2\xde\x1f\x0byaml:"oseq"\x12(\n\x05state\x18\x05 \x01(\tB\x19\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state":\x04\xe8\xa0\x1f\x00B0Z.github.com/ovrclk/akash/x/market/types/v1beta2b\x06proto3')
_ORDERID = DESCRIPTOR.message_types_by_name['OrderID']
_ORDER = DESCRIPTOR.message_types_by_name['Order']
_ORDERFILTERS = DESCRIPTOR.message_types_by_name['OrderFilters']
_ORDER_STATE = _ORDER.enum_types_by_name['State']
OrderID = _reflection.GeneratedProtocolMessageType('OrderID', (_message.Message,), {'DESCRIPTOR': _ORDERID, '__module__': 'akash.market.v1beta2.order_pb2'})
_sym_db.RegisterMessage(OrderID)
Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {'DESCRIPTOR': _ORDER, '__module__': 'akash.market.v1beta2.order_pb2'})
_sym_db.RegisterMessage(Order)
OrderFilters = _reflection.GeneratedProtocolMessageType('OrderFilters', (_message.Message,), {'DESCRIPTOR': _ORDERFILTERS, '__module__': 'akash.market.v1beta2.order_pb2'})
_sym_db.RegisterMessage(OrderFilters)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z.github.com/ovrclk/akash/x/market/types/v1beta2'
    _ORDERID.fields_by_name['owner']._options = None
    _ORDERID.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _ORDERID.fields_by_name['dseq']._options = None
    _ORDERID.fields_by_name['dseq']._serialized_options = b'\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"'
    _ORDERID.fields_by_name['gseq']._options = None
    _ORDERID.fields_by_name['gseq']._serialized_options = b'\xe2\xde\x1f\x04GSeq\xea\xde\x1f\x04gseq\xf2\xde\x1f\x0byaml:"gseq"'
    _ORDERID.fields_by_name['oseq']._options = None
    _ORDERID.fields_by_name['oseq']._serialized_options = b'\xe2\xde\x1f\x04OSeq\xea\xde\x1f\x04oseq\xf2\xde\x1f\x0byaml:"oseq"'
    _ORDERID._options = None
    _ORDERID._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x00'
    _ORDER_STATE._options = None
    _ORDER_STATE._serialized_options = b'\x88\xa3\x1e\x00'
    _ORDER_STATE.values_by_name['invalid']._options = None
    _ORDER_STATE.values_by_name['invalid']._serialized_options = b'\x8a\x9d \x11OrderStateInvalid'
    _ORDER_STATE.values_by_name['open']._options = None
    _ORDER_STATE.values_by_name['open']._serialized_options = b'\x8a\x9d \tOrderOpen'
    _ORDER_STATE.values_by_name['active']._options = None
    _ORDER_STATE.values_by_name['active']._serialized_options = b'\x8a\x9d \x0bOrderActive'
    _ORDER_STATE.values_by_name['closed']._options = None
    _ORDER_STATE.values_by_name['closed']._serialized_options = b'\x8a\x9d \x0bOrderClosed'
    _ORDER.fields_by_name['order_id']._options = None
    _ORDER.fields_by_name['order_id']._serialized_options = b'\xe2\xde\x1f\x07OrderID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _ORDER.fields_by_name['state']._options = None
    _ORDER.fields_by_name['state']._serialized_options = b'\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"'
    _ORDER.fields_by_name['spec']._options = None
    _ORDER.fields_by_name['spec']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04spec\xf2\xde\x1f\x0byaml:"spec"'
    _ORDER._options = None
    _ORDER._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x00'
    _ORDERFILTERS.fields_by_name['owner']._options = None
    _ORDERFILTERS.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _ORDERFILTERS.fields_by_name['dseq']._options = None
    _ORDERFILTERS.fields_by_name['dseq']._serialized_options = b'\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"'
    _ORDERFILTERS.fields_by_name['gseq']._options = None
    _ORDERFILTERS.fields_by_name['gseq']._serialized_options = b'\xe2\xde\x1f\x04GSeq\xea\xde\x1f\x04gseq\xf2\xde\x1f\x0byaml:"gseq"'
    _ORDERFILTERS.fields_by_name['oseq']._options = None
    _ORDERFILTERS.fields_by_name['oseq']._serialized_options = b'\xe2\xde\x1f\x04OSeq\xea\xde\x1f\x04oseq\xf2\xde\x1f\x0byaml:"oseq"'
    _ORDERFILTERS.fields_by_name['state']._options = None
    _ORDERFILTERS.fields_by_name['state']._serialized_options = b'\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"'
    _ORDERFILTERS._options = None
    _ORDERFILTERS._serialized_options = b'\xe8\xa0\x1f\x00'
    _ORDERID._serialized_start = 123
    _ORDERID._serialized_end = 325
    _ORDER._serialized_start = 328
    _ORDER._serialized_end = 742
    _ORDER_STATE._serialized_start = 600
    _ORDER_STATE._serialized_end = 732
    _ORDERFILTERS._serialized_start = 745
    _ORDERFILTERS._serialized_end = 990

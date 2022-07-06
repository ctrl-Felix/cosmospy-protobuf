
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....akash.market.v1beta2 import bid_pb2 as akash_dot_market_dot_v1beta2_dot_bid__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n akash/market/v1beta2/lease.proto\x12\x14akash.market.v1beta2\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1eakash/market/v1beta2/bid.proto"\xfd\x01\n\x07LeaseID\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12-\n\x04dseq\x18\x02 \x01(\x04B\x1f\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"\x12-\n\x04gseq\x18\x03 \x01(\rB\x1f\xe2\xde\x1f\x04GSeq\xea\xde\x1f\x04gseq\xf2\xde\x1f\x0byaml:"gseq"\x12-\n\x04oseq\x18\x04 \x01(\rB\x1f\xe2\xde\x1f\x04OSeq\xea\xde\x1f\x04oseq\xf2\xde\x1f\x0byaml:"oseq"\x121\n\x08provider\x18\x05 \x01(\tB\x1f\xea\xde\x1f\x08provider\xf2\xde\x1f\x0fyaml:"provider":\x08\xe8\xa0\x1f\x00\x98\xa0\x1f\x00"\xc8\x03\n\x05Lease\x12S\n\x08lease_id\x18\x01 \x01(\x0b2\x1d.akash.market.v1beta2.LeaseIDB"\xe2\xde\x1f\x07LeaseID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"\x12K\n\x05state\x18\x02 \x01(\x0e2!.akash.market.v1beta2.Lease.StateB\x19\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"\x12J\n\x05price\x18\x03 \x01(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB\x1d\xc8\xde\x1f\x00\xea\xde\x1f\x05price\xf2\xde\x1f\x0cyaml:"price"\x12\x12\n\ncreated_at\x18\x04 \x01(\x03\x12\x11\n\tclosed_on\x18\x05 \x01(\x03"\x9f\x01\n\x05State\x12"\n\x07invalid\x10\x00\x1a\x15\x8a\x9d \x11LeaseStateInvalid\x12\x1b\n\x06active\x10\x01\x1a\x0f\x8a\x9d \x0bLeaseActive\x122\n\x12insufficient_funds\x10\x02\x1a\x1a\x8a\x9d \x16LeaseInsufficientFunds\x12\x1b\n\x06closed\x10\x03\x1a\x0f\x8a\x9d \x0bLeaseClosed\x1a\x04\x88\xa3\x1e\x00:\x08\xe8\xa0\x1f\x00\x98\xa0\x1f\x00"\xa8\x02\n\x0cLeaseFilters\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12-\n\x04dseq\x18\x02 \x01(\x04B\x1f\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"\x12-\n\x04gseq\x18\x03 \x01(\rB\x1f\xe2\xde\x1f\x04GSeq\xea\xde\x1f\x04gseq\xf2\xde\x1f\x0byaml:"gseq"\x12-\n\x04oseq\x18\x04 \x01(\rB\x1f\xe2\xde\x1f\x04OSeq\xea\xde\x1f\x04oseq\xf2\xde\x1f\x0byaml:"oseq"\x121\n\x08provider\x18\x05 \x01(\tB\x1f\xea\xde\x1f\x08provider\xf2\xde\x1f\x0fyaml:"provider"\x12(\n\x05state\x18\x06 \x01(\tB\x19\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state":\x04\xe8\xa0\x1f\x00"e\n\x0eMsgCreateLease\x12M\n\x06bid_id\x18\x01 \x01(\x0b2\x1b.akash.market.v1beta2.BidIDB \xe2\xde\x1f\x05BidID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id":\x04\xe8\xa0\x1f\x00"\x18\n\x16MsgCreateLeaseResponse"k\n\x10MsgWithdrawLease\x12Q\n\x06bid_id\x18\x01 \x01(\x0b2\x1d.akash.market.v1beta2.LeaseIDB"\xe2\xde\x1f\x07LeaseID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id":\x04\xe8\xa0\x1f\x00"\x1a\n\x18MsgWithdrawLeaseResponse"j\n\rMsgCloseLease\x12S\n\x08lease_id\x18\x01 \x01(\x0b2\x1d.akash.market.v1beta2.LeaseIDB"\xe2\xde\x1f\x07LeaseID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id":\x04\xe8\xa0\x1f\x00"\x17\n\x15MsgCloseLeaseResponseB0Z.github.com/ovrclk/akash/x/market/types/v1beta2b\x06proto3')
_LEASEID = DESCRIPTOR.message_types_by_name['LeaseID']
_LEASE = DESCRIPTOR.message_types_by_name['Lease']
_LEASEFILTERS = DESCRIPTOR.message_types_by_name['LeaseFilters']
_MSGCREATELEASE = DESCRIPTOR.message_types_by_name['MsgCreateLease']
_MSGCREATELEASERESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateLeaseResponse']
_MSGWITHDRAWLEASE = DESCRIPTOR.message_types_by_name['MsgWithdrawLease']
_MSGWITHDRAWLEASERESPONSE = DESCRIPTOR.message_types_by_name['MsgWithdrawLeaseResponse']
_MSGCLOSELEASE = DESCRIPTOR.message_types_by_name['MsgCloseLease']
_MSGCLOSELEASERESPONSE = DESCRIPTOR.message_types_by_name['MsgCloseLeaseResponse']
_LEASE_STATE = _LEASE.enum_types_by_name['State']
LeaseID = _reflection.GeneratedProtocolMessageType('LeaseID', (_message.Message,), {'DESCRIPTOR': _LEASEID, '__module__': 'akash.market.v1beta2.lease_pb2'})
_sym_db.RegisterMessage(LeaseID)
Lease = _reflection.GeneratedProtocolMessageType('Lease', (_message.Message,), {'DESCRIPTOR': _LEASE, '__module__': 'akash.market.v1beta2.lease_pb2'})
_sym_db.RegisterMessage(Lease)
LeaseFilters = _reflection.GeneratedProtocolMessageType('LeaseFilters', (_message.Message,), {'DESCRIPTOR': _LEASEFILTERS, '__module__': 'akash.market.v1beta2.lease_pb2'})
_sym_db.RegisterMessage(LeaseFilters)
MsgCreateLease = _reflection.GeneratedProtocolMessageType('MsgCreateLease', (_message.Message,), {'DESCRIPTOR': _MSGCREATELEASE, '__module__': 'akash.market.v1beta2.lease_pb2'})
_sym_db.RegisterMessage(MsgCreateLease)
MsgCreateLeaseResponse = _reflection.GeneratedProtocolMessageType('MsgCreateLeaseResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATELEASERESPONSE, '__module__': 'akash.market.v1beta2.lease_pb2'})
_sym_db.RegisterMessage(MsgCreateLeaseResponse)
MsgWithdrawLease = _reflection.GeneratedProtocolMessageType('MsgWithdrawLease', (_message.Message,), {'DESCRIPTOR': _MSGWITHDRAWLEASE, '__module__': 'akash.market.v1beta2.lease_pb2'})
_sym_db.RegisterMessage(MsgWithdrawLease)
MsgWithdrawLeaseResponse = _reflection.GeneratedProtocolMessageType('MsgWithdrawLeaseResponse', (_message.Message,), {'DESCRIPTOR': _MSGWITHDRAWLEASERESPONSE, '__module__': 'akash.market.v1beta2.lease_pb2'})
_sym_db.RegisterMessage(MsgWithdrawLeaseResponse)
MsgCloseLease = _reflection.GeneratedProtocolMessageType('MsgCloseLease', (_message.Message,), {'DESCRIPTOR': _MSGCLOSELEASE, '__module__': 'akash.market.v1beta2.lease_pb2'})
_sym_db.RegisterMessage(MsgCloseLease)
MsgCloseLeaseResponse = _reflection.GeneratedProtocolMessageType('MsgCloseLeaseResponse', (_message.Message,), {'DESCRIPTOR': _MSGCLOSELEASERESPONSE, '__module__': 'akash.market.v1beta2.lease_pb2'})
_sym_db.RegisterMessage(MsgCloseLeaseResponse)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z.github.com/ovrclk/akash/x/market/types/v1beta2'
    _LEASEID.fields_by_name['owner']._options = None
    _LEASEID.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _LEASEID.fields_by_name['dseq']._options = None
    _LEASEID.fields_by_name['dseq']._serialized_options = b'\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"'
    _LEASEID.fields_by_name['gseq']._options = None
    _LEASEID.fields_by_name['gseq']._serialized_options = b'\xe2\xde\x1f\x04GSeq\xea\xde\x1f\x04gseq\xf2\xde\x1f\x0byaml:"gseq"'
    _LEASEID.fields_by_name['oseq']._options = None
    _LEASEID.fields_by_name['oseq']._serialized_options = b'\xe2\xde\x1f\x04OSeq\xea\xde\x1f\x04oseq\xf2\xde\x1f\x0byaml:"oseq"'
    _LEASEID.fields_by_name['provider']._options = None
    _LEASEID.fields_by_name['provider']._serialized_options = b'\xea\xde\x1f\x08provider\xf2\xde\x1f\x0fyaml:"provider"'
    _LEASEID._options = None
    _LEASEID._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x00'
    _LEASE_STATE._options = None
    _LEASE_STATE._serialized_options = b'\x88\xa3\x1e\x00'
    _LEASE_STATE.values_by_name['invalid']._options = None
    _LEASE_STATE.values_by_name['invalid']._serialized_options = b'\x8a\x9d \x11LeaseStateInvalid'
    _LEASE_STATE.values_by_name['active']._options = None
    _LEASE_STATE.values_by_name['active']._serialized_options = b'\x8a\x9d \x0bLeaseActive'
    _LEASE_STATE.values_by_name['insufficient_funds']._options = None
    _LEASE_STATE.values_by_name['insufficient_funds']._serialized_options = b'\x8a\x9d \x16LeaseInsufficientFunds'
    _LEASE_STATE.values_by_name['closed']._options = None
    _LEASE_STATE.values_by_name['closed']._serialized_options = b'\x8a\x9d \x0bLeaseClosed'
    _LEASE.fields_by_name['lease_id']._options = None
    _LEASE.fields_by_name['lease_id']._serialized_options = b'\xe2\xde\x1f\x07LeaseID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _LEASE.fields_by_name['state']._options = None
    _LEASE.fields_by_name['state']._serialized_options = b'\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"'
    _LEASE.fields_by_name['price']._options = None
    _LEASE.fields_by_name['price']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x05price\xf2\xde\x1f\x0cyaml:"price"'
    _LEASE._options = None
    _LEASE._serialized_options = b'\xe8\xa0\x1f\x00\x98\xa0\x1f\x00'
    _LEASEFILTERS.fields_by_name['owner']._options = None
    _LEASEFILTERS.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _LEASEFILTERS.fields_by_name['dseq']._options = None
    _LEASEFILTERS.fields_by_name['dseq']._serialized_options = b'\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"'
    _LEASEFILTERS.fields_by_name['gseq']._options = None
    _LEASEFILTERS.fields_by_name['gseq']._serialized_options = b'\xe2\xde\x1f\x04GSeq\xea\xde\x1f\x04gseq\xf2\xde\x1f\x0byaml:"gseq"'
    _LEASEFILTERS.fields_by_name['oseq']._options = None
    _LEASEFILTERS.fields_by_name['oseq']._serialized_options = b'\xe2\xde\x1f\x04OSeq\xea\xde\x1f\x04oseq\xf2\xde\x1f\x0byaml:"oseq"'
    _LEASEFILTERS.fields_by_name['provider']._options = None
    _LEASEFILTERS.fields_by_name['provider']._serialized_options = b'\xea\xde\x1f\x08provider\xf2\xde\x1f\x0fyaml:"provider"'
    _LEASEFILTERS.fields_by_name['state']._options = None
    _LEASEFILTERS.fields_by_name['state']._serialized_options = b'\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"'
    _LEASEFILTERS._options = None
    _LEASEFILTERS._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGCREATELEASE.fields_by_name['bid_id']._options = None
    _MSGCREATELEASE.fields_by_name['bid_id']._serialized_options = b'\xe2\xde\x1f\x05BidID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGCREATELEASE._options = None
    _MSGCREATELEASE._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGWITHDRAWLEASE.fields_by_name['bid_id']._options = None
    _MSGWITHDRAWLEASE.fields_by_name['bid_id']._serialized_options = b'\xe2\xde\x1f\x07LeaseID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGWITHDRAWLEASE._options = None
    _MSGWITHDRAWLEASE._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGCLOSELEASE.fields_by_name['lease_id']._options = None
    _MSGCLOSELEASE.fields_by_name['lease_id']._serialized_options = b'\xe2\xde\x1f\x07LeaseID\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGCLOSELEASE._options = None
    _MSGCLOSELEASE._serialized_options = b'\xe8\xa0\x1f\x00'
    _LEASEID._serialized_start = 145
    _LEASEID._serialized_end = 398
    _LEASE._serialized_start = 401
    _LEASE._serialized_end = 857
    _LEASE_STATE._serialized_start = 688
    _LEASE_STATE._serialized_end = 847
    _LEASEFILTERS._serialized_start = 860
    _LEASEFILTERS._serialized_end = 1156
    _MSGCREATELEASE._serialized_start = 1158
    _MSGCREATELEASE._serialized_end = 1259
    _MSGCREATELEASERESPONSE._serialized_start = 1261
    _MSGCREATELEASERESPONSE._serialized_end = 1285
    _MSGWITHDRAWLEASE._serialized_start = 1287
    _MSGWITHDRAWLEASE._serialized_end = 1394
    _MSGWITHDRAWLEASERESPONSE._serialized_start = 1396
    _MSGWITHDRAWLEASERESPONSE._serialized_end = 1422
    _MSGCLOSELEASE._serialized_start = 1424
    _MSGCLOSELEASE._serialized_end = 1530
    _MSGCLOSELEASERESPONSE._serialized_start = 1532
    _MSGCLOSELEASERESPONSE._serialized_end = 1555

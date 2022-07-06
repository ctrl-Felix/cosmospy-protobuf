
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....akash.market.v1beta2 import order_pb2 as akash_dot_market_dot_v1beta2_dot_order__pb2
from ....akash.market.v1beta2 import bid_pb2 as akash_dot_market_dot_v1beta2_dot_bid__pb2
from ....akash.market.v1beta2 import lease_pb2 as akash_dot_market_dot_v1beta2_dot_lease__pb2
from ....akash.escrow.v1beta2 import types_pb2 as akash_dot_escrow_dot_v1beta2_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n akash/market/v1beta2/query.proto\x12\x14akash.market.v1beta2\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a akash/market/v1beta2/order.proto\x1a\x1eakash/market/v1beta2/bid.proto\x1a akash/market/v1beta2/lease.proto\x1a akash/escrow/v1beta2/types.proto"\x8b\x01\n\x12QueryOrdersRequest\x129\n\x07filters\x18\x01 \x01(\x0b2".akash.market.v1beta2.OrderFiltersB\x04\xc8\xde\x1f\x00\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8f\x01\n\x13QueryOrdersResponse\x12;\n\x06orders\x18\x01 \x03(\x0b2\x1b.akash.market.v1beta2.OrderB\x0e\xc8\xde\x1f\x00\xaa\xdf\x1f\x06Orders\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"J\n\x11QueryOrderRequest\x125\n\x02id\x18\x01 \x01(\x0b2\x1d.akash.market.v1beta2.OrderIDB\n\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID"F\n\x12QueryOrderResponse\x120\n\x05order\x18\x01 \x01(\x0b2\x1b.akash.market.v1beta2.OrderB\x04\xc8\xde\x1f\x00"\x87\x01\n\x10QueryBidsRequest\x127\n\x07filters\x18\x01 \x01(\x0b2 .akash.market.v1beta2.BidFiltersB\x04\xc8\xde\x1f\x00\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8c\x01\n\x11QueryBidsResponse\x12:\n\x04bids\x18\x01 \x03(\x0b2&.akash.market.v1beta2.QueryBidResponseB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"F\n\x0fQueryBidRequest\x123\n\x02id\x18\x01 \x01(\x0b2\x1b.akash.market.v1beta2.BidIDB\n\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID"}\n\x10QueryBidResponse\x12,\n\x03bid\x18\x01 \x01(\x0b2\x19.akash.market.v1beta2.BidB\x04\xc8\xde\x1f\x00\x12;\n\x0eescrow_account\x18\x02 \x01(\x0b2\x1d.akash.escrow.v1beta2.AccountB\x04\xc8\xde\x1f\x00"\x8b\x01\n\x12QueryLeasesRequest\x129\n\x07filters\x18\x01 \x01(\x0b2".akash.market.v1beta2.LeaseFiltersB\x04\xc8\xde\x1f\x00\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x92\x01\n\x13QueryLeasesResponse\x12>\n\x06leases\x18\x01 \x03(\x0b2(.akash.market.v1beta2.QueryLeaseResponseB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"J\n\x11QueryLeaseRequest\x125\n\x02id\x18\x01 \x01(\x0b2\x1d.akash.market.v1beta2.LeaseIDB\n\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID"\x8d\x01\n\x12QueryLeaseResponse\x120\n\x05lease\x18\x01 \x01(\x0b2\x1b.akash.market.v1beta2.LeaseB\x04\xc8\xde\x1f\x00\x12E\n\x0eescrow_payment\x18\x02 \x01(\x0b2\'.akash.escrow.v1beta2.FractionalPaymentB\x04\xc8\xde\x1f\x002\xaf\x06\n\x05Query\x12\x88\x01\n\x06Orders\x12(.akash.market.v1beta2.QueryOrdersRequest\x1a).akash.market.v1beta2.QueryOrdersResponse")\x82\xd3\xe4\x93\x02#\x12!/akash/market/v1beta2/orders/list\x12\x85\x01\n\x05Order\x12\'.akash.market.v1beta2.QueryOrderRequest\x1a(.akash.market.v1beta2.QueryOrderResponse")\x82\xd3\xe4\x93\x02#\x12!/akash/market/v1beta2/orders/info\x12\x80\x01\n\x04Bids\x12&.akash.market.v1beta2.QueryBidsRequest\x1a\'.akash.market.v1beta2.QueryBidsResponse"\'\x82\xd3\xe4\x93\x02!\x12\x1f/akash/market/v1beta2/bids/list\x12}\n\x03Bid\x12%.akash.market.v1beta2.QueryBidRequest\x1a&.akash.market.v1beta2.QueryBidResponse"\'\x82\xd3\xe4\x93\x02!\x12\x1f/akash/market/v1beta2/bids/info\x12\x88\x01\n\x06Leases\x12(.akash.market.v1beta2.QueryLeasesRequest\x1a).akash.market.v1beta2.QueryLeasesResponse")\x82\xd3\xe4\x93\x02#\x12!/akash/market/v1beta2/leases/list\x12\x85\x01\n\x05Lease\x12\'.akash.market.v1beta2.QueryLeaseRequest\x1a(.akash.market.v1beta2.QueryLeaseResponse")\x82\xd3\xe4\x93\x02#\x12!/akash/market/v1beta2/leases/infoB0Z.github.com/ovrclk/akash/x/market/types/v1beta2b\x06proto3')
_QUERYORDERSREQUEST = DESCRIPTOR.message_types_by_name['QueryOrdersRequest']
_QUERYORDERSRESPONSE = DESCRIPTOR.message_types_by_name['QueryOrdersResponse']
_QUERYORDERREQUEST = DESCRIPTOR.message_types_by_name['QueryOrderRequest']
_QUERYORDERRESPONSE = DESCRIPTOR.message_types_by_name['QueryOrderResponse']
_QUERYBIDSREQUEST = DESCRIPTOR.message_types_by_name['QueryBidsRequest']
_QUERYBIDSRESPONSE = DESCRIPTOR.message_types_by_name['QueryBidsResponse']
_QUERYBIDREQUEST = DESCRIPTOR.message_types_by_name['QueryBidRequest']
_QUERYBIDRESPONSE = DESCRIPTOR.message_types_by_name['QueryBidResponse']
_QUERYLEASESREQUEST = DESCRIPTOR.message_types_by_name['QueryLeasesRequest']
_QUERYLEASESRESPONSE = DESCRIPTOR.message_types_by_name['QueryLeasesResponse']
_QUERYLEASEREQUEST = DESCRIPTOR.message_types_by_name['QueryLeaseRequest']
_QUERYLEASERESPONSE = DESCRIPTOR.message_types_by_name['QueryLeaseResponse']
QueryOrdersRequest = _reflection.GeneratedProtocolMessageType('QueryOrdersRequest', (_message.Message,), {'DESCRIPTOR': _QUERYORDERSREQUEST, '__module__': 'akash.market.v1beta2.query_pb2'})
_sym_db.RegisterMessage(QueryOrdersRequest)
QueryOrdersResponse = _reflection.GeneratedProtocolMessageType('QueryOrdersResponse', (_message.Message,), {'DESCRIPTOR': _QUERYORDERSRESPONSE, '__module__': 'akash.market.v1beta2.query_pb2'})
_sym_db.RegisterMessage(QueryOrdersResponse)
QueryOrderRequest = _reflection.GeneratedProtocolMessageType('QueryOrderRequest', (_message.Message,), {'DESCRIPTOR': _QUERYORDERREQUEST, '__module__': 'akash.market.v1beta2.query_pb2'})
_sym_db.RegisterMessage(QueryOrderRequest)
QueryOrderResponse = _reflection.GeneratedProtocolMessageType('QueryOrderResponse', (_message.Message,), {'DESCRIPTOR': _QUERYORDERRESPONSE, '__module__': 'akash.market.v1beta2.query_pb2'})
_sym_db.RegisterMessage(QueryOrderResponse)
QueryBidsRequest = _reflection.GeneratedProtocolMessageType('QueryBidsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYBIDSREQUEST, '__module__': 'akash.market.v1beta2.query_pb2'})
_sym_db.RegisterMessage(QueryBidsRequest)
QueryBidsResponse = _reflection.GeneratedProtocolMessageType('QueryBidsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYBIDSRESPONSE, '__module__': 'akash.market.v1beta2.query_pb2'})
_sym_db.RegisterMessage(QueryBidsResponse)
QueryBidRequest = _reflection.GeneratedProtocolMessageType('QueryBidRequest', (_message.Message,), {'DESCRIPTOR': _QUERYBIDREQUEST, '__module__': 'akash.market.v1beta2.query_pb2'})
_sym_db.RegisterMessage(QueryBidRequest)
QueryBidResponse = _reflection.GeneratedProtocolMessageType('QueryBidResponse', (_message.Message,), {'DESCRIPTOR': _QUERYBIDRESPONSE, '__module__': 'akash.market.v1beta2.query_pb2'})
_sym_db.RegisterMessage(QueryBidResponse)
QueryLeasesRequest = _reflection.GeneratedProtocolMessageType('QueryLeasesRequest', (_message.Message,), {'DESCRIPTOR': _QUERYLEASESREQUEST, '__module__': 'akash.market.v1beta2.query_pb2'})
_sym_db.RegisterMessage(QueryLeasesRequest)
QueryLeasesResponse = _reflection.GeneratedProtocolMessageType('QueryLeasesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYLEASESRESPONSE, '__module__': 'akash.market.v1beta2.query_pb2'})
_sym_db.RegisterMessage(QueryLeasesResponse)
QueryLeaseRequest = _reflection.GeneratedProtocolMessageType('QueryLeaseRequest', (_message.Message,), {'DESCRIPTOR': _QUERYLEASEREQUEST, '__module__': 'akash.market.v1beta2.query_pb2'})
_sym_db.RegisterMessage(QueryLeaseRequest)
QueryLeaseResponse = _reflection.GeneratedProtocolMessageType('QueryLeaseResponse', (_message.Message,), {'DESCRIPTOR': _QUERYLEASERESPONSE, '__module__': 'akash.market.v1beta2.query_pb2'})
_sym_db.RegisterMessage(QueryLeaseResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z.github.com/ovrclk/akash/x/market/types/v1beta2'
    _QUERYORDERSREQUEST.fields_by_name['filters']._options = None
    _QUERYORDERSREQUEST.fields_by_name['filters']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYORDERSRESPONSE.fields_by_name['orders']._options = None
    _QUERYORDERSRESPONSE.fields_by_name['orders']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\x06Orders'
    _QUERYORDERREQUEST.fields_by_name['id']._options = None
    _QUERYORDERREQUEST.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID'
    _QUERYORDERRESPONSE.fields_by_name['order']._options = None
    _QUERYORDERRESPONSE.fields_by_name['order']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYBIDSREQUEST.fields_by_name['filters']._options = None
    _QUERYBIDSREQUEST.fields_by_name['filters']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYBIDSRESPONSE.fields_by_name['bids']._options = None
    _QUERYBIDSRESPONSE.fields_by_name['bids']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYBIDREQUEST.fields_by_name['id']._options = None
    _QUERYBIDREQUEST.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID'
    _QUERYBIDRESPONSE.fields_by_name['bid']._options = None
    _QUERYBIDRESPONSE.fields_by_name['bid']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYBIDRESPONSE.fields_by_name['escrow_account']._options = None
    _QUERYBIDRESPONSE.fields_by_name['escrow_account']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYLEASESREQUEST.fields_by_name['filters']._options = None
    _QUERYLEASESREQUEST.fields_by_name['filters']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYLEASESRESPONSE.fields_by_name['leases']._options = None
    _QUERYLEASESRESPONSE.fields_by_name['leases']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYLEASEREQUEST.fields_by_name['id']._options = None
    _QUERYLEASEREQUEST.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID'
    _QUERYLEASERESPONSE.fields_by_name['lease']._options = None
    _QUERYLEASERESPONSE.fields_by_name['lease']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYLEASERESPONSE.fields_by_name['escrow_payment']._options = None
    _QUERYLEASERESPONSE.fields_by_name['escrow_payment']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Orders']._options = None
    _QUERY.methods_by_name['Orders']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/akash/market/v1beta2/orders/list'
    _QUERY.methods_by_name['Order']._options = None
    _QUERY.methods_by_name['Order']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/akash/market/v1beta2/orders/info'
    _QUERY.methods_by_name['Bids']._options = None
    _QUERY.methods_by_name['Bids']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/akash/market/v1beta2/bids/list'
    _QUERY.methods_by_name['Bid']._options = None
    _QUERY.methods_by_name['Bid']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/akash/market/v1beta2/bids/info'
    _QUERY.methods_by_name['Leases']._options = None
    _QUERY.methods_by_name['Leases']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/akash/market/v1beta2/leases/list'
    _QUERY.methods_by_name['Lease']._options = None
    _QUERY.methods_by_name['Lease']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/akash/market/v1beta2/leases/info'
    _QUERYORDERSREQUEST._serialized_start = 289
    _QUERYORDERSREQUEST._serialized_end = 428
    _QUERYORDERSRESPONSE._serialized_start = 431
    _QUERYORDERSRESPONSE._serialized_end = 574
    _QUERYORDERREQUEST._serialized_start = 576
    _QUERYORDERREQUEST._serialized_end = 650
    _QUERYORDERRESPONSE._serialized_start = 652
    _QUERYORDERRESPONSE._serialized_end = 722
    _QUERYBIDSREQUEST._serialized_start = 725
    _QUERYBIDSREQUEST._serialized_end = 860
    _QUERYBIDSRESPONSE._serialized_start = 863
    _QUERYBIDSRESPONSE._serialized_end = 1003
    _QUERYBIDREQUEST._serialized_start = 1005
    _QUERYBIDREQUEST._serialized_end = 1075
    _QUERYBIDRESPONSE._serialized_start = 1077
    _QUERYBIDRESPONSE._serialized_end = 1202
    _QUERYLEASESREQUEST._serialized_start = 1205
    _QUERYLEASESREQUEST._serialized_end = 1344
    _QUERYLEASESRESPONSE._serialized_start = 1347
    _QUERYLEASESRESPONSE._serialized_end = 1493
    _QUERYLEASEREQUEST._serialized_start = 1495
    _QUERYLEASEREQUEST._serialized_end = 1569
    _QUERYLEASERESPONSE._serialized_start = 1572
    _QUERYLEASERESPONSE._serialized_end = 1713
    _QUERY._serialized_start = 1716
    _QUERY._serialized_end = 2531

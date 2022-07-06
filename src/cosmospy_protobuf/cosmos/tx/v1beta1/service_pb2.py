
'Generated protocol buffer code.'
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.abci.v1beta1 import abci_pb2 as cosmos_dot_base_dot_abci_dot_v1beta1_dot_abci__pb2
from ....cosmos.tx.v1beta1 import tx_pb2 as cosmos_dot_tx_dot_v1beta1_dot_tx__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....tendermint.types import block_pb2 as tendermint_dot_types_dot_block__pb2
from ....tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/tx/v1beta1/service.proto\x12\x11cosmos.tx.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a#cosmos/base/abci/v1beta1/abci.proto\x1a\x1acosmos/tx/v1beta1/tx.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1ctendermint/types/block.proto\x1a\x1ctendermint/types/types.proto"\x8e\x01\n\x12GetTxsEventRequest\x12\x0e\n\x06events\x18\x01 \x03(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest\x12,\n\x08order_by\x18\x03 \x01(\x0e2\x1a.cosmos.tx.v1beta1.OrderBy"\xb2\x01\n\x13GetTxsEventResponse\x12"\n\x03txs\x18\x01 \x03(\x0b2\x15.cosmos.tx.v1beta1.Tx\x12:\n\x0ctx_responses\x18\x02 \x03(\x0b2$.cosmos.base.abci.v1beta1.TxResponse\x12;\n\npagination\x18\x03 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"V\n\x12BroadcastTxRequest\x12\x10\n\x08tx_bytes\x18\x01 \x01(\x0c\x12.\n\x04mode\x18\x02 \x01(\x0e2 .cosmos.tx.v1beta1.BroadcastMode"P\n\x13BroadcastTxResponse\x129\n\x0btx_response\x18\x01 \x01(\x0b2$.cosmos.base.abci.v1beta1.TxResponse"J\n\x0fSimulateRequest\x12%\n\x02tx\x18\x01 \x01(\x0b2\x15.cosmos.tx.v1beta1.TxB\x02\x18\x01\x12\x10\n\x08tx_bytes\x18\x02 \x01(\x0c"y\n\x10SimulateResponse\x123\n\x08gas_info\x18\x01 \x01(\x0b2!.cosmos.base.abci.v1beta1.GasInfo\x120\n\x06result\x18\x02 \x01(\x0b2 .cosmos.base.abci.v1beta1.Result"\x1c\n\x0cGetTxRequest\x12\x0c\n\x04hash\x18\x01 \x01(\t"m\n\rGetTxResponse\x12!\n\x02tx\x18\x01 \x01(\x0b2\x15.cosmos.tx.v1beta1.Tx\x129\n\x0btx_response\x18\x02 \x01(\x0b2$.cosmos.base.abci.v1beta1.TxResponse"d\n\x16GetBlockWithTxsRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xcf\x01\n\x17GetBlockWithTxsResponse\x12"\n\x03txs\x18\x01 \x03(\x0b2\x15.cosmos.tx.v1beta1.Tx\x12+\n\x08block_id\x18\x02 \x01(\x0b2\x19.tendermint.types.BlockID\x12&\n\x05block\x18\x03 \x01(\x0b2\x17.tendermint.types.Block\x12;\n\npagination\x18\x04 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse*H\n\x07OrderBy\x12\x18\n\x14ORDER_BY_UNSPECIFIED\x10\x00\x12\x10\n\x0cORDER_BY_ASC\x10\x01\x12\x11\n\rORDER_BY_DESC\x10\x02*|\n\rBroadcastMode\x12\x1e\n\x1aBROADCAST_MODE_UNSPECIFIED\x10\x00\x12\x18\n\x14BROADCAST_MODE_BLOCK\x10\x01\x12\x17\n\x13BROADCAST_MODE_SYNC\x10\x02\x12\x18\n\x14BROADCAST_MODE_ASYNC\x10\x032\x92\x05\n\x07Service\x12{\n\x08Simulate\x12".cosmos.tx.v1beta1.SimulateRequest\x1a#.cosmos.tx.v1beta1.SimulateResponse"&\x82\xd3\xe4\x93\x02 "\x1b/cosmos/tx/v1beta1/simulate:\x01*\x12q\n\x05GetTx\x12\x1f.cosmos.tx.v1beta1.GetTxRequest\x1a .cosmos.tx.v1beta1.GetTxResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/tx/v1beta1/txs/{hash}\x12\x7f\n\x0bBroadcastTx\x12%.cosmos.tx.v1beta1.BroadcastTxRequest\x1a&.cosmos.tx.v1beta1.BroadcastTxResponse"!\x82\xd3\xe4\x93\x02\x1b"\x16/cosmos/tx/v1beta1/txs:\x01*\x12|\n\x0bGetTxsEvent\x12%.cosmos.tx.v1beta1.GetTxsEventRequest\x1a&.cosmos.tx.v1beta1.GetTxsEventResponse"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/cosmos/tx/v1beta1/txs\x12\x97\x01\n\x0fGetBlockWithTxs\x12).cosmos.tx.v1beta1.GetBlockWithTxsRequest\x1a*.cosmos.tx.v1beta1.GetBlockWithTxsResponse"-\x82\xd3\xe4\x93\x02\'\x12%/cosmos/tx/v1beta1/txs/block/{height}B\'Z%github.com/cosmos/cosmos-sdk/types/txb\x06proto3')
_ORDERBY = DESCRIPTOR.enum_types_by_name['OrderBy']
OrderBy = enum_type_wrapper.EnumTypeWrapper(_ORDERBY)
_BROADCASTMODE = DESCRIPTOR.enum_types_by_name['BroadcastMode']
BroadcastMode = enum_type_wrapper.EnumTypeWrapper(_BROADCASTMODE)
ORDER_BY_UNSPECIFIED = 0
ORDER_BY_ASC = 1
ORDER_BY_DESC = 2
BROADCAST_MODE_UNSPECIFIED = 0
BROADCAST_MODE_BLOCK = 1
BROADCAST_MODE_SYNC = 2
BROADCAST_MODE_ASYNC = 3
_GETTXSEVENTREQUEST = DESCRIPTOR.message_types_by_name['GetTxsEventRequest']
_GETTXSEVENTRESPONSE = DESCRIPTOR.message_types_by_name['GetTxsEventResponse']
_BROADCASTTXREQUEST = DESCRIPTOR.message_types_by_name['BroadcastTxRequest']
_BROADCASTTXRESPONSE = DESCRIPTOR.message_types_by_name['BroadcastTxResponse']
_SIMULATEREQUEST = DESCRIPTOR.message_types_by_name['SimulateRequest']
_SIMULATERESPONSE = DESCRIPTOR.message_types_by_name['SimulateResponse']
_GETTXREQUEST = DESCRIPTOR.message_types_by_name['GetTxRequest']
_GETTXRESPONSE = DESCRIPTOR.message_types_by_name['GetTxResponse']
_GETBLOCKWITHTXSREQUEST = DESCRIPTOR.message_types_by_name['GetBlockWithTxsRequest']
_GETBLOCKWITHTXSRESPONSE = DESCRIPTOR.message_types_by_name['GetBlockWithTxsResponse']
GetTxsEventRequest = _reflection.GeneratedProtocolMessageType('GetTxsEventRequest', (_message.Message,), {'DESCRIPTOR': _GETTXSEVENTREQUEST, '__module__': 'cosmos.tx.v1beta1.service_pb2'})
_sym_db.RegisterMessage(GetTxsEventRequest)
GetTxsEventResponse = _reflection.GeneratedProtocolMessageType('GetTxsEventResponse', (_message.Message,), {'DESCRIPTOR': _GETTXSEVENTRESPONSE, '__module__': 'cosmos.tx.v1beta1.service_pb2'})
_sym_db.RegisterMessage(GetTxsEventResponse)
BroadcastTxRequest = _reflection.GeneratedProtocolMessageType('BroadcastTxRequest', (_message.Message,), {'DESCRIPTOR': _BROADCASTTXREQUEST, '__module__': 'cosmos.tx.v1beta1.service_pb2'})
_sym_db.RegisterMessage(BroadcastTxRequest)
BroadcastTxResponse = _reflection.GeneratedProtocolMessageType('BroadcastTxResponse', (_message.Message,), {'DESCRIPTOR': _BROADCASTTXRESPONSE, '__module__': 'cosmos.tx.v1beta1.service_pb2'})
_sym_db.RegisterMessage(BroadcastTxResponse)
SimulateRequest = _reflection.GeneratedProtocolMessageType('SimulateRequest', (_message.Message,), {'DESCRIPTOR': _SIMULATEREQUEST, '__module__': 'cosmos.tx.v1beta1.service_pb2'})
_sym_db.RegisterMessage(SimulateRequest)
SimulateResponse = _reflection.GeneratedProtocolMessageType('SimulateResponse', (_message.Message,), {'DESCRIPTOR': _SIMULATERESPONSE, '__module__': 'cosmos.tx.v1beta1.service_pb2'})
_sym_db.RegisterMessage(SimulateResponse)
GetTxRequest = _reflection.GeneratedProtocolMessageType('GetTxRequest', (_message.Message,), {'DESCRIPTOR': _GETTXREQUEST, '__module__': 'cosmos.tx.v1beta1.service_pb2'})
_sym_db.RegisterMessage(GetTxRequest)
GetTxResponse = _reflection.GeneratedProtocolMessageType('GetTxResponse', (_message.Message,), {'DESCRIPTOR': _GETTXRESPONSE, '__module__': 'cosmos.tx.v1beta1.service_pb2'})
_sym_db.RegisterMessage(GetTxResponse)
GetBlockWithTxsRequest = _reflection.GeneratedProtocolMessageType('GetBlockWithTxsRequest', (_message.Message,), {'DESCRIPTOR': _GETBLOCKWITHTXSREQUEST, '__module__': 'cosmos.tx.v1beta1.service_pb2'})
_sym_db.RegisterMessage(GetBlockWithTxsRequest)
GetBlockWithTxsResponse = _reflection.GeneratedProtocolMessageType('GetBlockWithTxsResponse', (_message.Message,), {'DESCRIPTOR': _GETBLOCKWITHTXSRESPONSE, '__module__': 'cosmos.tx.v1beta1.service_pb2'})
_sym_db.RegisterMessage(GetBlockWithTxsResponse)
_SERVICE = DESCRIPTOR.services_by_name['Service']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z%github.com/cosmos/cosmos-sdk/types/tx'
    _SIMULATEREQUEST.fields_by_name['tx']._options = None
    _SIMULATEREQUEST.fields_by_name['tx']._serialized_options = b'\x18\x01'
    _SERVICE.methods_by_name['Simulate']._options = None
    _SERVICE.methods_by_name['Simulate']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/cosmos/tx/v1beta1/simulate:\x01*'
    _SERVICE.methods_by_name['GetTx']._options = None
    _SERVICE.methods_by_name['GetTx']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/tx/v1beta1/txs/{hash}'
    _SERVICE.methods_by_name['BroadcastTx']._options = None
    _SERVICE.methods_by_name['BroadcastTx']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b"\x16/cosmos/tx/v1beta1/txs:\x01*'
    _SERVICE.methods_by_name['GetTxsEvent']._options = None
    _SERVICE.methods_by_name['GetTxsEvent']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18\x12\x16/cosmos/tx/v1beta1/txs'
    _SERVICE.methods_by_name['GetBlockWithTxs']._options = None
    _SERVICE.methods_by_name['GetBlockWithTxs']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/cosmos/tx/v1beta1/txs/block/{height}"
    _ORDERBY._serialized_start = 1401
    _ORDERBY._serialized_end = 1473
    _BROADCASTMODE._serialized_start = 1475
    _BROADCASTMODE._serialized_end = 1599
    _GETTXSEVENTREQUEST._serialized_start = 254
    _GETTXSEVENTREQUEST._serialized_end = 396
    _GETTXSEVENTRESPONSE._serialized_start = 399
    _GETTXSEVENTRESPONSE._serialized_end = 577
    _BROADCASTTXREQUEST._serialized_start = 579
    _BROADCASTTXREQUEST._serialized_end = 665
    _BROADCASTTXRESPONSE._serialized_start = 667
    _BROADCASTTXRESPONSE._serialized_end = 747
    _SIMULATEREQUEST._serialized_start = 749
    _SIMULATEREQUEST._serialized_end = 823
    _SIMULATERESPONSE._serialized_start = 825
    _SIMULATERESPONSE._serialized_end = 946
    _GETTXREQUEST._serialized_start = 948
    _GETTXREQUEST._serialized_end = 976
    _GETTXRESPONSE._serialized_start = 978
    _GETTXRESPONSE._serialized_end = 1087
    _GETBLOCKWITHTXSREQUEST._serialized_start = 1089
    _GETBLOCKWITHTXSREQUEST._serialized_end = 1189
    _GETBLOCKWITHTXSRESPONSE._serialized_start = 1192
    _GETBLOCKWITHTXSRESPONSE._serialized_end = 1399
    _SERVICE._serialized_start = 1602
    _SERVICE._serialized_end = 2260

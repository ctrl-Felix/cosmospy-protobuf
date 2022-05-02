
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ...cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ...cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ...osmosis.incentives import gauge_pb2 as osmosis_dot_incentives_dot_gauge__pb2
from ...osmosis.lockup import lock_pb2 as osmosis_dot_lockup_dot_lock__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eosmosis/incentives/query.proto\x12\x12osmosis.incentives\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1eosmosis/incentives/gauge.proto\x1a\x19osmosis/lockup/lock.proto" \n\x1eModuleToDistributeCoinsRequest"}\n\x1fModuleToDistributeCoinsResponse\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\x1f\n\x1dModuleDistributedCoinsRequest"|\n\x1eModuleDistributedCoinsResponse\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\x1e\n\x10GaugeByIDRequest\x12\n\n\x02id\x18\x01 \x01(\x04"=\n\x11GaugeByIDResponse\x12(\n\x05gauge\x18\x01 \x01(\x0b2\x19.osmosis.incentives.Gauge"K\n\rGaugesRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"|\n\x0eGaugesResponse\x12-\n\x04data\x18\x01 \x03(\x0b2\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"Q\n\x13ActiveGaugesRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x82\x01\n\x14ActiveGaugesResponse\x12-\n\x04data\x18\x01 \x03(\x0b2\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"h\n\x1bActiveGaugesPerDenomRequest\x12\r\n\x05denom\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8a\x01\n\x1cActiveGaugesPerDenomResponse\x12-\n\x04data\x18\x01 \x03(\x0b2\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"S\n\x15UpcomingGaugesRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x84\x01\n\x16UpcomingGaugesResponse\x12-\n\x04data\x18\x01 \x03(\x0b2\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"j\n\x1dUpcomingGaugesPerDenomRequest\x12\r\n\x05denom\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x97\x01\n\x1eUpcomingGaugesPerDenomResponse\x128\n\x0fupcoming_gauges\x18\x01 \x03(\x0b2\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"Y\n\x11RewardsEstRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12\x10\n\x08lock_ids\x18\x02 \x03(\x04\x12\x11\n\tend_epoch\x18\x03 \x01(\x03"p\n\x12RewardsEstResponse\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\x1f\n\x1dQueryLockableDurationsRequest"~\n\x1eQueryLockableDurationsResponse\x12\\\n\x12lockable_durations\x18\x01 \x03(\x0b2\x19.google.protobuf.DurationB%\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x19yaml:"lockable_durations"2\x96\r\n\x05Query\x12\xc2\x01\n\x17ModuleToDistributeCoins\x122.osmosis.incentives.ModuleToDistributeCoinsRequest\x1a3.osmosis.incentives.ModuleToDistributeCoinsResponse">\x82\xd3\xe4\x93\x028\x126/osmosis/incentives/v1beta1/module_to_distribute_coins\x12\xbd\x01\n\x16ModuleDistributedCoins\x121.osmosis.incentives.ModuleDistributedCoinsRequest\x1a2.osmosis.incentives.ModuleDistributedCoinsResponse"<\x82\xd3\xe4\x93\x026\x124/osmosis/incentives/v1beta1/module_distributed_coins\x12\x8e\x01\n\tGaugeByID\x12$.osmosis.incentives.GaugeByIDRequest\x1a%.osmosis.incentives.GaugeByIDResponse"4\x82\xd3\xe4\x93\x02.\x12,/osmosis/incentives/v1beta1/gauge_by_id/{id}\x12{\n\x06Gauges\x12!.osmosis.incentives.GaugesRequest\x1a".osmosis.incentives.GaugesResponse"*\x82\xd3\xe4\x93\x02$\x12"/osmosis/incentives/v1beta1/gauges\x12\x94\x01\n\x0cActiveGauges\x12\'.osmosis.incentives.ActiveGaugesRequest\x1a(.osmosis.incentives.ActiveGaugesResponse"1\x82\xd3\xe4\x93\x02+\x12)/osmosis/incentives/v1beta1/active_gauges\x12\xb6\x01\n\x14ActiveGaugesPerDenom\x12/.osmosis.incentives.ActiveGaugesPerDenomRequest\x1a0.osmosis.incentives.ActiveGaugesPerDenomResponse";\x82\xd3\xe4\x93\x025\x123/osmosis/incentives/v1beta1/active_gauges_per_denom\x12\x9c\x01\n\x0eUpcomingGauges\x12).osmosis.incentives.UpcomingGaugesRequest\x1a*.osmosis.incentives.UpcomingGaugesResponse"3\x82\xd3\xe4\x93\x02-\x12+/osmosis/incentives/v1beta1/upcoming_gauges\x12\xbe\x01\n\x16UpcomingGaugesPerDenom\x121.osmosis.incentives.UpcomingGaugesPerDenomRequest\x1a2.osmosis.incentives.UpcomingGaugesPerDenomResponse"=\x82\xd3\xe4\x93\x027\x125/osmosis/incentives/v1beta1/upcoming_gauges_per_denom\x12\x94\x01\n\nRewardsEst\x12%.osmosis.incentives.RewardsEstRequest\x1a&.osmosis.incentives.RewardsEstResponse"7\x82\xd3\xe4\x93\x021\x12//osmosis/incentives/v1beta1/rewards_est/{owner}\x12\xb2\x01\n\x11LockableDurations\x121.osmosis.incentives.QueryLockableDurationsRequest\x1a2.osmosis.incentives.QueryLockableDurationsResponse"6\x82\xd3\xe4\x93\x020\x12./osmosis/incentives/v1beta1/lockable_durationsB7Z5github.com/osmosis-labs/osmosis/v7/x/incentives/typesb\x06proto3')
_MODULETODISTRIBUTECOINSREQUEST = DESCRIPTOR.message_types_by_name['ModuleToDistributeCoinsRequest']
_MODULETODISTRIBUTECOINSRESPONSE = DESCRIPTOR.message_types_by_name['ModuleToDistributeCoinsResponse']
_MODULEDISTRIBUTEDCOINSREQUEST = DESCRIPTOR.message_types_by_name['ModuleDistributedCoinsRequest']
_MODULEDISTRIBUTEDCOINSRESPONSE = DESCRIPTOR.message_types_by_name['ModuleDistributedCoinsResponse']
_GAUGEBYIDREQUEST = DESCRIPTOR.message_types_by_name['GaugeByIDRequest']
_GAUGEBYIDRESPONSE = DESCRIPTOR.message_types_by_name['GaugeByIDResponse']
_GAUGESREQUEST = DESCRIPTOR.message_types_by_name['GaugesRequest']
_GAUGESRESPONSE = DESCRIPTOR.message_types_by_name['GaugesResponse']
_ACTIVEGAUGESREQUEST = DESCRIPTOR.message_types_by_name['ActiveGaugesRequest']
_ACTIVEGAUGESRESPONSE = DESCRIPTOR.message_types_by_name['ActiveGaugesResponse']
_ACTIVEGAUGESPERDENOMREQUEST = DESCRIPTOR.message_types_by_name['ActiveGaugesPerDenomRequest']
_ACTIVEGAUGESPERDENOMRESPONSE = DESCRIPTOR.message_types_by_name['ActiveGaugesPerDenomResponse']
_UPCOMINGGAUGESREQUEST = DESCRIPTOR.message_types_by_name['UpcomingGaugesRequest']
_UPCOMINGGAUGESRESPONSE = DESCRIPTOR.message_types_by_name['UpcomingGaugesResponse']
_UPCOMINGGAUGESPERDENOMREQUEST = DESCRIPTOR.message_types_by_name['UpcomingGaugesPerDenomRequest']
_UPCOMINGGAUGESPERDENOMRESPONSE = DESCRIPTOR.message_types_by_name['UpcomingGaugesPerDenomResponse']
_REWARDSESTREQUEST = DESCRIPTOR.message_types_by_name['RewardsEstRequest']
_REWARDSESTRESPONSE = DESCRIPTOR.message_types_by_name['RewardsEstResponse']
_QUERYLOCKABLEDURATIONSREQUEST = DESCRIPTOR.message_types_by_name['QueryLockableDurationsRequest']
_QUERYLOCKABLEDURATIONSRESPONSE = DESCRIPTOR.message_types_by_name['QueryLockableDurationsResponse']
ModuleToDistributeCoinsRequest = _reflection.GeneratedProtocolMessageType('ModuleToDistributeCoinsRequest', (_message.Message,), {'DESCRIPTOR': _MODULETODISTRIBUTECOINSREQUEST, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(ModuleToDistributeCoinsRequest)
ModuleToDistributeCoinsResponse = _reflection.GeneratedProtocolMessageType('ModuleToDistributeCoinsResponse', (_message.Message,), {'DESCRIPTOR': _MODULETODISTRIBUTECOINSRESPONSE, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(ModuleToDistributeCoinsResponse)
ModuleDistributedCoinsRequest = _reflection.GeneratedProtocolMessageType('ModuleDistributedCoinsRequest', (_message.Message,), {'DESCRIPTOR': _MODULEDISTRIBUTEDCOINSREQUEST, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(ModuleDistributedCoinsRequest)
ModuleDistributedCoinsResponse = _reflection.GeneratedProtocolMessageType('ModuleDistributedCoinsResponse', (_message.Message,), {'DESCRIPTOR': _MODULEDISTRIBUTEDCOINSRESPONSE, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(ModuleDistributedCoinsResponse)
GaugeByIDRequest = _reflection.GeneratedProtocolMessageType('GaugeByIDRequest', (_message.Message,), {'DESCRIPTOR': _GAUGEBYIDREQUEST, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(GaugeByIDRequest)
GaugeByIDResponse = _reflection.GeneratedProtocolMessageType('GaugeByIDResponse', (_message.Message,), {'DESCRIPTOR': _GAUGEBYIDRESPONSE, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(GaugeByIDResponse)
GaugesRequest = _reflection.GeneratedProtocolMessageType('GaugesRequest', (_message.Message,), {'DESCRIPTOR': _GAUGESREQUEST, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(GaugesRequest)
GaugesResponse = _reflection.GeneratedProtocolMessageType('GaugesResponse', (_message.Message,), {'DESCRIPTOR': _GAUGESRESPONSE, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(GaugesResponse)
ActiveGaugesRequest = _reflection.GeneratedProtocolMessageType('ActiveGaugesRequest', (_message.Message,), {'DESCRIPTOR': _ACTIVEGAUGESREQUEST, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(ActiveGaugesRequest)
ActiveGaugesResponse = _reflection.GeneratedProtocolMessageType('ActiveGaugesResponse', (_message.Message,), {'DESCRIPTOR': _ACTIVEGAUGESRESPONSE, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(ActiveGaugesResponse)
ActiveGaugesPerDenomRequest = _reflection.GeneratedProtocolMessageType('ActiveGaugesPerDenomRequest', (_message.Message,), {'DESCRIPTOR': _ACTIVEGAUGESPERDENOMREQUEST, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(ActiveGaugesPerDenomRequest)
ActiveGaugesPerDenomResponse = _reflection.GeneratedProtocolMessageType('ActiveGaugesPerDenomResponse', (_message.Message,), {'DESCRIPTOR': _ACTIVEGAUGESPERDENOMRESPONSE, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(ActiveGaugesPerDenomResponse)
UpcomingGaugesRequest = _reflection.GeneratedProtocolMessageType('UpcomingGaugesRequest', (_message.Message,), {'DESCRIPTOR': _UPCOMINGGAUGESREQUEST, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(UpcomingGaugesRequest)
UpcomingGaugesResponse = _reflection.GeneratedProtocolMessageType('UpcomingGaugesResponse', (_message.Message,), {'DESCRIPTOR': _UPCOMINGGAUGESRESPONSE, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(UpcomingGaugesResponse)
UpcomingGaugesPerDenomRequest = _reflection.GeneratedProtocolMessageType('UpcomingGaugesPerDenomRequest', (_message.Message,), {'DESCRIPTOR': _UPCOMINGGAUGESPERDENOMREQUEST, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(UpcomingGaugesPerDenomRequest)
UpcomingGaugesPerDenomResponse = _reflection.GeneratedProtocolMessageType('UpcomingGaugesPerDenomResponse', (_message.Message,), {'DESCRIPTOR': _UPCOMINGGAUGESPERDENOMRESPONSE, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(UpcomingGaugesPerDenomResponse)
RewardsEstRequest = _reflection.GeneratedProtocolMessageType('RewardsEstRequest', (_message.Message,), {'DESCRIPTOR': _REWARDSESTREQUEST, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(RewardsEstRequest)
RewardsEstResponse = _reflection.GeneratedProtocolMessageType('RewardsEstResponse', (_message.Message,), {'DESCRIPTOR': _REWARDSESTRESPONSE, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(RewardsEstResponse)
QueryLockableDurationsRequest = _reflection.GeneratedProtocolMessageType('QueryLockableDurationsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYLOCKABLEDURATIONSREQUEST, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(QueryLockableDurationsRequest)
QueryLockableDurationsResponse = _reflection.GeneratedProtocolMessageType('QueryLockableDurationsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYLOCKABLEDURATIONSRESPONSE, '__module__': 'osmosis.incentives.query_pb2'})
_sym_db.RegisterMessage(QueryLockableDurationsResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/osmosis-labs/osmosis/v7/x/incentives/types'
    _MODULETODISTRIBUTECOINSRESPONSE.fields_by_name['coins']._options = None
    _MODULETODISTRIBUTECOINSRESPONSE.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MODULEDISTRIBUTEDCOINSRESPONSE.fields_by_name['coins']._options = None
    _MODULEDISTRIBUTEDCOINSRESPONSE.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _GAUGESRESPONSE.fields_by_name['data']._options = None
    _GAUGESRESPONSE.fields_by_name['data']._serialized_options = b'\xc8\xde\x1f\x00'
    _ACTIVEGAUGESRESPONSE.fields_by_name['data']._options = None
    _ACTIVEGAUGESRESPONSE.fields_by_name['data']._serialized_options = b'\xc8\xde\x1f\x00'
    _ACTIVEGAUGESPERDENOMRESPONSE.fields_by_name['data']._options = None
    _ACTIVEGAUGESPERDENOMRESPONSE.fields_by_name['data']._serialized_options = b'\xc8\xde\x1f\x00'
    _UPCOMINGGAUGESRESPONSE.fields_by_name['data']._options = None
    _UPCOMINGGAUGESRESPONSE.fields_by_name['data']._serialized_options = b'\xc8\xde\x1f\x00'
    _UPCOMINGGAUGESPERDENOMRESPONSE.fields_by_name['upcoming_gauges']._options = None
    _UPCOMINGGAUGESPERDENOMRESPONSE.fields_by_name['upcoming_gauges']._serialized_options = b'\xc8\xde\x1f\x00'
    _REWARDSESTREQUEST.fields_by_name['owner']._options = None
    _REWARDSESTREQUEST.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _REWARDSESTRESPONSE.fields_by_name['coins']._options = None
    _REWARDSESTRESPONSE.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYLOCKABLEDURATIONSRESPONSE.fields_by_name['lockable_durations']._options = None
    _QUERYLOCKABLEDURATIONSRESPONSE.fields_by_name['lockable_durations']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x19yaml:"lockable_durations"'
    _QUERY.methods_by_name['ModuleToDistributeCoins']._options = None
    _QUERY.methods_by_name['ModuleToDistributeCoins']._serialized_options = b'\x82\xd3\xe4\x93\x028\x126/osmosis/incentives/v1beta1/module_to_distribute_coins'
    _QUERY.methods_by_name['ModuleDistributedCoins']._options = None
    _QUERY.methods_by_name['ModuleDistributedCoins']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/osmosis/incentives/v1beta1/module_distributed_coins'
    _QUERY.methods_by_name['GaugeByID']._options = None
    _QUERY.methods_by_name['GaugeByID']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/osmosis/incentives/v1beta1/gauge_by_id/{id}'
    _QUERY.methods_by_name['Gauges']._options = None
    _QUERY.methods_by_name['Gauges']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/osmosis/incentives/v1beta1/gauges'
    _QUERY.methods_by_name['ActiveGauges']._options = None
    _QUERY.methods_by_name['ActiveGauges']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/osmosis/incentives/v1beta1/active_gauges'
    _QUERY.methods_by_name['ActiveGaugesPerDenom']._options = None
    _QUERY.methods_by_name['ActiveGaugesPerDenom']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/osmosis/incentives/v1beta1/active_gauges_per_denom'
    _QUERY.methods_by_name['UpcomingGauges']._options = None
    _QUERY.methods_by_name['UpcomingGauges']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/osmosis/incentives/v1beta1/upcoming_gauges'
    _QUERY.methods_by_name['UpcomingGaugesPerDenom']._options = None
    _QUERY.methods_by_name['UpcomingGaugesPerDenom']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/osmosis/incentives/v1beta1/upcoming_gauges_per_denom'
    _QUERY.methods_by_name['RewardsEst']._options = None
    _QUERY.methods_by_name['RewardsEst']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//osmosis/incentives/v1beta1/rewards_est/{owner}'
    _QUERY.methods_by_name['LockableDurations']._options = None
    _QUERY.methods_by_name['LockableDurations']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./osmosis/incentives/v1beta1/lockable_durations'
    _MODULETODISTRIBUTECOINSREQUEST._serialized_start = 273
    _MODULETODISTRIBUTECOINSREQUEST._serialized_end = 305
    _MODULETODISTRIBUTECOINSRESPONSE._serialized_start = 307
    _MODULETODISTRIBUTECOINSRESPONSE._serialized_end = 432
    _MODULEDISTRIBUTEDCOINSREQUEST._serialized_start = 434
    _MODULEDISTRIBUTEDCOINSREQUEST._serialized_end = 465
    _MODULEDISTRIBUTEDCOINSRESPONSE._serialized_start = 467
    _MODULEDISTRIBUTEDCOINSRESPONSE._serialized_end = 591
    _GAUGEBYIDREQUEST._serialized_start = 593
    _GAUGEBYIDREQUEST._serialized_end = 623
    _GAUGEBYIDRESPONSE._serialized_start = 625
    _GAUGEBYIDRESPONSE._serialized_end = 686
    _GAUGESREQUEST._serialized_start = 688
    _GAUGESREQUEST._serialized_end = 763
    _GAUGESRESPONSE._serialized_start = 765
    _GAUGESRESPONSE._serialized_end = 889
    _ACTIVEGAUGESREQUEST._serialized_start = 891
    _ACTIVEGAUGESREQUEST._serialized_end = 972
    _ACTIVEGAUGESRESPONSE._serialized_start = 975
    _ACTIVEGAUGESRESPONSE._serialized_end = 1105
    _ACTIVEGAUGESPERDENOMREQUEST._serialized_start = 1107
    _ACTIVEGAUGESPERDENOMREQUEST._serialized_end = 1211
    _ACTIVEGAUGESPERDENOMRESPONSE._serialized_start = 1214
    _ACTIVEGAUGESPERDENOMRESPONSE._serialized_end = 1352
    _UPCOMINGGAUGESREQUEST._serialized_start = 1354
    _UPCOMINGGAUGESREQUEST._serialized_end = 1437
    _UPCOMINGGAUGESRESPONSE._serialized_start = 1440
    _UPCOMINGGAUGESRESPONSE._serialized_end = 1572
    _UPCOMINGGAUGESPERDENOMREQUEST._serialized_start = 1574
    _UPCOMINGGAUGESPERDENOMREQUEST._serialized_end = 1680
    _UPCOMINGGAUGESPERDENOMRESPONSE._serialized_start = 1683
    _UPCOMINGGAUGESPERDENOMRESPONSE._serialized_end = 1834
    _REWARDSESTREQUEST._serialized_start = 1836
    _REWARDSESTREQUEST._serialized_end = 1925
    _REWARDSESTRESPONSE._serialized_start = 1927
    _REWARDSESTRESPONSE._serialized_end = 2039
    _QUERYLOCKABLEDURATIONSREQUEST._serialized_start = 2041
    _QUERYLOCKABLEDURATIONSREQUEST._serialized_end = 2072
    _QUERYLOCKABLEDURATIONSRESPONSE._serialized_start = 2074
    _QUERYLOCKABLEDURATIONSRESPONSE._serialized_end = 2200
    _QUERY._serialized_start = 2203
    _QUERY._serialized_end = 3889

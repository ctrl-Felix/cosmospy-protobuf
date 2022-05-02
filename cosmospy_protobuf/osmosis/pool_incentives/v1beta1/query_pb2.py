
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....osmosis.incentives import gauge_pb2 as osmosis_dot_incentives_dot_gauge__pb2
from ....osmosis.pool_incentives.v1beta1 import incentives_pb2 as osmosis_dot_pool__incentives_dot_v1beta1_dot_incentives__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+osmosis/pool-incentives/v1beta1/query.proto\x12\x1eosmosis.poolincentives.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1eosmosis/incentives/gauge.proto\x1a0osmosis/pool-incentives/v1beta1/incentives.proto";\n\x14QueryGaugeIdsRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id""\x9d\x02\n\x15QueryGaugeIdsResponse\x12\x8e\x01\n\x17gauge_ids_with_duration\x18\x01 \x03(\x0b2I.osmosis.poolincentives.v1beta1.QueryGaugeIdsResponse.GaugeIdWithDurationB"\xf2\xde\x1f\x1eyaml:"gauge_ids_with_duration"\x1as\n\x13GaugeIdWithDuration\x12%\n\x08gauge_id\x18\x01 \x01(\x04B\x13\xf2\xde\x1f\x0fyaml:"gauge_id"\x125\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01"\x17\n\x15QueryDistrInfoRequest"r\n\x16QueryDistrInfoResponse\x12X\n\ndistr_info\x18\x01 \x01(\x0b2).osmosis.poolincentives.v1beta1.DistrInfoB\x19\xc8\xde\x1f\x00\xf2\xde\x1f\x11yaml:"distr_info""\x14\n\x12QueryParamsRequest"S\n\x13QueryParamsResponse\x12<\n\x06params\x18\x01 \x01(\x0b2&.osmosis.poolincentives.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"\x1f\n\x1dQueryLockableDurationsRequest"~\n\x1eQueryLockableDurationsResponse\x12\\\n\x12lockable_durations\x18\x01 \x03(\x0b2\x19.google.protobuf.DurationB%\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x19yaml:"lockable_durations""\x1f\n\x1dQueryIncentivizedPoolsRequest"\xba\x01\n\x10IncentivizedPool\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12Z\n\x11lockable_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB$\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x18yaml:"lockable_duration"\x12%\n\x08gauge_id\x18\x03 \x01(\x04B\x13\xf2\xde\x1f\x0fyaml:"gauge_id""\x91\x01\n\x1eQueryIncentivizedPoolsResponse\x12o\n\x12incentivized_pools\x18\x01 \x03(\x0b20.osmosis.poolincentives.v1beta1.IncentivizedPoolB!\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:"incentivized_pools""%\n#QueryExternalIncentiveGaugesRequest"U\n$QueryExternalIncentiveGaugesResponse\x12-\n\x04data\x18\x01 \x03(\x0b2\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x002\xa5\t\n\x05Query\x12\xb5\x01\n\x08GaugeIds\x124.osmosis.poolincentives.v1beta1.QueryGaugeIdsRequest\x1a5.osmosis.poolincentives.v1beta1.QueryGaugeIdsResponse"<\x82\xd3\xe4\x93\x026\x124/osmosis/pool-incentives/v1beta1/gauge-ids/{pool_id}\x12\xaf\x01\n\tDistrInfo\x125.osmosis.poolincentives.v1beta1.QueryDistrInfoRequest\x1a6.osmosis.poolincentives.v1beta1.QueryDistrInfoResponse"3\x82\xd3\xe4\x93\x02-\x12+/osmosis/pool-incentives/v1beta1/distr_info\x12\xa2\x01\n\x06Params\x122.osmosis.poolincentives.v1beta1.QueryParamsRequest\x1a3.osmosis.poolincentives.v1beta1.QueryParamsResponse"/\x82\xd3\xe4\x93\x02)\x12\'/osmosis/pool-incentives/v1beta1/params\x12\xcf\x01\n\x11LockableDurations\x12=.osmosis.poolincentives.v1beta1.QueryLockableDurationsRequest\x1a>.osmosis.poolincentives.v1beta1.QueryLockableDurationsResponse";\x82\xd3\xe4\x93\x025\x123/osmosis/pool-incentives/v1beta1/lockable_durations\x12\xcf\x01\n\x11IncentivizedPools\x12=.osmosis.poolincentives.v1beta1.QueryIncentivizedPoolsRequest\x1a>.osmosis.poolincentives.v1beta1.QueryIncentivizedPoolsResponse";\x82\xd3\xe4\x93\x025\x123/osmosis/pool-incentives/v1beta1/incentivized_pools\x12\xe8\x01\n\x17ExternalIncentiveGauges\x12C.osmosis.poolincentives.v1beta1.QueryExternalIncentiveGaugesRequest\x1aD.osmosis.poolincentives.v1beta1.QueryExternalIncentiveGaugesResponse"B\x82\xd3\xe4\x93\x02<\x12:/osmosis/pool-incentives/v1beta1/external_incentive_gaugesB<Z:github.com/osmosis-labs/osmosis/v7/x/pool-incentives/typesb\x06proto3')
_QUERYGAUGEIDSREQUEST = DESCRIPTOR.message_types_by_name['QueryGaugeIdsRequest']
_QUERYGAUGEIDSRESPONSE = DESCRIPTOR.message_types_by_name['QueryGaugeIdsResponse']
_QUERYGAUGEIDSRESPONSE_GAUGEIDWITHDURATION = _QUERYGAUGEIDSRESPONSE.nested_types_by_name['GaugeIdWithDuration']
_QUERYDISTRINFOREQUEST = DESCRIPTOR.message_types_by_name['QueryDistrInfoRequest']
_QUERYDISTRINFORESPONSE = DESCRIPTOR.message_types_by_name['QueryDistrInfoResponse']
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
_QUERYLOCKABLEDURATIONSREQUEST = DESCRIPTOR.message_types_by_name['QueryLockableDurationsRequest']
_QUERYLOCKABLEDURATIONSRESPONSE = DESCRIPTOR.message_types_by_name['QueryLockableDurationsResponse']
_QUERYINCENTIVIZEDPOOLSREQUEST = DESCRIPTOR.message_types_by_name['QueryIncentivizedPoolsRequest']
_INCENTIVIZEDPOOL = DESCRIPTOR.message_types_by_name['IncentivizedPool']
_QUERYINCENTIVIZEDPOOLSRESPONSE = DESCRIPTOR.message_types_by_name['QueryIncentivizedPoolsResponse']
_QUERYEXTERNALINCENTIVEGAUGESREQUEST = DESCRIPTOR.message_types_by_name['QueryExternalIncentiveGaugesRequest']
_QUERYEXTERNALINCENTIVEGAUGESRESPONSE = DESCRIPTOR.message_types_by_name['QueryExternalIncentiveGaugesResponse']
QueryGaugeIdsRequest = _reflection.GeneratedProtocolMessageType('QueryGaugeIdsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYGAUGEIDSREQUEST, '__module__': 'osmosis.pool_incentives.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryGaugeIdsRequest)
QueryGaugeIdsResponse = _reflection.GeneratedProtocolMessageType('QueryGaugeIdsResponse', (_message.Message,), {'GaugeIdWithDuration': _reflection.GeneratedProtocolMessageType('GaugeIdWithDuration', (_message.Message,), {'DESCRIPTOR': _QUERYGAUGEIDSRESPONSE_GAUGEIDWITHDURATION, '__module__': 'osmosis.pool_incentives.v1beta1.query_pb2'}), 'DESCRIPTOR': _QUERYGAUGEIDSRESPONSE, '__module__': 'osmosis.pool_incentives.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryGaugeIdsResponse)
_sym_db.RegisterMessage(QueryGaugeIdsResponse.GaugeIdWithDuration)
QueryDistrInfoRequest = _reflection.GeneratedProtocolMessageType('QueryDistrInfoRequest', (_message.Message,), {'DESCRIPTOR': _QUERYDISTRINFOREQUEST, '__module__': 'osmosis.pool_incentives.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDistrInfoRequest)
QueryDistrInfoResponse = _reflection.GeneratedProtocolMessageType('QueryDistrInfoResponse', (_message.Message,), {'DESCRIPTOR': _QUERYDISTRINFORESPONSE, '__module__': 'osmosis.pool_incentives.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDistrInfoResponse)
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSREQUEST, '__module__': 'osmosis.pool_incentives.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsRequest)
QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSRESPONSE, '__module__': 'osmosis.pool_incentives.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryParamsResponse)
QueryLockableDurationsRequest = _reflection.GeneratedProtocolMessageType('QueryLockableDurationsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYLOCKABLEDURATIONSREQUEST, '__module__': 'osmosis.pool_incentives.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryLockableDurationsRequest)
QueryLockableDurationsResponse = _reflection.GeneratedProtocolMessageType('QueryLockableDurationsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYLOCKABLEDURATIONSRESPONSE, '__module__': 'osmosis.pool_incentives.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryLockableDurationsResponse)
QueryIncentivizedPoolsRequest = _reflection.GeneratedProtocolMessageType('QueryIncentivizedPoolsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYINCENTIVIZEDPOOLSREQUEST, '__module__': 'osmosis.pool_incentives.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryIncentivizedPoolsRequest)
IncentivizedPool = _reflection.GeneratedProtocolMessageType('IncentivizedPool', (_message.Message,), {'DESCRIPTOR': _INCENTIVIZEDPOOL, '__module__': 'osmosis.pool_incentives.v1beta1.query_pb2'})
_sym_db.RegisterMessage(IncentivizedPool)
QueryIncentivizedPoolsResponse = _reflection.GeneratedProtocolMessageType('QueryIncentivizedPoolsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYINCENTIVIZEDPOOLSRESPONSE, '__module__': 'osmosis.pool_incentives.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryIncentivizedPoolsResponse)
QueryExternalIncentiveGaugesRequest = _reflection.GeneratedProtocolMessageType('QueryExternalIncentiveGaugesRequest', (_message.Message,), {'DESCRIPTOR': _QUERYEXTERNALINCENTIVEGAUGESREQUEST, '__module__': 'osmosis.pool_incentives.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryExternalIncentiveGaugesRequest)
QueryExternalIncentiveGaugesResponse = _reflection.GeneratedProtocolMessageType('QueryExternalIncentiveGaugesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYEXTERNALINCENTIVEGAUGESRESPONSE, '__module__': 'osmosis.pool_incentives.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryExternalIncentiveGaugesResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z:github.com/osmosis-labs/osmosis/v7/x/pool-incentives/types'
    _QUERYGAUGEIDSREQUEST.fields_by_name['pool_id']._options = None
    _QUERYGAUGEIDSREQUEST.fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _QUERYGAUGEIDSRESPONSE_GAUGEIDWITHDURATION.fields_by_name['gauge_id']._options = None
    _QUERYGAUGEIDSRESPONSE_GAUGEIDWITHDURATION.fields_by_name['gauge_id']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"gauge_id"'
    _QUERYGAUGEIDSRESPONSE_GAUGEIDWITHDURATION.fields_by_name['duration']._options = None
    _QUERYGAUGEIDSRESPONSE_GAUGEIDWITHDURATION.fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _QUERYGAUGEIDSRESPONSE.fields_by_name['gauge_ids_with_duration']._options = None
    _QUERYGAUGEIDSRESPONSE.fields_by_name['gauge_ids_with_duration']._serialized_options = b'\xf2\xde\x1f\x1eyaml:"gauge_ids_with_duration"'
    _QUERYDISTRINFORESPONSE.fields_by_name['distr_info']._options = None
    _QUERYDISTRINFORESPONSE.fields_by_name['distr_info']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x11yaml:"distr_info"'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYLOCKABLEDURATIONSRESPONSE.fields_by_name['lockable_durations']._options = None
    _QUERYLOCKABLEDURATIONSRESPONSE.fields_by_name['lockable_durations']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x19yaml:"lockable_durations"'
    _INCENTIVIZEDPOOL.fields_by_name['pool_id']._options = None
    _INCENTIVIZEDPOOL.fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _INCENTIVIZEDPOOL.fields_by_name['lockable_duration']._options = None
    _INCENTIVIZEDPOOL.fields_by_name['lockable_duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x18yaml:"lockable_duration"'
    _INCENTIVIZEDPOOL.fields_by_name['gauge_id']._options = None
    _INCENTIVIZEDPOOL.fields_by_name['gauge_id']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"gauge_id"'
    _QUERYINCENTIVIZEDPOOLSRESPONSE.fields_by_name['incentivized_pools']._options = None
    _QUERYINCENTIVIZEDPOOLSRESPONSE.fields_by_name['incentivized_pools']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:"incentivized_pools"'
    _QUERYEXTERNALINCENTIVEGAUGESRESPONSE.fields_by_name['data']._options = None
    _QUERYEXTERNALINCENTIVEGAUGESRESPONSE.fields_by_name['data']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['GaugeIds']._options = None
    _QUERY.methods_by_name['GaugeIds']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/osmosis/pool-incentives/v1beta1/gauge-ids/{pool_id}'
    _QUERY.methods_by_name['DistrInfo']._options = None
    _QUERY.methods_by_name['DistrInfo']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/osmosis/pool-incentives/v1beta1/distr_info'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/osmosis/pool-incentives/v1beta1/params"
    _QUERY.methods_by_name['LockableDurations']._options = None
    _QUERY.methods_by_name['LockableDurations']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/osmosis/pool-incentives/v1beta1/lockable_durations'
    _QUERY.methods_by_name['IncentivizedPools']._options = None
    _QUERY.methods_by_name['IncentivizedPools']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/osmosis/pool-incentives/v1beta1/incentivized_pools'
    _QUERY.methods_by_name['ExternalIncentiveGauges']._options = None
    _QUERY.methods_by_name['ExternalIncentiveGauges']._serialized_options = b'\x82\xd3\xe4\x93\x02<\x12:/osmosis/pool-incentives/v1beta1/external_incentive_gauges'
    _QUERYGAUGEIDSREQUEST._serialized_start = 245
    _QUERYGAUGEIDSREQUEST._serialized_end = 304
    _QUERYGAUGEIDSRESPONSE._serialized_start = 307
    _QUERYGAUGEIDSRESPONSE._serialized_end = 592
    _QUERYGAUGEIDSRESPONSE_GAUGEIDWITHDURATION._serialized_start = 477
    _QUERYGAUGEIDSRESPONSE_GAUGEIDWITHDURATION._serialized_end = 592
    _QUERYDISTRINFOREQUEST._serialized_start = 594
    _QUERYDISTRINFOREQUEST._serialized_end = 617
    _QUERYDISTRINFORESPONSE._serialized_start = 619
    _QUERYDISTRINFORESPONSE._serialized_end = 733
    _QUERYPARAMSREQUEST._serialized_start = 735
    _QUERYPARAMSREQUEST._serialized_end = 755
    _QUERYPARAMSRESPONSE._serialized_start = 757
    _QUERYPARAMSRESPONSE._serialized_end = 840
    _QUERYLOCKABLEDURATIONSREQUEST._serialized_start = 842
    _QUERYLOCKABLEDURATIONSREQUEST._serialized_end = 873
    _QUERYLOCKABLEDURATIONSRESPONSE._serialized_start = 875
    _QUERYLOCKABLEDURATIONSRESPONSE._serialized_end = 1001
    _QUERYINCENTIVIZEDPOOLSREQUEST._serialized_start = 1003
    _QUERYINCENTIVIZEDPOOLSREQUEST._serialized_end = 1034
    _INCENTIVIZEDPOOL._serialized_start = 1037
    _INCENTIVIZEDPOOL._serialized_end = 1223
    _QUERYINCENTIVIZEDPOOLSRESPONSE._serialized_start = 1226
    _QUERYINCENTIVIZEDPOOLSRESPONSE._serialized_end = 1371
    _QUERYEXTERNALINCENTIVEGAUGESREQUEST._serialized_start = 1373
    _QUERYEXTERNALINCENTIVEGAUGESREQUEST._serialized_end = 1410
    _QUERYEXTERNALINCENTIVEGAUGESRESPONSE._serialized_start = 1412
    _QUERYEXTERNALINCENTIVEGAUGESRESPONSE._serialized_end = 1497
    _QUERY._serialized_start = 1500
    _QUERY._serialized_end = 2689

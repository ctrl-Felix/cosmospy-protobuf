
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ...google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ...osmosis.superfluid import superfluid_pb2 as osmosis_dot_superfluid_dot_superfluid__pb2
from ...osmosis.superfluid import params_pb2 as osmosis_dot_superfluid_dot_params__pb2
from ...osmosis.lockup import lock_pb2 as osmosis_dot_lockup_dot_lock__pb2
from ...cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eosmosis/superfluid/query.proto\x12\x12osmosis.superfluid\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a#osmosis/superfluid/superfluid.proto\x1a\x1fosmosis/superfluid/params.proto\x1a\x19osmosis/lockup/lock.proto\x1a*cosmos/base/query/v1beta1/pagination.proto"\x14\n\x12QueryParamsRequest"G\n\x13QueryParamsResponse\x120\n\x06params\x18\x01 \x01(\x0b2\x1a.osmosis.superfluid.ParamsB\x04\xc8\xde\x1f\x00"!\n\x10AssetTypeRequest\x12\r\n\x05denom\x18\x01 \x01(\t"P\n\x11AssetTypeResponse\x12;\n\nasset_type\x18\x01 \x01(\x0e2\'.osmosis.superfluid.SuperfluidAssetType"\x12\n\x10AllAssetsRequest"N\n\x11AllAssetsResponse\x129\n\x06assets\x18\x01 \x03(\x0b2#.osmosis.superfluid.SuperfluidAssetB\x04\xc8\xde\x1f\x00"\'\n\x16AssetMultiplierRequest\x12\r\n\x05denom\x18\x01 \x01(\t"q\n\x17AssetMultiplierResponse\x12V\n\x1aosmo_equivalent_multiplier\x18\x01 \x01(\x0b22.osmosis.superfluid.OsmoEquivalentMultiplierRecord"g\n!SuperfluidIntermediaryAccountInfo\x12\r\n\x05denom\x18\x01 \x01(\t\x12\x10\n\x08val_addr\x18\x02 \x01(\t\x12\x10\n\x08gauge_id\x18\x03 \x01(\x04\x12\x0f\n\x07address\x18\x04 \x01(\t"\\\n\x1eAllIntermediaryAccountsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xad\x01\n\x1fAllIntermediaryAccountsResponse\x12M\n\x08accounts\x18\x01 \x03(\x0b25.osmosis.superfluid.SuperfluidIntermediaryAccountInfoB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"6\n#ConnectedIntermediaryAccountRequest\x12\x0f\n\x07lock_id\x18\x01 \x01(\x04"n\n$ConnectedIntermediaryAccountResponse\x12F\n\x07account\x18\x01 \x01(\x0b25.osmosis.superfluid.SuperfluidIntermediaryAccountInfo"#\n!TotalSuperfluidDelegationsRequest"\x95\x01\n"TotalSuperfluidDelegationsResponse\x12o\n\x10totalDelegations\x18\x01 \x01(\tBU\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f#yaml:"total_superfluid_delegations"\xc8\xde\x1f\x00"h\n!SuperfluidDelegationAmountRequest\x12\x19\n\x11delegator_address\x18\x01 \x01(\t\x12\x19\n\x11validator_address\x18\x02 \x01(\t\x12\r\n\x05denom\x18\x03 \x01(\t"\x81\x01\n"SuperfluidDelegationAmountResponse\x12[\n\x06amount\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"D\n\'SuperfluidDelegationsByDelegatorRequest\x12\x19\n\x11delegator_address\x18\x01 \x01(\t"\xf3\x01\n(SuperfluidDelegationsByDelegatorResponse\x12[\n\x1dsuperfluid_delegation_records\x18\x01 \x03(\x0b2..osmosis.superfluid.SuperfluidDelegationRecordB\x04\xc8\xde\x1f\x00\x12j\n\x15total_delegated_coins\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"U\n)SuperfluidUndelegationsByDelegatorRequest\x12\x19\n\x11delegator_address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"\xb5\x02\n*SuperfluidUndelegationsByDelegatorResponse\x12[\n\x1dsuperfluid_delegation_records\x18\x01 \x03(\x0b2..osmosis.superfluid.SuperfluidDelegationRecordB\x04\xc8\xde\x1f\x00\x12l\n\x17total_undelegated_coins\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12<\n\x0fsynthetic_locks\x18\x03 \x03(\x0b2\x1d.osmosis.lockup.SyntheticLockB\x04\xc8\xde\x1f\x00"X\n,SuperfluidDelegationsByValidatorDenomRequest\x12\x19\n\x11validator_address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"\x8c\x01\n-SuperfluidDelegationsByValidatorDenomResponse\x12[\n\x1dsuperfluid_delegation_records\x18\x01 \x03(\x0b2..osmosis.superfluid.SuperfluidDelegationRecordB\x04\xc8\xde\x1f\x00"d\n8EstimateSuperfluidDelegatedAmountByValidatorDenomRequest\x12\x19\n\x11validator_address\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"\xa7\x01\n9EstimateSuperfluidDelegatedAmountByValidatorDenomResponse\x12j\n\x15total_delegated_coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins2\xb0\x13\n\x05Query\x12\x85\x01\n\x06Params\x12&.osmosis.superfluid.QueryParamsRequest\x1a\'.osmosis.superfluid.QueryParamsResponse"*\x82\xd3\xe4\x93\x02$\x12"/osmosis/superfluid/v1beta1/params\x12\x88\x01\n\tAssetType\x12$.osmosis.superfluid.AssetTypeRequest\x1a%.osmosis.superfluid.AssetTypeResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/superfluid/v1beta1/asset_type\x12\x88\x01\n\tAllAssets\x12$.osmosis.superfluid.AllAssetsRequest\x1a%.osmosis.superfluid.AllAssetsResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/superfluid/v1beta1/all_assets\x12\xa0\x01\n\x0fAssetMultiplier\x12*.osmosis.superfluid.AssetMultiplierRequest\x1a+.osmosis.superfluid.AssetMultiplierResponse"4\x82\xd3\xe4\x93\x02.\x12,/osmosis/superfluid/v1beta1/asset_multiplier\x12\xc1\x01\n\x17AllIntermediaryAccounts\x122.osmosis.superfluid.AllIntermediaryAccountsRequest\x1a3.osmosis.superfluid.AllIntermediaryAccountsResponse"=\x82\xd3\xe4\x93\x027\x125/osmosis/superfluid/v1beta1/all_intermediary_accounts\x12\xdf\x01\n\x1cConnectedIntermediaryAccount\x127.osmosis.superfluid.ConnectedIntermediaryAccountRequest\x1a8.osmosis.superfluid.ConnectedIntermediaryAccountResponse"L\x82\xd3\xe4\x93\x02F\x12D/osmosis/superfluid/v1beta1/connected_intermediary_account/{lock_id}\x12\xcb\x01\n\x1aTotalSuperfluidDelegations\x125.osmosis.superfluid.TotalSuperfluidDelegationsRequest\x1a6.osmosis.superfluid.TotalSuperfluidDelegationsResponse">\x82\xd3\xe4\x93\x028\x126/osmosis/superfluid/v1beta1/all_superfluid_delegations\x12\xcd\x01\n\x1aSuperfluidDelegationAmount\x125.osmosis.superfluid.SuperfluidDelegationAmountRequest\x1a6.osmosis.superfluid.SuperfluidDelegationAmountResponse"@\x82\xd3\xe4\x93\x02:\x128/osmosis/superfluid/v1beta1/superfluid_delegation_amount\x12\xed\x01\n SuperfluidDelegationsByDelegator\x12;.osmosis.superfluid.SuperfluidDelegationsByDelegatorRequest\x1a<.osmosis.superfluid.SuperfluidDelegationsByDelegatorResponse"N\x82\xd3\xe4\x93\x02H\x12F/osmosis/superfluid/v1beta1/superfluid_delegations/{delegator_address}\x12\x82\x02\n"SuperfluidUndelegationsByDelegator\x12=.osmosis.superfluid.SuperfluidUndelegationsByDelegatorRequest\x1a>.osmosis.superfluid.SuperfluidUndelegationsByDelegatorResponse"]\x82\xd3\xe4\x93\x02W\x12U/osmosis/superfluid/v1beta1/superfluid_undelegations_by_delegator/{delegator_address}\x12\xfb\x01\n%SuperfluidDelegationsByValidatorDenom\x12@.osmosis.superfluid.SuperfluidDelegationsByValidatorDenomRequest\x1aA.osmosis.superfluid.SuperfluidDelegationsByValidatorDenomResponse"M\x82\xd3\xe4\x93\x02G\x12E/osmosis/superfluid/v1beta1/superfluid_delegations_by_validator_denom\x12\xae\x02\n1EstimateSuperfluidDelegatedAmountByValidatorDenom\x12L.osmosis.superfluid.EstimateSuperfluidDelegatedAmountByValidatorDenomRequest\x1aM.osmosis.superfluid.EstimateSuperfluidDelegatedAmountByValidatorDenomResponse"\\\x82\xd3\xe4\x93\x02V\x12T/osmosis/superfluid/v1beta1/estimate_superfluid_delegation_amount_by_validator_denomB7Z5github.com/osmosis-labs/osmosis/v7/x/superfluid/typesb\x06proto3')
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
_ASSETTYPEREQUEST = DESCRIPTOR.message_types_by_name['AssetTypeRequest']
_ASSETTYPERESPONSE = DESCRIPTOR.message_types_by_name['AssetTypeResponse']
_ALLASSETSREQUEST = DESCRIPTOR.message_types_by_name['AllAssetsRequest']
_ALLASSETSRESPONSE = DESCRIPTOR.message_types_by_name['AllAssetsResponse']
_ASSETMULTIPLIERREQUEST = DESCRIPTOR.message_types_by_name['AssetMultiplierRequest']
_ASSETMULTIPLIERRESPONSE = DESCRIPTOR.message_types_by_name['AssetMultiplierResponse']
_SUPERFLUIDINTERMEDIARYACCOUNTINFO = DESCRIPTOR.message_types_by_name['SuperfluidIntermediaryAccountInfo']
_ALLINTERMEDIARYACCOUNTSREQUEST = DESCRIPTOR.message_types_by_name['AllIntermediaryAccountsRequest']
_ALLINTERMEDIARYACCOUNTSRESPONSE = DESCRIPTOR.message_types_by_name['AllIntermediaryAccountsResponse']
_CONNECTEDINTERMEDIARYACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['ConnectedIntermediaryAccountRequest']
_CONNECTEDINTERMEDIARYACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['ConnectedIntermediaryAccountResponse']
_TOTALSUPERFLUIDDELEGATIONSREQUEST = DESCRIPTOR.message_types_by_name['TotalSuperfluidDelegationsRequest']
_TOTALSUPERFLUIDDELEGATIONSRESPONSE = DESCRIPTOR.message_types_by_name['TotalSuperfluidDelegationsResponse']
_SUPERFLUIDDELEGATIONAMOUNTREQUEST = DESCRIPTOR.message_types_by_name['SuperfluidDelegationAmountRequest']
_SUPERFLUIDDELEGATIONAMOUNTRESPONSE = DESCRIPTOR.message_types_by_name['SuperfluidDelegationAmountResponse']
_SUPERFLUIDDELEGATIONSBYDELEGATORREQUEST = DESCRIPTOR.message_types_by_name['SuperfluidDelegationsByDelegatorRequest']
_SUPERFLUIDDELEGATIONSBYDELEGATORRESPONSE = DESCRIPTOR.message_types_by_name['SuperfluidDelegationsByDelegatorResponse']
_SUPERFLUIDUNDELEGATIONSBYDELEGATORREQUEST = DESCRIPTOR.message_types_by_name['SuperfluidUndelegationsByDelegatorRequest']
_SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE = DESCRIPTOR.message_types_by_name['SuperfluidUndelegationsByDelegatorResponse']
_SUPERFLUIDDELEGATIONSBYVALIDATORDENOMREQUEST = DESCRIPTOR.message_types_by_name['SuperfluidDelegationsByValidatorDenomRequest']
_SUPERFLUIDDELEGATIONSBYVALIDATORDENOMRESPONSE = DESCRIPTOR.message_types_by_name['SuperfluidDelegationsByValidatorDenomResponse']
_ESTIMATESUPERFLUIDDELEGATEDAMOUNTBYVALIDATORDENOMREQUEST = DESCRIPTOR.message_types_by_name['EstimateSuperfluidDelegatedAmountByValidatorDenomRequest']
_ESTIMATESUPERFLUIDDELEGATEDAMOUNTBYVALIDATORDENOMRESPONSE = DESCRIPTOR.message_types_by_name['EstimateSuperfluidDelegatedAmountByValidatorDenomResponse']
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSREQUEST, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(QueryParamsRequest)
QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPARAMSRESPONSE, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(QueryParamsResponse)
AssetTypeRequest = _reflection.GeneratedProtocolMessageType('AssetTypeRequest', (_message.Message,), {'DESCRIPTOR': _ASSETTYPEREQUEST, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(AssetTypeRequest)
AssetTypeResponse = _reflection.GeneratedProtocolMessageType('AssetTypeResponse', (_message.Message,), {'DESCRIPTOR': _ASSETTYPERESPONSE, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(AssetTypeResponse)
AllAssetsRequest = _reflection.GeneratedProtocolMessageType('AllAssetsRequest', (_message.Message,), {'DESCRIPTOR': _ALLASSETSREQUEST, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(AllAssetsRequest)
AllAssetsResponse = _reflection.GeneratedProtocolMessageType('AllAssetsResponse', (_message.Message,), {'DESCRIPTOR': _ALLASSETSRESPONSE, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(AllAssetsResponse)
AssetMultiplierRequest = _reflection.GeneratedProtocolMessageType('AssetMultiplierRequest', (_message.Message,), {'DESCRIPTOR': _ASSETMULTIPLIERREQUEST, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(AssetMultiplierRequest)
AssetMultiplierResponse = _reflection.GeneratedProtocolMessageType('AssetMultiplierResponse', (_message.Message,), {'DESCRIPTOR': _ASSETMULTIPLIERRESPONSE, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(AssetMultiplierResponse)
SuperfluidIntermediaryAccountInfo = _reflection.GeneratedProtocolMessageType('SuperfluidIntermediaryAccountInfo', (_message.Message,), {'DESCRIPTOR': _SUPERFLUIDINTERMEDIARYACCOUNTINFO, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(SuperfluidIntermediaryAccountInfo)
AllIntermediaryAccountsRequest = _reflection.GeneratedProtocolMessageType('AllIntermediaryAccountsRequest', (_message.Message,), {'DESCRIPTOR': _ALLINTERMEDIARYACCOUNTSREQUEST, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(AllIntermediaryAccountsRequest)
AllIntermediaryAccountsResponse = _reflection.GeneratedProtocolMessageType('AllIntermediaryAccountsResponse', (_message.Message,), {'DESCRIPTOR': _ALLINTERMEDIARYACCOUNTSRESPONSE, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(AllIntermediaryAccountsResponse)
ConnectedIntermediaryAccountRequest = _reflection.GeneratedProtocolMessageType('ConnectedIntermediaryAccountRequest', (_message.Message,), {'DESCRIPTOR': _CONNECTEDINTERMEDIARYACCOUNTREQUEST, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(ConnectedIntermediaryAccountRequest)
ConnectedIntermediaryAccountResponse = _reflection.GeneratedProtocolMessageType('ConnectedIntermediaryAccountResponse', (_message.Message,), {'DESCRIPTOR': _CONNECTEDINTERMEDIARYACCOUNTRESPONSE, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(ConnectedIntermediaryAccountResponse)
TotalSuperfluidDelegationsRequest = _reflection.GeneratedProtocolMessageType('TotalSuperfluidDelegationsRequest', (_message.Message,), {'DESCRIPTOR': _TOTALSUPERFLUIDDELEGATIONSREQUEST, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(TotalSuperfluidDelegationsRequest)
TotalSuperfluidDelegationsResponse = _reflection.GeneratedProtocolMessageType('TotalSuperfluidDelegationsResponse', (_message.Message,), {'DESCRIPTOR': _TOTALSUPERFLUIDDELEGATIONSRESPONSE, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(TotalSuperfluidDelegationsResponse)
SuperfluidDelegationAmountRequest = _reflection.GeneratedProtocolMessageType('SuperfluidDelegationAmountRequest', (_message.Message,), {'DESCRIPTOR': _SUPERFLUIDDELEGATIONAMOUNTREQUEST, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(SuperfluidDelegationAmountRequest)
SuperfluidDelegationAmountResponse = _reflection.GeneratedProtocolMessageType('SuperfluidDelegationAmountResponse', (_message.Message,), {'DESCRIPTOR': _SUPERFLUIDDELEGATIONAMOUNTRESPONSE, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(SuperfluidDelegationAmountResponse)
SuperfluidDelegationsByDelegatorRequest = _reflection.GeneratedProtocolMessageType('SuperfluidDelegationsByDelegatorRequest', (_message.Message,), {'DESCRIPTOR': _SUPERFLUIDDELEGATIONSBYDELEGATORREQUEST, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(SuperfluidDelegationsByDelegatorRequest)
SuperfluidDelegationsByDelegatorResponse = _reflection.GeneratedProtocolMessageType('SuperfluidDelegationsByDelegatorResponse', (_message.Message,), {'DESCRIPTOR': _SUPERFLUIDDELEGATIONSBYDELEGATORRESPONSE, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(SuperfluidDelegationsByDelegatorResponse)
SuperfluidUndelegationsByDelegatorRequest = _reflection.GeneratedProtocolMessageType('SuperfluidUndelegationsByDelegatorRequest', (_message.Message,), {'DESCRIPTOR': _SUPERFLUIDUNDELEGATIONSBYDELEGATORREQUEST, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(SuperfluidUndelegationsByDelegatorRequest)
SuperfluidUndelegationsByDelegatorResponse = _reflection.GeneratedProtocolMessageType('SuperfluidUndelegationsByDelegatorResponse', (_message.Message,), {'DESCRIPTOR': _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(SuperfluidUndelegationsByDelegatorResponse)
SuperfluidDelegationsByValidatorDenomRequest = _reflection.GeneratedProtocolMessageType('SuperfluidDelegationsByValidatorDenomRequest', (_message.Message,), {'DESCRIPTOR': _SUPERFLUIDDELEGATIONSBYVALIDATORDENOMREQUEST, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(SuperfluidDelegationsByValidatorDenomRequest)
SuperfluidDelegationsByValidatorDenomResponse = _reflection.GeneratedProtocolMessageType('SuperfluidDelegationsByValidatorDenomResponse', (_message.Message,), {'DESCRIPTOR': _SUPERFLUIDDELEGATIONSBYVALIDATORDENOMRESPONSE, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(SuperfluidDelegationsByValidatorDenomResponse)
EstimateSuperfluidDelegatedAmountByValidatorDenomRequest = _reflection.GeneratedProtocolMessageType('EstimateSuperfluidDelegatedAmountByValidatorDenomRequest', (_message.Message,), {'DESCRIPTOR': _ESTIMATESUPERFLUIDDELEGATEDAMOUNTBYVALIDATORDENOMREQUEST, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(EstimateSuperfluidDelegatedAmountByValidatorDenomRequest)
EstimateSuperfluidDelegatedAmountByValidatorDenomResponse = _reflection.GeneratedProtocolMessageType('EstimateSuperfluidDelegatedAmountByValidatorDenomResponse', (_message.Message,), {'DESCRIPTOR': _ESTIMATESUPERFLUIDDELEGATEDAMOUNTBYVALIDATORDENOMRESPONSE, '__module__': 'osmosis.superfluid.query_pb2'})
_sym_db.RegisterMessage(EstimateSuperfluidDelegatedAmountByValidatorDenomResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/osmosis-labs/osmosis/v7/x/superfluid/types'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _ALLASSETSRESPONSE.fields_by_name['assets']._options = None
    _ALLASSETSRESPONSE.fields_by_name['assets']._serialized_options = b'\xc8\xde\x1f\x00'
    _ALLINTERMEDIARYACCOUNTSRESPONSE.fields_by_name['accounts']._options = None
    _ALLINTERMEDIARYACCOUNTSRESPONSE.fields_by_name['accounts']._serialized_options = b'\xc8\xde\x1f\x00'
    _TOTALSUPERFLUIDDELEGATIONSRESPONSE.fields_by_name['totalDelegations']._options = None
    _TOTALSUPERFLUIDDELEGATIONSRESPONSE.fields_by_name['totalDelegations']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f#yaml:"total_superfluid_delegations"\xc8\xde\x1f\x00'
    _SUPERFLUIDDELEGATIONAMOUNTRESPONSE.fields_by_name['amount']._options = None
    _SUPERFLUIDDELEGATIONAMOUNTRESPONSE.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _SUPERFLUIDDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['superfluid_delegation_records']._options = None
    _SUPERFLUIDDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['superfluid_delegation_records']._serialized_options = b'\xc8\xde\x1f\x00'
    _SUPERFLUIDDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['total_delegated_coins']._options = None
    _SUPERFLUIDDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['total_delegated_coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['superfluid_delegation_records']._options = None
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['superfluid_delegation_records']._serialized_options = b'\xc8\xde\x1f\x00'
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['total_undelegated_coins']._options = None
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['total_undelegated_coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['synthetic_locks']._options = None
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE.fields_by_name['synthetic_locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _SUPERFLUIDDELEGATIONSBYVALIDATORDENOMRESPONSE.fields_by_name['superfluid_delegation_records']._options = None
    _SUPERFLUIDDELEGATIONSBYVALIDATORDENOMRESPONSE.fields_by_name['superfluid_delegation_records']._serialized_options = b'\xc8\xde\x1f\x00'
    _ESTIMATESUPERFLUIDDELEGATEDAMOUNTBYVALIDATORDENOMRESPONSE.fields_by_name['total_delegated_coins']._options = None
    _ESTIMATESUPERFLUIDDELEGATEDAMOUNTBYVALIDATORDENOMRESPONSE.fields_by_name['total_delegated_coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/osmosis/superfluid/v1beta1/params'
    _QUERY.methods_by_name['AssetType']._options = None
    _QUERY.methods_by_name['AssetType']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/superfluid/v1beta1/asset_type'
    _QUERY.methods_by_name['AllAssets']._options = None
    _QUERY.methods_by_name['AllAssets']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/superfluid/v1beta1/all_assets'
    _QUERY.methods_by_name['AssetMultiplier']._options = None
    _QUERY.methods_by_name['AssetMultiplier']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/osmosis/superfluid/v1beta1/asset_multiplier'
    _QUERY.methods_by_name['AllIntermediaryAccounts']._options = None
    _QUERY.methods_by_name['AllIntermediaryAccounts']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/osmosis/superfluid/v1beta1/all_intermediary_accounts'
    _QUERY.methods_by_name['ConnectedIntermediaryAccount']._options = None
    _QUERY.methods_by_name['ConnectedIntermediaryAccount']._serialized_options = b'\x82\xd3\xe4\x93\x02F\x12D/osmosis/superfluid/v1beta1/connected_intermediary_account/{lock_id}'
    _QUERY.methods_by_name['TotalSuperfluidDelegations']._options = None
    _QUERY.methods_by_name['TotalSuperfluidDelegations']._serialized_options = b'\x82\xd3\xe4\x93\x028\x126/osmosis/superfluid/v1beta1/all_superfluid_delegations'
    _QUERY.methods_by_name['SuperfluidDelegationAmount']._options = None
    _QUERY.methods_by_name['SuperfluidDelegationAmount']._serialized_options = b'\x82\xd3\xe4\x93\x02:\x128/osmosis/superfluid/v1beta1/superfluid_delegation_amount'
    _QUERY.methods_by_name['SuperfluidDelegationsByDelegator']._options = None
    _QUERY.methods_by_name['SuperfluidDelegationsByDelegator']._serialized_options = b'\x82\xd3\xe4\x93\x02H\x12F/osmosis/superfluid/v1beta1/superfluid_delegations/{delegator_address}'
    _QUERY.methods_by_name['SuperfluidUndelegationsByDelegator']._options = None
    _QUERY.methods_by_name['SuperfluidUndelegationsByDelegator']._serialized_options = b'\x82\xd3\xe4\x93\x02W\x12U/osmosis/superfluid/v1beta1/superfluid_undelegations_by_delegator/{delegator_address}'
    _QUERY.methods_by_name['SuperfluidDelegationsByValidatorDenom']._options = None
    _QUERY.methods_by_name['SuperfluidDelegationsByValidatorDenom']._serialized_options = b'\x82\xd3\xe4\x93\x02G\x12E/osmosis/superfluid/v1beta1/superfluid_delegations_by_validator_denom'
    _QUERY.methods_by_name['EstimateSuperfluidDelegatedAmountByValidatorDenom']._options = None
    _QUERY.methods_by_name['EstimateSuperfluidDelegatedAmountByValidatorDenom']._serialized_options = b'\x82\xd3\xe4\x93\x02V\x12T/osmosis/superfluid/v1beta1/estimate_superfluid_delegation_amount_by_validator_denom'
    _QUERYPARAMSREQUEST._serialized_start = 344
    _QUERYPARAMSREQUEST._serialized_end = 364
    _QUERYPARAMSRESPONSE._serialized_start = 366
    _QUERYPARAMSRESPONSE._serialized_end = 437
    _ASSETTYPEREQUEST._serialized_start = 439
    _ASSETTYPEREQUEST._serialized_end = 472
    _ASSETTYPERESPONSE._serialized_start = 474
    _ASSETTYPERESPONSE._serialized_end = 554
    _ALLASSETSREQUEST._serialized_start = 556
    _ALLASSETSREQUEST._serialized_end = 574
    _ALLASSETSRESPONSE._serialized_start = 576
    _ALLASSETSRESPONSE._serialized_end = 654
    _ASSETMULTIPLIERREQUEST._serialized_start = 656
    _ASSETMULTIPLIERREQUEST._serialized_end = 695
    _ASSETMULTIPLIERRESPONSE._serialized_start = 697
    _ASSETMULTIPLIERRESPONSE._serialized_end = 810
    _SUPERFLUIDINTERMEDIARYACCOUNTINFO._serialized_start = 812
    _SUPERFLUIDINTERMEDIARYACCOUNTINFO._serialized_end = 915
    _ALLINTERMEDIARYACCOUNTSREQUEST._serialized_start = 917
    _ALLINTERMEDIARYACCOUNTSREQUEST._serialized_end = 1009
    _ALLINTERMEDIARYACCOUNTSRESPONSE._serialized_start = 1012
    _ALLINTERMEDIARYACCOUNTSRESPONSE._serialized_end = 1185
    _CONNECTEDINTERMEDIARYACCOUNTREQUEST._serialized_start = 1187
    _CONNECTEDINTERMEDIARYACCOUNTREQUEST._serialized_end = 1241
    _CONNECTEDINTERMEDIARYACCOUNTRESPONSE._serialized_start = 1243
    _CONNECTEDINTERMEDIARYACCOUNTRESPONSE._serialized_end = 1353
    _TOTALSUPERFLUIDDELEGATIONSREQUEST._serialized_start = 1355
    _TOTALSUPERFLUIDDELEGATIONSREQUEST._serialized_end = 1390
    _TOTALSUPERFLUIDDELEGATIONSRESPONSE._serialized_start = 1393
    _TOTALSUPERFLUIDDELEGATIONSRESPONSE._serialized_end = 1542
    _SUPERFLUIDDELEGATIONAMOUNTREQUEST._serialized_start = 1544
    _SUPERFLUIDDELEGATIONAMOUNTREQUEST._serialized_end = 1648
    _SUPERFLUIDDELEGATIONAMOUNTRESPONSE._serialized_start = 1651
    _SUPERFLUIDDELEGATIONAMOUNTRESPONSE._serialized_end = 1780
    _SUPERFLUIDDELEGATIONSBYDELEGATORREQUEST._serialized_start = 1782
    _SUPERFLUIDDELEGATIONSBYDELEGATORREQUEST._serialized_end = 1850
    _SUPERFLUIDDELEGATIONSBYDELEGATORRESPONSE._serialized_start = 1853
    _SUPERFLUIDDELEGATIONSBYDELEGATORRESPONSE._serialized_end = 2096
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORREQUEST._serialized_start = 2098
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORREQUEST._serialized_end = 2183
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE._serialized_start = 2186
    _SUPERFLUIDUNDELEGATIONSBYDELEGATORRESPONSE._serialized_end = 2495
    _SUPERFLUIDDELEGATIONSBYVALIDATORDENOMREQUEST._serialized_start = 2497
    _SUPERFLUIDDELEGATIONSBYVALIDATORDENOMREQUEST._serialized_end = 2585
    _SUPERFLUIDDELEGATIONSBYVALIDATORDENOMRESPONSE._serialized_start = 2588
    _SUPERFLUIDDELEGATIONSBYVALIDATORDENOMRESPONSE._serialized_end = 2728
    _ESTIMATESUPERFLUIDDELEGATEDAMOUNTBYVALIDATORDENOMREQUEST._serialized_start = 2730
    _ESTIMATESUPERFLUIDDELEGATEDAMOUNTBYVALIDATORDENOMREQUEST._serialized_end = 2830
    _ESTIMATESUPERFLUIDDELEGATEDAMOUNTBYVALIDATORDENOMRESPONSE._serialized_start = 2833
    _ESTIMATESUPERFLUIDDELEGATEDAMOUNTBYVALIDATORDENOMRESPONSE._serialized_end = 3000
    _QUERY._serialized_start = 3003
    _QUERY._serialized_end = 5483

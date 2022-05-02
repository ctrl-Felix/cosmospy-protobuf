
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.distribution.v1beta1 import distribution_pb2 as cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)cosmos/distribution/v1beta1/genesis.proto\x12\x1bcosmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a.cosmos/distribution/v1beta1/distribution.proto\x1a\x19cosmos_proto/cosmos.proto"\x8a\x01\n\x15DelegatorWithdrawInfo\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x122\n\x10withdraw_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\xd2\x01\n!ValidatorOutstandingRewardsRecord\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12n\n\x13outstanding_rewards\x18\x02 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\xbd\x01\n$ValidatorAccumulatedCommissionRecord\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12V\n\x0baccumulated\x18\x02 \x01(\x0b2;.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\xc1\x01\n ValidatorHistoricalRewardsRecord\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x0e\n\x06period\x18\x02 \x01(\x04\x12N\n\x07rewards\x18\x03 \x01(\x0b27.cosmos.distribution.v1beta1.ValidatorHistoricalRewardsB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\xab\x01\n\x1dValidatorCurrentRewardsRecord\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12K\n\x07rewards\x18\x02 \x01(\x0b24.cosmos.distribution.v1beta1.ValidatorCurrentRewardsB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\xe2\x01\n\x1bDelegatorStartingInfoRecord\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x123\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12O\n\rstarting_info\x18\x03 \x01(\x0b22.cosmos.distribution.v1beta1.DelegatorStartingInfoB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\xd1\x01\n\x19ValidatorSlashEventRecord\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x0e\n\x06height\x18\x02 \x01(\x04\x12\x0e\n\x06period\x18\x03 \x01(\x04\x12U\n\x15validator_slash_event\x18\x04 \x01(\x0b20.cosmos.distribution.v1beta1.ValidatorSlashEventB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x89\x07\n\x0cGenesisState\x129\n\x06params\x18\x01 \x01(\x0b2#.cosmos.distribution.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12<\n\x08fee_pool\x18\x02 \x01(\x0b2$.cosmos.distribution.v1beta1.FeePoolB\x04\xc8\xde\x1f\x00\x12Z\n\x18delegator_withdraw_infos\x18\x03 \x03(\x0b22.cosmos.distribution.v1beta1.DelegatorWithdrawInfoB\x04\xc8\xde\x1f\x00\x123\n\x11previous_proposer\x18\x04 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12a\n\x13outstanding_rewards\x18\x05 \x03(\x0b2>.cosmos.distribution.v1beta1.ValidatorOutstandingRewardsRecordB\x04\xc8\xde\x1f\x00\x12r\n!validator_accumulated_commissions\x18\x06 \x03(\x0b2A.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionRecordB\x04\xc8\xde\x1f\x00\x12i\n\x1cvalidator_historical_rewards\x18\x07 \x03(\x0b2=.cosmos.distribution.v1beta1.ValidatorHistoricalRewardsRecordB\x04\xc8\xde\x1f\x00\x12c\n\x19validator_current_rewards\x18\x08 \x03(\x0b2:.cosmos.distribution.v1beta1.ValidatorCurrentRewardsRecordB\x04\xc8\xde\x1f\x00\x12`\n\x18delegator_starting_infos\x18\t \x03(\x0b28.cosmos.distribution.v1beta1.DelegatorStartingInfoRecordB\x04\xc8\xde\x1f\x00\x12\\\n\x16validator_slash_events\x18\n \x03(\x0b26.cosmos.distribution.v1beta1.ValidatorSlashEventRecordB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00B7Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01b\x06proto3')
_DELEGATORWITHDRAWINFO = DESCRIPTOR.message_types_by_name['DelegatorWithdrawInfo']
_VALIDATOROUTSTANDINGREWARDSRECORD = DESCRIPTOR.message_types_by_name['ValidatorOutstandingRewardsRecord']
_VALIDATORACCUMULATEDCOMMISSIONRECORD = DESCRIPTOR.message_types_by_name['ValidatorAccumulatedCommissionRecord']
_VALIDATORHISTORICALREWARDSRECORD = DESCRIPTOR.message_types_by_name['ValidatorHistoricalRewardsRecord']
_VALIDATORCURRENTREWARDSRECORD = DESCRIPTOR.message_types_by_name['ValidatorCurrentRewardsRecord']
_DELEGATORSTARTINGINFORECORD = DESCRIPTOR.message_types_by_name['DelegatorStartingInfoRecord']
_VALIDATORSLASHEVENTRECORD = DESCRIPTOR.message_types_by_name['ValidatorSlashEventRecord']
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
DelegatorWithdrawInfo = _reflection.GeneratedProtocolMessageType('DelegatorWithdrawInfo', (_message.Message,), {'DESCRIPTOR': _DELEGATORWITHDRAWINFO, '__module__': 'cosmos.distribution.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(DelegatorWithdrawInfo)
ValidatorOutstandingRewardsRecord = _reflection.GeneratedProtocolMessageType('ValidatorOutstandingRewardsRecord', (_message.Message,), {'DESCRIPTOR': _VALIDATOROUTSTANDINGREWARDSRECORD, '__module__': 'cosmos.distribution.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(ValidatorOutstandingRewardsRecord)
ValidatorAccumulatedCommissionRecord = _reflection.GeneratedProtocolMessageType('ValidatorAccumulatedCommissionRecord', (_message.Message,), {'DESCRIPTOR': _VALIDATORACCUMULATEDCOMMISSIONRECORD, '__module__': 'cosmos.distribution.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(ValidatorAccumulatedCommissionRecord)
ValidatorHistoricalRewardsRecord = _reflection.GeneratedProtocolMessageType('ValidatorHistoricalRewardsRecord', (_message.Message,), {'DESCRIPTOR': _VALIDATORHISTORICALREWARDSRECORD, '__module__': 'cosmos.distribution.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(ValidatorHistoricalRewardsRecord)
ValidatorCurrentRewardsRecord = _reflection.GeneratedProtocolMessageType('ValidatorCurrentRewardsRecord', (_message.Message,), {'DESCRIPTOR': _VALIDATORCURRENTREWARDSRECORD, '__module__': 'cosmos.distribution.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(ValidatorCurrentRewardsRecord)
DelegatorStartingInfoRecord = _reflection.GeneratedProtocolMessageType('DelegatorStartingInfoRecord', (_message.Message,), {'DESCRIPTOR': _DELEGATORSTARTINGINFORECORD, '__module__': 'cosmos.distribution.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(DelegatorStartingInfoRecord)
ValidatorSlashEventRecord = _reflection.GeneratedProtocolMessageType('ValidatorSlashEventRecord', (_message.Message,), {'DESCRIPTOR': _VALIDATORSLASHEVENTRECORD, '__module__': 'cosmos.distribution.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(ValidatorSlashEventRecord)
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'cosmos.distribution.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01'
    _DELEGATORWITHDRAWINFO.fields_by_name['delegator_address']._options = None
    _DELEGATORWITHDRAWINFO.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _DELEGATORWITHDRAWINFO.fields_by_name['withdraw_address']._options = None
    _DELEGATORWITHDRAWINFO.fields_by_name['withdraw_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _DELEGATORWITHDRAWINFO._options = None
    _DELEGATORWITHDRAWINFO._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['validator_address']._options = None
    _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['outstanding_rewards']._options = None
    _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['outstanding_rewards']._serialized_options = b'\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _VALIDATOROUTSTANDINGREWARDSRECORD._options = None
    _VALIDATOROUTSTANDINGREWARDSRECORD._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['validator_address']._options = None
    _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['accumulated']._options = None
    _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['accumulated']._serialized_options = b'\xc8\xde\x1f\x00'
    _VALIDATORACCUMULATEDCOMMISSIONRECORD._options = None
    _VALIDATORACCUMULATEDCOMMISSIONRECORD._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['validator_address']._options = None
    _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['rewards']._options = None
    _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00'
    _VALIDATORHISTORICALREWARDSRECORD._options = None
    _VALIDATORHISTORICALREWARDSRECORD._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _VALIDATORCURRENTREWARDSRECORD.fields_by_name['validator_address']._options = None
    _VALIDATORCURRENTREWARDSRECORD.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _VALIDATORCURRENTREWARDSRECORD.fields_by_name['rewards']._options = None
    _VALIDATORCURRENTREWARDSRECORD.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00'
    _VALIDATORCURRENTREWARDSRECORD._options = None
    _VALIDATORCURRENTREWARDSRECORD._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _DELEGATORSTARTINGINFORECORD.fields_by_name['delegator_address']._options = None
    _DELEGATORSTARTINGINFORECORD.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _DELEGATORSTARTINGINFORECORD.fields_by_name['validator_address']._options = None
    _DELEGATORSTARTINGINFORECORD.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _DELEGATORSTARTINGINFORECORD.fields_by_name['starting_info']._options = None
    _DELEGATORSTARTINGINFORECORD.fields_by_name['starting_info']._serialized_options = b'\xc8\xde\x1f\x00'
    _DELEGATORSTARTINGINFORECORD._options = None
    _DELEGATORSTARTINGINFORECORD._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_address']._options = None
    _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_slash_event']._options = None
    _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_slash_event']._serialized_options = b'\xc8\xde\x1f\x00'
    _VALIDATORSLASHEVENTRECORD._options = None
    _VALIDATORSLASHEVENTRECORD._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['fee_pool']._options = None
    _GENESISSTATE.fields_by_name['fee_pool']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['delegator_withdraw_infos']._options = None
    _GENESISSTATE.fields_by_name['delegator_withdraw_infos']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['previous_proposer']._options = None
    _GENESISSTATE.fields_by_name['previous_proposer']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _GENESISSTATE.fields_by_name['outstanding_rewards']._options = None
    _GENESISSTATE.fields_by_name['outstanding_rewards']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['validator_accumulated_commissions']._options = None
    _GENESISSTATE.fields_by_name['validator_accumulated_commissions']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['validator_historical_rewards']._options = None
    _GENESISSTATE.fields_by_name['validator_historical_rewards']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['validator_current_rewards']._options = None
    _GENESISSTATE.fields_by_name['validator_current_rewards']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['delegator_starting_infos']._options = None
    _GENESISSTATE.fields_by_name['delegator_starting_infos']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['validator_slash_events']._options = None
    _GENESISSTATE.fields_by_name['validator_slash_events']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE._options = None
    _GENESISSTATE._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _DELEGATORWITHDRAWINFO._serialized_start = 204
    _DELEGATORWITHDRAWINFO._serialized_end = 342
    _VALIDATOROUTSTANDINGREWARDSRECORD._serialized_start = 345
    _VALIDATOROUTSTANDINGREWARDSRECORD._serialized_end = 555
    _VALIDATORACCUMULATEDCOMMISSIONRECORD._serialized_start = 558
    _VALIDATORACCUMULATEDCOMMISSIONRECORD._serialized_end = 747
    _VALIDATORHISTORICALREWARDSRECORD._serialized_start = 750
    _VALIDATORHISTORICALREWARDSRECORD._serialized_end = 943
    _VALIDATORCURRENTREWARDSRECORD._serialized_start = 946
    _VALIDATORCURRENTREWARDSRECORD._serialized_end = 1117
    _DELEGATORSTARTINGINFORECORD._serialized_start = 1120
    _DELEGATORSTARTINGINFORECORD._serialized_end = 1346
    _VALIDATORSLASHEVENTRECORD._serialized_start = 1349
    _VALIDATORSLASHEVENTRECORD._serialized_end = 1558
    _GENESISSTATE._serialized_start = 1561
    _GENESISSTATE._serialized_end = 2466

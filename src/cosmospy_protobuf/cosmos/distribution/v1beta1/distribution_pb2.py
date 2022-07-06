
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.cosmos/distribution/v1beta1/distribution.proto\x12\x1bcosmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x19cosmos_proto/cosmos.proto"\xbb\x02\n\x06Params\x12S\n\rcommunity_tax\x18\x01 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12Z\n\x14base_proposer_reward\x18\x02 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12[\n\x15bonus_proposer_reward\x18\x03 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x1d\n\x15withdraw_addr_enabled\x18\x04 \x01(\x08:\x04\x98\xa0\x1f\x00"\xa9\x01\n\x1aValidatorHistoricalRewards\x12r\n\x17cumulative_reward_ratio\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\x12\x17\n\x0freference_count\x18\x02 \x01(\r"\x8d\x01\n\x17ValidatorCurrentRewards\x12b\n\x07rewards\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\x12\x0e\n\x06period\x18\x02 \x01(\x04"\x87\x01\n\x1eValidatorAccumulatedCommission\x12e\n\ncommission\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00"\x81\x01\n\x1bValidatorOutstandingRewards\x12b\n\x07rewards\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00"\x7f\n\x13ValidatorSlashEvent\x12\x18\n\x10validator_period\x18\x01 \x01(\x04\x12N\n\x08fraction\x18\x02 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"t\n\x14ValidatorSlashEvents\x12V\n\x16validator_slash_events\x18\x01 \x03(\x0b20.cosmos.distribution.v1beta1.ValidatorSlashEventB\x04\xc8\xde\x1f\x00:\x04\x98\xa0\x1f\x00"t\n\x07FeePool\x12i\n\x0ecommunity_pool\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins"\xbe\x01\n\x1aCommunityPoolSpendProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x11\n\trecipient\x18\x03 \x01(\t\x12[\n\x06amount\x18\x04 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00"\xa2\x01\n\x15DelegatorStartingInfo\x12\x17\n\x0fprevious_period\x18\x01 \x01(\x04\x12K\n\x05stake\x18\x02 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12#\n\x06height\x18\x03 \x01(\x04B\x13\xea\xde\x1f\x0fcreation_height"\xbd\x01\n\x19DelegationDelegatorReward\x123\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12a\n\x06reward\x18\x02 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x01"\x89\x01\n%CommunityPoolSpendProposalWithDeposit\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x11\n\trecipient\x18\x03 \x01(\t\x12\x0e\n\x06amount\x18\x04 \x01(\t\x12\x0f\n\x07deposit\x18\x05 \x01(\t:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x01B7Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01b\x06proto3')
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
_VALIDATORHISTORICALREWARDS = DESCRIPTOR.message_types_by_name['ValidatorHistoricalRewards']
_VALIDATORCURRENTREWARDS = DESCRIPTOR.message_types_by_name['ValidatorCurrentRewards']
_VALIDATORACCUMULATEDCOMMISSION = DESCRIPTOR.message_types_by_name['ValidatorAccumulatedCommission']
_VALIDATOROUTSTANDINGREWARDS = DESCRIPTOR.message_types_by_name['ValidatorOutstandingRewards']
_VALIDATORSLASHEVENT = DESCRIPTOR.message_types_by_name['ValidatorSlashEvent']
_VALIDATORSLASHEVENTS = DESCRIPTOR.message_types_by_name['ValidatorSlashEvents']
_FEEPOOL = DESCRIPTOR.message_types_by_name['FeePool']
_COMMUNITYPOOLSPENDPROPOSAL = DESCRIPTOR.message_types_by_name['CommunityPoolSpendProposal']
_DELEGATORSTARTINGINFO = DESCRIPTOR.message_types_by_name['DelegatorStartingInfo']
_DELEGATIONDELEGATORREWARD = DESCRIPTOR.message_types_by_name['DelegationDelegatorReward']
_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT = DESCRIPTOR.message_types_by_name['CommunityPoolSpendProposalWithDeposit']
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {'DESCRIPTOR': _PARAMS, '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'})
_sym_db.RegisterMessage(Params)
ValidatorHistoricalRewards = _reflection.GeneratedProtocolMessageType('ValidatorHistoricalRewards', (_message.Message,), {'DESCRIPTOR': _VALIDATORHISTORICALREWARDS, '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'})
_sym_db.RegisterMessage(ValidatorHistoricalRewards)
ValidatorCurrentRewards = _reflection.GeneratedProtocolMessageType('ValidatorCurrentRewards', (_message.Message,), {'DESCRIPTOR': _VALIDATORCURRENTREWARDS, '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'})
_sym_db.RegisterMessage(ValidatorCurrentRewards)
ValidatorAccumulatedCommission = _reflection.GeneratedProtocolMessageType('ValidatorAccumulatedCommission', (_message.Message,), {'DESCRIPTOR': _VALIDATORACCUMULATEDCOMMISSION, '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'})
_sym_db.RegisterMessage(ValidatorAccumulatedCommission)
ValidatorOutstandingRewards = _reflection.GeneratedProtocolMessageType('ValidatorOutstandingRewards', (_message.Message,), {'DESCRIPTOR': _VALIDATOROUTSTANDINGREWARDS, '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'})
_sym_db.RegisterMessage(ValidatorOutstandingRewards)
ValidatorSlashEvent = _reflection.GeneratedProtocolMessageType('ValidatorSlashEvent', (_message.Message,), {'DESCRIPTOR': _VALIDATORSLASHEVENT, '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'})
_sym_db.RegisterMessage(ValidatorSlashEvent)
ValidatorSlashEvents = _reflection.GeneratedProtocolMessageType('ValidatorSlashEvents', (_message.Message,), {'DESCRIPTOR': _VALIDATORSLASHEVENTS, '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'})
_sym_db.RegisterMessage(ValidatorSlashEvents)
FeePool = _reflection.GeneratedProtocolMessageType('FeePool', (_message.Message,), {'DESCRIPTOR': _FEEPOOL, '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'})
_sym_db.RegisterMessage(FeePool)
CommunityPoolSpendProposal = _reflection.GeneratedProtocolMessageType('CommunityPoolSpendProposal', (_message.Message,), {'DESCRIPTOR': _COMMUNITYPOOLSPENDPROPOSAL, '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'})
_sym_db.RegisterMessage(CommunityPoolSpendProposal)
DelegatorStartingInfo = _reflection.GeneratedProtocolMessageType('DelegatorStartingInfo', (_message.Message,), {'DESCRIPTOR': _DELEGATORSTARTINGINFO, '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'})
_sym_db.RegisterMessage(DelegatorStartingInfo)
DelegationDelegatorReward = _reflection.GeneratedProtocolMessageType('DelegationDelegatorReward', (_message.Message,), {'DESCRIPTOR': _DELEGATIONDELEGATORREWARD, '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'})
_sym_db.RegisterMessage(DelegationDelegatorReward)
CommunityPoolSpendProposalWithDeposit = _reflection.GeneratedProtocolMessageType('CommunityPoolSpendProposalWithDeposit', (_message.Message,), {'DESCRIPTOR': _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT, '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'})
_sym_db.RegisterMessage(CommunityPoolSpendProposalWithDeposit)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01'
    _PARAMS.fields_by_name['community_tax']._options = None
    _PARAMS.fields_by_name['community_tax']._serialized_options = b'\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['base_proposer_reward']._options = None
    _PARAMS.fields_by_name['base_proposer_reward']._serialized_options = b'\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['bonus_proposer_reward']._options = None
    _PARAMS.fields_by_name['bonus_proposer_reward']._serialized_options = b'\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS._options = None
    _PARAMS._serialized_options = b'\x98\xa0\x1f\x00'
    _VALIDATORHISTORICALREWARDS.fields_by_name['cumulative_reward_ratio']._options = None
    _VALIDATORHISTORICALREWARDS.fields_by_name['cumulative_reward_ratio']._serialized_options = b'\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _VALIDATORCURRENTREWARDS.fields_by_name['rewards']._options = None
    _VALIDATORCURRENTREWARDS.fields_by_name['rewards']._serialized_options = b'\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _VALIDATORACCUMULATEDCOMMISSION.fields_by_name['commission']._options = None
    _VALIDATORACCUMULATEDCOMMISSION.fields_by_name['commission']._serialized_options = b'\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _VALIDATOROUTSTANDINGREWARDS.fields_by_name['rewards']._options = None
    _VALIDATOROUTSTANDINGREWARDS.fields_by_name['rewards']._serialized_options = b'\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _VALIDATORSLASHEVENT.fields_by_name['fraction']._options = None
    _VALIDATORSLASHEVENT.fields_by_name['fraction']._serialized_options = b'\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _VALIDATORSLASHEVENTS.fields_by_name['validator_slash_events']._options = None
    _VALIDATORSLASHEVENTS.fields_by_name['validator_slash_events']._serialized_options = b'\xc8\xde\x1f\x00'
    _VALIDATORSLASHEVENTS._options = None
    _VALIDATORSLASHEVENTS._serialized_options = b'\x98\xa0\x1f\x00'
    _FEEPOOL.fields_by_name['community_pool']._options = None
    _FEEPOOL.fields_by_name['community_pool']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _COMMUNITYPOOLSPENDPROPOSAL.fields_by_name['amount']._options = None
    _COMMUNITYPOOLSPENDPROPOSAL.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _COMMUNITYPOOLSPENDPROPOSAL._options = None
    _COMMUNITYPOOLSPENDPROPOSAL._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _DELEGATORSTARTINGINFO.fields_by_name['stake']._options = None
    _DELEGATORSTARTINGINFO.fields_by_name['stake']._serialized_options = b'\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _DELEGATORSTARTINGINFO.fields_by_name['height']._options = None
    _DELEGATORSTARTINGINFO.fields_by_name['height']._serialized_options = b'\xea\xde\x1f\x0fcreation_height'
    _DELEGATIONDELEGATORREWARD.fields_by_name['validator_address']._options = None
    _DELEGATIONDELEGATORREWARD.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _DELEGATIONDELEGATORREWARD.fields_by_name['reward']._options = None
    _DELEGATIONDELEGATORREWARD.fields_by_name['reward']._serialized_options = b'\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00'
    _DELEGATIONDELEGATORREWARD._options = None
    _DELEGATIONDELEGATORREWARD._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x01'
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT._options = None
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x01'
    _PARAMS._serialized_start = 161
    _PARAMS._serialized_end = 476
    _VALIDATORHISTORICALREWARDS._serialized_start = 479
    _VALIDATORHISTORICALREWARDS._serialized_end = 648
    _VALIDATORCURRENTREWARDS._serialized_start = 651
    _VALIDATORCURRENTREWARDS._serialized_end = 792
    _VALIDATORACCUMULATEDCOMMISSION._serialized_start = 795
    _VALIDATORACCUMULATEDCOMMISSION._serialized_end = 930
    _VALIDATOROUTSTANDINGREWARDS._serialized_start = 933
    _VALIDATOROUTSTANDINGREWARDS._serialized_end = 1062
    _VALIDATORSLASHEVENT._serialized_start = 1064
    _VALIDATORSLASHEVENT._serialized_end = 1191
    _VALIDATORSLASHEVENTS._serialized_start = 1193
    _VALIDATORSLASHEVENTS._serialized_end = 1309
    _FEEPOOL._serialized_start = 1311
    _FEEPOOL._serialized_end = 1427
    _COMMUNITYPOOLSPENDPROPOSAL._serialized_start = 1430
    _COMMUNITYPOOLSPENDPROPOSAL._serialized_end = 1620
    _DELEGATORSTARTINGINFO._serialized_start = 1623
    _DELEGATORSTARTINGINFO._serialized_end = 1785
    _DELEGATIONDELEGATORREWARD._serialized_start = 1788
    _DELEGATIONDELEGATORREWARD._serialized_end = 1977
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT._serialized_start = 1980
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT._serialized_end = 2117

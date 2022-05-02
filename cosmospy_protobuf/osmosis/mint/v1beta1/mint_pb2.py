
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fosmosis/mint/v1beta1/mint.proto\x12\x14osmosis.mint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto"m\n\x06Minter\x12c\n\x10epoch_provisions\x18\x01 \x01(\tBI\xf2\xde\x1f\x17yaml:"epoch_provisions"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"\x87\x01\n\x0fWeightedAddress\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12O\n\x06weight\x18\x02 \x01(\tB?\xf2\xde\x1f\ryaml:"weight"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"\x97\x03\n\x17DistributionProportions\x12Q\n\x07staking\x18\x01 \x01(\tB@\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x0eyaml:"staking"\xc8\xde\x1f\x00\x12a\n\x0fpool_incentives\x18\x02 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x16yaml:"pool_incentives"\xc8\xde\x1f\x00\x12e\n\x11developer_rewards\x18\x03 \x01(\tBJ\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x18yaml:"developer_rewards"\xc8\xde\x1f\x00\x12_\n\x0ecommunity_pool\x18\x04 \x01(\tBG\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x15yaml:"community_pool"\xc8\xde\x1f\x00"\xbc\x05\n\x06Params\x12\x12\n\nmint_denom\x18\x01 \x01(\t\x12s\n\x18genesis_epoch_provisions\x18\x02 \x01(\tBQ\xf2\xde\x1f\x1fyaml:"genesis_epoch_provisions"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x125\n\x10epoch_identifier\x18\x03 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:"epoch_identifier"\x12I\n\x1areduction_period_in_epochs\x18\x04 \x01(\x03B%\xf2\xde\x1f!yaml:"reduction_period_in_epochs"\x12c\n\x10reduction_factor\x18\x05 \x01(\tBI\xf2\xde\x1f\x17yaml:"reduction_factor"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12U\n\x18distribution_proportions\x18\x06 \x01(\x0b2-.osmosis.mint.v1beta1.DistributionProportionsB\x04\xc8\xde\x1f\x00\x12~\n$weighted_developer_rewards_receivers\x18\x07 \x03(\x0b2%.osmosis.mint.v1beta1.WeightedAddressB)\xf2\xde\x1f!yaml:"developer_rewards_receiver"\xc8\xde\x1f\x00\x12e\n(minting_rewards_distribution_start_epoch\x18\x08 \x01(\x03B3\xf2\xde\x1f/yaml:"minting_rewards_distribution_start_epoch":\x04\x98\xa0\x1f\x00B1Z/github.com/osmosis-labs/osmosis/v7/x/mint/typesb\x06proto3')
_MINTER = DESCRIPTOR.message_types_by_name['Minter']
_WEIGHTEDADDRESS = DESCRIPTOR.message_types_by_name['WeightedAddress']
_DISTRIBUTIONPROPORTIONS = DESCRIPTOR.message_types_by_name['DistributionProportions']
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
Minter = _reflection.GeneratedProtocolMessageType('Minter', (_message.Message,), {'DESCRIPTOR': _MINTER, '__module__': 'osmosis.mint.v1beta1.mint_pb2'})
_sym_db.RegisterMessage(Minter)
WeightedAddress = _reflection.GeneratedProtocolMessageType('WeightedAddress', (_message.Message,), {'DESCRIPTOR': _WEIGHTEDADDRESS, '__module__': 'osmosis.mint.v1beta1.mint_pb2'})
_sym_db.RegisterMessage(WeightedAddress)
DistributionProportions = _reflection.GeneratedProtocolMessageType('DistributionProportions', (_message.Message,), {'DESCRIPTOR': _DISTRIBUTIONPROPORTIONS, '__module__': 'osmosis.mint.v1beta1.mint_pb2'})
_sym_db.RegisterMessage(DistributionProportions)
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {'DESCRIPTOR': _PARAMS, '__module__': 'osmosis.mint.v1beta1.mint_pb2'})
_sym_db.RegisterMessage(Params)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z/github.com/osmosis-labs/osmosis/v7/x/mint/types'
    _MINTER.fields_by_name['epoch_provisions']._options = None
    _MINTER.fields_by_name['epoch_provisions']._serialized_options = b'\xf2\xde\x1f\x17yaml:"epoch_provisions"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _WEIGHTEDADDRESS.fields_by_name['address']._options = None
    _WEIGHTEDADDRESS.fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _WEIGHTEDADDRESS.fields_by_name['weight']._options = None
    _WEIGHTEDADDRESS.fields_by_name['weight']._serialized_options = b'\xf2\xde\x1f\ryaml:"weight"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _DISTRIBUTIONPROPORTIONS.fields_by_name['staking']._options = None
    _DISTRIBUTIONPROPORTIONS.fields_by_name['staking']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x0eyaml:"staking"\xc8\xde\x1f\x00'
    _DISTRIBUTIONPROPORTIONS.fields_by_name['pool_incentives']._options = None
    _DISTRIBUTIONPROPORTIONS.fields_by_name['pool_incentives']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x16yaml:"pool_incentives"\xc8\xde\x1f\x00'
    _DISTRIBUTIONPROPORTIONS.fields_by_name['developer_rewards']._options = None
    _DISTRIBUTIONPROPORTIONS.fields_by_name['developer_rewards']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x18yaml:"developer_rewards"\xc8\xde\x1f\x00'
    _DISTRIBUTIONPROPORTIONS.fields_by_name['community_pool']._options = None
    _DISTRIBUTIONPROPORTIONS.fields_by_name['community_pool']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x15yaml:"community_pool"\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['genesis_epoch_provisions']._options = None
    _PARAMS.fields_by_name['genesis_epoch_provisions']._serialized_options = b'\xf2\xde\x1f\x1fyaml:"genesis_epoch_provisions"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['epoch_identifier']._options = None
    _PARAMS.fields_by_name['epoch_identifier']._serialized_options = b'\xf2\xde\x1f\x17yaml:"epoch_identifier"'
    _PARAMS.fields_by_name['reduction_period_in_epochs']._options = None
    _PARAMS.fields_by_name['reduction_period_in_epochs']._serialized_options = b'\xf2\xde\x1f!yaml:"reduction_period_in_epochs"'
    _PARAMS.fields_by_name['reduction_factor']._options = None
    _PARAMS.fields_by_name['reduction_factor']._serialized_options = b'\xf2\xde\x1f\x17yaml:"reduction_factor"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['distribution_proportions']._options = None
    _PARAMS.fields_by_name['distribution_proportions']._serialized_options = b'\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['weighted_developer_rewards_receivers']._options = None
    _PARAMS.fields_by_name['weighted_developer_rewards_receivers']._serialized_options = b'\xf2\xde\x1f!yaml:"developer_rewards_receiver"\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['minting_rewards_distribution_start_epoch']._options = None
    _PARAMS.fields_by_name['minting_rewards_distribution_start_epoch']._serialized_options = b'\xf2\xde\x1f/yaml:"minting_rewards_distribution_start_epoch"'
    _PARAMS._options = None
    _PARAMS._serialized_options = b'\x98\xa0\x1f\x00'
    _MINTER._serialized_start = 171
    _MINTER._serialized_end = 280
    _WEIGHTEDADDRESS._serialized_start = 283
    _WEIGHTEDADDRESS._serialized_end = 418
    _DISTRIBUTIONPROPORTIONS._serialized_start = 421
    _DISTRIBUTIONPROPORTIONS._serialized_end = 828
    _PARAMS._serialized_start = 831
    _PARAMS._serialized_end = 1531

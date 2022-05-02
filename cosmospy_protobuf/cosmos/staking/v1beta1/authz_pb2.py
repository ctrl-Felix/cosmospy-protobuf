
'Generated protocol buffer code.'
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"cosmos/staking/v1beta1/authz.proto\x12\x16cosmos.staking.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xaa\x03\n\x12StakeAuthorization\x12Z\n\nmax_tokens\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB+\xaa\xdf\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\x12K\n\nallow_list\x18\x02 \x01(\x0b25.cosmos.staking.v1beta1.StakeAuthorization.ValidatorsH\x00\x12J\n\tdeny_list\x18\x03 \x01(\x0b25.cosmos.staking.v1beta1.StakeAuthorization.ValidatorsH\x00\x12E\n\x12authorization_type\x18\x04 \x01(\x0e2).cosmos.staking.v1beta1.AuthorizationType\x1a7\n\nValidators\x12)\n\x07address\x18\x01 \x03(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x11\xca\xb4-\rAuthorizationB\x0c\n\nvalidators*\x9e\x01\n\x11AuthorizationType\x12"\n\x1eAUTHORIZATION_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bAUTHORIZATION_TYPE_DELEGATE\x10\x01\x12!\n\x1dAUTHORIZATION_TYPE_UNDELEGATE\x10\x02\x12!\n\x1dAUTHORIZATION_TYPE_REDELEGATE\x10\x03B.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')
_AUTHORIZATIONTYPE = DESCRIPTOR.enum_types_by_name['AuthorizationType']
AuthorizationType = enum_type_wrapper.EnumTypeWrapper(_AUTHORIZATIONTYPE)
AUTHORIZATION_TYPE_UNSPECIFIED = 0
AUTHORIZATION_TYPE_DELEGATE = 1
AUTHORIZATION_TYPE_UNDELEGATE = 2
AUTHORIZATION_TYPE_REDELEGATE = 3
_STAKEAUTHORIZATION = DESCRIPTOR.message_types_by_name['StakeAuthorization']
_STAKEAUTHORIZATION_VALIDATORS = _STAKEAUTHORIZATION.nested_types_by_name['Validators']
StakeAuthorization = _reflection.GeneratedProtocolMessageType('StakeAuthorization', (_message.Message,), {'Validators': _reflection.GeneratedProtocolMessageType('Validators', (_message.Message,), {'DESCRIPTOR': _STAKEAUTHORIZATION_VALIDATORS, '__module__': 'cosmos.staking.v1beta1.authz_pb2'}), 'DESCRIPTOR': _STAKEAUTHORIZATION, '__module__': 'cosmos.staking.v1beta1.authz_pb2'})
_sym_db.RegisterMessage(StakeAuthorization)
_sym_db.RegisterMessage(StakeAuthorization.Validators)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
    _STAKEAUTHORIZATION_VALIDATORS.fields_by_name['address']._options = None
    _STAKEAUTHORIZATION_VALIDATORS.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _STAKEAUTHORIZATION.fields_by_name['max_tokens']._options = None
    _STAKEAUTHORIZATION.fields_by_name['max_tokens']._serialized_options = b"\xaa\xdf\x1f'github.com/cosmos/cosmos-sdk/types.Coin"
    _STAKEAUTHORIZATION._options = None
    _STAKEAUTHORIZATION._serialized_options = b'\xca\xb4-\rAuthorization'
    _AUTHORIZATIONTYPE._serialized_start = 573
    _AUTHORIZATIONTYPE._serialized_end = 731
    _STAKEAUTHORIZATION._serialized_start = 144
    _STAKEAUTHORIZATION._serialized_end = 570
    _STAKEAUTHORIZATION_VALIDATORS._serialized_start = 482
    _STAKEAUTHORIZATION_VALIDATORS._serialized_end = 537

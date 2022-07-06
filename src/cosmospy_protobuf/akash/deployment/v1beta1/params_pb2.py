
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%akash/deployment/v1beta1/params.proto\x12\x18akash.deployment.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x9d\x01\n\x06Params\x12\x92\x01\n\x16deployment_min_deposit\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinBW\xe2\xde\x1f\x14DeploymentMinDeposit\xc8\xde\x1f\x00\xea\xde\x1f\x16deployment_min_deposit\xf2\xde\x1f\x1dyaml:"deployment_min_deposit"B4Z2github.com/ovrclk/akash/x/deployment/types/v1beta1b\x06proto3')
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {'DESCRIPTOR': _PARAMS, '__module__': 'akash.deployment.v1beta1.params_pb2'})
_sym_db.RegisterMessage(Params)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/ovrclk/akash/x/deployment/types/v1beta1'
    _PARAMS.fields_by_name['deployment_min_deposit']._options = None
    _PARAMS.fields_by_name['deployment_min_deposit']._serialized_options = b'\xe2\xde\x1f\x14DeploymentMinDeposit\xc8\xde\x1f\x00\xea\xde\x1f\x16deployment_min_deposit\xf2\xde\x1f\x1dyaml:"deployment_min_deposit"'
    _PARAMS._serialized_start = 122
    _PARAMS._serialized_end = 279

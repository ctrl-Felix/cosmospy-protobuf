
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.deployment.v1beta1 import deployment_pb2 as akash_dot_deployment_dot_v1beta1_dot_deployment__pb2
from ....akash.deployment.v1beta1 import group_pb2 as akash_dot_deployment_dot_v1beta1_dot_group__pb2
from ....akash.deployment.v1beta1 import params_pb2 as akash_dot_deployment_dot_v1beta1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&akash/deployment/v1beta1/genesis.proto\x12\x18akash.deployment.v1beta1\x1a\x14gogoproto/gogo.proto\x1a)akash/deployment/v1beta1/deployment.proto\x1a$akash/deployment/v1beta1/group.proto\x1a%akash/deployment/v1beta1/params.proto"\xc8\x01\n\x11GenesisDeployment\x12a\n\ndeployment\x18\x01 \x01(\x0b2$.akash.deployment.v1beta1.DeploymentB\'\xc8\xde\x1f\x00\xea\xde\x1f\ndeployment\xf2\xde\x1f\x11yaml:"deployment"\x12P\n\x06groups\x18\x02 \x03(\x0b2\x1f.akash.deployment.v1beta1.GroupB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06groups\xf2\xde\x1f\ryaml:"groups""\xce\x01\n\x0cGenesisState\x12k\n\x0bdeployments\x18\x01 \x03(\x0b2+.akash.deployment.v1beta1.GenesisDeploymentB)\xc8\xde\x1f\x00\xea\xde\x1f\x0bdeployments\xf2\xde\x1f\x12yaml:"deployments"\x12Q\n\x06params\x18\x02 \x01(\x0b2 .akash.deployment.v1beta1.ParamsB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06params\xf2\xde\x1f\ryaml:"params"B4Z2github.com/ovrclk/akash/x/deployment/types/v1beta1b\x06proto3')
_GENESISDEPLOYMENT = DESCRIPTOR.message_types_by_name['GenesisDeployment']
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisDeployment = _reflection.GeneratedProtocolMessageType('GenesisDeployment', (_message.Message,), {'DESCRIPTOR': _GENESISDEPLOYMENT, '__module__': 'akash.deployment.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisDeployment)
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'akash.deployment.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/ovrclk/akash/x/deployment/types/v1beta1'
    _GENESISDEPLOYMENT.fields_by_name['deployment']._options = None
    _GENESISDEPLOYMENT.fields_by_name['deployment']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\ndeployment\xf2\xde\x1f\x11yaml:"deployment"'
    _GENESISDEPLOYMENT.fields_by_name['groups']._options = None
    _GENESISDEPLOYMENT.fields_by_name['groups']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06groups\xf2\xde\x1f\ryaml:"groups"'
    _GENESISSTATE.fields_by_name['deployments']._options = None
    _GENESISSTATE.fields_by_name['deployments']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x0bdeployments\xf2\xde\x1f\x12yaml:"deployments"'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06params\xf2\xde\x1f\ryaml:"params"'
    _GENESISDEPLOYMENT._serialized_start = 211
    _GENESISDEPLOYMENT._serialized_end = 411
    _GENESISSTATE._serialized_start = 414
    _GENESISSTATE._serialized_end = 620

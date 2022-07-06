
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....akash.deployment.v1beta1 import deployment_pb2 as akash_dot_deployment_dot_v1beta1_dot_deployment__pb2
from ....akash.deployment.v1beta1 import group_pb2 as akash_dot_deployment_dot_v1beta1_dot_group__pb2
from ....akash.escrow.v1beta1 import types_pb2 as akash_dot_escrow_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$akash/deployment/v1beta1/query.proto\x12\x18akash.deployment.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a)akash/deployment/v1beta1/deployment.proto\x1a$akash/deployment/v1beta1/group.proto\x1a akash/escrow/v1beta1/types.proto"\x99\x01\n\x17QueryDeploymentsRequest\x12B\n\x07filters\x18\x01 \x01(\x0b2+.akash.deployment.v1beta1.DeploymentFiltersB\x04\xc8\xde\x1f\x00\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xbc\x01\n\x18QueryDeploymentsResponse\x12c\n\x0bdeployments\x18\x01 \x03(\x0b21.akash.deployment.v1beta1.QueryDeploymentResponseB\x1b\xc8\xde\x1f\x00\xaa\xdf\x1f\x13DeploymentResponses\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"X\n\x16QueryDeploymentRequest\x12>\n\x02id\x18\x01 \x01(\x0b2&.akash.deployment.v1beta1.DeploymentIDB\n\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID"\x91\x02\n\x17QueryDeploymentResponse\x12a\n\ndeployment\x18\x01 \x01(\x0b2$.akash.deployment.v1beta1.DeploymentB\'\xc8\xde\x1f\x00\xea\xde\x1f\ndeployment\xf2\xde\x1f\x11yaml:"deployment"\x12P\n\x06groups\x18\x02 \x03(\x0b2\x1f.akash.deployment.v1beta1.GroupB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06groups\xf2\xde\x1f\ryaml:"groups"\x12;\n\x0eescrow_account\x18\x03 \x01(\x0b2\x1d.akash.escrow.v1beta1.AccountB\x04\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x00"N\n\x11QueryGroupRequest\x129\n\x02id\x18\x01 \x01(\x0b2!.akash.deployment.v1beta1.GroupIDB\n\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID"J\n\x12QueryGroupResponse\x124\n\x05group\x18\x01 \x01(\x0b2\x1f.akash.deployment.v1beta1.GroupB\x04\xc8\xde\x1f\x002\xee\x03\n\x05Query\x12\xa8\x01\n\x0bDeployments\x121.akash.deployment.v1beta1.QueryDeploymentsRequest\x1a2.akash.deployment.v1beta1.QueryDeploymentsResponse"2\x82\xd3\xe4\x93\x02,\x12*/akash/deployment/v1beta1/deployments/list\x12\xa5\x01\n\nDeployment\x120.akash.deployment.v1beta1.QueryDeploymentRequest\x1a1.akash.deployment.v1beta1.QueryDeploymentResponse"2\x82\xd3\xe4\x93\x02,\x12*/akash/deployment/v1beta1/deployments/info\x12\x91\x01\n\x05Group\x12+.akash.deployment.v1beta1.QueryGroupRequest\x1a,.akash.deployment.v1beta1.QueryGroupResponse"-\x82\xd3\xe4\x93\x02\'\x12%/akash/deployment/v1beta1/groups/infoB4Z2github.com/ovrclk/akash/x/deployment/types/v1beta1b\x06proto3')
_QUERYDEPLOYMENTSREQUEST = DESCRIPTOR.message_types_by_name['QueryDeploymentsRequest']
_QUERYDEPLOYMENTSRESPONSE = DESCRIPTOR.message_types_by_name['QueryDeploymentsResponse']
_QUERYDEPLOYMENTREQUEST = DESCRIPTOR.message_types_by_name['QueryDeploymentRequest']
_QUERYDEPLOYMENTRESPONSE = DESCRIPTOR.message_types_by_name['QueryDeploymentResponse']
_QUERYGROUPREQUEST = DESCRIPTOR.message_types_by_name['QueryGroupRequest']
_QUERYGROUPRESPONSE = DESCRIPTOR.message_types_by_name['QueryGroupResponse']
QueryDeploymentsRequest = _reflection.GeneratedProtocolMessageType('QueryDeploymentsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYDEPLOYMENTSREQUEST, '__module__': 'akash.deployment.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDeploymentsRequest)
QueryDeploymentsResponse = _reflection.GeneratedProtocolMessageType('QueryDeploymentsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYDEPLOYMENTSRESPONSE, '__module__': 'akash.deployment.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDeploymentsResponse)
QueryDeploymentRequest = _reflection.GeneratedProtocolMessageType('QueryDeploymentRequest', (_message.Message,), {'DESCRIPTOR': _QUERYDEPLOYMENTREQUEST, '__module__': 'akash.deployment.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDeploymentRequest)
QueryDeploymentResponse = _reflection.GeneratedProtocolMessageType('QueryDeploymentResponse', (_message.Message,), {'DESCRIPTOR': _QUERYDEPLOYMENTRESPONSE, '__module__': 'akash.deployment.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryDeploymentResponse)
QueryGroupRequest = _reflection.GeneratedProtocolMessageType('QueryGroupRequest', (_message.Message,), {'DESCRIPTOR': _QUERYGROUPREQUEST, '__module__': 'akash.deployment.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryGroupRequest)
QueryGroupResponse = _reflection.GeneratedProtocolMessageType('QueryGroupResponse', (_message.Message,), {'DESCRIPTOR': _QUERYGROUPRESPONSE, '__module__': 'akash.deployment.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryGroupResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/ovrclk/akash/x/deployment/types/v1beta1'
    _QUERYDEPLOYMENTSREQUEST.fields_by_name['filters']._options = None
    _QUERYDEPLOYMENTSREQUEST.fields_by_name['filters']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYDEPLOYMENTSRESPONSE.fields_by_name['deployments']._options = None
    _QUERYDEPLOYMENTSRESPONSE.fields_by_name['deployments']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\x13DeploymentResponses'
    _QUERYDEPLOYMENTREQUEST.fields_by_name['id']._options = None
    _QUERYDEPLOYMENTREQUEST.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID'
    _QUERYDEPLOYMENTRESPONSE.fields_by_name['deployment']._options = None
    _QUERYDEPLOYMENTRESPONSE.fields_by_name['deployment']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\ndeployment\xf2\xde\x1f\x11yaml:"deployment"'
    _QUERYDEPLOYMENTRESPONSE.fields_by_name['groups']._options = None
    _QUERYDEPLOYMENTRESPONSE.fields_by_name['groups']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06groups\xf2\xde\x1f\ryaml:"groups"'
    _QUERYDEPLOYMENTRESPONSE.fields_by_name['escrow_account']._options = None
    _QUERYDEPLOYMENTRESPONSE.fields_by_name['escrow_account']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYDEPLOYMENTRESPONSE._options = None
    _QUERYDEPLOYMENTRESPONSE._serialized_options = b'\xe8\xa0\x1f\x00'
    _QUERYGROUPREQUEST.fields_by_name['id']._options = None
    _QUERYGROUPREQUEST.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID'
    _QUERYGROUPRESPONSE.fields_by_name['group']._options = None
    _QUERYGROUPRESPONSE.fields_by_name['group']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Deployments']._options = None
    _QUERY.methods_by_name['Deployments']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/akash/deployment/v1beta1/deployments/list'
    _QUERY.methods_by_name['Deployment']._options = None
    _QUERY.methods_by_name['Deployment']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/akash/deployment/v1beta1/deployments/info'
    _QUERY.methods_by_name['Group']._options = None
    _QUERY.methods_by_name['Group']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/akash/deployment/v1beta1/groups/info"
    _QUERYDEPLOYMENTSREQUEST._serialized_start = 278
    _QUERYDEPLOYMENTSREQUEST._serialized_end = 431
    _QUERYDEPLOYMENTSRESPONSE._serialized_start = 434
    _QUERYDEPLOYMENTSRESPONSE._serialized_end = 622
    _QUERYDEPLOYMENTREQUEST._serialized_start = 624
    _QUERYDEPLOYMENTREQUEST._serialized_end = 712
    _QUERYDEPLOYMENTRESPONSE._serialized_start = 715
    _QUERYDEPLOYMENTRESPONSE._serialized_end = 988
    _QUERYGROUPREQUEST._serialized_start = 990
    _QUERYGROUPREQUEST._serialized_end = 1068
    _QUERYGROUPRESPONSE._serialized_start = 1070
    _QUERYGROUPRESPONSE._serialized_end = 1144
    _QUERY._serialized_start = 1147
    _QUERY._serialized_end = 1641

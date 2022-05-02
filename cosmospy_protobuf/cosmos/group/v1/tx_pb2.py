
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
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos.group.v1 import types_pb2 as cosmos_dot_group_dot_v1_dot_types__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18cosmos/group/v1/tx.proto\x12\x0fcosmos.group.v1\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x19google/protobuf/any.proto\x1a\x1bcosmos/group/v1/types.proto\x1a\x17cosmos/msg/v1/msg.proto"\x8e\x01\n\x0eMsgCreateGroup\x12\'\n\x05admin\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x125\n\x07members\x18\x02 \x03(\x0b2\x1e.cosmos.group.v1.MemberRequestB\x04\xc8\xde\x1f\x00\x12\x10\n\x08metadata\x18\x03 \x01(\t:\n\x82\xe7\xb0*\x05admin"*\n\x16MsgCreateGroupResponse\x12\x10\n\x08group_id\x18\x01 \x01(\x04"\x9c\x01\n\x15MsgUpdateGroupMembers\x12\'\n\x05admin\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x10\n\x08group_id\x18\x02 \x01(\x04\x12<\n\x0emember_updates\x18\x03 \x03(\x0b2\x1e.cosmos.group.v1.MemberRequestB\x04\xc8\xde\x1f\x00:\n\x82\xe7\xb0*\x05admin"\x1f\n\x1dMsgUpdateGroupMembersResponse"\x89\x01\n\x13MsgUpdateGroupAdmin\x12\'\n\x05admin\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x10\n\x08group_id\x18\x02 \x01(\x04\x12+\n\tnew_admin\x18\x03 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\n\x82\xe7\xb0*\x05admin"\x1d\n\x1bMsgUpdateGroupAdminResponse"q\n\x16MsgUpdateGroupMetadata\x12\'\n\x05admin\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x10\n\x08group_id\x18\x02 \x01(\x04\x12\x10\n\x08metadata\x18\x03 \x01(\t:\n\x82\xe7\xb0*\x05admin" \n\x1eMsgUpdateGroupMetadataResponse"\xc6\x01\n\x14MsgCreateGroupPolicy\x12\'\n\x05admin\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x10\n\x08group_id\x18\x02 \x01(\x04\x12\x10\n\x08metadata\x18\x03 \x01(\t\x12Q\n\x0fdecision_policy\x18\x04 \x01(\x0b2\x14.google.protobuf.AnyB"\xca\xb4-\x1ecosmos.group.v1.DecisionPolicy:\x0e\x82\xe7\xb0*\x05admin\x88\xa0\x1f\x00"I\n\x1cMsgCreateGroupPolicyResponse\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString"\xb5\x01\n\x19MsgUpdateGroupPolicyAdmin\x12\'\n\x05admin\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x126\n\x14group_policy_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12+\n\tnew_admin\x18\x03 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\n\x82\xe7\xb0*\x05admin"\xb3\x02\n\x18MsgCreateGroupWithPolicy\x12\'\n\x05admin\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x125\n\x07members\x18\x02 \x03(\x0b2\x1e.cosmos.group.v1.MemberRequestB\x04\xc8\xde\x1f\x00\x12\x16\n\x0egroup_metadata\x18\x03 \x01(\t\x12\x1d\n\x15group_policy_metadata\x18\x04 \x01(\t\x12\x1d\n\x15group_policy_as_admin\x18\x05 \x01(\x08\x12Q\n\x0fdecision_policy\x18\x06 \x01(\x0b2\x14.google.protobuf.AnyB"\xca\xb4-\x1ecosmos.group.v1.DecisionPolicy:\x0e\x82\xe7\xb0*\x05admin\x88\xa0\x1f\x00"l\n MsgCreateGroupWithPolicyResponse\x12\x10\n\x08group_id\x18\x01 \x01(\x04\x126\n\x14group_policy_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString"#\n!MsgUpdateGroupPolicyAdminResponse"\xe8\x01\n"MsgUpdateGroupPolicyDecisionPolicy\x12\'\n\x05admin\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x126\n\x14group_policy_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12Q\n\x0fdecision_policy\x18\x03 \x01(\x0b2\x14.google.protobuf.AnyB"\xca\xb4-\x1ecosmos.group.v1.DecisionPolicy:\x0e\x82\xe7\xb0*\x05admin\x88\xa0\x1f\x00",\n*MsgUpdateGroupPolicyDecisionPolicyResponse"\x9d\x01\n\x1cMsgUpdateGroupPolicyMetadata\x12\'\n\x05admin\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x126\n\x14group_policy_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x10\n\x08metadata\x18\x03 \x01(\t:\n\x82\xe7\xb0*\x05admin"&\n$MsgUpdateGroupPolicyMetadataResponse"\xd1\x01\n\x11MsgSubmitProposal\x126\n\x14group_policy_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x11\n\tproposers\x18\x02 \x03(\t\x12\x10\n\x08metadata\x18\x03 \x01(\t\x12&\n\x08messages\x18\x04 \x03(\x0b2\x14.google.protobuf.Any\x12#\n\x04exec\x18\x05 \x01(\x0e2\x15.cosmos.group.v1.Exec:\x12\x82\xe7\xb0*\tproposers\x88\xa0\x1f\x00"0\n\x19MsgSubmitProposalResponse\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04"c\n\x13MsgWithdrawProposal\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12)\n\x07address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x0c\x82\xe7\xb0*\x07address"\x1d\n\x1bMsgWithdrawProposalResponse"\xb7\x01\n\x07MsgVote\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12+\n\x06option\x18\x03 \x01(\x0e2\x1b.cosmos.group.v1.VoteOption\x12\x10\n\x08metadata\x18\x04 \x01(\t\x12#\n\x04exec\x18\x05 \x01(\x0e2\x15.cosmos.group.v1.Exec:\n\x82\xe7\xb0*\x05voter"\x11\n\x0fMsgVoteResponse"W\n\x07MsgExec\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12*\n\x08executor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x0b\x82\xe7\xb0*\x06signer"J\n\x0fMsgExecResponse\x127\n\x06result\x18\x02 \x01(\x0e2\'.cosmos.group.v1.ProposalExecutorResult"Z\n\rMsgLeaveGroup\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x10\n\x08group_id\x18\x02 \x01(\x04:\x0c\x82\xe7\xb0*\x07address"\x17\n\x15MsgLeaveGroupResponse**\n\x04Exec\x12\x14\n\x10EXEC_UNSPECIFIED\x10\x00\x12\x0c\n\x08EXEC_TRY\x10\x012\xc3\x0b\n\x03Msg\x12W\n\x0bCreateGroup\x12\x1f.cosmos.group.v1.MsgCreateGroup\x1a\'.cosmos.group.v1.MsgCreateGroupResponse\x12l\n\x12UpdateGroupMembers\x12&.cosmos.group.v1.MsgUpdateGroupMembers\x1a..cosmos.group.v1.MsgUpdateGroupMembersResponse\x12f\n\x10UpdateGroupAdmin\x12$.cosmos.group.v1.MsgUpdateGroupAdmin\x1a,.cosmos.group.v1.MsgUpdateGroupAdminResponse\x12o\n\x13UpdateGroupMetadata\x12\'.cosmos.group.v1.MsgUpdateGroupMetadata\x1a/.cosmos.group.v1.MsgUpdateGroupMetadataResponse\x12i\n\x11CreateGroupPolicy\x12%.cosmos.group.v1.MsgCreateGroupPolicy\x1a-.cosmos.group.v1.MsgCreateGroupPolicyResponse\x12u\n\x15CreateGroupWithPolicy\x12).cosmos.group.v1.MsgCreateGroupWithPolicy\x1a1.cosmos.group.v1.MsgCreateGroupWithPolicyResponse\x12x\n\x16UpdateGroupPolicyAdmin\x12*.cosmos.group.v1.MsgUpdateGroupPolicyAdmin\x1a2.cosmos.group.v1.MsgUpdateGroupPolicyAdminResponse\x12\x93\x01\n\x1fUpdateGroupPolicyDecisionPolicy\x123.cosmos.group.v1.MsgUpdateGroupPolicyDecisionPolicy\x1a;.cosmos.group.v1.MsgUpdateGroupPolicyDecisionPolicyResponse\x12\x81\x01\n\x19UpdateGroupPolicyMetadata\x12-.cosmos.group.v1.MsgUpdateGroupPolicyMetadata\x1a5.cosmos.group.v1.MsgUpdateGroupPolicyMetadataResponse\x12`\n\x0eSubmitProposal\x12".cosmos.group.v1.MsgSubmitProposal\x1a*.cosmos.group.v1.MsgSubmitProposalResponse\x12f\n\x10WithdrawProposal\x12$.cosmos.group.v1.MsgWithdrawProposal\x1a,.cosmos.group.v1.MsgWithdrawProposalResponse\x12B\n\x04Vote\x12\x18.cosmos.group.v1.MsgVote\x1a .cosmos.group.v1.MsgVoteResponse\x12B\n\x04Exec\x12\x18.cosmos.group.v1.MsgExec\x1a .cosmos.group.v1.MsgExecResponse\x12T\n\nLeaveGroup\x12\x1e.cosmos.group.v1.MsgLeaveGroup\x1a&.cosmos.group.v1.MsgLeaveGroupResponseB&Z$github.com/cosmos/cosmos-sdk/x/groupb\x06proto3')
_EXEC = DESCRIPTOR.enum_types_by_name['Exec']
Exec = enum_type_wrapper.EnumTypeWrapper(_EXEC)
EXEC_UNSPECIFIED = 0
EXEC_TRY = 1
_MSGCREATEGROUP = DESCRIPTOR.message_types_by_name['MsgCreateGroup']
_MSGCREATEGROUPRESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateGroupResponse']
_MSGUPDATEGROUPMEMBERS = DESCRIPTOR.message_types_by_name['MsgUpdateGroupMembers']
_MSGUPDATEGROUPMEMBERSRESPONSE = DESCRIPTOR.message_types_by_name['MsgUpdateGroupMembersResponse']
_MSGUPDATEGROUPADMIN = DESCRIPTOR.message_types_by_name['MsgUpdateGroupAdmin']
_MSGUPDATEGROUPADMINRESPONSE = DESCRIPTOR.message_types_by_name['MsgUpdateGroupAdminResponse']
_MSGUPDATEGROUPMETADATA = DESCRIPTOR.message_types_by_name['MsgUpdateGroupMetadata']
_MSGUPDATEGROUPMETADATARESPONSE = DESCRIPTOR.message_types_by_name['MsgUpdateGroupMetadataResponse']
_MSGCREATEGROUPPOLICY = DESCRIPTOR.message_types_by_name['MsgCreateGroupPolicy']
_MSGCREATEGROUPPOLICYRESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateGroupPolicyResponse']
_MSGUPDATEGROUPPOLICYADMIN = DESCRIPTOR.message_types_by_name['MsgUpdateGroupPolicyAdmin']
_MSGCREATEGROUPWITHPOLICY = DESCRIPTOR.message_types_by_name['MsgCreateGroupWithPolicy']
_MSGCREATEGROUPWITHPOLICYRESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateGroupWithPolicyResponse']
_MSGUPDATEGROUPPOLICYADMINRESPONSE = DESCRIPTOR.message_types_by_name['MsgUpdateGroupPolicyAdminResponse']
_MSGUPDATEGROUPPOLICYDECISIONPOLICY = DESCRIPTOR.message_types_by_name['MsgUpdateGroupPolicyDecisionPolicy']
_MSGUPDATEGROUPPOLICYDECISIONPOLICYRESPONSE = DESCRIPTOR.message_types_by_name['MsgUpdateGroupPolicyDecisionPolicyResponse']
_MSGUPDATEGROUPPOLICYMETADATA = DESCRIPTOR.message_types_by_name['MsgUpdateGroupPolicyMetadata']
_MSGUPDATEGROUPPOLICYMETADATARESPONSE = DESCRIPTOR.message_types_by_name['MsgUpdateGroupPolicyMetadataResponse']
_MSGSUBMITPROPOSAL = DESCRIPTOR.message_types_by_name['MsgSubmitProposal']
_MSGSUBMITPROPOSALRESPONSE = DESCRIPTOR.message_types_by_name['MsgSubmitProposalResponse']
_MSGWITHDRAWPROPOSAL = DESCRIPTOR.message_types_by_name['MsgWithdrawProposal']
_MSGWITHDRAWPROPOSALRESPONSE = DESCRIPTOR.message_types_by_name['MsgWithdrawProposalResponse']
_MSGVOTE = DESCRIPTOR.message_types_by_name['MsgVote']
_MSGVOTERESPONSE = DESCRIPTOR.message_types_by_name['MsgVoteResponse']
_MSGEXEC = DESCRIPTOR.message_types_by_name['MsgExec']
_MSGEXECRESPONSE = DESCRIPTOR.message_types_by_name['MsgExecResponse']
_MSGLEAVEGROUP = DESCRIPTOR.message_types_by_name['MsgLeaveGroup']
_MSGLEAVEGROUPRESPONSE = DESCRIPTOR.message_types_by_name['MsgLeaveGroupResponse']
MsgCreateGroup = _reflection.GeneratedProtocolMessageType('MsgCreateGroup', (_message.Message,), {'DESCRIPTOR': _MSGCREATEGROUP, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateGroup)
MsgCreateGroupResponse = _reflection.GeneratedProtocolMessageType('MsgCreateGroupResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATEGROUPRESPONSE, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateGroupResponse)
MsgUpdateGroupMembers = _reflection.GeneratedProtocolMessageType('MsgUpdateGroupMembers', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEGROUPMEMBERS, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgUpdateGroupMembers)
MsgUpdateGroupMembersResponse = _reflection.GeneratedProtocolMessageType('MsgUpdateGroupMembersResponse', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEGROUPMEMBERSRESPONSE, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgUpdateGroupMembersResponse)
MsgUpdateGroupAdmin = _reflection.GeneratedProtocolMessageType('MsgUpdateGroupAdmin', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEGROUPADMIN, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgUpdateGroupAdmin)
MsgUpdateGroupAdminResponse = _reflection.GeneratedProtocolMessageType('MsgUpdateGroupAdminResponse', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEGROUPADMINRESPONSE, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgUpdateGroupAdminResponse)
MsgUpdateGroupMetadata = _reflection.GeneratedProtocolMessageType('MsgUpdateGroupMetadata', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEGROUPMETADATA, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgUpdateGroupMetadata)
MsgUpdateGroupMetadataResponse = _reflection.GeneratedProtocolMessageType('MsgUpdateGroupMetadataResponse', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEGROUPMETADATARESPONSE, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgUpdateGroupMetadataResponse)
MsgCreateGroupPolicy = _reflection.GeneratedProtocolMessageType('MsgCreateGroupPolicy', (_message.Message,), {'DESCRIPTOR': _MSGCREATEGROUPPOLICY, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateGroupPolicy)
MsgCreateGroupPolicyResponse = _reflection.GeneratedProtocolMessageType('MsgCreateGroupPolicyResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATEGROUPPOLICYRESPONSE, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateGroupPolicyResponse)
MsgUpdateGroupPolicyAdmin = _reflection.GeneratedProtocolMessageType('MsgUpdateGroupPolicyAdmin', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEGROUPPOLICYADMIN, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgUpdateGroupPolicyAdmin)
MsgCreateGroupWithPolicy = _reflection.GeneratedProtocolMessageType('MsgCreateGroupWithPolicy', (_message.Message,), {'DESCRIPTOR': _MSGCREATEGROUPWITHPOLICY, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateGroupWithPolicy)
MsgCreateGroupWithPolicyResponse = _reflection.GeneratedProtocolMessageType('MsgCreateGroupWithPolicyResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATEGROUPWITHPOLICYRESPONSE, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateGroupWithPolicyResponse)
MsgUpdateGroupPolicyAdminResponse = _reflection.GeneratedProtocolMessageType('MsgUpdateGroupPolicyAdminResponse', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEGROUPPOLICYADMINRESPONSE, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgUpdateGroupPolicyAdminResponse)
MsgUpdateGroupPolicyDecisionPolicy = _reflection.GeneratedProtocolMessageType('MsgUpdateGroupPolicyDecisionPolicy', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEGROUPPOLICYDECISIONPOLICY, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgUpdateGroupPolicyDecisionPolicy)
MsgUpdateGroupPolicyDecisionPolicyResponse = _reflection.GeneratedProtocolMessageType('MsgUpdateGroupPolicyDecisionPolicyResponse', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEGROUPPOLICYDECISIONPOLICYRESPONSE, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgUpdateGroupPolicyDecisionPolicyResponse)
MsgUpdateGroupPolicyMetadata = _reflection.GeneratedProtocolMessageType('MsgUpdateGroupPolicyMetadata', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEGROUPPOLICYMETADATA, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgUpdateGroupPolicyMetadata)
MsgUpdateGroupPolicyMetadataResponse = _reflection.GeneratedProtocolMessageType('MsgUpdateGroupPolicyMetadataResponse', (_message.Message,), {'DESCRIPTOR': _MSGUPDATEGROUPPOLICYMETADATARESPONSE, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgUpdateGroupPolicyMetadataResponse)
MsgSubmitProposal = _reflection.GeneratedProtocolMessageType('MsgSubmitProposal', (_message.Message,), {'DESCRIPTOR': _MSGSUBMITPROPOSAL, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgSubmitProposal)
MsgSubmitProposalResponse = _reflection.GeneratedProtocolMessageType('MsgSubmitProposalResponse', (_message.Message,), {'DESCRIPTOR': _MSGSUBMITPROPOSALRESPONSE, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgSubmitProposalResponse)
MsgWithdrawProposal = _reflection.GeneratedProtocolMessageType('MsgWithdrawProposal', (_message.Message,), {'DESCRIPTOR': _MSGWITHDRAWPROPOSAL, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgWithdrawProposal)
MsgWithdrawProposalResponse = _reflection.GeneratedProtocolMessageType('MsgWithdrawProposalResponse', (_message.Message,), {'DESCRIPTOR': _MSGWITHDRAWPROPOSALRESPONSE, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgWithdrawProposalResponse)
MsgVote = _reflection.GeneratedProtocolMessageType('MsgVote', (_message.Message,), {'DESCRIPTOR': _MSGVOTE, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgVote)
MsgVoteResponse = _reflection.GeneratedProtocolMessageType('MsgVoteResponse', (_message.Message,), {'DESCRIPTOR': _MSGVOTERESPONSE, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgVoteResponse)
MsgExec = _reflection.GeneratedProtocolMessageType('MsgExec', (_message.Message,), {'DESCRIPTOR': _MSGEXEC, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgExec)
MsgExecResponse = _reflection.GeneratedProtocolMessageType('MsgExecResponse', (_message.Message,), {'DESCRIPTOR': _MSGEXECRESPONSE, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgExecResponse)
MsgLeaveGroup = _reflection.GeneratedProtocolMessageType('MsgLeaveGroup', (_message.Message,), {'DESCRIPTOR': _MSGLEAVEGROUP, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgLeaveGroup)
MsgLeaveGroupResponse = _reflection.GeneratedProtocolMessageType('MsgLeaveGroupResponse', (_message.Message,), {'DESCRIPTOR': _MSGLEAVEGROUPRESPONSE, '__module__': 'cosmos.group.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgLeaveGroupResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/group'
    _MSGCREATEGROUP.fields_by_name['admin']._options = None
    _MSGCREATEGROUP.fields_by_name['admin']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGCREATEGROUP.fields_by_name['members']._options = None
    _MSGCREATEGROUP.fields_by_name['members']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCREATEGROUP._options = None
    _MSGCREATEGROUP._serialized_options = b'\x82\xe7\xb0*\x05admin'
    _MSGUPDATEGROUPMEMBERS.fields_by_name['admin']._options = None
    _MSGUPDATEGROUPMEMBERS.fields_by_name['admin']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEGROUPMEMBERS.fields_by_name['member_updates']._options = None
    _MSGUPDATEGROUPMEMBERS.fields_by_name['member_updates']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGUPDATEGROUPMEMBERS._options = None
    _MSGUPDATEGROUPMEMBERS._serialized_options = b'\x82\xe7\xb0*\x05admin'
    _MSGUPDATEGROUPADMIN.fields_by_name['admin']._options = None
    _MSGUPDATEGROUPADMIN.fields_by_name['admin']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEGROUPADMIN.fields_by_name['new_admin']._options = None
    _MSGUPDATEGROUPADMIN.fields_by_name['new_admin']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEGROUPADMIN._options = None
    _MSGUPDATEGROUPADMIN._serialized_options = b'\x82\xe7\xb0*\x05admin'
    _MSGUPDATEGROUPMETADATA.fields_by_name['admin']._options = None
    _MSGUPDATEGROUPMETADATA.fields_by_name['admin']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEGROUPMETADATA._options = None
    _MSGUPDATEGROUPMETADATA._serialized_options = b'\x82\xe7\xb0*\x05admin'
    _MSGCREATEGROUPPOLICY.fields_by_name['admin']._options = None
    _MSGCREATEGROUPPOLICY.fields_by_name['admin']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGCREATEGROUPPOLICY.fields_by_name['decision_policy']._options = None
    _MSGCREATEGROUPPOLICY.fields_by_name['decision_policy']._serialized_options = b'\xca\xb4-\x1ecosmos.group.v1.DecisionPolicy'
    _MSGCREATEGROUPPOLICY._options = None
    _MSGCREATEGROUPPOLICY._serialized_options = b'\x82\xe7\xb0*\x05admin\x88\xa0\x1f\x00'
    _MSGCREATEGROUPPOLICYRESPONSE.fields_by_name['address']._options = None
    _MSGCREATEGROUPPOLICYRESPONSE.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEGROUPPOLICYADMIN.fields_by_name['admin']._options = None
    _MSGUPDATEGROUPPOLICYADMIN.fields_by_name['admin']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEGROUPPOLICYADMIN.fields_by_name['group_policy_address']._options = None
    _MSGUPDATEGROUPPOLICYADMIN.fields_by_name['group_policy_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEGROUPPOLICYADMIN.fields_by_name['new_admin']._options = None
    _MSGUPDATEGROUPPOLICYADMIN.fields_by_name['new_admin']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEGROUPPOLICYADMIN._options = None
    _MSGUPDATEGROUPPOLICYADMIN._serialized_options = b'\x82\xe7\xb0*\x05admin'
    _MSGCREATEGROUPWITHPOLICY.fields_by_name['admin']._options = None
    _MSGCREATEGROUPWITHPOLICY.fields_by_name['admin']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGCREATEGROUPWITHPOLICY.fields_by_name['members']._options = None
    _MSGCREATEGROUPWITHPOLICY.fields_by_name['members']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCREATEGROUPWITHPOLICY.fields_by_name['decision_policy']._options = None
    _MSGCREATEGROUPWITHPOLICY.fields_by_name['decision_policy']._serialized_options = b'\xca\xb4-\x1ecosmos.group.v1.DecisionPolicy'
    _MSGCREATEGROUPWITHPOLICY._options = None
    _MSGCREATEGROUPWITHPOLICY._serialized_options = b'\x82\xe7\xb0*\x05admin\x88\xa0\x1f\x00'
    _MSGCREATEGROUPWITHPOLICYRESPONSE.fields_by_name['group_policy_address']._options = None
    _MSGCREATEGROUPWITHPOLICYRESPONSE.fields_by_name['group_policy_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEGROUPPOLICYDECISIONPOLICY.fields_by_name['admin']._options = None
    _MSGUPDATEGROUPPOLICYDECISIONPOLICY.fields_by_name['admin']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEGROUPPOLICYDECISIONPOLICY.fields_by_name['group_policy_address']._options = None
    _MSGUPDATEGROUPPOLICYDECISIONPOLICY.fields_by_name['group_policy_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEGROUPPOLICYDECISIONPOLICY.fields_by_name['decision_policy']._options = None
    _MSGUPDATEGROUPPOLICYDECISIONPOLICY.fields_by_name['decision_policy']._serialized_options = b'\xca\xb4-\x1ecosmos.group.v1.DecisionPolicy'
    _MSGUPDATEGROUPPOLICYDECISIONPOLICY._options = None
    _MSGUPDATEGROUPPOLICYDECISIONPOLICY._serialized_options = b'\x82\xe7\xb0*\x05admin\x88\xa0\x1f\x00'
    _MSGUPDATEGROUPPOLICYMETADATA.fields_by_name['admin']._options = None
    _MSGUPDATEGROUPPOLICYMETADATA.fields_by_name['admin']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEGROUPPOLICYMETADATA.fields_by_name['group_policy_address']._options = None
    _MSGUPDATEGROUPPOLICYMETADATA.fields_by_name['group_policy_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEGROUPPOLICYMETADATA._options = None
    _MSGUPDATEGROUPPOLICYMETADATA._serialized_options = b'\x82\xe7\xb0*\x05admin'
    _MSGSUBMITPROPOSAL.fields_by_name['group_policy_address']._options = None
    _MSGSUBMITPROPOSAL.fields_by_name['group_policy_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGSUBMITPROPOSAL._options = None
    _MSGSUBMITPROPOSAL._serialized_options = b'\x82\xe7\xb0*\tproposers\x88\xa0\x1f\x00'
    _MSGWITHDRAWPROPOSAL.fields_by_name['address']._options = None
    _MSGWITHDRAWPROPOSAL.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGWITHDRAWPROPOSAL._options = None
    _MSGWITHDRAWPROPOSAL._serialized_options = b'\x82\xe7\xb0*\x07address'
    _MSGVOTE.fields_by_name['voter']._options = None
    _MSGVOTE.fields_by_name['voter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGVOTE._options = None
    _MSGVOTE._serialized_options = b'\x82\xe7\xb0*\x05voter'
    _MSGEXEC.fields_by_name['executor']._options = None
    _MSGEXEC.fields_by_name['executor']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGEXEC._options = None
    _MSGEXEC._serialized_options = b'\x82\xe7\xb0*\x06signer'
    _MSGLEAVEGROUP.fields_by_name['address']._options = None
    _MSGLEAVEGROUP.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGLEAVEGROUP._options = None
    _MSGLEAVEGROUP._serialized_options = b'\x82\xe7\xb0*\x07address'
    _EXEC._serialized_start = 3155
    _EXEC._serialized_end = 3197
    _MSGCREATEGROUP._serialized_start = 176
    _MSGCREATEGROUP._serialized_end = 318
    _MSGCREATEGROUPRESPONSE._serialized_start = 320
    _MSGCREATEGROUPRESPONSE._serialized_end = 362
    _MSGUPDATEGROUPMEMBERS._serialized_start = 365
    _MSGUPDATEGROUPMEMBERS._serialized_end = 521
    _MSGUPDATEGROUPMEMBERSRESPONSE._serialized_start = 523
    _MSGUPDATEGROUPMEMBERSRESPONSE._serialized_end = 554
    _MSGUPDATEGROUPADMIN._serialized_start = 557
    _MSGUPDATEGROUPADMIN._serialized_end = 694
    _MSGUPDATEGROUPADMINRESPONSE._serialized_start = 696
    _MSGUPDATEGROUPADMINRESPONSE._serialized_end = 725
    _MSGUPDATEGROUPMETADATA._serialized_start = 727
    _MSGUPDATEGROUPMETADATA._serialized_end = 840
    _MSGUPDATEGROUPMETADATARESPONSE._serialized_start = 842
    _MSGUPDATEGROUPMETADATARESPONSE._serialized_end = 874
    _MSGCREATEGROUPPOLICY._serialized_start = 877
    _MSGCREATEGROUPPOLICY._serialized_end = 1075
    _MSGCREATEGROUPPOLICYRESPONSE._serialized_start = 1077
    _MSGCREATEGROUPPOLICYRESPONSE._serialized_end = 1150
    _MSGUPDATEGROUPPOLICYADMIN._serialized_start = 1153
    _MSGUPDATEGROUPPOLICYADMIN._serialized_end = 1334
    _MSGCREATEGROUPWITHPOLICY._serialized_start = 1337
    _MSGCREATEGROUPWITHPOLICY._serialized_end = 1644
    _MSGCREATEGROUPWITHPOLICYRESPONSE._serialized_start = 1646
    _MSGCREATEGROUPWITHPOLICYRESPONSE._serialized_end = 1754
    _MSGUPDATEGROUPPOLICYADMINRESPONSE._serialized_start = 1756
    _MSGUPDATEGROUPPOLICYADMINRESPONSE._serialized_end = 1791
    _MSGUPDATEGROUPPOLICYDECISIONPOLICY._serialized_start = 1794
    _MSGUPDATEGROUPPOLICYDECISIONPOLICY._serialized_end = 2026
    _MSGUPDATEGROUPPOLICYDECISIONPOLICYRESPONSE._serialized_start = 2028
    _MSGUPDATEGROUPPOLICYDECISIONPOLICYRESPONSE._serialized_end = 2072
    _MSGUPDATEGROUPPOLICYMETADATA._serialized_start = 2075
    _MSGUPDATEGROUPPOLICYMETADATA._serialized_end = 2232
    _MSGUPDATEGROUPPOLICYMETADATARESPONSE._serialized_start = 2234
    _MSGUPDATEGROUPPOLICYMETADATARESPONSE._serialized_end = 2272
    _MSGSUBMITPROPOSAL._serialized_start = 2275
    _MSGSUBMITPROPOSAL._serialized_end = 2484
    _MSGSUBMITPROPOSALRESPONSE._serialized_start = 2486
    _MSGSUBMITPROPOSALRESPONSE._serialized_end = 2534
    _MSGWITHDRAWPROPOSAL._serialized_start = 2536
    _MSGWITHDRAWPROPOSAL._serialized_end = 2635
    _MSGWITHDRAWPROPOSALRESPONSE._serialized_start = 2637
    _MSGWITHDRAWPROPOSALRESPONSE._serialized_end = 2666
    _MSGVOTE._serialized_start = 2669
    _MSGVOTE._serialized_end = 2852
    _MSGVOTERESPONSE._serialized_start = 2854
    _MSGVOTERESPONSE._serialized_end = 2871
    _MSGEXEC._serialized_start = 2873
    _MSGEXEC._serialized_end = 2960
    _MSGEXECRESPONSE._serialized_start = 2962
    _MSGEXECRESPONSE._serialized_end = 3036
    _MSGLEAVEGROUP._serialized_start = 3038
    _MSGLEAVEGROUP._serialized_end = 3128
    _MSGLEAVEGROUPRESPONSE._serialized_start = 3130
    _MSGLEAVEGROUPRESPONSE._serialized_end = 3153
    _MSG._serialized_start = 3200
    _MSG._serialized_end = 4675

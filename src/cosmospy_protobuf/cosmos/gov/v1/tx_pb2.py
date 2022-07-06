
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.gov.v1 import gov_pb2 as cosmos_dot_gov_dot_v1_dot_gov__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16cosmos/gov/v1/tx.proto\x12\rcosmos.gov.v1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x17cosmos/gov/v1/gov.proto\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x19google/protobuf/any.proto\x1a\x17cosmos/msg/v1/msg.proto"\xc2\x01\n\x11MsgSubmitProposal\x12&\n\x08messages\x18\x01 \x03(\x0b2\x14.google.protobuf.Any\x128\n\x0finitial_deposit\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12*\n\x08proposer\x18\x03 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x10\n\x08metadata\x18\x04 \x01(\t:\r\x82\xe7\xb0*\x08proposer"0\n\x19MsgSubmitProposalResponse\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04"m\n\x14MsgExecLegacyContent\x122\n\x07content\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyB\x0b\xca\xb4-\x07Content\x12\x11\n\tauthority\x18\x02 \x01(\t:\x0e\x82\xe7\xb0*\tauthority"\x1e\n\x1cMsgExecLegacyContentResponse"\xa1\x01\n\x07MsgVote\x12$\n\x0bproposal_id\x18\x01 \x01(\x04B\x0f\xea\xde\x1f\x0bproposal_id\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12)\n\x06option\x18\x03 \x01(\x0e2\x19.cosmos.gov.v1.VoteOption\x12\x10\n\x08metadata\x18\x04 \x01(\t:\n\x82\xe7\xb0*\x05voter"\x11\n\x0fMsgVoteResponse"\xb2\x01\n\x0fMsgVoteWeighted\x12$\n\x0bproposal_id\x18\x01 \x01(\x04B\x0f\xea\xde\x1f\x0bproposal_id\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x122\n\x07options\x18\x03 \x03(\x0b2!.cosmos.gov.v1.WeightedVoteOption\x12\x10\n\x08metadata\x18\x04 \x01(\t:\n\x82\xe7\xb0*\x05voter"\x19\n\x17MsgVoteWeightedResponse"\xa0\x01\n\nMsgDeposit\x12$\n\x0bproposal_id\x18\x01 \x01(\x04B\x0f\xea\xde\x1f\x0bproposal_id\x12+\n\tdepositor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12/\n\x06amount\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tdepositor"\x14\n\x12MsgDepositResponse2\xab\x03\n\x03Msg\x12\\\n\x0eSubmitProposal\x12 .cosmos.gov.v1.MsgSubmitProposal\x1a(.cosmos.gov.v1.MsgSubmitProposalResponse\x12e\n\x11ExecLegacyContent\x12#.cosmos.gov.v1.MsgExecLegacyContent\x1a+.cosmos.gov.v1.MsgExecLegacyContentResponse\x12>\n\x04Vote\x12\x16.cosmos.gov.v1.MsgVote\x1a\x1e.cosmos.gov.v1.MsgVoteResponse\x12V\n\x0cVoteWeighted\x12\x1e.cosmos.gov.v1.MsgVoteWeighted\x1a&.cosmos.gov.v1.MsgVoteWeightedResponse\x12G\n\x07Deposit\x12\x19.cosmos.gov.v1.MsgDeposit\x1a!.cosmos.gov.v1.MsgDepositResponseB-Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1b\x06proto3')
_MSGSUBMITPROPOSAL = DESCRIPTOR.message_types_by_name['MsgSubmitProposal']
_MSGSUBMITPROPOSALRESPONSE = DESCRIPTOR.message_types_by_name['MsgSubmitProposalResponse']
_MSGEXECLEGACYCONTENT = DESCRIPTOR.message_types_by_name['MsgExecLegacyContent']
_MSGEXECLEGACYCONTENTRESPONSE = DESCRIPTOR.message_types_by_name['MsgExecLegacyContentResponse']
_MSGVOTE = DESCRIPTOR.message_types_by_name['MsgVote']
_MSGVOTERESPONSE = DESCRIPTOR.message_types_by_name['MsgVoteResponse']
_MSGVOTEWEIGHTED = DESCRIPTOR.message_types_by_name['MsgVoteWeighted']
_MSGVOTEWEIGHTEDRESPONSE = DESCRIPTOR.message_types_by_name['MsgVoteWeightedResponse']
_MSGDEPOSIT = DESCRIPTOR.message_types_by_name['MsgDeposit']
_MSGDEPOSITRESPONSE = DESCRIPTOR.message_types_by_name['MsgDepositResponse']
MsgSubmitProposal = _reflection.GeneratedProtocolMessageType('MsgSubmitProposal', (_message.Message,), {'DESCRIPTOR': _MSGSUBMITPROPOSAL, '__module__': 'cosmos.gov.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgSubmitProposal)
MsgSubmitProposalResponse = _reflection.GeneratedProtocolMessageType('MsgSubmitProposalResponse', (_message.Message,), {'DESCRIPTOR': _MSGSUBMITPROPOSALRESPONSE, '__module__': 'cosmos.gov.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgSubmitProposalResponse)
MsgExecLegacyContent = _reflection.GeneratedProtocolMessageType('MsgExecLegacyContent', (_message.Message,), {'DESCRIPTOR': _MSGEXECLEGACYCONTENT, '__module__': 'cosmos.gov.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgExecLegacyContent)
MsgExecLegacyContentResponse = _reflection.GeneratedProtocolMessageType('MsgExecLegacyContentResponse', (_message.Message,), {'DESCRIPTOR': _MSGEXECLEGACYCONTENTRESPONSE, '__module__': 'cosmos.gov.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgExecLegacyContentResponse)
MsgVote = _reflection.GeneratedProtocolMessageType('MsgVote', (_message.Message,), {'DESCRIPTOR': _MSGVOTE, '__module__': 'cosmos.gov.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgVote)
MsgVoteResponse = _reflection.GeneratedProtocolMessageType('MsgVoteResponse', (_message.Message,), {'DESCRIPTOR': _MSGVOTERESPONSE, '__module__': 'cosmos.gov.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgVoteResponse)
MsgVoteWeighted = _reflection.GeneratedProtocolMessageType('MsgVoteWeighted', (_message.Message,), {'DESCRIPTOR': _MSGVOTEWEIGHTED, '__module__': 'cosmos.gov.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgVoteWeighted)
MsgVoteWeightedResponse = _reflection.GeneratedProtocolMessageType('MsgVoteWeightedResponse', (_message.Message,), {'DESCRIPTOR': _MSGVOTEWEIGHTEDRESPONSE, '__module__': 'cosmos.gov.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgVoteWeightedResponse)
MsgDeposit = _reflection.GeneratedProtocolMessageType('MsgDeposit', (_message.Message,), {'DESCRIPTOR': _MSGDEPOSIT, '__module__': 'cosmos.gov.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgDeposit)
MsgDepositResponse = _reflection.GeneratedProtocolMessageType('MsgDepositResponse', (_message.Message,), {'DESCRIPTOR': _MSGDEPOSITRESPONSE, '__module__': 'cosmos.gov.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgDepositResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1'
    _MSGSUBMITPROPOSAL.fields_by_name['initial_deposit']._options = None
    _MSGSUBMITPROPOSAL.fields_by_name['initial_deposit']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGSUBMITPROPOSAL.fields_by_name['proposer']._options = None
    _MSGSUBMITPROPOSAL.fields_by_name['proposer']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGSUBMITPROPOSAL._options = None
    _MSGSUBMITPROPOSAL._serialized_options = b'\x82\xe7\xb0*\x08proposer'
    _MSGEXECLEGACYCONTENT.fields_by_name['content']._options = None
    _MSGEXECLEGACYCONTENT.fields_by_name['content']._serialized_options = b'\xca\xb4-\x07Content'
    _MSGEXECLEGACYCONTENT._options = None
    _MSGEXECLEGACYCONTENT._serialized_options = b'\x82\xe7\xb0*\tauthority'
    _MSGVOTE.fields_by_name['proposal_id']._options = None
    _MSGVOTE.fields_by_name['proposal_id']._serialized_options = b'\xea\xde\x1f\x0bproposal_id'
    _MSGVOTE.fields_by_name['voter']._options = None
    _MSGVOTE.fields_by_name['voter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGVOTE._options = None
    _MSGVOTE._serialized_options = b'\x82\xe7\xb0*\x05voter'
    _MSGVOTEWEIGHTED.fields_by_name['proposal_id']._options = None
    _MSGVOTEWEIGHTED.fields_by_name['proposal_id']._serialized_options = b'\xea\xde\x1f\x0bproposal_id'
    _MSGVOTEWEIGHTED.fields_by_name['voter']._options = None
    _MSGVOTEWEIGHTED.fields_by_name['voter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGVOTEWEIGHTED._options = None
    _MSGVOTEWEIGHTED._serialized_options = b'\x82\xe7\xb0*\x05voter'
    _MSGDEPOSIT.fields_by_name['proposal_id']._options = None
    _MSGDEPOSIT.fields_by_name['proposal_id']._serialized_options = b'\xea\xde\x1f\x0bproposal_id'
    _MSGDEPOSIT.fields_by_name['depositor']._options = None
    _MSGDEPOSIT.fields_by_name['depositor']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGDEPOSIT.fields_by_name['amount']._options = None
    _MSGDEPOSIT.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGDEPOSIT._options = None
    _MSGDEPOSIT._serialized_options = b'\x82\xe7\xb0*\tdepositor'
    _MSGSUBMITPROPOSAL._serialized_start = 200
    _MSGSUBMITPROPOSAL._serialized_end = 394
    _MSGSUBMITPROPOSALRESPONSE._serialized_start = 396
    _MSGSUBMITPROPOSALRESPONSE._serialized_end = 444
    _MSGEXECLEGACYCONTENT._serialized_start = 446
    _MSGEXECLEGACYCONTENT._serialized_end = 555
    _MSGEXECLEGACYCONTENTRESPONSE._serialized_start = 557
    _MSGEXECLEGACYCONTENTRESPONSE._serialized_end = 587
    _MSGVOTE._serialized_start = 590
    _MSGVOTE._serialized_end = 751
    _MSGVOTERESPONSE._serialized_start = 753
    _MSGVOTERESPONSE._serialized_end = 770
    _MSGVOTEWEIGHTED._serialized_start = 773
    _MSGVOTEWEIGHTED._serialized_end = 951
    _MSGVOTEWEIGHTEDRESPONSE._serialized_start = 953
    _MSGVOTEWEIGHTEDRESPONSE._serialized_end = 978
    _MSGDEPOSIT._serialized_start = 981
    _MSGDEPOSIT._serialized_end = 1141
    _MSGDEPOSITRESPONSE._serialized_start = 1143
    _MSGDEPOSITRESPONSE._serialized_end = 1163
    _MSG._serialized_start = 1166
    _MSG._serialized_end = 1593

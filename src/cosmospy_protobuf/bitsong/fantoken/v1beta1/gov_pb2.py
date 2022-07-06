
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"bitsong/fantoken/v1beta1/gov.proto\x12\x18bitsong.fantoken.v1beta1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto"\x96\x02\n\x12UpdateFeesProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12F\n\tissue_fee\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x18\xf2\xde\x1f\x10yaml:"issue_fee"\xc8\xde\x1f\x00\x12D\n\x08mint_fee\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x17\xf2\xde\x1f\x0fyaml:"mint_fee"\xc8\xde\x1f\x00\x12D\n\x08burn_fee\x18\x05 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x17\xf2\xde\x1f\x0fyaml:"burn_fee"\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00"\x91\x01\n\x1dUpdateFeesProposalWithDeposit\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x11\n\tissue_fee\x18\x03 \x01(\t\x12\x10\n\x08mint_fee\x18\x04 \x01(\t\x12\x10\n\x08burn_fee\x18\x05 \x01(\t\x12\x0f\n\x07deposit\x18\x07 \x01(\t:\x04\x98\xa0\x1f\x01B<Z6github.com/bitsongofficial/go-bitsong/x/fantoken/types\xc8\xe1\x1e\x00b\x06proto3')
_UPDATEFEESPROPOSAL = DESCRIPTOR.message_types_by_name['UpdateFeesProposal']
_UPDATEFEESPROPOSALWITHDEPOSIT = DESCRIPTOR.message_types_by_name['UpdateFeesProposalWithDeposit']
UpdateFeesProposal = _reflection.GeneratedProtocolMessageType('UpdateFeesProposal', (_message.Message,), {'DESCRIPTOR': _UPDATEFEESPROPOSAL, '__module__': 'bitsong.fantoken.v1beta1.gov_pb2'})
_sym_db.RegisterMessage(UpdateFeesProposal)
UpdateFeesProposalWithDeposit = _reflection.GeneratedProtocolMessageType('UpdateFeesProposalWithDeposit', (_message.Message,), {'DESCRIPTOR': _UPDATEFEESPROPOSALWITHDEPOSIT, '__module__': 'bitsong.fantoken.v1beta1.gov_pb2'})
_sym_db.RegisterMessage(UpdateFeesProposalWithDeposit)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/bitsongofficial/go-bitsong/x/fantoken/types\xc8\xe1\x1e\x00'
    _UPDATEFEESPROPOSAL.fields_by_name['issue_fee']._options = None
    _UPDATEFEESPROPOSAL.fields_by_name['issue_fee']._serialized_options = b'\xf2\xde\x1f\x10yaml:"issue_fee"\xc8\xde\x1f\x00'
    _UPDATEFEESPROPOSAL.fields_by_name['mint_fee']._options = None
    _UPDATEFEESPROPOSAL.fields_by_name['mint_fee']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"mint_fee"\xc8\xde\x1f\x00'
    _UPDATEFEESPROPOSAL.fields_by_name['burn_fee']._options = None
    _UPDATEFEESPROPOSAL.fields_by_name['burn_fee']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"burn_fee"\xc8\xde\x1f\x00'
    _UPDATEFEESPROPOSAL._options = None
    _UPDATEFEESPROPOSAL._serialized_options = b'\xe8\xa0\x1f\x01\x98\xa0\x1f\x00'
    _UPDATEFEESPROPOSALWITHDEPOSIT._options = None
    _UPDATEFEESPROPOSALWITHDEPOSIT._serialized_options = b'\x98\xa0\x1f\x01'
    _UPDATEFEESPROPOSAL._serialized_start = 119
    _UPDATEFEESPROPOSAL._serialized_end = 397
    _UPDATEFEESPROPOSALWITHDEPOSIT._serialized_start = 400
    _UPDATEFEESPROPOSALWITHDEPOSIT._serialized_end = 545

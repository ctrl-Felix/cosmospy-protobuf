
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%bitsong/fantoken/v1beta1/params.proto\x12\x18bitsong.fantoken.v1beta1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto"\xe6\x01\n\x06Params\x12F\n\tissue_fee\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x18\xf2\xde\x1f\x10yaml:"issue_fee"\xc8\xde\x1f\x00\x12D\n\x08mint_fee\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x17\xf2\xde\x1f\x0fyaml:"mint_fee"\xc8\xde\x1f\x00\x12D\n\x08burn_fee\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x17\xf2\xde\x1f\x0fyaml:"burn_fee"\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00B<Z6github.com/bitsongofficial/go-bitsong/x/fantoken/types\xc8\xe1\x1e\x00b\x06proto3')
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {'DESCRIPTOR': _PARAMS, '__module__': 'bitsong.fantoken.v1beta1.params_pb2'})
_sym_db.RegisterMessage(Params)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/bitsongofficial/go-bitsong/x/fantoken/types\xc8\xe1\x1e\x00'
    _PARAMS.fields_by_name['issue_fee']._options = None
    _PARAMS.fields_by_name['issue_fee']._serialized_options = b'\xf2\xde\x1f\x10yaml:"issue_fee"\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['mint_fee']._options = None
    _PARAMS.fields_by_name['mint_fee']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"mint_fee"\xc8\xde\x1f\x00'
    _PARAMS.fields_by_name['burn_fee']._options = None
    _PARAMS.fields_by_name['burn_fee']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"burn_fee"\xc8\xde\x1f\x00'
    _PARAMS._options = None
    _PARAMS._serialized_options = b'\xe8\xa0\x1f\x01\x98\xa0\x1f\x00'
    _PARAMS._serialized_start = 122
    _PARAMS._serialized_end = 352

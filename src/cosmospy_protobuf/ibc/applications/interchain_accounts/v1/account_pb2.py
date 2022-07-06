
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....cosmos.auth.v1beta1 import auth_pb2 as cosmos_dot_auth_dot_v1beta1_dot_auth__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5ibc/applications/interchain_accounts/v1/account.proto\x12\'ibc.applications.interchain_accounts.v1\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/auth/v1beta1/auth.proto"\xb9\x01\n\x11InterchainAccount\x12S\n\x0cbase_account\x18\x01 \x01(\x0b2 .cosmos.auth.v1beta1.BaseAccountB\x1b\xd0\xde\x1f\x01\xf2\xde\x1f\x13yaml:"base_account"\x12/\n\raccount_owner\x18\x02 \x01(\tB\x18\xf2\xde\x1f\x14yaml:"account_owner":\x1e\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xca\xb4-\x12InterchainAccountIBGZEgithub.com/cosmos/ibc-go/v3/modules/apps/27-interchain-accounts/typesb\x06proto3')
_INTERCHAINACCOUNT = DESCRIPTOR.message_types_by_name['InterchainAccount']
InterchainAccount = _reflection.GeneratedProtocolMessageType('InterchainAccount', (_message.Message,), {'DESCRIPTOR': _INTERCHAINACCOUNT, '__module__': 'ibc.applications.interchain_accounts.v1.account_pb2'})
_sym_db.RegisterMessage(InterchainAccount)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZEgithub.com/cosmos/ibc-go/v3/modules/apps/27-interchain-accounts/types'
    _INTERCHAINACCOUNT.fields_by_name['base_account']._options = None
    _INTERCHAINACCOUNT.fields_by_name['base_account']._serialized_options = b'\xd0\xde\x1f\x01\xf2\xde\x1f\x13yaml:"base_account"'
    _INTERCHAINACCOUNT.fields_by_name['account_owner']._options = None
    _INTERCHAINACCOUNT.fields_by_name['account_owner']._serialized_options = b'\xf2\xde\x1f\x14yaml:"account_owner"'
    _INTERCHAINACCOUNT._options = None
    _INTERCHAINACCOUNT._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xca\xb4-\x12InterchainAccountI'
    _INTERCHAINACCOUNT._serialized_start = 180
    _INTERCHAINACCOUNT._serialized_end = 365

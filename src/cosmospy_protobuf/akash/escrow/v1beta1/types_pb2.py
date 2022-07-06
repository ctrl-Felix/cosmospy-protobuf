
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n akash/escrow/v1beta1/types.proto\x12\x14akash.escrow.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"`\n\tAccountID\x12(\n\x05scope\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05scope\xf2\xde\x1f\x0cyaml:"scope"\x12)\n\x03xid\x18\x02 \x01(\tB\x1c\xea\xde\x1f\x03xid\xf2\xde\x1f\nyaml:"xid"\xe2\xde\x1f\x03XID"\xd1\x04\n\x07Account\x12J\n\x02id\x18\x01 \x01(\x0b2\x1f.akash.escrow.v1beta1.AccountIDB\x1d\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"\xe2\xde\x1f\x02ID\x12(\n\x05owner\x18\x02 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12M\n\x05state\x18\x03 \x01(\x0e2#.akash.escrow.v1beta1.Account.StateB\x19\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"\x12M\n\x07balance\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB!\xc8\xde\x1f\x00\xea\xde\x1f\x07balance\xf2\xde\x1f\x0eyaml:"balance"\x12Y\n\x0btransferred\x18\x05 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB)\xc8\xde\x1f\x00\xea\xde\x1f\x0btransferred\xf2\xde\x1f\x12yaml:"transferred"\x12B\n\nsettled_at\x18\x06 \x01(\x03B.\xea\xde\x1f\tsettledAt\xf2\xde\x1f\x10yaml:"settledAt"\xe2\xde\x1f\tSettledAt"\x92\x01\n\x05State\x12$\n\x07invalid\x10\x00\x1a\x17\x8a\x9d \x13AccountStateInvalid\x12\x19\n\x04open\x10\x01\x1a\x0f\x8a\x9d \x0bAccountOpen\x12\x1d\n\x06closed\x10\x02\x1a\x11\x8a\x9d \rAccountClosed\x12#\n\toverdrawn\x10\x03\x1a\x14\x8a\x9d \x10AccountOverdrawn\x1a\x04\x88\xa3\x1e\x00"\xb4\x05\n\x07Payment\x12g\n\naccount_id\x18\x01 \x01(\x0b2\x1f.akash.escrow.v1beta1.AccountIDB2\xc8\xde\x1f\x00\xea\xde\x1f\taccountID\xf2\xde\x1f\x10yaml:"accountID"\xe2\xde\x1f\tAccountID\x12B\n\npayment_id\x18\x02 \x01(\tB.\xea\xde\x1f\tpaymentID\xf2\xde\x1f\x10yaml:"paymentID"\xe2\xde\x1f\tPaymentID\x12(\n\x05owner\x18\x03 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12M\n\x05state\x18\x04 \x01(\x0e2#.akash.escrow.v1beta1.Payment.StateB\x19\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"\x12D\n\x04rate\x18\x05 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04rate\xf2\xde\x1f\x0byaml:"rate"\x12M\n\x07balance\x18\x06 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB!\xc8\xde\x1f\x00\xea\xde\x1f\x07balance\xf2\xde\x1f\x0eyaml:"balance"\x12S\n\twithdrawn\x18\x07 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB%\xc8\xde\x1f\x00\xea\xde\x1f\twithdrawn\xf2\xde\x1f\x10yaml:"withdrawn""\x92\x01\n\x05State\x12$\n\x07invalid\x10\x00\x1a\x17\x8a\x9d \x13PaymentStateInvalid\x12\x19\n\x04open\x10\x01\x1a\x0f\x8a\x9d \x0bPaymentOpen\x12\x1d\n\x06closed\x10\x02\x1a\x11\x8a\x9d \rPaymentClosed\x12#\n\toverdrawn\x10\x03\x1a\x14\x8a\x9d \x10PaymentOverdrawn\x1a\x04\x88\xa3\x1e\x00:\x04\x98\xa0\x1f\x01B0Z.github.com/ovrclk/akash/x/escrow/types/v1beta1b\x06proto3')
_ACCOUNTID = DESCRIPTOR.message_types_by_name['AccountID']
_ACCOUNT = DESCRIPTOR.message_types_by_name['Account']
_PAYMENT = DESCRIPTOR.message_types_by_name['Payment']
_ACCOUNT_STATE = _ACCOUNT.enum_types_by_name['State']
_PAYMENT_STATE = _PAYMENT.enum_types_by_name['State']
AccountID = _reflection.GeneratedProtocolMessageType('AccountID', (_message.Message,), {'DESCRIPTOR': _ACCOUNTID, '__module__': 'akash.escrow.v1beta1.types_pb2'})
_sym_db.RegisterMessage(AccountID)
Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {'DESCRIPTOR': _ACCOUNT, '__module__': 'akash.escrow.v1beta1.types_pb2'})
_sym_db.RegisterMessage(Account)
Payment = _reflection.GeneratedProtocolMessageType('Payment', (_message.Message,), {'DESCRIPTOR': _PAYMENT, '__module__': 'akash.escrow.v1beta1.types_pb2'})
_sym_db.RegisterMessage(Payment)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z.github.com/ovrclk/akash/x/escrow/types/v1beta1'
    _ACCOUNTID.fields_by_name['scope']._options = None
    _ACCOUNTID.fields_by_name['scope']._serialized_options = b'\xea\xde\x1f\x05scope\xf2\xde\x1f\x0cyaml:"scope"'
    _ACCOUNTID.fields_by_name['xid']._options = None
    _ACCOUNTID.fields_by_name['xid']._serialized_options = b'\xea\xde\x1f\x03xid\xf2\xde\x1f\nyaml:"xid"\xe2\xde\x1f\x03XID'
    _ACCOUNT_STATE._options = None
    _ACCOUNT_STATE._serialized_options = b'\x88\xa3\x1e\x00'
    _ACCOUNT_STATE.values_by_name['invalid']._options = None
    _ACCOUNT_STATE.values_by_name['invalid']._serialized_options = b'\x8a\x9d \x13AccountStateInvalid'
    _ACCOUNT_STATE.values_by_name['open']._options = None
    _ACCOUNT_STATE.values_by_name['open']._serialized_options = b'\x8a\x9d \x0bAccountOpen'
    _ACCOUNT_STATE.values_by_name['closed']._options = None
    _ACCOUNT_STATE.values_by_name['closed']._serialized_options = b'\x8a\x9d \rAccountClosed'
    _ACCOUNT_STATE.values_by_name['overdrawn']._options = None
    _ACCOUNT_STATE.values_by_name['overdrawn']._serialized_options = b'\x8a\x9d \x10AccountOverdrawn'
    _ACCOUNT.fields_by_name['id']._options = None
    _ACCOUNT.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"\xe2\xde\x1f\x02ID'
    _ACCOUNT.fields_by_name['owner']._options = None
    _ACCOUNT.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _ACCOUNT.fields_by_name['state']._options = None
    _ACCOUNT.fields_by_name['state']._serialized_options = b'\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"'
    _ACCOUNT.fields_by_name['balance']._options = None
    _ACCOUNT.fields_by_name['balance']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x07balance\xf2\xde\x1f\x0eyaml:"balance"'
    _ACCOUNT.fields_by_name['transferred']._options = None
    _ACCOUNT.fields_by_name['transferred']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x0btransferred\xf2\xde\x1f\x12yaml:"transferred"'
    _ACCOUNT.fields_by_name['settled_at']._options = None
    _ACCOUNT.fields_by_name['settled_at']._serialized_options = b'\xea\xde\x1f\tsettledAt\xf2\xde\x1f\x10yaml:"settledAt"\xe2\xde\x1f\tSettledAt'
    _PAYMENT_STATE._options = None
    _PAYMENT_STATE._serialized_options = b'\x88\xa3\x1e\x00'
    _PAYMENT_STATE.values_by_name['invalid']._options = None
    _PAYMENT_STATE.values_by_name['invalid']._serialized_options = b'\x8a\x9d \x13PaymentStateInvalid'
    _PAYMENT_STATE.values_by_name['open']._options = None
    _PAYMENT_STATE.values_by_name['open']._serialized_options = b'\x8a\x9d \x0bPaymentOpen'
    _PAYMENT_STATE.values_by_name['closed']._options = None
    _PAYMENT_STATE.values_by_name['closed']._serialized_options = b'\x8a\x9d \rPaymentClosed'
    _PAYMENT_STATE.values_by_name['overdrawn']._options = None
    _PAYMENT_STATE.values_by_name['overdrawn']._serialized_options = b'\x8a\x9d \x10PaymentOverdrawn'
    _PAYMENT.fields_by_name['account_id']._options = None
    _PAYMENT.fields_by_name['account_id']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\taccountID\xf2\xde\x1f\x10yaml:"accountID"\xe2\xde\x1f\tAccountID'
    _PAYMENT.fields_by_name['payment_id']._options = None
    _PAYMENT.fields_by_name['payment_id']._serialized_options = b'\xea\xde\x1f\tpaymentID\xf2\xde\x1f\x10yaml:"paymentID"\xe2\xde\x1f\tPaymentID'
    _PAYMENT.fields_by_name['owner']._options = None
    _PAYMENT.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _PAYMENT.fields_by_name['state']._options = None
    _PAYMENT.fields_by_name['state']._serialized_options = b'\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"'
    _PAYMENT.fields_by_name['rate']._options = None
    _PAYMENT.fields_by_name['rate']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04rate\xf2\xde\x1f\x0byaml:"rate"'
    _PAYMENT.fields_by_name['balance']._options = None
    _PAYMENT.fields_by_name['balance']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x07balance\xf2\xde\x1f\x0eyaml:"balance"'
    _PAYMENT.fields_by_name['withdrawn']._options = None
    _PAYMENT.fields_by_name['withdrawn']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\twithdrawn\xf2\xde\x1f\x10yaml:"withdrawn"'
    _PAYMENT._options = None
    _PAYMENT._serialized_options = b'\x98\xa0\x1f\x01'
    _ACCOUNTID._serialized_start = 112
    _ACCOUNTID._serialized_end = 208
    _ACCOUNT._serialized_start = 211
    _ACCOUNT._serialized_end = 804
    _ACCOUNT_STATE._serialized_start = 658
    _ACCOUNT_STATE._serialized_end = 804
    _PAYMENT._serialized_start = 807
    _PAYMENT._serialized_end = 1499
    _PAYMENT_STATE._serialized_start = 1347
    _PAYMENT_STATE._serialized_end = 1493

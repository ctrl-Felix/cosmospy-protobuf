
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from .....cosmos.crypto.hd.v1 import hd_pb2 as cosmos_dot_crypto_dot_hd_dot_v1_dot_hd__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%cosmos/crypto/keyring/v1/record.proto\x12\x18cosmos.crypto.keyring.v1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1ccosmos/crypto/hd/v1/hd.proto"\xc5\x03\n\x06Record\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x07pub_key\x18\x02 \x01(\x0b2\x14.google.protobuf.Any\x127\n\x05local\x18\x03 \x01(\x0b2&.cosmos.crypto.keyring.v1.Record.LocalH\x00\x129\n\x06ledger\x18\x04 \x01(\x0b2\'.cosmos.crypto.keyring.v1.Record.LedgerH\x00\x127\n\x05multi\x18\x05 \x01(\x0b2&.cosmos.crypto.keyring.v1.Record.MultiH\x00\x12;\n\x07offline\x18\x06 \x01(\x0b2(.cosmos.crypto.keyring.v1.Record.OfflineH\x00\x1aF\n\x05Local\x12&\n\x08priv_key\x18\x01 \x01(\x0b2\x14.google.protobuf.Any\x12\x15\n\rpriv_key_type\x18\x02 \x01(\t\x1a8\n\x06Ledger\x12.\n\x04path\x18\x01 \x01(\x0b2 .cosmos.crypto.hd.v1.BIP44Params\x1a\x07\n\x05Multi\x1a\t\n\x07OfflineB\x06\n\x04itemB1Z+github.com/cosmos/cosmos-sdk/crypto/keyring\xc8\xe1\x1e\x00b\x06proto3')
_RECORD = DESCRIPTOR.message_types_by_name['Record']
_RECORD_LOCAL = _RECORD.nested_types_by_name['Local']
_RECORD_LEDGER = _RECORD.nested_types_by_name['Ledger']
_RECORD_MULTI = _RECORD.nested_types_by_name['Multi']
_RECORD_OFFLINE = _RECORD.nested_types_by_name['Offline']
Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), {'Local': _reflection.GeneratedProtocolMessageType('Local', (_message.Message,), {'DESCRIPTOR': _RECORD_LOCAL, '__module__': 'cosmos.crypto.keyring.v1.record_pb2'}), 'Ledger': _reflection.GeneratedProtocolMessageType('Ledger', (_message.Message,), {'DESCRIPTOR': _RECORD_LEDGER, '__module__': 'cosmos.crypto.keyring.v1.record_pb2'}), 'Multi': _reflection.GeneratedProtocolMessageType('Multi', (_message.Message,), {'DESCRIPTOR': _RECORD_MULTI, '__module__': 'cosmos.crypto.keyring.v1.record_pb2'}), 'Offline': _reflection.GeneratedProtocolMessageType('Offline', (_message.Message,), {'DESCRIPTOR': _RECORD_OFFLINE, '__module__': 'cosmos.crypto.keyring.v1.record_pb2'}), 'DESCRIPTOR': _RECORD, '__module__': 'cosmos.crypto.keyring.v1.record_pb2'})
_sym_db.RegisterMessage(Record)
_sym_db.RegisterMessage(Record.Local)
_sym_db.RegisterMessage(Record.Ledger)
_sym_db.RegisterMessage(Record.Multi)
_sym_db.RegisterMessage(Record.Offline)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z+github.com/cosmos/cosmos-sdk/crypto/keyring\xc8\xe1\x1e\x00'
    _RECORD._serialized_start = 147
    _RECORD._serialized_end = 600
    _RECORD_LOCAL._serialized_start = 444
    _RECORD_LOCAL._serialized_end = 514
    _RECORD_LEDGER._serialized_start = 516
    _RECORD_LEDGER._serialized_end = 572
    _RECORD_MULTI._serialized_start = 574
    _RECORD_MULTI._serialized_end = 581
    _RECORD_OFFLINE._serialized_start = 583
    _RECORD_OFFLINE._serialized_end = 592

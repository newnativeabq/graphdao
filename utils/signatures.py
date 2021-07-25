# signatures.py

from hashlib import blake2b
import json

# Create a general signing function for demonstration
def sign_general_signature(key:str, transaction:dict):
    h = blake2b(key=bytes(key, 'ascii'), digest_size=16)
    h.update(json.dumps(transaction).encode('ascii'))
    return h.hexdigest()


# Define a general state change for adding signatures.
#  For simplicity, we'll just use an ordered list of signatures
def add_general_signature(ident, key, tx):
    signature = {ident: sign_general_signature(key, tx)}
    if 'signatures' not in tx.keys():
        tx['signatures'] = []
        
    tx['signatures'].append(signature)
    return tx
        
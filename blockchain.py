import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_records = []
        # Genesis block
        self.new_block(previous_hash="1")

    def new_block(self, previous_hash=None):
        """Create a new Block in the Blockchain"""
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'records': self.pending_records,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        # Reset pending records
        self.pending_records = []

        self.chain.append(block)
        return block

    def new_record(self, patient_id, record_type, details):
        """Adds a new patient record to the list of pending ones"""
        self.pending_records.append({
            'patient_id': patient_id,
            'record_type': record_type,
            'details': details
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """Hashes a Block"""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

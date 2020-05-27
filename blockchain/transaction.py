import rsa
import hashlib
import time
from timestamped_message import TimestampedMessage

class Transaction:
    """
    # If we have time, we will use proof of work to make it cost time to generate a transaction.
    # 1 transaction should cost about 10 seconds of computation.
    # Good side effect is that it also salts, preventing someone from spamming transactions or quickly copying someone
    # else's transaction and putting their name as the author's name. (well, that's still an issue, but it's harder)
    #
    #
    # :param author: an RSA public key
    # :param body: the unencrypted message to post
    # :param salt: the value that makes the unencrypted_hash have enough leading zeros
    # :param encrypted_hash: all other fields concatenated together, 
    """
    HASH_METHOD = 'SHA-256'
    #leading_zeros_in_valid_hash = 7

    def __init__(self, author: rsa.PublicKey, timestamped_message: TimestampedMessage, signature: bytes):
        self.author = author
        self.timestamped_message = timestamped_message
        #self.salt = salt
        self.signature = signature
    
    @classmethod
    def create_now_with_keys(pub: rsa.PublicKey, priv: rsa.PrivateKey, body: bytes):
        author = pub
        timestamp = time.time_ns()
        timestamped_message = TimestampedMessage(body, timestamp)
        signature = rsa.sign(timestamped_message.to_bytes(), priv, Transaction.HASH_METHOD)
        return Transaction(author, timestamped_message, signature)
    
    def verify(self, timestamp_of_latest_block: int) -> bool:
        try:
            rsa.verify(self.timestamped_message.to_bytes(), self.signature, self.author)
        except rsa.VerificationError:
            return False
        now = time.time_ns()
        return self.timestamped_message.timestamp_in_left_open_interval(
            timestamp_of_latest_block,
            now
        )
    
    def hash(self):
        sha_summer = hashlib.sha256()
        sha_summer.update(self.author)
        sha_summer.update(self.timestamped_message.to_bytes())
        return sha_summer.digest()
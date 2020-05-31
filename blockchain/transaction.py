import rsa
import hashlib
import time
from timestamped_message import TimestampedMessage

class Transaction:
    """
    # If we have time, we will use proof of work to make it cost time to generate a transaction.
    # 1 transaction should cost about 10 seconds of computation.
    # Good side effect is that proof of work also salts. It would make it harder to quickly copying someone
    # else's transaction and putting their name as the author's name.
    #
    #
    # :param author: an RSA public key
    # :param body: the unencrypted message to post
    # :param salt: the value that makes the unencrypted_hash have enough leading zeros
    # :param encrypted_hash: all other fields concatenated together,
    """
    HASH_METHOD = 'SHA-256'
    #leading_zeros_in_valid_hash = 7

    def __init__(self, author: rsa.PublicKey, timestamped_msg: TimestampedMessage, signature: bytes):
        self.author = author
        self.timestamped_msg = timestamped_msg
        #self.salt = salt
        self.signature = signature

    def __gt__(self, other):
        if self.timestamped_msg > other.timestamped_msg:
            return True
        return self.author > other.author

    @classmethod
    def create_with_keys(pub: rsa.PublicKey, priv: rsa.PrivateKey, body: bytes, timestamp: int):
        author = pub
        timestamped_msg = TimestampedMessage(body, timestamp)
        signature = rsa.sign(timestamped_msg.to_bytes(), priv, Transaction.HASH_METHOD)
        return Transaction(author, timestamped_msg, signature)

    def verify(self, timestamp_of_latest_block: int) -> bool:
        try:
            rsa.verify(self.timestamped_msg.to_bytes(), self.signature, self.author)
        except rsa.VerificationError:
            return False
        now = time.time_ns()
        return self.timestamped_msg.timestamp_in_left_open_interval(
            timestamp_of_latest_block,
            now
        )

    def hash(self):
        sha_summer = hashlib.sha256()
        sha_summer.update(self.author)
        sha_summer.update(self.timestamped_msg.to_bytes())
        return sha_summer.digest()

    def __lt__(self):
        return self.timestamped_msg.timestamp

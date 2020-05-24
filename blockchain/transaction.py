class Transaction:
    """
    # If we have time, we will use proof of work to make it cost time to generate a transaction.
    # 1 transaction should cost about 10 seconds of computation.
    # Good side effect is that it also salts, preventing someone from spamming transactions
    #
    # TODO add timestamp? Do we want to drop messages older than the current block or keep them in the network until they become valid?
    #
    # :param author: an RSA public key
    # :param body: the unencrypted message to post
    # :param salt: the value that makes the unencrypted_hash have enough leading zeros
    # :param encrypted_hash: all other fields concatenated together, 
    """
    #leading_zeros_in_valid_hash = 7

    def __init__(self, author: str, body: str, encrypted_hash: str):
        self.author = author
        self.body = body
        #self.salt = salt
        self.encrypted_hash = encrypted_hash
    
    def verify(self):
        # Do some math!
        pass
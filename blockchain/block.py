from datetime import datetime  # for datetime representation of timestamp
import hashlib                 # for SHA256 cryptographic hashing
import transaction

MAX_TRANSACTIONS_PER_BLOCK=15
MIN_TRANSACTIONS_PER_BLOCK=3

class Block:
    def __init__(self, timestamp=datetime.now(), blockHash=None, index=0, previousBlockHash=None, proof=100, transactions=[]):

        # initially when block is created, updates to latest transaction time
        self.timestamp = timestamp

        self.transactions = transactions # the list of the block's transactions
        self.previousBlockHash = previousBlockHash # previous block's hash
        self.index = index # index of the block in the chain
        self.proof = proof # proof of block (initially 100 for Genesis Block)

        if blockHash == None: # if no hash is provided, it is auto-generated
            self.blockHash = self.hash()
        else:
            self.blockHash = blockHash

    def hash(self): # returns the SHA256 hash of the block
        hasher = hashlib.sha256()

        # add each component of the block to the hasher
        hasher.update(str(self.timestamp).encode('utf-8'))
        hasher.update(str(self.index).encode('utf-8'))
        hasher.update(str(self.previousBlockHash).encode('utf-8'))

        for transaction in self.transactions:
            hasher.update(transaction.hash())

        return hasher.hexdigest() # return the hexidecimal representing the hash

    def addTransaction(self, transactionToAdd): # adds transaction to the block
        self.transactions.append(transactionToAdd) # append new transaction
        self.transactions.sort()

        # Update timestamp to latest transaction in the list
        self.timestamp = self.transactions[-1].timestamped_msg.timestamp
        self.blockHash = self.hash() # update hash of block

    def verify(previousTimestamp, previousProof):
        hasher = hashlib.sha256()
        hasher.update(self.proof)
        hasher.update(previousProof)

        for i in range(0, len(self.transactions)):
            if self.transactions[i].verify(self.timestamp) == False:
                print("Verification failed: unverified transaction in block")
                return False
            for j in (i+1, len(self.transactions)):
                if self.transactions[i] == self.transactions[j]:
                    print("Verification failed: identical transactions in block")
                    return False
            hasher.update(transaction[i].hash)

        print(hasher.hexdigest)
        for i in range(0, 3):
            if str(hasher.hexdigest)[i] != 0:
                print("Verification failed: PoW hash didn't produce leading 0s")
                return False

        if len(self.transactions) >  MAX_TRANSACTIONS_PER_BLOCK:
            print("Verification failed: too many transactions in block")
            return False
        if len(self.transactions) < MIN_TRANSACTIONS_PER_BLOCK:
            print("Verification failed: too few transactions in block")
            return False

        return True

    def print(self): # prints the parameters of the block line by line
        print("Index: ", self.index)
        print("Timestamp: ", self.timestamp)
        print("Hash: ", self.blockHash)
        print("Previous Blocks Hash: ", self.previousBlockHash)
        print("Proof: ", self.proof)

        for transaction in self.transactions:
            print(transaction.author)
            print(transaction.timestamped_msg)
            print(transaction.signature)

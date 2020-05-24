from datetime import datetime  # for datetime representation of timestamp
import hashlib                 # for SHA256 cryptographic hashing

class Block:
    def __init__(self, paper, timestamp=datetime.now(), blockHash=None, index=0, previousBlockHash=None):
        self.timestamp = timestamp # timestamp recording when the block was generated
        self.paper = paper # the paper representing data stored in block
        self.previousBlockHash = previousBlockHash # hash of the previous block in the chain
        self.index = index # index of the block in the chain

        if blockHash == None: # if no hash is provided for the block, it is generated
            self.blockHash = self.hash()
        else:
            self.blockHash = blockHash

    def hash(self): # returns the SHA256 hash of the block
        hasher = hashlib.sha256()

        # add each component of the block to the hasher
        hasher.update(str(self.timestamp).encode('utf-8'))
        hasher.update(self.paper.encode('utf-8'))
        hasher.update(str(self.index).encode('utf-8'))
        hasher.update(str(self.previousBlockHash).encode('utf-8'))

        return hasher.hexdigest() # return the hexidecimal representing the hash

    def print(self): # prints the parameters of the block line by line
        print("Index: ", self.index)
        print("Timestamp: ", self.timestamp)
        print("Hash: ", self.blockHash)
        print("Previous Blocks Hash: ", self.previousBlockHash)
        print("Paper: ", self.paper)

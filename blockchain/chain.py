import block
import transaction
import util
import hashlib

import json # used for loading and saving json data

class Chain:
    def __init__(self, length=0, blockchain=[]):
        self.length = length # keeps track of the length of the chain
        self.blockchain = blockchain # the actual list of blocks in the chain

        if length == 0: # if length==0, the chain is new, so add a genesis block
            genesisBlock = self.generateGenesisBlock()
            self.blockchain = [genesisBlock]

    def generateGenesisBlock(self): # creates and returns a genesis block
        return block.Block("Genesis Block")

    def add(self, blockToAdd): # adds a new block to the blockchain
        self.length += 1 # increment blockchain length variable

        # calculate the hash of last block in the chain
        blockToAdd.previousBlockHash = self.blockchain[-1].hash()

        blockToAdd.index = self.length # the index will be the new length

        # calculates the proof of the new block using PoW and the prev (last) block in the chain.
        # Update either block or chain to take in list of transactions in order to add.
        blockToAdd.proof = self.proof_of_work(self.blockchain[-1].proof, blockToAdd.transactions)

        blockToAdd.blockHash = blockToAdd.hash() # update hash of new block
        self.blockchain.append(blockToAdd) # append the block to the blockchain

    def print(self): # prints out all of the blocks in the blockchain
        for block in self.blockchain:
            block.print()
            print()

    def save(self): # saves the entire blockchain to file as JSON
        filePath = "json/blockchain.json" # construct path to output
        jsonFile = open(filePath, 'w') # open JSON output file and dump data
        json.dump(self, jsonFile, default = util.objToDict)
        jsonFile.close() # close the JSON file after dump

    def load(self): # loads the blockchain in the file from JSON
        filePath = "json/blockchain.json" # construct path to JSON file
        jsonFile = open(filePath, 'r') # read file and add to data list
        blockchain = json.load(jsonFile, object_hook = util.dictToObj)
        return blockchain

    def proof_of_work(self, prev_proof, transactions_to_be_mined): # generates a proof for a block
        proof = 0
        prev = str(prev_proof)
        for transaction in transactions_to_be_mined:
            prev = prev_proof + transaction.hash() #you had prev_string i changed it to prev_proof -Dane

        while self.hash_proof(proof, prev) is False:
            proof += 1

        return proof

    def hash_proof(self, curr, prev):
        string = str(curr) + prev
        encoded_string = string.encode('utf-8')
        hash = hashlib.sha256(encoded_string).hexdigest()
        return hash[:4] == "0000"

    def verify(self):
        for i in range(0, len(self.blockchain) - 1):
            if self.blockchain[i + 1].verify(self.blockchain[i].timestamp, self.blockchain[i].proof) == False:
                return False

        if len(self.blockchain) != self.length:
            print("Verification failed: mismatched lengths in chain")
            return False

        if len(self.blockchain[0].transactions) > 0:
            print("Verification failed: transactions in genesis block")
            return False

        return True

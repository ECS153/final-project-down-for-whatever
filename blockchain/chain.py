import block
from transaction import Transaction
import util
import hashlib
import random

import json # used for loading and saving json data

ENOUGH_ZEROS_FOR_A_PROOF_OF_WORK = "0000"
TIMESTAMP_FOR_GENESIS_BLOCK: int = 0

class Chain:
    def __init__(self, length=0, data=[]):
        self.length = length # keeps track of the length of the chain
        self.data = data # the actual list of blocks in the chain

        if length == 0: # if length==0, the chain is new, so add a genesis block
            genesisBlock = self.generateGenesisBlock()
            self.data = [genesisBlock]

    def generateGenesisBlock(self): # creates and returns a genesis block
        return block.Block(TIMESTAMP_FOR_GENESIS_BLOCK)

    def add(self, blockToAdd: block.Block): # adds a new block to the blockchain
        self.length += 1 # increment blockchain length variable

        # calculate the hash of last block in the chain
        blockToAdd.previousBlockHash = self.data[-1].hash()

        blockToAdd.index = self.length # the index will be the new length

        # calculates the proof of the new block using PoW and the prev (last) block in the chain.
        # Update either block or chain to take in list of transactions in order to add.
        #blockToAdd.proof = self.proof_of_work(self.data[-1].proof, blockToAdd.transactions)

        blockToAdd.blockHash = blockToAdd.hash() # update hash of new block
        self.data.append(blockToAdd) # append the block to the blockchain

    def print(self): # prints out all of the blocks in the blockchain
        for block in self.data:
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
        data_in_hash = bytearray(str(prev_proof).encode())
        for transaction in transactions_to_be_mined:
            data_in_hash.extend(transaction.hash()) #you had prev_string i changed it to prev_proof -Dane

        guess_at_this_blocks_proof_number = random.random()
        if self.hash_proof(guess_at_this_blocks_proof_number, data_in_hash):
            print(guess_at_this_blocks_proof_number)
            return guess_at_this_blocks_proof_number
        return None

    def hash_proof(self, guess, data: bytearray):
        data_with_guess = data.copy().extend(str(guess).encode())
        #encoded_string = string.encode('utf-8')
        print("Total data to hash: " + str(data_with_guess))
        hash = hashlib.sha256(str(data_with_guess).encode()).hexdigest()
        print(hash)
        return hash.startswith(ENOUGH_ZEROS_FOR_A_PROOF_OF_WORK)

    def verify(self):
        for i in range(0, len(self.data) - 1):
            if self.data[i + 1].verify(self.data[i].timestamp, self.data[i].proof) == False:
                return False

        if len(self.data) != self.length:
            print("Verification failed: mismatched lengths in chain")
            return False

        if len(self.data[0].transactions) > 0:
            print("Verification failed: transactions in genesis block")
            return False

        return True

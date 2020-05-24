import block
import util

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

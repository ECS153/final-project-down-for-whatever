import requests
from envelope import Envelope
import pickle
from transaction import Transaction

"""
TODO
MIN_BLOCK_SIZE = 3
MAX_BLOCK_SIZE = 10
Block.MIN_BLOCK_SIZE

"""

ADDRESS = "http://127.0.0.1:5000/"


#returns the entire blockchain
def get_blockchain():
    r = requests.get(ADDRESS + "blockchain")
    bc = pickle.loads(r.content)
    #print(r)
    #print(type(r.status_code))
    return bc

#returns list of transactions
def get_transactions():
    r = requests.get(ADDRESS + "transactions")
    trans_list = pickle.loads(r.content)
    return trans_list

# length of blockchain and number of transactions is returned in an envelope class
def check_in():
    r = requests.get(ADDRESS + "check_in")
    envelope = pickle.loads(r.content)
    return envelope

#add a block to the blockchain if failed it means that your blockchain wrong and need to update the the correct one
#not sure if we are passing the whole block chain or just the block
def add_block(blockchain):
    pickled_blockchain = pickle.dumps(blockchain)
    r = requests.post(ADDRESS + "blockchain", data = pickled_blockchain)
    response = r.content.decode()
    if(response == "success"):
        return response
    else:
        #failed to write to blockchain need to get new block and current transactions
        return response

def add_transaction(transaction):
    pickled_transaction = pickle.dumps(transaction)
    r = requests.post(ADDRESS + "transactions", data = pickled_transaction)
    response = r.content.decode()

    if(response == "success"):
        return "success"
    else:
        return "failed"

##################################################################################################################
def main():
     #on start up pull transaction and block
     client_running = True
     do = 1
     chain = get_blockchain()
     transactions = get_transactions()

     while client_running:
        #python does not have a dow hile loop I made my own
        while True:
            #working on getting a transaction
            #or
            #working on mining 
            #NOT really sure how it is supose to work
            do = do + 1
            if (do > 50):
                break
        #do a check in 
        check = check_in()
        if check.blockchain > chain.length():
            chain = get_blockchain()
            #check if any of the transaction i was working on got changed???
            transactions = get_transactions()
        #transactions just got updated
        else:
            #check if any of the transaction i was working on got changed???
            transactions = get_transactions()

###################################################################################################

# temp code
def working_on_transaction():
    #doing somthing to gen a transaction
    
    #transaction created.... NOw need to write to server
    t = None #place holder need to change later 
    results = add_transaction(t)

    if (results == "failed"):
        #get new list of transactions
        transactions = get_transactions()
        #check to see if you can start mining a block?
    
    else: #it was a success
        #do what ever else you need to do 
        #check to see if you can start mining a block?
        continue

def working_on_bock():
    #doing somthing to mine a block
    #block as been mined
    
    chain = None #place holder
    block = None #place holder
    chain.add(block)

    results = add_block(chain)

    #to slow there are your chain is out of date
    if (results == "failed"):
        chain = get_blockchain()
        transaction = get_transactions()
        #now starting mining again 
        #or
        #start working on transactions
    
    else:#your chain was acepted
        transaction = get_transactions()
        #now starting mining again 
        #or
        #start working on transactions
        


        
         



"""
print(get_blockchain())
print(get_transactions())
check_in().e_print()

print(add_block("first block"))
print(get_blockchain())
"""

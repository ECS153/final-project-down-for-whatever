import requests
from envelope import Envelope
import pickle
import time
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
        while len(transactions) < 3:
            time.sleep(5)
        if (len(transactions) >= 3) and (len(transactions) <= 15):
            proof_of_work_trans = transactions
        else:#transactions are greater than 15
            proof_of_work_trans = transactions[:15]
        
        #python does not have a dow hile loop I made my own
        #this is the mining process
        while True:
            #proof_of_work(self, prev_proof, transactions_to_be_mined)
            prev_proof = chain.blockchain[-1].proof
            results = chain.proof_of_work(prev_proof, proof_of_work_trans)

            if(results != None):
                #generate block
                #timestamp=datetime.now(), blockHash=None, index=0, previousBlockHash=None, proof=100, transactions=[]
                new_block = Block() #figure out how to call client
                new_block.proof = results
                new_block.transactions = proof_of_work_trans
                new_block.timestamp = proof_of_work_trans[-1].timestamped_msg.timestamp

                chain.add(new_block)
                results = add_block(chain)
                if(results == "success"):
                    do = 51 #break do while loop 
                    transactions = get_transactions()
                else:
                    do = 51 #break do while loop and will go to check_in section to get the new chain and transactions

                #check to see if push was succesful 
                break

            do = do + 1
            if (do > 50):
                break
        
        #do a check in 
        check = check_in()
        if check.blockchain > chain.length():
            chain = get_blockchain()
            transactions = get_transactions()
        #transactions just got updated
        elif len(transactions) != check.transactions:
            transactions = get_transactions()
        else: 
            continue
        do = 1 #reset the do while loop

###################################################################################################



"""
print(get_blockchain())
print(get_transactions())
check_in().e_print()

print(add_block("first block"))
print(get_blockchain())
"""

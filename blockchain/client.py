import requests
from envelope import Envelope
import pickle

ADDRESS = "http://127.0.0.1:5000/"
#NEED to add checks for 200 and i think 500

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
def add_block(block):
    pickled_block = pickle.dumps(block)
    r = requests.post(ADDRESS + "blockchain", data = pickled_block)
    response = r.content.decode()
    if(response == "success"):
        return response
    else:
        #failed to write to blockchain need to get new block and current transactions
        return response

#NEED to ad function for transactions

print(get_blockchain())
print(get_transactions())
check_in().e_print()

print(add_block("first block"))
print(get_blockchain())

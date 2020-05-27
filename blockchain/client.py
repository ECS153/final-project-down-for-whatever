import requests
from envelope import Envelope
import pickle
"""
print(pickle.format_version)
data = pickle.dumps([1,2])
print(data)
print(pickle.loads(data))

r = requests.get("http://127.0.0.1:5000/")
print("HOME")
print(r)
print(type(r.status_code))
print(r.content)
print(r.content.decode())
print("---------------")
r = requests.get("http://127.0.0.1:5000/Get_BlockChain")
print("Get BlockChain")
print(r)
print(r.content)
print(r.content.decode())
print("---------------")

r = requests.get("http://127.0.0.1:5000/Get_Transactions")
print("Get Transactions")
print(r)
print(r.content)
data = pickle.loads(r.content)
print(data)
print(data[0])
print(data[1])
print("---------------")

r = requests.get("http://127.0.0.1:5000/check_in")
print("check in")
print(r)
print(r.content)
data = pickle.loads(r.content)
data.e_print()
print("hello")
#data.blockchain = pickle.loads(data.blockchain)
#data.transactions = pickle.loads(data.transactions)
print(data.blockchain)
print(data.transactions)
print("---------------")



r = requests.post("http://127.0.0.1:5000/Set_BlockChain", data = "changed BC")
print(r)
print(r.content.decode())
"""

#NEED to add checks for 200 and i think 500

#returns the entire blockchain
def get_blockchain():
    r = requests.get("http://127.0.0.1:5000/Get_BlockChain")
    bc = pickle.loads(r.content)
    #print(r)
    #print(type(r.status_code))
    return bc

#returns list of transactions
def get_transactions():
    r = requests.get("http://127.0.0.1:5000/Get_Transactions")
    trans_list = pickle.loads(r.content)
    return trans_list

# length of blockchain and number of transactions is returned in an envelope class
def check_in():
    r = requests.get("http://127.0.0.1:5000/check_in")
    envelope = pickle.loads(r.content)
    return envelope

#add a block to the blockchain if failed it means that your blockchain wrong and need to update the the correct one
#not sure if we are passing the whole block chain or just the block
def add_block(block):
    pickled_block = pickle.dumps(block)
    r = requests.post("http://127.0.0.1:5000/Set_BlockChain", data = pickled_block)
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

#r = requests.post("http://127.0.0.1:5000/Set_BlockChain", data = pickle.dumps("changed BC"))
#print(r)
#print(r.content.decode())

"""
I keep getting "local variable 'blockchain' reference before assignment"
yet i can access the blockchain in the other 3 functions 
add_block("first block")
"""


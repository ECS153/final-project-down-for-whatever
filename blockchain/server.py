from flask import Flask
from flask import request
from envelope import Envelope
import pickle
from transaction import Transaction
from chain import Chain
from block import Block
import bisect

"""
TODO:
ADD threads 
not sure how we handle the origin block ???
do i need to check if transaction already exists????
"""

blockchain = Chain() ## on start up create origin block with block static methond With @staticmethod of Block class
transactions =[] #sorted oldest to youngest... oldest has a smaller time stamp 

app = Flask(__name__)

@app.route("/") ##get everything????
def home():
    return "Hello! this is the main page"

@app.route("/blockchain", methods=["GET","POST"])
def get_BlockChain():
    global blockchain
    global transactions
    if request.method == 'GET':
        return pickle.dumps(blockchain)

    if request.method == 'POST':
        new_bc = request.data
        new_bc = pickle.loads(new_bc)

        if blockchain == None: #origin block ???
            blockchain = new_bc
            return "success"

        elif (new_bc.length > blockchain.length):
            blockchain = new_bc
            #Now removing transactions that have a timestamp older than the youngest block in the chain
            time_stamp =  blockchain.blockchain[-1].timestamp            
            for idx, val in enumerate(transactions):
                if val.timestamped_msg.timestamp <= time_stamp:
                    continue
                elif (val.timestamped_msg.timestamp == time_stamp) and (idx == len(transactions)-1):
                    transactions = []
                else:
                    neg_num = idx - len(transactions) #negative number 
                    transactions = transactions[neg_num:] #slicing the list in two and keeping the second half 
                    break
            return "success"

        else:
            return "failed"

@app.route("/transactions", methods=["GET", "POST"])
def get_Transactions():
    global blockchain
    global transactions
    if request.method == 'GET':

        return pickle.dumps(transactions)
    
    if request.method == 'POST':
        new_transaction = request.data
        new_transaction = pickle.loads(new_transaction)
        
        time_stamp = blockchain.blockchain[-1].timestamp
        verified_results = new_transaction.verify(time_stamp) #true or false

        if (verified_results):
            if(len(transactions) == 0):
                transactions.append(new_transaction)
            else:
                #insert new_transaction into a sorted list
                #https://stackoverflow.com/questions/26840413/insert-a-custom-object-in-a-sorted-list
                bisect.insort_right(transactions, new_transaction) #(IF somthing goes wrong)this suposed to use the def__gt__ in transaction.py and timestamped_message.py if
            return "success"
        else:
            return "failed" 

@app.route("/check_in", methods=["GET"])
def check_in(): #gives length of current block chain and how many current transactions 
    envelope = Envelope(len(blockchain), len(transactions))
    return pickle.dumps(envelope)

if __name__ == "__main__":
    app.run(debug=True)

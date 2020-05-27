from flask import Flask
from flask import request
from envelope import Envelope
import pickle
from transaction import Transaction

"""
TODO:
NOTE right now the blocks timestamp when created is when it is created not the youngest
transaction
TODO: order the list
ASK the first ever block 
"""

blockchain = "test"
transactions =["T1","T2"]

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
        if blockchain == None:
            blockchain = new_bc
            #transactions.clear()# TODO NEED TO REMOVE THE TRANSACTIONS IN THE LIST THAT WERE USED THE CREATE THIS BLOCK
            return "success"
        elif (len(new_bc) > len(blockchain)):
            blockchain = new_bc
            #transactions.clear()# TODO NEED TO REMOVE THE TRANSACTIONS IN THE LIST THAT WERE USED THE CREATE THIS BLOCK
            return "success"
        else:
            return "failed"

@app.route("/transactions", methods=["GET", "POST"])
def get_Transactions():
    global blockchain
    global transactions
    if request.method == 'GET':
        #print(pickle.dump(transactions))
        return pickle.dumps(transactions)
    if request.method == 'POST':
        new_transaction = request.data
        new_transaction = pickle.loads(new_transaction)
        
        #TODO
        #I need the youngest time stamp of the most recent block
        #time_stamp = block_time
        verified_results = new_transaction.verify(1) #true or false

        if (verified_results):
            #add transaction to ordered list of transactions
            #TODO create and sorted list of transactions by timesstamp
            return "success"
        else:
            return "failed"
        #get data
        # verify data
        # return success or fail
        # if fail return current Transactions and ?blockChain? 
        pass

@app.route("/check_in", methods=["GET"])
def check_in(): #gives length of current block chain and how many current transactions 
    envelope = Envelope(len(blockchain), len(transactions))
    return pickle.dumps(envelope)

if __name__ == "__main__":
    app.run(debug=True)

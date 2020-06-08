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
def g_p_blockchain():
    global blockchain
    global transactions
    if request.method == 'GET':
        return pickle.dumps(blockchain)

    if request.method == 'POST':
        new_bc = request.data
        new_bc = pickle.loads(new_bc)

        #does blockchain.verify go here?????
        if (new_bc.length > blockchain.length and new_bc.verify()): # my_list.filter { item -> item.timestamp < some_other_constant }
            blockchain = new_bc
            #Now removing transactions that have a timestamp older than the youngest block in the chain

            timestamp_of_last_block = blockchain.data[-1].timestamp


            trans_temp = []
            for val in transactions:
                if val.timestamped_msg.timestamp > timestamp_of_last_block:
                    trans_temp.append(val)
            transactions = trans_temp

            return "success"

        else:
            return "failed"

@app.route("/transactions", methods=["GET", "POST"])
def g_p_transactions():
    global blockchain
    global transactions
    if request.method == 'GET':

        return pickle.dumps(transactions)

    if request.method == 'POST':
        new_transaction = request.data
        new_transaction = pickle.loads(new_transaction)

        time_stamp = blockchain.data[-1].timestamp
        transaction_is_valid = new_transaction.verify(time_stamp) #true or false

        if transaction_is_valid:
            #insert new_transaction into a sorted list
            #https://stackoverflow.com/questions/26840413/insert-a-custom-object-in-a-sorted-list
            bisect.insort_right(transactions, new_transaction) #(IF somthing goes wrong)this suposed to use the def__gt__ in transaction.py and timestamped_message.py if
            #print for check
            for i in transactions:
                print(str(i.author.n)[-10:] + " " + str(i.timestamped_msg.timestamp))

            return "success"
        else:
            return "failed"

@app.route("/check_in", methods=["GET"])
def check_in(): #gives length of current block chain and how many current transactions
    envelope = Envelope(blockchain.length, len(transactions))
    return pickle.dumps(envelope)

if __name__ == "__main__":
    app.run(debug=True)

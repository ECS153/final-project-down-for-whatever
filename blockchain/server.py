from flask import Flask
from flask import request
from envelope import Envelope
import pickle

blockchain = "test"
transactions =["T1","T2"]

app = Flask(__name__)

@app.route("/") ##get everything????
def home():
    return "Hello! this is the main page"

@app.route("/Get_BlockChain", methods=["GET"])
def get_BlockChain():
    #pickle is going to be used in here need to change later 
    return pickle.dumps(blockchain)

@app.route("/Set_BlockChain", methods=["POST"])
def set_BlockChain():
    #pickle is going to be used in here need to change later 
    new_bc = request.data
    new_bc = pickle.loads(new_bc)
    blockchain = new_bc #this block chain is not global???
    print(blockchain)
    return 'hi'
    '''
    new_bc = request.data
    new_bc = pickle.loads(new_bc)
    if blockchain == None:
        blockchain = new_bc
        transactions.clear()#clear transactions?
        return "success"
    elif (len(new_bc) > len(blockchain)):
        blockchain = new_bc
        transactions.clear()#clear transactions?
        return "success"
    else:
        return "failed"
    '''


@app.route("/Get_Transactions", methods=["GET"])
def get_Transactions():
    #print(pickle.dump(transactions))
    return pickle.dumps(transactions)

@app.route("/Add_Transactions", methods=["POST"])
def add_Transactions():
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

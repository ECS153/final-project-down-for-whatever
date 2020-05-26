class Envelope:
    def __init__(self, blockchain, transactions):
        self.blockchain = blockchain
        self.transactions = transactions
    
    def e_print(self):
        print(self.blockchain)
        print(self.transactions)

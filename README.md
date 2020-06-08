## Running the Code

Step 1) Start Server: in a terminal enter this line "python server.py"

Step 2) Adding transactions: in a seperate terminal eather the following two line or use both to add one transaction. the differnet lines
reperesent different authors posting transactions you need at least 3 to start the mining process

"python publish.py --pub public.pem --priv key.pem --data message.txt"

"python publish.py --pub public2.pem --priv key2.pem --data message.txt"

These lines can be call in just one terminal

Step 3) Clients: each termerninal you open for clients is an additional miner the line is "python client.py"

Step 4) While Client is running you can keep adding transactions to the server else the client will mine all transactions and then just
keep sleeping until more transactions com in

## Changing the speed

If you want to reduce or add more time for when the client checks into the server go to the client.py file and change the max_loop number

If you want the miners to take longer or shorter time to mine a block add or shrink the amount of zeros in the block.py file the value
you are changing is ENOUGH_ZEROS_FOR_A_PROOF_OF_WORK. with 4 zeros 1 miner is able to get a block with in seconds 5 zeros takes about
30 to 50 seconds and so on

## Mapping Concepts to Code

* block.py defines an object class representing the blocks in the blockchain. It defines the creation, hashing, and verification of blocks. You can also ass transactions to blocks using block.addTransaction(), print blocks for debugging using block.print(), generate a proof of work for a block using block.proof_of_work(), and hash a proof for a block using block.hash_proof().

* chain.py defines an a object class representing the actual chain of blocks that defines the blockchain. It defines creation, saving, loading, printing, and verification of the blockchain. You can also generate a genesis block, or the first block of a chain using chain.generateGenesisBlock(), and add blocks to the chain using chain.add().

## General Structure of the Code

The Chain consists of a python list of Blocks. Blocks contain a python list of Transactions. Transactions contain timestamped_msgs and their author. The network is composed of servers and clients. 

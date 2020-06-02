## Running the Code

Step 1) Start Server: in a terminal enter this line "python server.py"

Step 2) Adding transactions: in a seperate terminal eather the following two line or use both to add one transaction. the differnet lines
reperesent different authors posting transactions you need at least 3 to start the mining process
"python publish.py --pub public.pem --priv key.pem --data message.txt"
"python publish.py --pub public2.pem --priv key2.pem --data message.txt"

Step 3) Clients: each termerninal you open for clients is an additional miner the line is "python client.py"

## Changing the speed

if you want to reduce or add more time for when the client checks into the server go to the client.py file and change the max_loop number

if you want the miners to take longer or shorter time to mine a block add or shrink the amount of zeros in the block.py file the value 
you are changing is ENOUGH_ZEROS_FOR_A_PROOF_OF_WORK. with 4 zeros 1 miner is able to get a block with in seconds 5 zeros takes about 
30 to 50 seconds and so on 


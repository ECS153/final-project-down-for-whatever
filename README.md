## Running the Code

Step 1) Start Server: in a terminal enter this line `python server.py`

Step 2) Adding transactions: in a separate terminal use either of the following two lines or both to add transactions. The different lines
represent different authors posting transactions. You need at least 3 to start the mining process:

`python publish.py --pub sample_rsa_keys/public.pem --priv sample_rsa_keys/key.pem --data message.txt`

`python publish.py --pub sample_rsa_keys/public2.pem --priv sample_rsa_keys/key2.pem --data message.txt`

These lines can be called in just one terminal.

Step 3) Clients: each terminal you open for clients is an additional miner. Launch a client with: `python client.py`

Step 4) While Client is running you can keep adding transactions to the server else the client will mine all transactions and then just
keep sleeping until more transactions come in

## Changing the speed

If you want to reduce or add more time for when the client checks into the server go to the client.py file and change the max_loop number

If you want the miners to take longer or shorter time to mine a block add or shrink the amount of zeros in the block.py file the value
you are changing is ENOUGH_ZEROS_FOR_A_PROOF_OF_WORK. with 4 zeros 1 miner is able to get a block with in seconds 5 zeros takes about
30 to 50 seconds and so on

## Mapping Concepts to Code and General Structure

The `Chain` consists of a Python list of `Block`s.

A `Block` contains a Python list of `Transaction`s.

A `Transaction` contains one `TimestampedMessage` which forms the content/"body" of the `Transaction`.

The network is composed of one `Server`, which stores the authoritative version of the `Chain`, and zero or more `Client`s mining `Transaction`s into `Block`s.

A single `Transaction` can be submitted to the `Server` by running the publish.py script. The `Server` then passes the new `Transaction` to all clients.

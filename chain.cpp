#include <iostream>
#include <fstream>

#include "chain.h"
#include "openssl/sha.h"

Chain::Chain() { // Constructor
    transactions = 0;

}

Chain::~Chain() { // Destructor
    std::cout << "Destructor!" << "\n";
}

Chain loadChain() { // load chain if existing, else construct new chain
    std::ifstream blockchainFile("blockchain"); // file storing blockchain
    std::streampos blockchainFileSize = blockchainFile.tellg(); // size of file

    if(blockchainFileSize == 0) { // if file is empty
        Chain newChain;           // generate a new blockchain
        return newChain;          // and return it
    }

    Chain blockchain; // blockchain object to load to from file
    blockchainFile.open("blockchainFile"); // open blockchain file
    blockchainFile >> blockchain.transactions; // read attributes from file
    return blockchain; // return loaded blockchain
}

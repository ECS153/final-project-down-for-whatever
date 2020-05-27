#include <set>
#include <ctime>

#include "transaction.h"

class Block {
    public:
        // std::set<Transaction> transactions;
        std::size_t previousBlockHash;
        std::size_t currentBlockHash;
        std::size_t proofOfWork; // number that, when concatenated to the rest of the class members, can be hashed to get a number with X leading 0's.
        int index;
        time_t timestamp;
        std::string paper;

        Block(std::string data, int indx);
        ~Block();
};

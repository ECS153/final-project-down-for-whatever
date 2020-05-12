#include <set>
#include "transaction.h"

namespace DFW {

public class Block {
    public:
        std::set<Transaction> transactions;
        std::size_t previousBlockHash;
        std::size_t proofOfWork; // number that, when concatenated to the rest of the class members, can be hashed to get a number with X leading 0's.
        Block(void);
        ~Block();

}

}

#include "block.h"
#include <vector>

class Chain {
    public:
        int transactions;
        int length;
        std::vector<Block> blockchain;

        Chain(void);
        ~Chain();
        bool append(Block b); // return success of append
        bool validate(void); // validates all blocks in the chain
        std::size_t size(void);
        Block latest(void); // return latest block
};

Chain loadChain();

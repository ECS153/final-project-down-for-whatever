#include <string>
#include <list>
#include <set>
// #include "peer.h"
#include "chain.h"

// Hard part. We will need to wait on a given socket, mining when not processing
// messages from nodes.
class Node {
    public:
        std::list<Transaction> uncommittedTransactions;
        Node(std::string id, Chain chain, const std::set<Peer> peers);
        void listen(void);
};

#include <string>

class Transaction { // transaction's public key is author's name. Decrypt the message with it to verify it is what the author says it is.
    // need a way to verify message is legit (could just be random numbers).
    // perhaps the decrypted message must start with the public key?
    public:
        std::string sender;
        std::size_t timestamp; // for canonical ordering of transactions
        std::string encrypted_message; // TODO do we want to store decrypted version too?
        Transaction(std::string sender, std::string encrypted_message); // TODO probably want constructor (or static method) that does the encrypting
        bool verify(void);
};

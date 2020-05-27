#include "block.h"

Block::Block(std::string data, int indx) { // Constructor

    timestamp = time(NULL);
    index = indx;

}

Block::~Block() { // Destructor
}

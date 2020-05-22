#include <iostream>
#include <termbox> // must install system library... or "git clone" and change this to local import
#include "CLI11.hpp" // https://github.com/CLIUtils/CLI11
#include "block.h"
#include "node.h"
using namespace std;

namespace DFW {

int main(int argc, char** argv)
{
    CLI::App app{"Blockchain for research projects"};
    // TODO add command-line options

    CLI11_PARSE(app, argc, argv);

    // if no help flag:

    tb_init();

    // load chain from disk
    // verify chain
    // load peers from disk
    // broadcast that this node is now a peer
    while (true) {
        // listen for transactions
        // mine current queue of transactions into block
    }

    tb_shutdown();
}

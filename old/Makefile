CFLAGS := -Wall -Werror
CC := g++

blockchain.x: main.cpp chain.o block.o
	$(CC) $^ $(CFLAGS) -o $@

chain.o: chain.cpp chain.h block.h
	$(CC) $(CFLAGS) -c $<

block.o: block.cpp block.h
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f *.o *.x

.PHONY: clean

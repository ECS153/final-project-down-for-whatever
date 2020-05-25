import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())#Gets your local IP address (IPv4)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

#AF_INET is IPv4
#socket.AF_INET is the type of socket you will be accepting
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#this function will be running for each client 
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        #if we are sending a REALLY big msg we may need a bigger HEADER
        msg_length = conn.recv(HEADER).decode(FORMAT) # first msge tells us how long the msg is
        if msg_length: #when you first connect it is blank WE are checking if we actually got a msg
            msg_length = int(msg_length) #convert it to an int
            msg = conn.recv(msg_length).decode(FORMAT) #and then take in the whole msg
            if msg == DISCONNECT_MESSAGE: #if client disconnects connection 
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
    
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    #server.listen(5)
    while True:
        #wating for a new conection to occur
        #when it dose occur we will store the addr and socket obect (conn)
        #that will allow us to send information back
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print("ACTIVE CONNECTIONS " + str(threading.activeCount() - 1))

print("server is starting.....")
start()

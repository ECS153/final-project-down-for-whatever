import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client. connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    mesg_length = len(message)
    send_length = str(mesg_length).encode(FORMAT)
    '''
    if(send_length > HEADER):
        print("ERROR message from client is to big need to fix HEADER in client.py and server.py")
    else:
        send_length += b' ' * (HEADER - len(send_length)) #adding padding
        client.send(send_length)
        client.send(message)
    '''
    send_length += b' ' * (HEADER - len(send_length)) #adding padding
    client.send(send_length)
    client.send(message)

    #MORE WORK TO DO FOLLOW SAME FORMAT WITH IN SERVER.py
    print(client.recv(2048).decode(FORMAT))

send("Hello World")
send("hello buddy")
send("My Man!")
input()
send(DISCONNECT_MESSAGE)
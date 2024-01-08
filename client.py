import socket


HEADER = 128
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT!"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(msg)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' '* (HEADER - len(send_len))

    client.send(send_len)
    client.send(message)


send("Hello")
send(DISCONNECT_MESSAGE)
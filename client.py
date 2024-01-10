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


send("files/1.txt")
send("files/2.txt")
send("files/3.txt")
send("files/4.txt")
send("files/5.txt")


send("files/6.txt")
send("files/7.txt")
send("files/8.txt")
send("files/9.txt")
send("files/10.txt")

send(DISCONNECT_MESSAGE)
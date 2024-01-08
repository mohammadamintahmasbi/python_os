import socket
import time
import threading

HEADER = 128
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT!"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handel_request(conn, addr):
    print(f"[CONNECTION] {addr} connected!")
    connected = True
    while(connected):
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
    conn.close()

def start():
    server.listen()
    print("[LISTENING] server is listening now...")
    # print(SERVER)
    while True:
        conn, addr = server.accept()
        theard = threading.Thread(target=handel_request, args=(conn, addr))
        theard.start()
        print("[ACTIVE CONNECTION]")



print("[START] server is started...")
start()
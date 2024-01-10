import socket
import time
import threading
import multiprocessing
from worker import hash_to_md5

HEADER = 128
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

Addresses = []
processes = []

# multiprocessing.set_start_method('spawn')
def create_workers(addresses: [str]):
    finish = False
    i = 0
    while not finish:
        process_0 = multiprocessing.Process(target=hash_to_md5, args=[addresses[i:i+5]])
        process_0.start()
        processes.append(process_0)
        i+=5
        if i == len(addresses):
            finish = True


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
                break

            print(f"[{addr}] {msg}")
            
            if len(Addresses) >= 5:
                print("[ERROR] You have illegal number of address")
                connected = False
                # break
            print(msg)
            Addresses.append(msg)
    # print(Addresses[0])
    create_workers(Addresses)
    for p in processes:
        print("Reach to this part")
        p.join()

    # conn.close()


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
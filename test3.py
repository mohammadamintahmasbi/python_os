import os
import socket
import threading
from queue import Queue

HEADER = 128
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT!"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
lock = threading.Lock()

files = []
f = []

def get_addresses():
    directory = "files"
    files_and_dirs = os.listdir(directory)
    files = [f for f in files_and_dirs if os.path.isfile(os.path.join(directory, f))]
    
    for file in files:
        f.append(os.path.join(directory, file))
    
    return f

def send(q):
    while True:
        file = q.get()
        if file == DISCONNECT_MESSAGE:
            break
        with lock:
            message = file.encode(FORMAT)
            msg_len = len(file)
            send_len = str(msg_len).encode(FORMAT)
            send_len += b' '* (HEADER - len(send_len))
            client.send(send_len)
            client.send(message)
            print(message)
        q.task_done()

q = Queue()

files = get_addresses()
for file in files:
    q.put(file)

for i in range(5):
    t = threading.Thread(target=send, args=(q,))
    t.start()

q.put(DISCONNECT_MESSAGE)
q.join()

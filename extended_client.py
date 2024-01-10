import os
import socket
import threading


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

def get_addresses():
    directory = "files"

    files_and_dirs = os.listdir(directory)

    print("path:" + str(os.listdir(directory)))
    
    
    files = [f for f in files_and_dirs if os.path.isfile(os.path.join(directory, f))]
   
    for file in files:
        print(os.path.join(directory, file))
        print(len(files))


def send(msg):
    with lock:
        message = msg.encode(FORMAT)
        msg_len = len(msg)
        send_len = str(msg_len).encode(FORMAT)
        send_len += b' '* (HEADER - len(send_len))

        client.send(send_len)
        client.send(message)
        
def threading_send(file):
    thread = threading.Thread(target=send, args=[file])
    thread.start()


file_finder = threading.Thread(target=get_addresses)

for file in files:
    threading_send(file)

threading_send(DISCONNECT_MESSAGE)
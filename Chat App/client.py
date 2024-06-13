# client.py
import socket
import threading

def receive_message(s):
    while True:
        data = s.recv(1024)
        if not data:
            break
        print('Received :', repr(data))

def send_message(s):
    while True:
        message = input()
        s.sendall(message.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 12345))

threading.Thread(target=receive_message, args=(s,)).start()
threading.Thread(target=send_message, args=(s,)).start()
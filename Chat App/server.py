# server.py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(2)

conn1, addr1 = server.accept()
print('Connected by', addr1)

conn2, addr2 = server.accept()
print('Connected by', addr2)

while True:
    data = conn1.recv(1024)
    if not data:
        break
    conn2.sendall(data)

    data = conn2.recv(1024)
    if not data:
        break
    conn1.sendall(data)

conn1.close()
conn2.close()
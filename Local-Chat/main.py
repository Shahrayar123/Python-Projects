import socket
import sys
import os
import time
from art import *
import random
import string
import hashlib
import threading
from _thread import *

import multiprocessing
import tkinter as tk
import time


characters = string.ascii_letters + string.digits





class Server():
    
    def __init__(self, ip_adr, port, key, nickname):
        
        self.ip_adr = ip_adr
        self.port = port
        self.key = key
        self.nickname = nickname
        self.socket = None
        self.socketConnection = None
        self.connectionAddress = None
        self.clients = []
        self.nicknames = []


    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.broadcast(f'{nickname} has left the chat room!'.encode('utf-8'))
                self.nicknames.remove(nickname)
                break


   

    def broadcast(self, message):
        for client in self.clients:
            print(message)
            client.send(message)

    def runServer(self):

        self.socket = socket.socket()
        self.socket.bind((self.ip_adr, self.port))
        self.socket.listen()
        print(f'Server is running and listening on port {self.port} by private key {self.key}...')
        while True:
            print(self.clients, self.nickname)
            self.socketConnection, self.connectionAddress = self.socket.accept()
            print(f'connection is established with {str(self.connectionAddress)}')

            receivedMsg = self.socketConnection.recv(128)

            receivedString = receivedMsg.decode('utf-8')

            nickname = receivedString[-16::]
            nickname.replace("\x00", "")

            if nickname not in self.nicknames:
                self.nicknames.append(nickname)
            
            if self.socketConnection not in self.clients:
                self.clients.append(self.socketConnection)

            nickname_for_send = nickname.replace("\x00", "")
            self.broadcast(f'\xaa{nickname_for_send} has connected to chat'.encode('utf-8'))
            thread = threading.Thread(target=self.handle_client, args=(self.socketConnection,))
            thread.start()

        

    def closeConnection(self):
        self.socketConnection.close()
        self.socket.close()
        self.connectionAddress = None



class Client():

    def __init__(self, ip_adr, port, key, nickname, queue, queue_send):
        self.ip_adr = ip_adr
        self.port = port 
        self.key = key
        self.nickname = nickname
        self.socket = None
        self.root = None
        self.label1 = None
        self.button1 = None
        self.scrollbar = None
        self.text_output = None
        self.full_recieved_msg = ''
        self.queue = queue
        self.queue_send = queue_send
        #TODO: queue v __init__ (param) a dalshe hz


    def connect_to_server(self):
        self.socket = socket.socket()
        count_of_connection = 0
        while True:
            try:
                self.socket.connect((self.ip_adr, self.port))
                break
            except socket.error as error:
                print("Error while connecting to server")
                print(error)
                count_of_connection += 1
                if count_of_connection > 4:
                    print("You try it for 5+ times, we gonna close your connection")
                    self.socket.close()
                    return False
                time.sleep(1)
        list_for_join = []
        nickname_enc = self.nickname.encode('utf-8')
        need_bytes_of_zero = 16 - len(nickname_enc)

        list_for_join.append(b'\x00'*need_bytes_of_zero)
        list_for_join.append(nickname_enc)

        messageToSend = b''.join(list_for_join)

        try:
            self.socket.send(messageToSend)
        except socket.error as error:
            print("Sorry, we can't send your message")
            print(error)
        return True
    
    def sendMsg(self):
        while True:
            if not self.queue_send.empty():
                keyboardInput = self.queue_send.get()
                list_for_join = []

                message_enc = keyboardInput.encode("utf-8")

                nickname_enc = self.nickname.encode('utf-8')
                need_bytes_of_zero = 16 - len(nickname_enc)

                list_for_join.append(message_enc)
                list_for_join.append(b'\x00'*need_bytes_of_zero)
                list_for_join.append(nickname_enc)

                messageToSend = b''.join(list_for_join)

                try:
                    self.socket.send(messageToSend)
                except socket.error as error:
                    print("Sorry, we can't send your message")
                    print(error)

    def recieveMsg(self):

        while True:
            receivedMsg = self.socket.recv(128)
            
            if receivedMsg[0] == 194:
                receivedString = receivedMsg.decode("utf-8")

            else:
                receivedString = receivedMsg.decode("utf-8")

                nickname = receivedString[-16::]
                nickname.replace("\x00", "")


                if nickname.replace("\x00", "") != self.nickname.replace("\x00", ""):
                    message = receivedString[0:-16]
                    self.full_recieved_msg = f"{nickname}: {message}"
                    self.queue.put(self.full_recieved_msg)

    


    def add_lines(self):

        try:
           
            if not self.queue.empty():
                recieved_msg_from_queue = self.queue.get()
                kastil = "".join(map(str, list(recieved_msg_from_queue))).replace('\x00', '')

                self.text_output.insert("end", kastil + "\n") 
                self.text_output.see("end")  # Scroll to the end of the Text widget
            self.root.after(100, self.add_lines)  # Schedule the next update
        except Exception as ex:
            print(ex)
    
    def send_msg_button(self):
        msg_for_send = self.entry1.get()
        self.queue.put(f'{self.nickname} : {msg_for_send}')
        self.queue_send.put(msg_for_send)
        self.entry1.delete(0, 'end')


    def run_gui(self):
        self.root= tk.Tk()

        self.label1 = tk.Label(self.root, text='Anon chat')
        self.label1.config(font=('helvetica', 14))
        self.label1.place(x=220, y=15)

        self.entry1 = tk.Entry(self.root) 
        self.entry1.place(x=15, y=400, width=450, height=50)

        self.button1 = tk.Button(self.root, text='send', command=self.send_msg_button)
        self.button1.place(x=400, y=450)



        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side="right", fill="none", expand=True)
        self.text_output = tk.Text(self.root, yscrollcommand=self.scrollbar.set)
        self.text_output.place(x=15, y=50, width=450, height=300)
        self.scrollbar.config(command=self.text_output.yview)

        self.root.minsize(500, 500)
        self.root.maxsize(500, 500)


        self.root.after(0, self.add_lines)
        self.root.mainloop()


    def runClient(self):
        
        
        guiThread = multiprocessing.Process(target=self.run_gui)
        sendThread = threading.Thread(target=self.sendMsg)
        receiveThread = threading.Thread(target=self.recieveMsg)

        guiThread.start()
        sendThread.start()
        receiveThread.start()
        

        sendThread.join()
        receiveThread.join()

        
        
        

    def closeConnection(self):
        self.socket.close()



class Start():
    def main_start():


        #### read open ports ####
        list_of_ports = []

        for i in range(65536):
            s = socket.socket()
            s.settimeout(1)
            try:
                s.connect(('127.0.0.1', i))
            except socket.error:
                pass
            else:
                s.close
                list_of_ports.append(i)
        #########################

        os.system("clear")
        tprint("Anon    chat")




        command = str(input("Are you [S]erver or [C]lient?\n"))

        if command == "S":
            key_is_correct = False
            ip_adr = "localhost"
            nickname = None
            while not key_is_correct:
                os.system("clear")
                tprint("Anon    chat")
                private_key = "?" + ''.join(random.choice(characters) for i in range(6))
                print(f"checking key {private_key} for unic.")
                time.sleep(0.75)
                os.system("clear")
                tprint("Anon    chat")
                print(f"checking key {private_key} for unic..")
                time.sleep(0.75)
                os.system("clear")
                tprint("Anon    chat")
                print(f"checking key {private_key} for unic...")
                time.sleep(0.75)
                
                hash_object = hashlib.sha256(bytes(private_key.encode('utf-8')))
                hash_dig = hash_object.hexdigest()
                numbers = ''.join(i for i in hash_dig if not i.isalpha())
                port_for_key = int(sum(list(map(int, numbers)))**1.64)
                time.sleep(0.3)

                if port_for_key not in list_of_ports or port_for_key > 2000:
                    try:
                        
                        os.system("clear")
                        tprint("Anon    chat")
                        print(f"trying to create server by private key {private_key}")
                        server = Server(ip_adr, port_for_key, private_key, nickname)
                        server.runServer()
                        
                        
                        key_is_correct = True
                    except:

                        key_is_correct = False
            


        elif command == "C":
            queue = multiprocessing.Queue()
            queue_send = multiprocessing.Queue()
            
            ip_adr = "localhost"

            private_key_for_client = input("Enter the key: ")
            
            hash_object = hashlib.sha256(bytes(private_key_for_client.encode('utf-8')))
            hash_dig = hash_object.hexdigest()
            numbers = ''.join(i for i in hash_dig if not i.isalpha())
            port_for_key = int(sum(list(map(int, numbers)))**1.64)
            time.sleep(0.3)

            if port_for_key not in list_of_ports or port_for_key < 2000:
                key_is_correct = True
                os.system("clear")
                tprint("Anon    chat")
                print(f"done! {private_key_for_client} is correct")
            nickname = input("Enter your nickname for chat (max len 16): ")

            client = Client(ip_adr, port_for_key, private_key_for_client, nickname, queue, queue_send)

            isConnected = client.connect_to_server()

            if isConnected:
                

                client.runClient()
                

                
                
            else:
                print("Error while connecting to server")
                exit()

        else:
            print("wrong input, restarting software")
            Start.main_start()



if __name__ == "__main__":
    
    Start.main_start()
    
    #TODO: 1. check users by ip
    #      2. create ports for chat by some hash func
   
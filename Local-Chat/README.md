# Local Chat

This program allows you to create a channel in the local network for communication between users through the use of a secret key that is generated when a server is created at the host.

# Usage

1. If you don't already have tkinter installed, you need to download it. tkinter is a standard GUI library for Python, and it's usually included with Python installations. However, if you don't have it installed, you can install it using your package manager. For example, on Ubuntu or Debian-based systems, you can use:
```
sudo apt-get install python3-tk
```


2. Install the required libraries listed in `requirements.txt` file using `pip`:

```
pip3 install -r requirements.txt
```

3. Run `main.py` to create a server:

```
python3 main.py
```
Once the script is executed, you'll be prompted to input S on the terminal to create the server.

**Important:** Make sure to save the key provided by the program. You'll need this key to connect to the server or to allow others to join your channel.


<img src="https://github.com/p4sh4bsc/Python-Projects/blob/local_chat/Local-Chat/src/Server.gif" width="500" height="300" />



4. Run `main.py` again from another terminal, but this time we're going to connect to the server as a client:

```
python3 main.py
```



<img src="https://github.com/p4sh4bsc/Python-Projects/blob/local_chat/Local-Chat/src/Client.gif" width="500" height="300" />



5. Start chatting with your friends!
<img src="https://github.com/p4sh4bsc/Python-Projects/blob/local_chat/Local-Chat/src/GUI.png" width="500" height="300" />



# TODO list
1. check users by ip
2. create ports for chat by some hash func
3. create secure connection between users(for sure every non chat user can listening chat by Wireshark)

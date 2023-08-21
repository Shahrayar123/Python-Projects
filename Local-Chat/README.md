# Local Chat

This program allows you to create a channel in the local network for communication between users through the use of a secret key that is generated when a server is created at the host.

# Usage

1. Install the required libraries listed in `requirements.txt` file using `pip`:

```
pip3 install -r requirements.txt
```

2. Run `main.py` to create server.

```
python3 main.py
```
after running the script print S parameter(to create server)

!!! be sure to save the key that the program will give you !!!


<img src="https://github.com/p4sh4bsc/Python-Projects/blob/local_chat/Local_chat/src/Server.gif" width="500" height="300" />



3. Also run `main.py`, but now we gonna connetct to the server as client.
```
python3 main.py
```
after running the script print C parameter(for connection to the server)



<img src="https://github.com/p4sh4bsc/Python-Projects/blob/local_chat/Local_chat/src/Client.gif" width="500" height="300" />
4. Start chatting with your friends!

# TODO list
1. check users by ip
2. create ports for chat by some hash func
3. create secure connection between users(for sure every non chat user can listening chat by Wireshark)
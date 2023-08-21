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
![](https://github.com/p4sh4bsc/Python-Projects/blob/local_chat/Local_chat/src/Server.gif)
3. Also run `main.py`, but now we gonna connetct to the server as client.
```
python3 main.py
```
after running the script print C parameter(for connection to the server)
![](https://github.com/p4sh4bsc/Python-Projects/blob/local_chat/Local_chat/src/Client.gif)
4. Start chatting with your friends!
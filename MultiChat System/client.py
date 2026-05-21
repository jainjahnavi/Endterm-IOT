import socket
import threading

server_ip= "127.0.0.1"
port=5000

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((server_ip,port))

def rec_message():
    while True:
     try:
        message=client.recv(1024).decode()
        if message=="USERNAME":
            username=input("enter your username: ")
            client.send(username.encode())
     except:
        print("connectin closed")
        client.close()
def send_message():
    message=input()
    client.send(message.encode())

threading.Thread(target=rec_message).start()
threading.Thread(target=send_message).start()

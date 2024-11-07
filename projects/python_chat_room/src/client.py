import socket
import random
from threading import Thread
import datetime

# from colorama import Fore, init, Back






if name := input("Enter your name: ") != "quit":
    print("exited")


SERVER_HOST = "127.0.0.1" # you will need to change this to Felix`s macbook IP if you want to connect. 
SERVER_PORT = 30000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


print(f"connecting to {SERVER_HOST} on port {SERVER_PORT}")
try:
    s.connect((SERVER_HOST, SERVER_PORT))
except Exception:
    print("server is not on try checking later or your not connected to the internet")
print(f"connected to {SERVER_HOST}")

#send name one time
s.send(name.encode())



# thread_2c
# waits for messges from the sever, then prints them out for the user
def listen_for_messge():
    while True:
        try:
            messge = s.recv(1024).decode()
        except ConnectionResetError:
            exit()
        
        print(f"{messge}\n")
# create a diffrent thread so listen_for_messge can run in the backround while the main messge loop continues to run

# thread_1
# this is where you will send your messges to the server
def main_loop():
    while True:
    # input a messge you want to send to other ppl in the chat room or a command
        try:
            messge = str(input("\n"))
        except KeyboardInterrupt:
            send_messge("/Quit")
        
        send_messge(messge)






        


        
    
    
        



def send_messge(messge) -> None: 
    
    messge = f"{name}<wep>{messge}"
    try:
        s.send(messge.encode())
    except BrokenPipeError:
        print("server turned off or is down. diconneted [500]")
        


# create a diffrent thread so listen_for_messge can run in the backround while the main messge loop continues to run
t = Thread(target=listen_for_messge, daemon=True)

t.start()



# start main_loop with main thread
main_loop()



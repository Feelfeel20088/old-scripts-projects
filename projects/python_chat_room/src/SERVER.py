import socket
from threading import Thread
from datetime import datetime
import random
import json
import os
# from dotenv import load_dotenv

# load_dotenv()

PORT = int(os.getenv("SERVER_PORT"))
IP = os.getenv("SERVER_HOST")




# no worky
# hostname = socket.gethostname() 
# print(hostname)
# SERVER_HOST = socket.gethostbyname(hostname)   
# print(hostname, SERVER_HOST) 

# set of client addresses and client sockets

cs = set()
cn = set()
ca = set()
cc = set()



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))



class server_relient_commands:
    reset_color = '\033[0m'
    def set_vars(self, name, command, client_socket, client_address, color):
        self.commands = {"/List" : self.List, 
                         "/Quit" : self.Quit_Current_Clinet, 
                         "/Start-Game" : Games, 
                         "/Name" : self.Name, 
                         "/Credits" : self.Credits,
                         "/Help" : self.Help
                        } # update this as needed to make more commandsd
        self.name = name
        self.client_address = client_address
        self.color = color
        self.client_socket = client_socket
        

        self.commands[command]()
    

    
    def List(self):
        messge = "online:\n "
        for (name, client, color) in zip(cn, ca, cc):

            print(name, client)
            messge += f"\t{color} {name}: {client} {server_relient_commands.reset_color}\n"
        self.send_client(messge)
            

    
    def Quit_Current_Clinet(self):
        self.brodcast(f"{self.name} left the chat")
        get_back_color(self.color)
        cn.discard(self.name)
        cs.discard(self.client_socket)
        ca.discard(self.client_address)
        client_socket.close()

    def Name(self):
        cn.add(self.name)
        self.brodcast(f"client changed name to {self.name}")


    def Credits(self):
        self.brodcast("""       Main dev: Felix Vujasin 
                                insperation: RealPython.com""")
    
    def Help(self):
        self.send_client("""
                \nonline chat room for sending messges to other ppl, have fun and keep conversations respectable.\n
                commands:\n
                    # /Help displays all commands.
                    # /Quit quits the program
                    # /List lists all connected clients
                    # /Name prompts you to enter your name again\n
                    # /Credits displays the creators of this shitty program
                """)
    
    

        
    

    

    


    

    
    
    
    def brodcast(self, messge):
        for client_socket in cs:
            client_socket.send(messge.encode())
            
            
            


    def send_client(self, messge):
        self.client_socket.send(messge.encode())





class Games:

    def Help():
        pass
    
        
        

        
    









# start socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)
print(f"Listening as {IP} : {PORT}")



    
def load_color():
    with open("colors.json", "r") as cj:
        return json.load(cj)["colors"]



def choose_color(colors):
    color = random.choice(colors)
    colors.remove(color)
    cc.add(color)
    
    return color


def get_back_color(color):
    colors.append(color)
    cc.discard(color)





    
        
    

# recive a messge then fowerd it to all connected clients
def handel_client_messges(client_socket, colors, client_address):
    server_commands = server_relient_commands()
    
    color = choose_color(colors)
    while True:
        try:
            msg = client_socket.recv(1024).decode()
        except Exception:
            server_commands.Quit_Current_Clinet()
            break
        
        part = msg.split("<wep>")
        
        # second item in the list, first letter 
        try:
            if part[1][0] == "/": # the client may send a messge of a empty string resuting in a erroh for the server, we will use try block to stop this
                server_commands.set_vars(part[0], part[1], client_socket, client_address, color)

            else:
                server_commands.brodcast(f"{color}[{datetime.now()}] {part[0]}: {part[1]} {server_relient_commands.reset_color}")
            
        except IndexError:
            pass

            
            

        
def debug_REPL():
    while True:
        input()
        print(f"client sockets: {cs}\nclient names: {cn}\nclient addreses {ca}\nclient colors: {cc}\n")
       
        
    







# main loop that accepts connectuon from cliant and starts a new thread with the cliant socket to listen for its messges 
d = Thread(target=debug_REPL)
d.daemon = True
d.start()
colors = load_color()
c1 = server_relient_commands
while True:

    client_socket, client_address = s.accept()
    cn.add(client_socket.recv(1024).decode())
    cs.add(client_socket)
    ca.add(client_address)


    
    
    
    
    print(f"creating new thread for {client_address}")
    # Creates a separate thread for the function to run asynchronously (DOES NOT START THE FUNCTION).
    # t.start() will start the specified function, meaning that each connection for a client is run in a separate thread and broadcasts its message to the other clients!
    t = Thread(target=handel_client_messges, args=(client_socket,colors,client_address))
    
    t.daemon = True

    t.start()
        
    







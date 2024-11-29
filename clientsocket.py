# import socket
# c=socket.socket()

# print("Socket Created")

# c.connect(("localhost",9999))
# name=input("Enter your name")
# c.send(bytes(name,"utf-8"))


# print(c.recv(1024).decode())


import socket

client=socket.socket()

print("Socket created for client")

client.connect(("192.168.0.165",1234))

print("connected to server")
name=input("Enter your Name here ")
client.send(bytes(name,"utf-8"))
print(client.recv(1024).decode())
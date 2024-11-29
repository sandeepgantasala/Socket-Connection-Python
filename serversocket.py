# import socket

# s= socket.socket()  #type of network can be created here 

# print("Socket Created")

# s.bind(("localhost",9999))    #port number can be used which is available 0-65535 Range 

# s.listen(3)

# print("Waiting for connections")

# while True:
#     Objc,addr=s.accept()
#     name=Objc.recv(1024).decode()
#     print("Connected with",addr,name)
#     Objc.send(bytes("Hello this is Sandeep","utf-8"))

#     Objc.close()


import socket
server=socket.socket()

print("Socket Created")

server.bind(("192.168.0.165", 1234))  

server.listen(3)

print("Waiting for conections")

while True:          # here it returns client socket and address
    client, address=server.accept()
    name=client.recv(1024).decode()  
    print("Connected with ", address,name)

    client.send(bytes(f"Hello {name} Welcome to sandeep server","utf-8"))

    client.close()








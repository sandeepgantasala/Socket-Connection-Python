import socket
server=socket.socket()     #created server conncetion with socket 

print("Socket Created")

server.bind(("192.168.0.165", 1234))  #server connection with localhost

server.listen(3)

print("Waiting for conections")

while True:          # here it returns client socket and address
    client, address=server.accept()
    name=client.recv(1024).decode()  #receiving clint message 
    print("Connected with ", address,name)

    client.send(bytes(f"Hello {name} Welcome to sandeep server","utf-8"))

    client.close()








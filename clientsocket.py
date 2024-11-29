
import socket

client=socket.socket()                 #creating object socket connection

print("Socket created for client")

client.connect(("192.168.0.165",1234))   #should connect to server side ip address

print("connected to server")
name=input("Enter your Name here ")
client.send(bytes(name,"utf-8"))           #sending the message as name 
print(client.recv(1024).decode())          #recieving response from server as message
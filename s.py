#SOCKETS - Sockets can be used to connect two nodes together.  

#!/bin/python3
import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is ipv4, sock stream is a port
s.connect((HOST,PORT))

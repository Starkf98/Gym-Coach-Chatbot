#!/usr/bin/python # This is client.py file
import socket # Import socket module
s = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name
port = 20201 # Reserve a port for your service.
s.connect((host, port))


MESSAGE=str(input('Any Question?\t'))
lenMESSAGE=len(MESSAGE)
s.send(MESSAGE) 
data = s.recv(lenMESSAGE)

#ask and send
#
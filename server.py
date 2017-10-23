
#!/usr/bin/python # This is server.py file
import socket # Import socket module
s = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name
port = 20201 # Reserve a port for your service.
s.bind((host, port)) # Bind to the port
s.listen(1) # Now wait for client connection.

while True:
    c, addr = s.accept() # Establish connection with client.
    print ('Got connection from', addr)
    c.send('Something')
    
    
c.send('Thank you for connecting')
c.close() # Close the connection





'''

MESSAGE=str(input('Any Question?\t'))
lenMESSAGE=len(MESSAGE)
s.send(MESSAGE) 
data = s.recv(lenMESSAGE)

'''
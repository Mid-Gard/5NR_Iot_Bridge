#!/usr/bin/env python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 18:11:26 2022

@author: tamizh
"""

# echo-client.py

import socket

HOST = "10.0.0.4"  # The server's hostname or IP address
PORT = 65433  # The port used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.connect((HOST, PORT))
#    data=b"1"
#    s.sendall(data)
#    data = s.recv(1024)

#print(f"Received {data!r}")
while True:
    data= input("Enter your input:")
    s.sendall(data)
    data = s.recv(1024)
#    if command == 'EXIT':
#        s.send(str.encode(command))
#        break
#    elif command == 'KILL':
#        s.send(str.encode(command))
#        break
#    s.send(str.encode(command))
        
        

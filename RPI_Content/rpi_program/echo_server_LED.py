#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 19:04:31 2022

@author: tamizh
"""
# echo-server.py

import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

HOST = "10.0.0.2"  # Standard loopback interface address (localhost)
PORT = 65440  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
#        print("Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print("Received:")
            d=data.decode('UTF-8')
            print(d)
            GPIO.setup(25,GPIO.OUT)
            if d=="F":
               print("LED off")
               GPIO.output(25,GPIO.LOW)
            elif d=="T":
               print("LED on")
               GPIO.output(25,GPIO.HIGH)
            if not data:
                break
            conn.sendall(data)
#b.decode('UTF-8')













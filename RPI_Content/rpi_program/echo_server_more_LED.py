# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 12:33:55 2022

@author: tamizh
"""

import socket
import RPi.GPIO as GPIO
import time
import RPi.GPIO as GPIO
import time
from sys import argv

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

HOST = "10.0.0.4"  # Standard loopback interface address (localhost)
PORT = 65437  # Port to listen on (non-privileged ports are > 1023)

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
            whichled=argv[1]
            ledaction = argv[2]
            LEDa=17
            LEDb=18
            LEDc=25
            LEDd=23
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(LEDa, GPIO.OUT)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(LEDb, GPIO.OUT)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(LEDc, GPIO.OUT)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(LEDd, GPIO.OUT)
            
            if ledaction=="off":
                if whichled=="a":
                    GPIO.output(LEDa, False)
                if whichled=="b":
                    GPIO.output(LEDb, False)
                if whichled=="c":
                    GPIO.output(LEDc, False)
                if whichled=="d":
                    GPIO.output(LEDd, False)
                if whichled=="all":
                    GPIO.output(LEDa, False)
                    GPIO.output(LEDb, False)
                    GPIO.output(LEDc, False)
                    GPIO.output(LEDd, False)
                    
            if ledaction=="on":
                if whichled=="a":
                    GPIO.output(LEDa, True)
                if whichled=="b":
                    GPIO.output(LEDb, True)
                if whichled=="c":
                    GPIO.output(LEDc, True)
                if whichled=="d":
                    GPIO.output(LEDd, True)
                if whichled=="all":
                    GPIO.output(LEDa, True)
                    GPIO.output(LEDb, True)
                    GPIO.output(LEDc, True)
                    GPIO.output(LEDd, True)


#            GPIO.setup(24,GPIO.OUT)
#            if d== 0:
#               print("LED off")
#               GPIO.output(24,GPIO.LOW)
#            elif d== 1:
#               print("LED on")
#               GPIO.output(24,GPIO.HIGH)
#            if not data:
#                break
            conn.sendall(data)


#whichled=argv[1]
#ledaction = argv[2]


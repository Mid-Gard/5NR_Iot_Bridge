from time import sleep
import os,sys
import RPi.GPIO as GPIO
#import paho.mqtt.client as paho

#import urlparse
#import urllib.parse as urlparse


import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

in1 = 24  # RIGHT SIDE
in2 = 23
en1 = 25
temp1 = 1

in3 = 10  # LEFT SIDE
in4 = 9
en2 = 11
temp2 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en1, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p1 = GPIO.PWM(en1, 2)

GPIO.setmode(GPIO.BCM)

GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
p2 = GPIO.PWM(en2, 2)

p1.start(25)
p2.start(25)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")
            

HOST = "172.16.0.6"  # Standard loopback interface address (localhost)
PORT = 65450  # Port to listen on (non-privileged ports are > 1023)



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
            if d == "F":
                print("forward")
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.HIGH)
                temp1 = 1
                temp2 = 1
            elif d == "B":
                print("backward")
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.HIGH)
                GPIO.output(in3, GPIO.HIGH)
                GPIO.output(in4, GPIO.LOW)
                temp1 = 0
                temp2 = 0
            elif d == "L":
                print("left")
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.LOW)
            elif d == "R":
                print("right")
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.HIGH)
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.LOW)
            elif d == 'S':
                print("STOP!")
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.LOW)
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.LOW)
            elif d == 'l':
                print("low")
                p1.ChangeDutyCycle(2)
                p2.ChangeDutyCycle(2)
            elif d == 'm':
                print("medium")
                p1.ChangeDutyCycle(50)
                p2.ChangeDutyCycle(50)

            elif d == 'h':
                print("high")
                p1.ChangeDutyCycle(100)
                p2.ChangeDutyCycle(100)

            else:
                print("RETRY!!")  # LED OFF

            conn.sendall(data)

#           def on_connect(self, mosq, obj, rc):
  #              self.subscribe("car", 0)


   #         def on_message(mosq, obj, msg):
    #            print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


# def on_publish(mosq, obj, mid):
#     print("mid: " + str(mid))
#
#
# def on_subscribe(mosq, obj, mid, granted_qos):
#     print("Subscribed: " + str(mid) + " " + str(granted_qos))
#
#
#
# mqttc = paho.Client()                        # object declaration
# # Assign event callbacks
# mqttc.on_message = on_message                          # called as callback
# mqttc.on_connect = on_connect
# mqttc.on_publish = on_publish
# mqttc.on_subscribe = on_subscribe


#url_str = os.environ.get('CLOUDMQTT_URL', 'tcp://broker.emqx.io:1883')                  # pass broker addr e.g. "tcp://iot.eclipse.org"
#url_str = os.environ.get('CLOUDMQTT_URL', 'tcp://broker.hivemq.com:1883')
# url_str = os.environ.get('CLOUDMQTT_URL', 'tcp://broker.emqx.io:1883')
# url = urlparse.urlparse(url_str)
# mqttc.connect(url.hostname, url.port)
#
# rc = 0
# while True:
#     while rc == 0:
#         import time
#         rc = mqttc.loop()
#         #time.sleep(0.5)
#     print("rc: " + str(rc))

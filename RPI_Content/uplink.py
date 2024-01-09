import serial               #import serial pacakge
from time import sleep
import webbrowser           #import package for opening link in browser
import sys                  #import system package
from threading import Timer, Thread
import RPi.GPIO as GPIO
import time
import math

def GPS_Info():
    global NMEA_buff
    global lat_in_degrees
    global long_in_degrees
    nmea_time = []
    nmea_latitude = []
    nmea_longitude = []
    nmea_time = NMEA_buff[0]                    #extract time from GPGGA string
    nmea_latitude = NMEA_buff[1]                #extract latitude from GPGGA string
    nmea_longitude = NMEA_buff[3]               #extract longitude from GPGGA string
    
    #print("NMEA Time: ", nmea_time,'\n')
    #print ("NMEA Latitude:", nmea_latitude,"NMEA Longitude:", nmea_longitude,'\n')
    
    lat = float(nmea_latitude)                  #convert string into float for calculation
    longi = float(nmea_longitude)               #convertr string into float for calculation
    
    lat_in_degrees = convert_to_degrees(lat)    #get latitude in degree decimal format
    long_in_degrees = convert_to_degrees(longi) #get longitude in degree decimal format
    
#convert raw NMEA string into degree decimal format   
def convert_to_degrees(raw_value):
    decimal_value = raw_value/100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value))/0.6
    position = degrees + mm_mmmm
    position = "%.4f" %(position)
    return position
    


gpgga_info = "$GPGGA,"
ser = serial.Serial ("/dev/ttyS0")              #Open port with baud rate
GPGGA_buffer = 0
NMEA_buff = 0
lat_in_degrees = 0
long_in_degrees = 0
    
    
# class which creates a resettable timer as a thread
class ResetTimer(object):
    def __init__(self, time, function, daemon=None):
        self.__time = time
        self.__function = function
        self.__set()
        self.__running = False
        self.__killed = False
        Thread.__init__(self)
        self.__daemon = daemon
        
    def __set(self):
        self.__timer = Timer(self.__time, self.__function)
 
    def stop(self):
        self.__daemon = True
 
    def run(self):
        self.__running = True
        self.__timer.start()
 
        if self.__daemon == True:
            sys.exit(0)
            
    def cancel(self):
        self.__running = False
        self.__timer.cancel()
 
    def reset(self, start = False):
        if self.__running:
            self.__timer.cancel()
        self.__set()
        if self.__running or start:
            self.start()
 
# method that counts how often the light barrier is triggered
def count(self):
    global counter
    counter = counter + 1
# method for calculating / displaying of rotations


    
    
    
    
    
try:
	while True:
		received_data = (str)(ser.readline())                   #read NMEA string received
		GPGGA_data_available = received_data.find(gpgga_info)   #check for NMEA GPGGA string                 
		if (GPGGA_data_available>0):
			GPGGA_buffer = received_data.split("$GPGGA,",1)[1]  #store data coming after "$GPGGA," string 
			NMEA_buff = (GPGGA_buffer.split(','))               #store comma separated data in buffer
			GPS_Info()                                         #get time, latitude, longitude
 
			#print("lat in degrees:", lat_in_degrees," long in degree: ", long_in_degrees, '\n')
			def output():
				global counter
				timer.cancel() # stopping the timer
				#RPM= (((counter))/wheel)
				speed = (counter*math.pi*d)/wheel # calculating rotations per minute
				print("lat in degrees:", lat_in_degrees," long in degree: ", long_in_degrees, '\n')
				print("The Speed of the Car is " + str(speed) + " m/s")# output
				#print("The RPM of the Car is " + str(RPM))
				counter = 0 # resetting the counter
				timer.reset() # resetting the timer
				timer.run() # restart timer
			# setting variables
			counter = 0
			d=0.066
			pin = 4 # pin assignmespeed = (((counter))/wheel)*math.pi*dnt
			interval = 10.0 # interval of 10 seconds
			calc = 60 / int(interval) # project interval to a minute
			wheel = 20 # amounts of holes in the disk
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(pin,GPIO.IN)
			# create the timer which will execute the method output after interval seconds 
			timer = ResetTimer(interval, output)
			# main programm
			try: 
				# executes method count if the voltage drops at the pin
				GPIO.add_event_detect(pin, GPIO.FALLING,count)
				# start timer
				timer.run()
 
			except KeyboardInterrupt:
				timer.stop()
				timer.join()
				GPIO.cleanup()

except KeyboardInterrupt:
    print("exited")

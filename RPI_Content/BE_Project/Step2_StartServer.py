import httplib
import urllib
import time
import serial

key = "SWNIY15Q6LJ7KLDU"  # Put your API Key here

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

def iot_main():
    while True:
        incoming = ser.readline().strip()
        data = incoming.decode()
        
        print(data)

        idx1 = data.find("d=")
        if idx1 == 0:
            val1 = data[idx1 + 2:idx1 + 4]
            params = urllib.urlencode({'field1': val1, 'key': key})

        idx2 = data.find("B=")
        if idx2 == 0:
            val2 = data[idx2 + 2:idx2 + 5]
            print('Router2:', val2)

        idx4 = data.find("x=")
        if idx4 == 0:
            val3 = data[idx4 + 2:idx4 + 5]
            print('End Router:', val3)

        idx6 = data.find("A=")
        if idx6 == 0:
            val4 = data[idx6 + 2:idx6 + 5]
            print('Router1:', val4)

        idx7 = data.find("H=")
        if idx7 == 0:
            val5 = data[idx7 + 2:idx7 + 5]
            print('Router(std router):', val5)

if __name__ == "__main__":
    try:
        while True:
            iot_main()
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass


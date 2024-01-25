import httplib
import urllib
import time
import serial
import requests
import json
import random
import time

key = "SWNIY15Q6LJ7KLDU"  # Put your API Key here

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# url = 'https://d66c-14-139-113-18.ngrok-free.app/weatherstation/weather_get/'
url = 'https://fc7a-14-139-113-18.ngrok-free.app/weatherstation/weather_get/'
# url = 'http://192.168.0.160:8000/weatherstation/weather_get/'
# url = 'http://192.168.0.160:8000/livestock/test_post/'
# url = 'http://14.139.113.18:8000/livestock/test_post/'


headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Content-Type": "application/json" 
}

def parse_weather_data(data_line):
    # Split the data_line into individual values
    values = data_line.split(',')
    
    # Assign values to parameters
    id = int(time.time())  # Current timestamp
    temperature = float(values[0])
    humidity = float(values[1])
    pressure = float(values[2])
    light_level = int(values[3])
    soil_moisture = int(values[4])
    soil_temp = float(values[5])
    wind_speed = float(values[6])
    wind_direction = values[7]
    rain_gauge = int(values[8])
    altitude = float(values[9])
    
    return {
        'id': id,
        'temperature': temperature,
        'humidity': humidity,
        'Pressure': pressure,
        'LightLevel': light_level,
        'SoilMoisture': soil_moisture,
        'SoilTemp': soil_temp,
        'WindSpeed': wind_speed,
        'WindDirection': wind_direction,
        'RainGuage': rain_gauge,
        'Altitude': altitude,
    }

def iot_main():
    while True:
        incoming = ser.readline().strip()
        data = incoming.decode()
        
        print(data)
        
        # Check if the line starts with a digit (to identify the third line)
        if data and data[0].isdigit():
            # Parse the weather data
            print("Weather Data Receieved : ", data)
            weather_data = parse_weather_data(data)
            
            # Create the payload
            payload = json.dumps({'weather_data': weather_data})
            print(payload)
            
            # Send the POST request
            response = requests.post(url, data=payload, headers=headersList)
            print(response)

if __name__ == "__main__":
    try:
        while True:
            iot_main()
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass














# import httplib
# import urllib
# import time
# import serial
# import requests
# import json
# import random
# import time

# key = "SWNIY15Q6LJ7KLDU"  # Put your API Key here

# ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# url = 'http://192.168.0.160:8000/weatherstation/weather_get/'
# # url = 'http://192.168.0.160:8000/livestock/test_post/'
# # url = 'http://14.139.113.18:8000/livestock/test_post/'

# headersList = {
#  "Accept": "*/*",
#  "User-Agent": "Thunder Client (https://www.thunderclient.com)",
#  "Content-Type": "application/json" 
# }

# def iot_main():
#     while True:
#         incoming = ser.readline().strip()
#         data = incoming.decode()
        
#         print(data)
#         # give me code here
        
#         # payload = json.dumps(data)
#         # print(payload)
#         # response = requests.request("POST", url, data=payload,  headers=headersList)
#         # print(response)

# if __name__ == "__main__":
#     try:
#         while True:
#             iot_main()
#     except KeyboardInterrupt:
#         print("Press Ctrl-C to terminate while statement")
#         pass



#!/usr/bin/python
from temperature import Temperature
from data import Data
import time
import serial

# Serial Port
serial_port = '/dev/ttyUSB0'
time_to_wait = 1.8

# Values from Raspberry
data = {}
data['relay'] = False;
data['relay_main'] = False;
data['temperature'] = 23;

def split_serial_values (string):
    data = str(string).split("'")[1]
    data = str(data).split("\\")[0]
    #values = list(filter(None, data))
    variable = data.split(':')[1]
    print(variable)

def send_serial ():
    if(data['relay']):
        Serial.write("relay_on:".encode())
        print("relay_on")
    else:
        Serial.write("relay_off:".encode())
        print("relay_off")
    if(data['relay_main']):
        Serial.write("relay_main_on:".encode())
        print("relay_main_on")
    else:
        Serial.write("relay_main_off:".encode())
        print("relay_main_off")
    temp = ("temperature: " + str(data['temperature']))
    Serial.write(temp.encode())

Temperature = Temperature()
#Led = Led()
Data = Data()

# Iniciando conexión serial
Serial = serial.Serial(serial_port, 9600, timeout=1)
# Retardo para establecer la conexión serial
time.sleep(time_to_wait)
# Serial.write(flagCharacter)


while True:
    
    #Temperature.add(arduino['temperature'])
    #Temperature.log_realtime()

    db_data = Data.get()
    data = db_data

    Data.log_realtime()

    serial_value = Serial.readline()
    split_serial_values(serial_value)

	# Emmit system configuration
    send_serial()
    #    Serial.write(serial_construct().encode());

    # Delay
    time.sleep(0.5) 

# Cerrando puerto serial
Serial.close()

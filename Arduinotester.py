import serial as s
import time as t
import subprocess

arduino = s.Serial(port="COM1", baudrate=9600, timeout=.1)

string = '252 1\n'
next = False

while(1):
    #arduino.write(string.encode())

    t.sleep(2)

    #print(arduino.readline())

    def write_data():
        data = arduino.readline()
        data = data.decode()
        data = data.rstrip("\r\n")
        data = data.split(" ")
        return data
    
    print(write_data())

    
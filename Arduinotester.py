import time as t
import serial
import subprocess

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)

string = b'765 1'
next = False

while(1):
    arduino.write(string)

    t.sleep(8)

    print(arduino.read())

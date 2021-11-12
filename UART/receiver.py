import serial
import time

ser = serial.Serial(port='COM5', baudrate=115200)

while (True):
    if (ser.in_waiting > 0):
        data = ser.read(ser.in_waiting).decode('ascii')
        print(data)
    time.sleep(0.01) 

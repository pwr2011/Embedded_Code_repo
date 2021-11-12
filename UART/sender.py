import serial
import time

serial_port = serial.Serial(port='COM3', baudrate=115200)

try:
    while True:
        tx_data = input()
        serial_port.write(bytes(tx_data,encoding='ascii'))
        time.sleep(1)
        
except KeyboardInterrupt:
    serial_port.close()

import serial
import json

ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600)

while True:
  line = ser.readline().decode('utf-8')[:-1]
  try:
    print("payload:", json.loads(line))
  except:
    pass

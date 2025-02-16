import serial
import json

ser = serial.Serial(port='PORT', baudrate=9600)
ser.readline()

while True:
  line = ser.readline().decode('utf-8')
  try:
    dic = json.loads(line[:-1])
  except:
    print('Error!')
  else:
    print(dic)

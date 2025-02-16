import serial
import json
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.username_pw_set(username='ship', password='1234')

# 포트 이름과 baud rate을 확인하세요
ser = serial.Serial(port='PORT', baudrate=9600)
ser.readline()
client.connect('localhost', 1883, 60)

while True:
  line = ser.readline().decode('utf-8')
  try:
    dic = json.loads(line[:-1])
  except:
    print('Error!')
  else:
    print(dic)
    for key, value in dic.items():
      client.publish(key, value)

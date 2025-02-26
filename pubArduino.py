import serial
import json
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.username_pw_set(username='ship', password='1234')
client.connect('localhost', 1883, 60)

ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600)
ser.readline()

while True:
  if ser.readable():
    line = ser.readline().decode('utf-8')[:-1]
    try:
      message = json.loads(line)
    except:
      pass
    else:
      # print("message:", message)
      for topic, payload in message.items():
        client.publish(topic, payload)
        print(f'publishing - topic:{topic}  \tpayload:{payload}')
      print()

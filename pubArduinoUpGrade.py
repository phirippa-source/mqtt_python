import serial
import json
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.username_pw_set(username='ship', password='1234')
ser = serial.Serial(port='PORT', baudrate=9600)
ser.readline()
topic = 'MyOffice/Indoor/Values'
client.connect('localhost', 1883, 60)

while True:
  line = ser.readline().decode('utf-8')[:-1]
  try:
    message = json.loads(line)
  except:
    pass
  else:
    payload = json.dumps(message)
    client.publish(topic, payload)
    print(f'Topic:{topic}\tPayload:{payload}')

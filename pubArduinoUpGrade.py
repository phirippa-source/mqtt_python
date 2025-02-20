import serial
import json
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.username_pw_set(username='ship', password='1234')
ser = serial.Serial(port='PORT', baudrate=9600)
topic = 'MyOffice/Indoor/Values'
client.connect('localhost', 1883, 60)
ser.readline()

while True:
  payload = ser.readline().decode('utf-8')[:-1]
  try:
    client.publish(topic, payload)
    print('Topic :',topic, 'Payload :', payload)
  except:
    print('Error!')

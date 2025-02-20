import serial
import json
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.username_pw_set(username='ship', password='1234')
ser = serial.Serial(port='PORT', baudrate=9600)
client.connect('localhost', 1883, 60)
ser.readline()

while True:
  line = ser.readline().decode('utf-8')
  try:
    client.publish('MyOffice/Indoor/Values', line[:-1])
    print('Topic:"sensors", Payload:', line[:-1])
  except:
    print('Error!')

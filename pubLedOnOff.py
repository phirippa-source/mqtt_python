import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.username_pw_set(username='ship', passwd='1234')
client.connect('localhost', 1883, 60)

topic = 'MyOffice/Outdoor/Led'

while True:
  client.publish(tocpic, 'on')
  print('Led ON')
  time.sleep(3)    # 3초 대기

  client.publish(topic, 'off')
  print('Led OFF')
  time.sleep(1)    # 1초 대기

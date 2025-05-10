import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect('localhost', 1883, 60)

for i in range(3):
    client.publish('MyOffice/Indoor/Temp', 25.1)
    print('MyOffice/Indoor/Temp', 25.1)
    client.publish('MyOffice/Indoor/Humi', 33)
    print('MyOffice/Indoor/Humi', 33)
        
    client.publish('MyOffice/Outdoor/Temp', 33.9)
    print('MyOffice/Outdoor/Temp', 33.9)    
    client.publish('MyOffice/Outdoor/Humi', 23)
    print('MyOffice/Outdoor/Humi', 23)
    time.sleep(2)


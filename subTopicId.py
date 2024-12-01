import paho.mqtt.client as mqtt

def on_connect(clinet, userdata, flag, rc):
    print('Connect with result code : ' + str(rc))
    clinet.subscribe('MyOffice/Indoor/#')

def on_message(client, userdata, msg):
    print(msg.topic + ':' + str(msg.payload))

client = mqtt.Client()
client.username_pw_set(username='mqtt_ship', password='1234')
client.on_connect = on_connect
client.on_message = on_message

client.connect('localhost', 1883, 60)
client.loop_forever()

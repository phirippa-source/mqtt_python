from influxdb import InfluxDBClient
import paho.mqtt.client as mqtt

dbClient =  InfluxDBClient(host='localhost', port=8086, username='ship', password='1234', database='dbSensorData')

def on_connect(clinet, userdata, flag, rc):
    print('Connect with result code : ' + str(rc))
    clinet.subscribe('MyOffice/Outdoor/#')

def on_message(client, userdata, msg):
    print(msg.topic + ':' + str(msg.payload))

    topic = msg.topic.split('/')
    json_body =[]
    data_point = { 'measurement':'sensors',
                    'tags':{'Location':'', 'SubLocation':''},
                    'fields':{'Temp':0.0, 'Humi':0.0}
                }
    data_point['tags']['Location'] = topic[0]
    data_point['tags']['SubLocation'] = topic[1]
    data_point['fields'][topic[2]] = float(msg.payload)
    json_body.append(data_point)
    dbClient.write_points(json_body)

client = mqtt.Client()
client.username_pw_set(username='mqtt_ship', password='1234')

client.on_connect = on_connect
client.on_message = on_message

client.connect('localhost', 1883, 60)
client.loop_forever()

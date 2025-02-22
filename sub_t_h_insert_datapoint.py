from influxdb import InfluxDBClient
import paho.mqtt.client as mqtt

dbClient =  InfluxDBClient(host='localhost',
                           port=8086,
                           username='ship',
                           password='1234',
                           database='dbData')

def on_connect(clinet, userdata, flag, rc):
    print('Connect with result code : ' + str(rc))
    clinet.subscribe('MyOffice/Outdoor/#')

def on_message(client, userdata, msg):
    print(msg.topic + ':' + str(msg.payload))     # MyOffice/Outdoor/Temp 또는 MyOffice/Outdoor/Humi
    topic = msg.topic.split('/')                  # topci --> ['MyOffice', 'Outdoor', 'Temp']
    json_body =[]
    data_point = { 'measurement':'sensors',
                    'tags':{'Location':'', 'SubLocation':''},
                    'fields':{'Temp':0.0, 'Humi':0.0}
                }
    data_point['tags']['Location'] = topic[0]
    data_point['tags']['SubLocation'] = topic[1]
    data_point['fields'][topic[2]] = float(msg.payload)
    json_body.append(data_point)

    print(f'Inserted: {json_body}', end='\n\n')
    dbClient.write_points(json_body)

client = mqtt.Client()
client.username_pw_set(username='ship', password='1234')
client.on_connect = on_connect
client.on_message = on_message
client.connect('localhost', 1883, 60)
client.loop_forever()

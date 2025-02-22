from influxdb import InfluxDBClient
import paho.mqtt.client as mqtt
import json

dbClient =  InfluxDBClient(host='localhost',
                           port=8086,
                           username='ship',
                           password='1234',
                           database='dbData')

def on_connect(clinet, userdata, flag, rc):
    print('Connect with result code : ' + str(rc))
    clinet.subscribe('MyOffice/Outdoor/Value')

def on_message(client, userdata, msg):
    print(msg.topic + ':' + str(msg.payload))

    #----------------------------------------------------
    (location, sublocation, value) = msg.topic.split('/')
    # msg.payload - '{"Temp":34.1, "Humi":45.1}'
    payload = json.loads(msg.payload)
    # payload = {"Temp":23.1, "Humi":45.1}
    # payload['Temp'] --> 23.1
    #----------------------------------------------------

    json_body =[]
    data_point = { 'measurement':'sensors',
                    'tags':{'Location':'', 'SubLocation':''},
                    'fields':{'Temp':0.0, 'Humi':0.0}
                }
    data_point['tags']['Location'] = location
    data_point['tags']['SubLocation'] = sublocation
    data_point['fields']['Temp'] = payload['Temp']
    data_point['fields']['Humi'] = payload['Humi']
    json_body.append(data_point)
  
    print(f'Inserted: {json_body}', end='\n\n')
    dbClient.write_points(json_body)

client = mqtt.Client()
client.username_pw_set(username='ship', password='1234')
client.on_connect = on_connect
client.on_message = on_message
client.connect('localhost', 1883, 60)
client.loop_forever()

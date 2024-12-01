from influxdb import InfluxDBClient
import time
import random

client = InfluxDBClient(host='localhost',port=8086,username='ship',password='1234',database='dbSensorData')

def genRandomDataPoint():
    json_body=[]
    data_point ={   'measurement':'sensors',
                    'tags':{'Location':''},
                    'fields':{'Temp':0.0, 'Humi':0.0}
                }
    if(random.random() > 0.5) :
        data_point['tags']['Location'] = 'Indoor'
    else:
        data_point['tags']['Location'] = 'Outdoor'

    data_point['fields']['Temp'] = random.random()
    data_point['fields']['Humi'] = random.random()

    json_body.append(data_point)
    return json_body

while True:
    json_body = genRandomDataPoint()
    print(json_body)
    client.write_points(json_body)
    time.sleep(5)

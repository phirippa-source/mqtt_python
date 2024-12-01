from influxdb import InfluxDBClient

client =  InfluxDBClient(
                host = 'localhost',
                port = 8086,
                username = 'ship',
                password = '1234',
                database = 'dbSensorData')

json_body = [
                {
                    "measurement" : "temperature", 
                    "tags":{"Location":"Indoor"},
                    "fields":{"Temp":0.0}
                }
            ]

client.write_points(json_body)

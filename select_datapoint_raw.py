from influxdb import InfluxDBClient
client = InfluxDBClient( host='localhost', port='8086', username='ship', password='1234', database='dbData')

result = client.query('select * from sensors')
print( result.raw )

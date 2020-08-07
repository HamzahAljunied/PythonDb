from influxdb import InfluxDBClient

client = InfluxDBClient(host='127.0.0.1', port=8086)
client.create_database('pyInfluxdbTest')
print(client.get_list_database())
from gps3 import gps3
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
def getGPS():

    for new_data in gps_socket:
        if new_data:
            data_stream.unpack(new_data)
            print([data_stream.TPV['lat'], data_stream.TPV['lon']])
            print([type(data_stream.TPV['lat']), type(data_stream.TPV['lon'])])
            if data_stream.TPV['lat'] == 'n/a' or data_stream.TPV['lon'] == 'n/a':
                print("default return")
                return (24.7871229, 120.9967369)
            else: 
                return data_stream.TPV['lat'], data_stream.TPV['lon']
# print('Altitude = ', data_stream.TPV['alt'])
#print('Longitude=' , data_stream.TPV['lon'])
#print('Latitude = ', data_stream.TPV['lat'])

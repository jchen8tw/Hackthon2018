import sys
import googlemaps
import pandas as pd
import time
from expressData import *

if len(sys.argv) == 2:
	googleMapKey = sys.argv[1]
elif len(sys.argv) == 1:
	googleMapKey = "AIzaSyCq6_Zryl4bgEIk_f8NDv7A3-niGGfuKNM"
else:
	exit(-1)
gmaps = googlemaps.Client(key = googleMapKey)
Exceptions = googlemaps.exceptions
def getData(lat, lng):
	try:
		loc = {'lat': lat, 'lng': lng}
		query_result = gmaps.places_nearby(keyword = "building",location = loc, radius = 1000)
	except (Exceptions.ApiError, Exceptions.TransportError, Exceptions.HTTPError, Exceptions.Timeout):
		print("ERROR: getData")
	else:
		return query_result

if __name__ == '__main__':
	latNlng = [24.7871229, 120.9967369]
	#print(latNlng)
	degree = 0
	direction = 'left'
	results = getData(latNlng[0], latNlng[1])
	datas = []
	#datas = [{'lat': 23.7871229, 'lng': 120.9967369, 'name': '橄欖樹廚房', 'place_id': 'ChIJC9294xI2aDQRM3uLb9yfs7c'}, {'lat': 24.7893222, 'lng': 121.0027161, 'name': '麗緻巴賽麗法式餐廳 Brasserie Liz Restaurant', 'place_id': 'ChIJ7ThJZRE2aDQRv4DM1CFoKko'}, {'lat': 24.7958397, 'lng': 120.9984181, 'name': 'Mercuries Beef Noodle Restaurant', 'place_id': 'ChIJEX6W6sE1aDQRiYUjziT0hvI'}, {'lat': 24.7929314, 'lng': 121.0020218, 'name': 'Chengdu Lao Guo Beef Noodle Restaurant', 'place_id': 'ChIJe97NARM2aDQR2D8S7rJCTmQ'}, {'lat': 24.7796415, 'lng': 121.0057166, 'name': 'Burger King Hsinchu Science Park', 'place_id': 'ChIJk5rJxR42aDQRUs45baSmRHI'}, {'lat': 24.7916199, 'lng': 121.0069856, 'name': 'Da Nei Beef Noodle Restaurant', 'place_id': 'ChIJuX1M-BQ2aDQRPsiLb3VYdvI'}, {'lat': 24.7893331, 'lng': 121.0031303, 'name': '暐順麗緻-聖香樓', 'place_id': 'ChIJj0ysbhE2aDQR6Epr9cAIXAY'}, {'lat': 24.7964685, 'lng': 121.0022224, 'name': 'Zhan Ramen Restaurant', 'place_id': 'ChIJ4wzs3mw2aDQRbki_3VkwnIo'}, {'lat': 24.7977669, 'lng': 120.9981233, 'name': 'Jiangong Breakfast Restaurant', 'place_id': 'ChIJWRo0WWw2aDQRUuvo0P0CVS0'}, {'lat': 24.7959721, 'lng': 120.9982175, 'name': '肯德基 新竹清大餐廳', 'place_id': 'ChIJO_OCTg02aDQRcTy2wyrtLY4'}, {'lat': 24.7862836, 'lng': 120.9996931, 'name': 'LALA Kitchen', 'place_id': 'ChIJ1R1lGRA2aDQR0OU4Hv0sMnU'}, {'lat': 24.796304, 'lng': 120.9993449, 'name': '微笑的魚', 'place_id': 'ChIJeXQ7VG02aDQR2WlUvNapuS8'}]
	for result in results['results']:
		datas.append({
			'lat': result['geometry']['location']['lat'],
			'lng': result['geometry']['location']['lng'],
			'name': result['name'],
			'place_id': result['place_id']
		})
	correctFront, correctLeft, correctBack, correctRight = findByDirection(degree, latNlng, datas)
	stage = 0 # change when longpress
	stage1_index = 0
	stage2_index = 0
	kinds = ['餐廳', '建築', '商店', '公車站'] # 0: stop, 1: inKind, 2: option(front, left, back, right)

	names = []
	names.append('Front')
	for i in range(correctFront):
		names.append(i['name'])
	names.append('Right')
	for i in range(correctRight):
		names.append(i['name'])
	names.append('Left')
	for i in range(correctLeft):
		names.append(i['name'])
	names.append('Back')
	for i in range(correctBack):
		names.append(i['name'])



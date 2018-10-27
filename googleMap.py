import sys
import googlemaps
import pandas as pd
import time

def getData(lat, lng):
	googleMapKey = sys.argv[1]
	gmaps = googlemaps.Client(key = googleMapKey)
	loc = {'lat': lat, 'lng': lng}
	query_result = gmaps.places_nearby(keyword = "restaurant",location = loc, radius = 200)
	result = []
	for i in query_result['results']:
		result.append(i['name'])
	for place in result:
		print(place)
	return query_result
	

if __name__ == '__main__':
	getData(24.7871229, 120.9967369)['results']
	datas = []
	for result in getData(24.7871229, 120.9967369)['results']:
		datas.append({
			'location': result['geometry']['location'],
			'name': result['name'],
			'place_id': result['place_id']
		})
	for data in datas:
		print("place data:")
		print(data)


import sys
import googlemaps
import pandas as pd
import time

googleMapKey = sys.argv[1]
gmaps = googlemaps.Client(key = googleMapKey)

def getData(lat, lng):
	loc = {'lat': lat, 'lng': lng}
	query_result = gmaps.places_nearby(keyword = "restaurant",location = loc, radius = 200)
	result = []
	for i in query_result['results']:
		result.append(i['name'])
	for place in result:
		print(place)
	return query_result

def find_place(place_id):
	try:
		found_place = gmaps.place(place_id = place_id)
	except:
		print("ERROR: find_place")
	else:
		return found_place
	

if __name__ == '__main__':
	getData(24.7871229, 120.9967369)['results']
	datas = []
	for result in getData(24.7871229, 120.9967369)['results']:
		datas.append({
			'lan': result['geometry']['location']['lan'],
			'lng': result['geometry']['location']['lng'],
			'name': result['name'],
			'place_id': result['place_id']
		})
	print(datas)
	for data in datas:
		print("place data:")
		print(data)


import sys
import googlemaps
import pandas as pd
import time

googleMapKey = sys.argv[1]
gmaps = googlemaps.Client(key = googleMapKey)
def getData(lat, lng):
	try:
		loc = {'lat': lat, 'lng': lng}
		query_result = gmaps.places_nearby(keyword = "restaurant",location = loc, radius = 1000)
	except:
		print("ERROR: getData")
	else:
		return query_result

def find_place(place_id):
	try:
		found_place = gmaps.place(place_id = place_id)
	except:
		print("ERROR: find_place")
	else:
		return found_place
	

if __name__ == '__main__':
	results = getData(24.7871229, 120.9967369)
	datas = []
	for result in results['results']:
		datas.append({
			'lat': result['geometry']['location']['lat'],
			'lng': result['geometry']['location']['lng'],
			'name': result['name'],
			'place_id': result['place_id']
		})
	print(datas)
	for data in datas:
		print("place data:")
		print(data)


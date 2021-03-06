import sys
import googlemaps
import pandas as pd
import time
from expressData import *
from controller import *

if len(sys.argv) == 2:
	googleMapKey = sys.argv[1]
elif len(sys.argv) == 1:
	googleMapKey = "AIzaSyCq6_Zryl4bgEIk_f8NDv7A3-niGGfuKNM"
else:
	exit(-1)
gmaps = googlemaps.Client(key = googleMapKey)
Exceptions = googlemaps.exceptions

def getData(lat, lng, key):
	try:
		loc = {'lat': lat, 'lng': lng}
		query_result = gmaps.places_nearby(keyword = key,location = loc, radius = 1000)
	except (Exceptions.ApiError, Exceptions.TransportError, Exceptions.HTTPError, Exceptions.Timeout):
		print("ERROR: getData")
	else:
		return query_result

if __name__ == '__main__':
	stage = 0 # change when longpress
	stage1_index = 0
	stage2_index = 0
	kinds = ['Restaurant', 'Building', 'Store', 'Bus stop'] # 0: stop, 1: inKind, 2: option(front, left, back, right)
	
	input_key = -1
	while True:
		input_key = int(input('input press: '))
		if input_key == 0:
			if stage == 0:
				stage, stage1_index = longPress(stage, stage1_index)
				latNlng = [24.7871229, 120.9967369]
				degree = 0
				speak(kinds[0])
			elif stage == 1:
				stage, stage2_index = longPress(stage, stage2_index)
				speak('loading')
				results = getData(latNlng[0], latNlng[1], kinds[stage1_index])
				datas = []
				for result in results['results']:
					datas.append({
						'lat': result['geometry']['location']['lat'],
						'lng': result['geometry']['location']['lng'],
						'name': result['name'],
						'place_id': result['place_id']
					})
				correctFront, correctLeft, correctBack, correctRight = findByDirection(degree, latNlng, datas)
				names = []
				names.append('Front')
				if len(correctFront):
					for i in correctFront:
						names.append(i['name'])
				names.append('Right')
				if len(correctRight):
					for i in correctRight:
						names.append(i['name'])
				names.append('Left')
				if len(correctLeft):
					for i in correctLeft:
						names.append(i['name'])
				names.append('Back')
				if len(correctBack):
					for i in correctBack:
						names.append(i['name'])
				speak('finish')
				speak(names[0])

		elif input_key == 1:
			if stage == 1:
				stage, stage1_index = changeOptions(stage, stage1_index, kinds)
			elif stage == 2:
				stage, stage2_index = changeOptions(stage, stage2_index, names)
		elif input_key == 2:
			stage, stage1_index, stage2_index = doublePress(stage, stage1_index, stage2_index)




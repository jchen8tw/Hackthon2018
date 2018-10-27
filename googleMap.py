import sys
import googlemaps
import time
from expressData import *
from controller import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
channel_1 = 13
channel_2 = 15
GPIO.setup(channel_1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(channel_2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
flag = 0

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

def functionshutdown():
	flag = 1


if __name__ == '__main__':
	stage = 0 # change when longpress
	stage1_index = 0
	stage2_index = 0
	kinds = ['Restaurant', 'Building', 'Store', 'Bus stop'] # 0: stop, 1: inKind, 2: option(front, left, back, right)
	
	GPIO.add_event_detect(channel_2, GPIO.FALLING, callback = functionshutdown)
	input_key = -1
	while True:
		if flag == 1:
			flag = 0
			stage, stage1_index, stage2_index = doublePress(stage, stage1_index, stage2_index)
			continue
		GPIO.wait_for_edge(channel_1, GPIO.FALLING)
		init_time = time.time()
		GPIO.wait_for_edge(channel_1, GPIO.RISING)
		current_time = time.time()
		if init_time - current_time >= 2:
			input_key = 0
		else:
			input_key = 1
		#input_key = int(input('input press: '))
		if input_key == 0:
			if stage == 0:
				speak('loading')
				stage, stage1_index = longPress(stage, stage1_index)
				latNlng = [24.7871229, 120.9967369]
				#print(latNlng)
				degree = 0
				direction = 'left'
				#datas = [{'lat': 23.7871229, 'lng': 120.9967369, 'name': '橄欖樹廚房', 'place_id': 'ChIJC9294xI2aDQRM3uLb9yfs7c'}, {'lat': 24.7893222, 'lng': 121.0027161, 'name': '麗緻巴賽麗法式餐廳 Brasserie Liz Restaurant', 'place_id': 'ChIJ7ThJZRE2aDQRv4DM1CFoKko'}, {'lat': 24.7958397, 'lng': 120.9984181, 'name': 'Mercuries Beef Noodle Restaurant', 'place_id': 'ChIJEX6W6sE1aDQRiYUjziT0hvI'}, {'lat': 24.7929314, 'lng': 121.0020218, 'name': 'Chengdu Lao Guo Beef Noodle Restaurant', 'place_id': 'ChIJe97NARM2aDQR2D8S7rJCTmQ'}, {'lat': 24.7796415, 'lng': 121.0057166, 'name': 'Burger King Hsinchu Science Park', 'place_id': 'ChIJk5rJxR42aDQRUs45baSmRHI'}, {'lat': 24.7916199, 'lng': 121.0069856, 'name': 'Da Nei Beef Noodle Restaurant', 'place_id': 'ChIJuX1M-BQ2aDQRPsiLb3VYdvI'}, {'lat': 24.7893331, 'lng': 121.0031303, 'name': '暐順麗緻-聖香樓', 'place_id': 'ChIJj0ysbhE2aDQR6Epr9cAIXAY'}, {'lat': 24.7964685, 'lng': 121.0022224, 'name': 'Zhan Ramen Restaurant', 'place_id': 'ChIJ4wzs3mw2aDQRbki_3VkwnIo'}, {'lat': 24.7977669, 'lng': 120.9981233, 'name': 'Jiangong Breakfast Restaurant', 'place_id': 'ChIJWRo0WWw2aDQRUuvo0P0CVS0'}, {'lat': 24.7959721, 'lng': 120.9982175, 'name': '肯德基 新竹清大餐廳', 'place_id': 'ChIJO_OCTg02aDQRcTy2wyrtLY4'}, {'lat': 24.7862836, 'lng': 120.9996931, 'name': 'LALA Kitchen', 'place_id': 'ChIJ1R1lGRA2aDQR0OU4Hv0sMnU'}, {'lat': 24.796304, 'lng': 120.9993449, 'name': '微笑的魚', 'place_id': 'ChIJeXQ7VG02aDQR2WlUvNapuS8'}]
				results = getData(latNlng[0], latNlng[1])
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
				speak('finish, press 1 to select option')
			elif stage == 1:
				stage, stage2_index = longPress(stage, stage2_index)
		elif input_key == 1:
			if stage == 1:
				stage, stage1_index = changeOptions(stage, stage1_index, kinds)
			elif stage == 2:
				stage, stage2_index = changeOptions(stage, stage2_index, names)




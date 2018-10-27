import math
import numpy as np
def checkPos(degree, latNlng, des_lat, dest_lng):
	unit_vector = np.array([math.cos(degree), math.sin(degree)])
	des_vector = np.array([des_lat - latNlng[0], dest_lng - latNlng[1]])
	check = np.dot(unit_vector, des_vector)
	if check >= 0:
		return True
	else:
		return False
def expressData(direction, datas, latNlng, lat, lng):
	if direction == 'front':
		degree = degree
	elif direction == 'left':
		degree = (degree + 270) % 360
	elif direction == 'right':
		degree = (degree + 90) % 360
	elif direction == 'back':
		degree = (degree + 180) % 360
	correctData = []
	for data in datas:
		if checkPos(degree, latNlng, data['lat'], data['lng']):
			correctData.append(data)
	if len(correctData):
		return True
	else:
		return False


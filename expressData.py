import math
import numpy as np
def checkPos(degree, latNlng, des_lat, dest_lng, viewPointDegree):
	unit_vector = np.array([math.cos(degree), math.sin(degree)])
	des_vector = np.array([des_lat - latNlng[0], dest_lng - latNlng[1]])
	check = np.dot(unit_vector, des_vector)
	cosine = check / (np.sqrt(np.square(unit_vector).sum()) * np.sqrt(np.square(des_vector).sum()))
	des_degree = math.acos(cosine) / (2 * math.pi) * 360
	if des_degree <= viewPointDegree / 2:
		return True
	else:
		return False
def expressData(direction, degree, datas, latNlng, correctData, viewPointDegree):
	correctDegree = 0
	if direction == 'front':
		correctDegree = degree
	elif direction == 'left':
		correctDegree = (degree + 270) % 360
	elif direction == 'right':
		correctDegree = (degree + 90) % 360
	elif direction == 'back':
		correctDegree = (degree + 180) % 360
	for data in datas:
		if checkPos(correctDegree, latNlng, data['lat'], data['lng'], viewPointDegree):
			correctData.append(data)
	if len(correctData):
		return True
	else:
		return False


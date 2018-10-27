import math
import numpy as np
def checkPos(_degree, latNlng, des_lat, dest_lng, viewPointDegree = 90):
	degree = _degree * math.pi / 180
	unit_vector = np.array([math.cos(degree), math.sin(degree)])
	des_vector = np.array([des_lat - latNlng[0], dest_lng - latNlng[1]])
	check = np.dot(unit_vector, des_vector)
	cosine = check / (np.sqrt(np.square(unit_vector).sum()) * np.sqrt(np.square(des_vector).sum()))
	des_degree = math.acos(cosine) / (2 * math.pi) * 360
	if des_degree <= viewPointDegree / 2:
		return True
	else:
		return False
def findByDirection(degree, latNlng, datas):
	correctFront = []
	correctLeft = []
	correctBack = []
	correctRight = []
	for data in datas:
		if checkPos(degree, latNlng, data['lat'], data['lng'], 90):
			correctFront.append(data)
		elif checkPos((degree + 270) % 360, latNlng, data['lat'], data['lng'], 90):
			correctLeft.append(data)
		elif checkPos((degree + 90) % 360, latNlng, data['lat'], data['lng'], 90):
			correctRight.append(data)
		elif checkPos((degree + 180) % 360, latNlng, data['lat'], data['lng'], 90):
			correctBack.append(data)
	return (correctFront, correctLeft, correctBack, correctRight)


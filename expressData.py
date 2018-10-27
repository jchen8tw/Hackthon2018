import math
import numpy as np
def expressData(degree, lat, lng, des_lat, dest_lng):
	unit_vector = np.array([math.cos(degree), math.sin(degree)])
	des_vector = np.array([des_lat - lat, dest_lng - lng])
	check = np.dot(unit_vector, des_vector)
	if check >= 0:
		return True
	else:
		return False
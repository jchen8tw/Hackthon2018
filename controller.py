from google_voice import * 

def speak(inp):
    print('\tspeak:', inp)
    string_to_google(inp)

def changeOptions(stage, index, currentList):
    index += 1
    if index == len(currentList):
        index = 0
    speak(currentList[index])
    return stage, index

def longPress(stage, index):
    stage = stage + 1
    index = 0
    if stage == 4:
        stage = 0
    return stage, index

def doublePress(stage, index1, index2):
	stage = 0
	index1 = 0
	index2 = 0
	speak('exit')
	return stage, index1, index2

def leadMe(degree, latNlng, lat, lng):
    toDirectVector = np.array([lng - latNlng[1], lat - latNlng[0]])
    orientVector = np.array([math.cos((90 - degree) * math.pi / 180), math.sin((90 - degree) * math.pi / 180)])
    cosTheta = np.dot(orientVector, toDirectVector) / np.sqrt(np.square(orientVector).sum()) * np.sqrt(np.square(toDirectVector).sum())
    cross = np.cross(orientVector, toDirectVector)
    if cosTheta > 0:
        if cross > 0:
            speak("Turn Left for degree" + str(math.acos(cosTheta)) + "and walk for" + str(sqrt(np.square(toDirectVector).sum())))
        else:
            speak("Turn Right for degree" + str(math.acos(cosTheta)) + "and walk for" + str(sqrt(np.square(toDirectVector).sum())))
    else:
        speak("It is in back of you")


    

from google_voice import * 
import numpy as np
import math

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

def leadMe(_degree, latNlng, des_lat, des_lng):
    # toDirectVector = np.array([lng - latNlng[1], lat - latNlng[0]])
    # orientVector = np.array([math.cos((90 - degree) * math.pi / 180), math.sin((90 - degree) * math.pi / 180)])
    # cosTheta = np.dot(orientVector, toDirectVector) / np.sqrt(np.square(orientVector).sum()) / np.sqrt(np.square(toDirectVector).sum())
    # cross = np.cross(orientVector, toDirectVector)
    degree = _degree * math.pi / 180
    unit_vector = np.array([math.cos(degree), math.sin(degree)])
    des_vector = np.array([des_lat - latNlng[0], dest_lng - latNlng[1]])
    check = np.dot(unit_vector, des_vector)
    cosine = check / (np.sqrt(np.square(unit_vector).sum()) * np.sqrt(np.square(des_vector).sum()))
    des_degree = math.acos(cosine) / (2 * math.pi) * 
    cross = np.cross(unit_vector, des_vector)
    if des_degree <= 90:
        if cross > 0:
            speak("Turn Left for degree " + str(int(des_degree)) + " and walk straight")
        else:
            speak("Turn Right for degree " + str(int(des_degree) + " and walk straight")
    else:
        speak("It is in back of you")
    # if cosTheta < 0:
    #     if cosTheta < -1:
    #         cosTheta = -0.99999
    #     if cross < 0:
    #         speak("Turn Left for degree " + str(int(math.acos(cosTheta)*180/math.pi)) + " and walk straight")
    #     else:
    #         speak("Turn Right for degree " + str(int(math.acos(cosTheta))*180/math.pi) + " and walk straight")
    # else:
    #     speak("It is in back of you")


    

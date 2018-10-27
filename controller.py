def speak(inp):
    print('\tspeak:', inp)

def changeOptions(stage, index, currentList):
    index += 1
    if index == len(currentList):
        index = 0
    speak(currentList[index])
    return stage, index

def longPress(stage, index):
    stage = stage + 1
    index = 0
    if stage == 3:
        stage = 0
    return stage, index

def doublePress(stage, index1, index2):
	stage = 0
	index1 = 0
	index2 = 0
	speak('exit')
	return stage, index1, index2
    
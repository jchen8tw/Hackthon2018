def speak(inp):
    print(inp, end = ', ')

def changeOptions(stage, index, currentList):
    index += 1
    if index == len(currentList):
        index = 0
    speak(currentList[index])

def longPress(stage, index):
    stage += 1
    index = 0
    if stage == 3:
        stage = 0
    
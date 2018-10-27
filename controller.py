stage = 0 # change when longpress
stage1_index = 0
stage2_index = 0
correctFront, correctLeft, correctBack, correctRight = [], [], [], []
kinds = ['餐廳', '建築', '商店', '公車站'] # 0: stop, 1: inKind, 2: option(front, left, back, right)

names = []
names.append('Front')
for i in range(correctFront):
    names.append(i['name'])
names.append('Right')
for i in range(correctRight):
    names.append(i['name'])
names.append('Left')
for i in range(correctLeft):
    names.append(i['name'])
names.append('Back')
for i in range(correctBack):
    names.append(i['name'])
    
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
    
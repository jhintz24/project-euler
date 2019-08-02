
def getNameIntValue(name):
    offset = 64 #ASCII value of 'A' is 65
    sum = 0
    for char in name:
        sum = sum + (ord(char)-offset)
    return sum


def ansFunction(nameList):
    nameList.sort()
    sum = 0

    for x in range(len(nameList)):
        sum = sum + ((x+1) * getNameIntValue(nameList[x]))

    return sum



names = []
with open('input-files/p022_names.txt','r') as f:
    names = f.read().replace('"','').split(",")

print ansFunction(names)
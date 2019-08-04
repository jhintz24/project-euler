
def ansFunction():
    ansDict = {}
    for a in range(2,101):
        for b in range(2, 101):
            ansDict[a**b] = 1
    return len(ansDict.keys())

print ansFunction()
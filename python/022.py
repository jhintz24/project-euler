#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 022
#
# Python 3.7.4
#

import time
import EulerLib as lib

def ansFunction(nameList):
    nameList.sort()
    sum = 0

    for x in range(len(nameList)):
        sum = sum + ((x+1) * lib.getWordIntValue(nameList[x]))

    return sum


names = []
with open('../input-files/p022_names.txt','r') as f:
    names = f.read().replace('"','').split(",")


startTime = time.time()
print('Answer: ', ansFunction(names))
endTime = time.time()
print ('Time: ', endTime - startTime)
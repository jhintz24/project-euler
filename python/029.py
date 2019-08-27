#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 029
#
# Python 3.7.4
#

import time

def ansFunction():

    ansDict = {}
    for a in range(2,101):
        for b in range(2, 101):
            ansDict[a**b] = 1

    return len(ansDict.keys())


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)
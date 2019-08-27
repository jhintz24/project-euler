#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 028
#
# Python 3.7.4
#

import time

def ansFunction(dimensionLimit):

    sum = 1
    currentDimension = 2
    sideSize = 3
    count = 1

    for x in range(2,(dimensionLimit**2)+1):

        if x > sideSize ** 2:
            sideSize += 2
            currentDimension += 2

        if count == currentDimension:
            #print(x)
            sum += x
            count = 1
        else:
            count += 1

    return sum


startTime = time.time()
print('Answer: ', ansFunction(1001))
endTime = time.time()
print ('Time: ', endTime - startTime)



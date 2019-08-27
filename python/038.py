#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 038
#
# Python 3.7.4
#

import time
import EulerLib as lib

def ansFunction():

    largestPandigital = 0

    for i in range(1,10000): # Semi-arbitrary boundary
        x = 1
        pandigital = ''
        while True:
            pandigital += str(i*x)

            if len(pandigital) > 9:
                break

            if lib.isPandigital(pandigital) and int(pandigital) > largestPandigital:
                largestPandigital = int(pandigital)
            x += 1

    return largestPandigital


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)
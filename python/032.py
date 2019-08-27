#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 032
#
# Python 3.7.4
#

import time
import EulerLib as lib


def ansFunction():

    pandigitals = {}
    for a in range(1,5000): #5,000 is slightly arbitrary. Need proof
        for b in range(1,5000):
            product = a * b
            combo = str(product) + str(a) + str(b)
            if lib.isPandigital(combo):
                pandigitals[product] = 1

    return sum(pandigitals.keys())


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)

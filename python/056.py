#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 056
#
# Python 3.7.4
#

import time

def ansFunction():

    max = 0
    for a in range(1, 100):
        for b in range(1, 100):
            c = a ** b
            c = list(str(c))

            for i in range(len(c)):
                c[i] = int(c[i])

            if sum(c) > max:
                max = sum(c)
    return max


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)
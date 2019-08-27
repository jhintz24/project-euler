#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 052
#
# Python 3.7.4
#

import time

def containSameDigits(a, b, c, d, e):
    return sorted(str(a)) == sorted(str(b)) == sorted(str(c)) == sorted(str(d)) == sorted(str(e))

def ansFunction():

    x = 1
    while True:
        if containSameDigits((2*x), (3*x), (4*x), (5*x), (6*x)):
            return x
        x += 1


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)
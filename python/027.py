#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 027
#
# Python 3.7.4
#

import time
import EulerLib as lib

def getConsecutiveN(a, b):

    n = 0
    while True:
        result = (n ** 2) + (a * n) + b
        if lib.isPrime(result):
            n += 1
        else:
            break
    return n


def ansFunction():

    aLimit = 1000
    bLimit = 1001

    #b must be prime
    bPrimes = []
    for x in range (2,bLimit):
        if lib.isPrime(x):
            bPrimes.append(x)

    largestN = 0
    bestA = 0
    bestB = 0

    for a in range(-(aLimit-1),aLimit,2): #a must be odd
        for b in bPrimes:
            n1 = getConsecutiveN(a, b)
            n2 = getConsecutiveN(a, -b)

            if n1 > largestN:
                largestN = n1
                bestA = a
                bestB = b
            if n2 > largestN:
                largestN = n2
                bestA = a
                bestB = -b

    return bestA * bestB


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)






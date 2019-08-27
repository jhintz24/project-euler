#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 058
#
# Python 3.7.4
#

import time
import EulerLib as lib

# Take the core logic from problem 028
# Takes a few minutes...
def ansFunction():

    primes = []
    nonPrimes = [1]
    currentDimension = 2
    sideSize = 3
    count = 1
    x = 2

    while True:

        if x > sideSize ** 2:
            if len(primes) > 0 and len(nonPrimes) > 0:
                ratio = float(len(primes)) / float(len(primes) + len(nonPrimes))
                #print(x, sideSize, ratio)
                if ratio < .1:
                    return sideSize

            sideSize += 2
            currentDimension += 2

        if count == currentDimension:
            if lib.isPrime(x):
                primes.append(x)
            else:
                nonPrimes.append(x)

            count = 1
        else:
            count += 1

        x += 1


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)
#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 050
#
# Python 3.7.4
#

import time
import EulerLib as lib

def ansFunction():

    primes = [2]
    longestChain = 0
    longestChainPrime = 0

    for x in range(3,1000000, 2):
        #print(x)
        if lib.isPrime(x):
            for z in range(len(primes)):
                y = z
                sum = 0
                count = 0

                while y < len(primes):
                    sum += primes[y]
                    count += 1
                    if sum == x and count > longestChain:
                        longestChain = count
                        longestChainPrime = x
                        break
                    if sum > x:
                        break
                    y += 1
            primes.append(x)

    return longestChainPrime


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)

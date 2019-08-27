#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 046
#
# Python 3.7.4
#

import time
import EulerLib as lib

def ansFunction():

    x = 3
    primes = [2]
    while True:
        if lib.isPrime(x):
            primes.append(x)
        else:
            flag = 0

            for prime in primes:
                y = 1
                calculation = 0

                while calculation < x:
                    calculation = prime + (2 * (y ** 2))
                    if calculation == x:
                        flag = 1
                        break
                    y += 1
                if flag == 1:
                    break
            if flag == 0:
                return x
        x += 2


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)
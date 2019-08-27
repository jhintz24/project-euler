#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 035
#
# Python 3.7.4
#

import time
import EulerLib as lib

def ansFunction(n):

    circularPrimes = [2]
    for x in range(3,n,2):
        if lib.isPrime(x):

            if len(str(x)) == 1:
                circularPrimes.append(x)
            else:
                rotatedNumber = str(x)
                rotations = [int(rotatedNumber)]

                for y in range(len(rotatedNumber)-1):
                    firstDigit = rotatedNumber[0]
                    rotatedNumber = rotatedNumber[1:]
                    rotatedNumber = rotatedNumber + firstDigit
                    if not lib.isPrime(int(rotatedNumber)):
                        break
                    if x != int(rotatedNumber):
                        rotations.append(int(rotatedNumber))
                else:
                    for number in rotations:
                        if number not in circularPrimes:
                            circularPrimes.append(number)

    return len(circularPrimes)


startTime = time.time()
print('Answer: ', ansFunction(1000000))
endTime = time.time()
print ('Time: ', endTime - startTime)
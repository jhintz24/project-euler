#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 026
#
# Python 3.7.4
#

import time

#Slow for n > 1,000
def ansFunction(n):

    d = 1
    largest = 0

    for x in range(1, n):
        numerator = 1
        remainders = []

        while numerator < x:
            numerator *= 10

        while True:
            remainder = numerator % x
            if remainder == 0:
                break

            if remainder in remainders:
                index = remainders.index(remainder)
                repeating = len(remainders[index:])
                if repeating > largest:
                    d = x
                    largest = repeating
                break

            remainders.append(remainder)

            numerator = remainder
            while numerator < x:
                numerator *= 10

    return d


startTime = time.time()
print('Answer: ', ansFunction(1000))
endTime = time.time()
print ('Time: ', endTime - startTime)


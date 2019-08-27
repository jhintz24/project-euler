#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 041
#
# Python 3.7.4
#

import time

import itertools
import EulerLib as lib

def ansFunction():

    digits = '123456789'
    largestPrime = 0

    for x in range(len(digits)):
        for combo in itertools.permutations(digits,len(digits)):
            number = ''

            for digit in combo:
                number += digit
            number = int(number)

            if lib.isPrime(number) and number > largestPrime:
                largestPrime = number

        if largestPrime > 0:
            return largestPrime

        digits = digits[:-1]


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)
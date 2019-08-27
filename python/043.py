#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 043
#
# Python 3.7.4
#

import time
import itertools

def ansFunction():

    digits = '0123456789'
    sum = 0

    for combo in itertools.permutations(digits,len(digits)):
        if int("".join(combo[1:4])) % 2 == 0:
            if int("".join(combo[2:5])) % 3 == 0:
                if int("".join(combo[3:6])) % 5 == 0:
                    if int("".join(combo[4:7])) % 7 == 0:
                        if int("".join(combo[5:8])) % 11 == 0:
                            if int("".join(combo[6:9])) % 13 == 0:
                                if int("".join(combo[7:10])) % 17 == 0:
                                    sum += int("".join(combo))

    return sum


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)
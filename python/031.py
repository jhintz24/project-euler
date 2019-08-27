#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 031
#
# Python 3.7.4
#

import time

def ansFunction():

    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    combinations = [0] * 200
    combinations = [1] + combinations

    for coin in coins:
        for x in range(len(combinations) - coin):
            combinations[x + coin] += combinations[x]

    return combinations[-1]


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)
#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 051
#
# Python 3.7.4
#

import time
import EulerLib as lib
import itertools

def getDuplicateNumberPositions(n):

    n = str(n)
    positions = []
    dict = {}

    for i in range(10):
        temp = []
        for j in range(len(n)):
            if str(i) == n[j]:
                temp.append(j)
        dict[i] = temp

    for num in dict:
        pos = dict[num]
        for x in range(2, len(pos) + 1):
            for y in itertools.combinations(dict[num], x):
                positions.append(y)

    return positions

def ansFunction():

    dict = {}
    x = 100001 # Educated guess starting number

    while True:
        if lib.isPrime(x):
            positions = getDuplicateNumberPositions(x)
            if len(positions) > 0:
                length = len(str(x))
                if length not in dict:
                    dict[len(str(x))] = {}

                for position in positions:
                    maskedX = str(x)
                    for index in position:
                        maskedX = maskedX[:index] + '*' + maskedX[index + 1:]
                    if maskedX in dict[len(str(x))]:
                        dict[len(str(x))][maskedX].append(x)
                        if len(dict[len(str(x))][maskedX]) == 8:
                            return dict[len(str(x))][maskedX]
                    else:
                        dict[len(str(x))][maskedX] = [x]
        x += 2


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)


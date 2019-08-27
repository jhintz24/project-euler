#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 045
#
# Python 3.7.4
#

import time

# Should probably use a yield statement here
def ansFunction():
    triangleNumbers = []
    pentagonalNumbers = []
    hexagonalNumbers = []

    triN = 1
    penN = 1
    hexN = 1

    while True:
        nextHex = hexN * ((2 * hexN) -1)
        hexagonalNumbers.append(nextHex)

        while len(pentagonalNumbers) == 0 or nextHex > pentagonalNumbers[-1]:
            nextPen = penN * ((3 * penN) -1) // 2
            pentagonalNumbers.append(nextPen)

            while len(triangleNumbers) == 0 or nextPen > triangleNumbers[-1]:
                nextTri = triN *(triN + 1) // 2
                triangleNumbers.append(nextTri)
                triN += 1

            penN += 1

        if hexagonalNumbers[-1] == pentagonalNumbers[-1] == triangleNumbers[-1]:
            if triangleNumbers[-1] > 40755:
                return triangleNumbers[-1]

        hexN += 1


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)

#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 059
#
# Python 3.7.4
#

import time

# We can use the core logic from problem 018
def ansFunction(tri):

    tri = tri[::-1]
    newTri = []
    for i in range(len(tri)):
        newTri.append([])
        for j in range(len(tri[i])):
            if i == 0:
                newTri[i].append(tri[i][j])
            else:
                newTri[i].append(tri[i][j] + max(newTri[i-1][j], newTri[i-1][j+1]))

    return newTri[-1][-1]


triangle = []
with open('../input-files/p067_triangle.txt') as f:
    for line in f:
        l = line.split(' ')
        for i in range(len(l)):
            l[i] = int(l[i])
        triangle.append(l)


startTime = time.time()
print('Answer: ', ansFunction(triangle))
endTime = time.time()
print ('Time: ', endTime - startTime)
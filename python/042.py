#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 042
#
# Python 3.7.4
#

import time
import EulerLib as lib

def ansFunction(wordList):

    count = 0
    n = 2
    triangleNumbers = [1]
    for word in wordList:
        wordValue = lib.getWordIntValue(word)
        if wordValue <= triangleNumbers[-1] and wordValue in triangleNumbers:
            count += 1
        elif wordValue > triangleNumbers[-1]:
            while True:
                triangleNumbers.append(.5 * n * (n + 1))
                if wordValue == triangleNumbers[-1]:
                    count += 1
                    break
                if wordValue < triangleNumbers[-1]:
                    break
                n += 1

    return count



words = []
with open('../input-files/p042_words.txt','r') as f:
    words = f.read().replace('"','').split(",")


startTime = time.time()
print('Answer: ', ansFunction(words))
endTime = time.time()
print ('Time: ', endTime - startTime)
import math
import itertools

#We can use the core (brute-force) logic from problem 046.
def isPrime(n):

    if n <= 1: #Modification in problem 037
        return False

    if n == 2: #Modification in problem 037
        return True

    if n % 2 == 0: #Modification from problem 027
        return False

    # Only search until the sqrt of the current number, increasing by two (only odd numbers)
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False

    return True

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
    x = 100001 #educated guess starting number

    while True:
        if isPrime(x):
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

print ansFunction()


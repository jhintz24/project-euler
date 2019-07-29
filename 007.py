import math

#More intelligent than brute force, but still slow for large n
def ansFunction(n):
    count = 1
    currentNumber = 1

    while count <= n:
        if currentNumber < 3:
            currentNumber = currentNumber + 1
        else:
            currentNumber = currentNumber + 2

        #Only search until the sqrt of the current number, increasing by two (only odd numbers)
        for x in range(3,int(math.sqrt(currentNumber))+1,2):
            if currentNumber % x == 0:
                break;
        else:
            count = count + 1

    return currentNumber

print ansFunction(10001)
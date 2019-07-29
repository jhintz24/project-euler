import math

def getDivisors(n):
    x = 1
    count = 0
    while x < math.sqrt(n):
        if n % x == 0:
            if n/x == x:
                count = count + 1
            else:
                count = count + 2
        x = x + 1
    return count

def ansFunction(n):

    x = 1
    y = 1
    while True:
        z = getDivisors(y)
        if z > n:
            return y
        x = x + 1
        y = y + x

print ansFunction(500)
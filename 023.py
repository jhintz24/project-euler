import math

# Use getDivisors function from problem 021
def getDivisors(n):
    x = 1
    divisors = []
    while x <= math.sqrt(n):
        if n % x == 0:
            if x not in divisors:
                divisors.append(x)
            if n/x not in divisors and n/x != n: # We do not include n
                divisors.append(n/x)
        x = x + 1
    return divisors

def ansFunction():

    abundantNumbers = []
    for x in range(1,28124): #There is a clever way to do this
        divisors = getDivisors(x)
        if sum(divisors) > x:
            abundantNumbers.append(x)

    ans = [False] * 28124
    for x in range(len(abundantNumbers)):
        for y in range(x,len(abundantNumbers)):
            if abundantNumbers[x] + abundantNumbers[y] < 28124:
                ans[abundantNumbers[x] + abundantNumbers[y]] = True
            else:
                break

    return sum(i for (i, j) in enumerate(ans) if not j)

print ansFunction()

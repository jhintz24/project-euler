
#Straightforward and simple. No clever math needed.
def fibonacci(n):
    returnSum = 0
    n0 = 0
    n1 = 1

    for x in range(1, n):
        nNext = n0 + n1
        if nNext > n:
            break
        if nNext % 2 == 0:
            returnSum = returnSum + nNext
        n0 = n1
        n1 = nNext
    return returnSum

print fibonacci(4000000)
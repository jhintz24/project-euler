

def fibonacci(n):
    sum = 0
    n0 = 0
    n1 = 1
    nNext = 0

    for x in range(1, n):
        nNext = n0 + n1
        if nNext > n:
            break
        if nNext % 2 == 0:
            sum = sum + nNext
        n0 = n1
        n1 = nNext
    return sum

print fibonacci(4000000)
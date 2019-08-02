
def fibonacci(n):
    f1 = 1
    f2 = 1
    index = 2
    fNext = 0
    while len(str(fNext)) < n:
        fNext = f1 + f2
        f1 = f2
        f2 = fNext
        index += 1

    return index

print fibonacci(1000)

def ansFunction(n):
    sum = 0
    for x in range(1, n):
        sum += (x ** x)

    return str(sum)[-10:]

print ansFunction(1001)
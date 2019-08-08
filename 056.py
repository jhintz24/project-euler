
def ansFunction():
    max = 0
    for a in range(1, 100):
        for b in range(1, 100):
            c = a ** b
            c = list(str(c))
            for i in range(len(c)):
                c[i] = int(c[i])
            if sum(c) > max:
                max = sum(c)
    return max

print ansFunction()
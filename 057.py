
#Need to work on this
def ansFunction(n):
    count = 0
    numer = 0
    denom = 1
    for x in range(n):
        numer, denom = denom, denom * 2 + numer
        if len(str(numer + denom)) > len(str(denom)):
            count += 1
    return count


print ansFunction(1000)
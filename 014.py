
def ansFunction(n):
    dict = {}
    max = 0
    start = 1

    for x in range(1,n):
        y = findChainLength(x, dict)
        print x,y
        if y > max:
            start = x
            max = y

    return start

def findChainLength(x, dict):
    if x == 1:
        return 1
    if x % 2 == 0:
        next = x / 2
    else:
        next = 3 * x + 1

    if next in dict:
        return dict[next] + 1
    else:
        dict[x] = findChainLength(next,dict) + 1

    return dict[x]

print ansFunction(1000000)
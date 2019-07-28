
#Import largestPrime() from problem 003
def largestPrime(n):
    x = 2
    while n > x:
        if n % x == 0:
            n = n/x
        else:
            x = x + 1
    return x

def smallestNumber():
    ans = 1
    for x in range(2,21):
        if ans % x != 0:
            ans = ans * largestPrime(x)
    return ans


print smallestNumber()
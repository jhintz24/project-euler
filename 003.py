
#Simple and straightforward. No clever math needed.
def largestPrime(n):
    x = 2
    while n > x:
        if n % x == 0:
            n = n/x
        else:
            x = x + 1

    return x

print largestPrime(600851475143)
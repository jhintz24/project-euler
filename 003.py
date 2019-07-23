def largestPrime(n):
    x = 2
    primeFactors = []
    while n >= x:
        if n % x == 0:
            primeFactors.append(x)
            n = n/x
        else:
            x = x + 1

    return primeFactors[-1]

print largestPrime(600851475143)
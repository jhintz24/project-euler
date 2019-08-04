import math

#We can use the core (brute-force) logic from problem 007.
def isPrime(n):

    if n < 0: #Modification from problem 007
        return False

    if n % 2 == 0: #Modification from problem 027
        return False

    # Only search until the sqrt of the current number, increasing by two (only odd numbers)
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False

    return True

def ansFunction(n):
    circularPrimes = [2]
    for x in range(3,n,2):
        if isPrime(x):
            if len(str(x)) == 1:
                circularPrimes.append(x)
            else:
                rotatedNumber = str(x)
                rotations = [int(rotatedNumber)]
                for y in range(len(rotatedNumber)-1):
                    firstDigit = rotatedNumber[0]
                    rotatedNumber = rotatedNumber[1:]
                    rotatedNumber = rotatedNumber + firstDigit
                    if not isPrime(int(rotatedNumber)):
                        break
                    if x != int(rotatedNumber):
                        rotations.append(int(rotatedNumber))
                else:
                    for number in rotations:
                        if number not in circularPrimes:
                            circularPrimes.append(number)

    return len(circularPrimes)

print ansFunction(1000000)
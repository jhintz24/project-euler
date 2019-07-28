#Helper function
def isPalindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False

#Brute force is fast for only 3 digits
def largestPalindrome():
    n1 = 999
    largest = 0
    for x in range(n1, 99, -1):
        for y in range(x, 99, -1):
            z = x * y
            if isPalindrome(z):
                if z > largest:
                    largest = z
    return largest

print largestPalindrome()



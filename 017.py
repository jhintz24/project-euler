
ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

#Contains duplicate code. Can definitely be simplified.
def ansFunction(n):
    count = 0
    for x in range(1,n+1):
        string = ''
        if x <= 10:
            string = string + ones[x-1]
        elif x < 20:
            string = string + teens[x-11]
        elif x < 100:
            firstDigit = int(str(x)[0])
            secondDigit = int(str(x)[1])

            string = string + tens[firstDigit-2]
            if secondDigit % 10 != 0:
                string = string + ones[secondDigit-1]

        elif x < 1000:
            firstDigit = int(str(x)[0])
            string = string + ones[firstDigit-1] + 'hundred'

            if x % 100 != 0:
                string = string + 'and'
                secondDigits = int(str(x)[1:])

                if secondDigits <= 10:
                    string = string + ones[secondDigits - 1]
                elif secondDigits < 20:
                    string = string + teens[secondDigits - 11]
                else:
                    firstDigit = int(str(x)[1])
                    secondDigit = int(str(x)[2])

                    string = string + tens[firstDigit - 2]
                    if secondDigit % 10 != 0:
                        string = string + ones[secondDigit - 1]

        else:
            string = 'onethousand'

        print x, string
        count = count + len(string)
    return count

print ansFunction(1000)


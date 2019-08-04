
#Modified function from problem 022
def getWordIntValue(word):
    offset = 64 #ASCII value of 'A' is 65
    sum = 0
    for char in word:
        sum = sum + (ord(char)-offset)
    return sum

def ansFunction(wordList):
    count = 0
    n = 2
    triangleNumbers = [1]
    for word in wordList:
        wordValue = getWordIntValue(word)
        if wordValue <= triangleNumbers[-1] and wordValue in triangleNumbers:
            count += 1
        elif wordValue > triangleNumbers[-1]:
            while True:
                triangleNumbers.append(.5 * n * (n + 1))
                if wordValue == triangleNumbers[-1]:
                    count += 1
                    break
                if wordValue < triangleNumbers[-1]:
                    break
                n += 1
    return count



words = []
with open('input-files/p042_words.txt','r') as f:
    words = f.read().replace('"','').split(",")

print ansFunction(words)
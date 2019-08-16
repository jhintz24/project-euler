

def getWinner(player1, player2):

    suitDict = {
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    #Format player hands
    for x in range(len(player1)):
        player1Card = player1[x]
        player2Card = player2[x]

        if player1Card[0] in suitDict:
            player1[x] = str(suitDict[player1Card[0]]) + player1Card[1:]
        if player2Card[0] in suitDict:
            player2[x] = str(suitDict[player2Card[0]]) + player2Card[1:]

        player1[x] = (player1[x][0], player1[x][1])
        player2[x] = (player2[x][0], player2[x][1])

    print player1
    print player2

def getHighHand(hand):

    #Check for Royal Flush
    pass






pokerHands = []
with open('input-files/p054_poker.txt') as f:
    for line in f:
        hands = line.strip('\n').split(' ')
        pokerHands.append([hands[:5], hands[5:]])


count = 0
for hand in pokerHands:
    winner = getWinner(hand[0], hand[1])
    if winner == 1:
        count += 1
    break

print count
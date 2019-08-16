

# Hand values
ROYAL_FLUSH = 10
STRAIGHT_FLUSH = 9
FOUR_KIND = 8
FULL_HOUSE = 7
FLUSH = 6
STRAIGHT = 5
THREE_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

def getWinner(player1, player2):

    #Format hands first

    suitDict = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    formattedPlayer1 = []
    for card in player1:
        num = card[0]
        if num in suitDict:
            num = suitDict[num]
        else:
            num = int(card[0])

        suit = card[1]
        formattedPlayer1.append(Card(num, suit))

    formattedPlayer2 = []
    for card in player2:
        num = card[0]
        if num in suitDict:
            num = suitDict[num]
        else:
            num = int(card[0])

        suit = card[1]
        formattedPlayer2.append(Card(num, suit))

    player1 = sorted(formattedPlayer1, key=lambda card: card.number)
    player2 = sorted(formattedPlayer2, key=lambda card: card.number)

    # Get hands for each player
    player1Hand = getHand(player1)
    player2Hand = getHand(player2)



def getHand(cards):

    hand = {}

    #Check for Royal Flush
    numbers = {10, 11, 12, 13, 14}
    suit = ''
    flag = 0
    for card in cards:
        if card.number in numbers:
            numbers.remove(card.number)
        else:
            flag = 1
            break
        if suit == '':
            suit = card.suit
        elif suit != card.suit:
            flag = 1
            break

    if flag == 0:
        hand['hand'] = ROYAL_FLUSH
        return hand

    #Check for straight flush
    number = 0
    suit = ''
    flag = 0
    for card in cards:
        if number == 0:
            number = card.number
        elif card.number != number + 1:
            flag = 1
            break

        if suit == '':
            suit = card.suit
        elif suit != card.suit:
            flag = 1
            break

    if flag == 0:
        hand['hand'] = STRAIGHT_FLUSH
        hand['high'] = cards[-1].number
        return hand

    #Check for four of a kind
    number = 0
    count = 0
    for card in cards:
        if number == 0:
            number = card.number
            count = 1
        elif card.number == number:
            count += 1
            if count == 4:
                break
        elif card.number != number:
            number = 0
            count = 0

    if count == 4:
        hand['hand'] = FOUR_KIND
        hand['high'] = number
        for card in cards:
            if card.number != number:
                hand['nextHigh'] = card.number
                break
        return hand










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
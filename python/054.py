#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 054
#
# Python 3.7.4
#

import time

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

class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.hand = None
        self.highCard = None
        self.secondHighCard = None

def getWinner(player1, player2):

    # Format hands first
    valueDict = {
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    formattedPlayer1 = []
    for card in player1:
        formattedPlayer1.append((valueDict[card[0]], card[1]))

    formattedPlayer2 = []
    for card in player2:
        formattedPlayer2.append((valueDict[card[0]], card[1]))

    player1 = sorted(formattedPlayer1, key=lambda card: card[0])
    player2 = sorted(formattedPlayer2, key=lambda card: card[0])


    # Get hands for each player
    player1Hand = getHand(player1)
    player2Hand = getHand(player2)

    print('Player 1: ', player1Hand.cards, player1Hand.hand, player1Hand.highCard, player1Hand.secondHighCard)
    print('Player 2: ', player2Hand.cards, player2Hand.hand, player2Hand.highCard, player2Hand.secondHighCard)
    print('\n')

    # This part needs correction and fleshing out for all cases
    if player1Hand.hand > player2Hand.hand:
        return 1
    if player1Hand.hand == player2Hand.hand:
        if player1Hand.highCard > player2Hand.highCard:
            return 1
    return 2

def getHand(cards):

    hand = Hand(cards)

    # Check for Royal Flush
    numbers = {10, 11, 12, 13, 14}
    suit = ''
    flag = 0
    for card in cards:
        # Check number
        if card[0] in numbers:
            numbers.remove(card[0])
        else:
            flag = 1
            break

        # Check suit
        if suit == '':
            suit = card[1]
        elif suit != card[1]:
            flag = 1
            break

    if flag == 0:
        hand.hand = ROYAL_FLUSH
        return hand

    # Check for straight flush
    number = 0
    suit = ''
    flag = 0
    for card in cards:
        if number == 0:
            number = card[0]
        elif card[0] == number + 1:
            number += 1
        else:
            flag = 1
            break

        if suit == '':
            suit = card[1]
        elif suit != card[1]:
            flag = 1
            break

    if flag == 0:
        hand.hand = STRAIGHT_FLUSH
        hand.highCard = cards[-1][0]
        return hand

    # Check for Four-of-a-Kind
    number = 0
    count = 0
    for card in cards:
        if number == 0:
            number = card[0]
            count = 1
        elif card[0] == number:
            count += 1
            if count == 4:
                break
        elif card[0] != number:
            number = 0
            count = 0

    if count == 4:
        hand.hand = FOUR_KIND
        hand.highCard = number
        return hand

    # Check for Full House
    suit1 = ''
    suit1Card = 0
    suit2 = ''
    suit2Card = 0
    count1 = 0
    count2 = 0
    for card in cards:
        if suit1 == '':
            suit1 = card[1]
            suit1Card = card[0]
        elif card[1] == suit1:
            count1 += 1
        elif suit2 == '':
            suit2 = card[1]
            suit2Card = card[0]
        elif card[1] == suit2:
            count2 += 1

    if (count1 == 2 and count2 == 3) or (count1 == 3 and count2 == 2):
        hand.hand = FULL_HOUSE
        if count1 > count2:
            hand.highCard = suit1Card
            hand.secondHighCard = suit2Card
        else:
            hand.highCard = suit2Card
            hand.secondHighCard = suit1Card
        return hand

    # Check for Flush
    suit = ''
    flag = 0
    for card in cards:
        if suit == '':
            suit = card[1]
        elif card[1] != suit:
            flag = 1
            break

    if flag == 0:
        hand.hand = FLUSH
        hand.highCard = cards[-1][0]

    # Check for Straight
    number = 0
    flag = 0
    for card in cards:
        if number == 0:
            number = card[0]
        elif card[0] == number + 1:
            number += 1
        else:
            flag = 1
            break

    if flag == 0:
        hand.hand = STRAIGHT
        hand.highCard = cards[-1][0]
        return hand

    # Check for Three-of-a-Kind
    number = 0
    count = 0
    for card in cards:
        if number == 0:
            number = card[0]
            count = 1
        elif card[0] == number:
            count += 1
            if count == 3:
                break
        elif card[0] != number:
            number = 0
            count = 0

    if count == 3:
        hand.hand = THREE_KIND
        hand.highCard = number
        return hand

    # Check for Two-Pair
    pair1Count = 0
    pair1Number = 0
    pair2Count = 0
    pair2Number = 0
    for card in cards:
        if pair1Count == 0:
            pair1Count += 1
            pair1Number = card[0]
        elif card[0] == pair1Number:
            pair1Count += 1
        elif pair2Count == 0:
            pair2Count += 1
            pair2Number = card[0]
        elif card[0] == pair2Number:
            pair2Count += 1

    if pair1Count == 2 and pair2Count == 2:
        hand.hand = TWO_PAIR
        if pair1Number > pair2Number:
            hand.highCard = pair1Number
            hand.secondHighCard = pair2Number
        else:
            hand.highCard = pair2Number
            hand.secondHighCard = pair1Number
        return hand

    # Check for One-Pair
    pair1Count = 0
    pair1Number = 0
    for card in cards:
        if pair1Count == 0:
            pair1Count += 1
            pair1Number = card[0]
        elif card[0] == pair1Number:
            pair1Count += 1

    if pair1Count == 2:
        hand.hand = ONE_PAIR
        hand.highCard = pair1Number
        return hand

    # High Card
    hand.hand = HIGH_CARD
    hand.highCard = cards[-1][0]
    return hand



pokerHands = []
with open('../input-files/p054_poker.txt') as f:
    for line in f:
        hands = line.strip('\n').split(' ')
        pokerHands.append([hands[:5], hands[5:]])

startTime = time.time()
count = 0
for hand in pokerHands:
    winner = getWinner(hand[0], hand[1])
    if winner == 1:
        count += 1
endTime = time.time()

print('Answer: ', count)
print('Time: ', endTime - startTime)
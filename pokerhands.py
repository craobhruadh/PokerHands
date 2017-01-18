# This code is my solution to problem 54 of Project Euler:
# https://projecteuler.net/problem=54
#
# I hope it's useful both as an example of python code,
# and as an example of how to code!  Solving problems is a good
# way to practice/build your coding skills, and/or to teach
# yourself a new langauge.  It's far easier to learn by
# doing/coding than learn by just looking at the syntax out
# of a book.
#
# Unrelated:  For people in our group transitioning from matlab
# time handling seems to be the big issue.  Take a look at:
# https://wiki.python.org/moin/WorkingWithTime

import sys, pdb, collections



# function CalculateHandResults()
# -------------------------------
# Takes in a "string" in the hands variable, assumes it's one
# specific match from the input


# function DetermineHandValue
# ---------------------------
# values:
# 0: High card
# 1: One pair
# 2: Two pairs
# 3: Three of a kind
# 4: Straight
# 5: Flush
# 6: Full House
# 7: Four of a Kind
# 8: Straight Flush
# 9: Royal Flush
#
# Strategy: Start from highest value, iterate downwards
def DetermineHandValue(hands):
    samesuit = CheckIfSameSuit(hands)
    isStraight = CheckStraightFlush(hands)

    if (samesuit and CheckRoyalFlush(hands)):
        cardvalue = 9
    elif (samesuit and isStraight):
        cardvalue = 8
    elif CheckFourOfAKind(hands):
        cardvalue = 7
    elif
#    pdb.set_trace()
    return cardvalue

def CheckFourOfAKind(hands):


def CheckStraightFlush(hands):
    CurrentHand = [];
    for i in hands:
        temp = i[0]
        if temp == 'J':
            temp = 11
        elif temp == 'Q':
            temp = 12
        elif temp == 'K':
            temp = 13
        elif temp = 'A':
            temp = 14
        else:
            temp = int(temp)
        CurrentHand.append(temp)
    CurrentHand.sort()
    for i in range(0,4):
        if CurrentHand[i+1] == CurrentHand[i]+1:
            isStraight = true
        else:
            isStraight = false
            break
    return isStraight;


def CheckRoyalFlush(hands):
    RoyalFlush = ['10', 'J', 'Q', 'K', 'A']
    CurrentHand = [];
    for i in hands:
        CurrentHand.append(i[0])
    pdb.set_trace()

    if collections.Counter(RoyalFlush) == collections.Counter(CurrentHand):
        return True
    else:
        return False

def CheckIfSameSuit(hands):
    for i in range(0,4):
        if hands[i][1] == hands[i+1][1]:
            samesuit = True
        else:
            samesuit = False
            break
    return samesuit


# function CalculateMatchResults
# ------------------------------
# Takes a single string, assumes that it's 10 hands with a newline
# character at the end, five per player, and calculates the value
# of each hand for each player
def CalculateMatchResult(hands):
#    pdb.set_trace() #for debugging, comment/remove to run it all

    # Remove newline character
    temp = hands.split('\n' )  # Alternately hands[-3:] returns all but the last 3 elements
    hands = temp[0]

    hands = hands.split(' ') #Should get a 10 element array.  Consider safety checking here!

    player1 = hands[0:5] #See python slices
    player2 = hands[5:]


    player1_result = DetermineHandValue(player1)



# function RunPokerSimulation()
# -----------------------------
# Main function, reads in poker hand data in variable "filename",
# calculates each hand result.
def RunPokerSimulation(filename):
    fid = open(filename)
    for line in fid:
        CalculateMatchResult(line)
    fid.close()


# Python looks for a function called main() and starts everything here
def main():
    filename = 'p054_poker.txt'
    RunPokerSimulation(filename)
#    print 'Hello there', sys.argv[1]
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()

#!/usr/bin/python3
#
# Nikki Benoit
# Aug 8 2019  15:51:56.5156
#

######################################
#  Guess - computer randomly selects a number between 1-10
#  and checks that against user input.
######################################
import random

# tuple yea - guessed correctly nay - guessed incorrectly
yea = ("I guessed your number!", "WooHoo, I got it!", "Success!", "Yahtzee!")
nay = ("Doh!", "I guessed incorrectly!", "Womp Womp", "Oh no! :'(")

# user number input
userguess = int(input("Pick a number between 1 and 10: "))
# random computer guesses
myguess = random.randint(1,10)

def randResp(tuple):
    return tuple[random.randint(0,len(tuple)-1)]

print("Is your number " + str(myguess) + "?")

# prints correct tuple response based on matching input and guess
if (myguess == userguess):
    print(randResp(yea))
else:
    print(randResp(nay))

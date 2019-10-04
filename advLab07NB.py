#!/usr/bin/python3
#
# Nikki Benoit
# Aug 8 2019  19:13:15.1315 MDT
#
######################################
# Guessing Game - User enters upper bounds number. Computer picks a number 1-upper bounds
# User enters number of tries. Wrong guesses are replied with 'too low' or 'two high'
######################################

import random

# user input of upper bounds
upperBounds = int(input("Pick the highest number to guess: "))
# user input of tries
userTries = int(input("How many guesses do you want: "))
# random computer number
numberPick = random.randint(1,upperBounds)
# tuple computer responses to guesses
higherLower = ("Too low", "Too high", "You guessed right!")
# guess count
guessCount = 0

while(True):
    # increment guessCount
    guessCount +=1

    if(guessCount > userTries):
        print("Too many guesses.  Nice try!")
        break
    # user guess
    userGuess = int(input("Guess a number between 1 and " + str(upperBounds) + ": "))

    # prints correct tuple response based on matching guess - pick
    if (userGuess < numberPick):
        print(higherLower[0])
    elif(userGuess > numberPick):
        print(higherLower[1])
    else:
        print(higherLower[2])
        break

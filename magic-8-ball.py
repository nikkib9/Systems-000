#!/usr/bin/python
#
# Nikki Benoit
# Tues Aug 8 16:37 MDT 2019
#
############################################
#  Magic Eight Ball
############################################

import random

person = input("What's your name? ")
question = input("What's your question? ")

choices=("Why you ask?", "I'm a ball!", "Why not", "HAHAHAHAHAHAHAHA no.", "Noooope")

value = random.randint(0,len(choices)-1)

print(choices[value])

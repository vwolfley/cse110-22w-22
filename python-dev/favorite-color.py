#####
# Date: 2022-01-06
# File: favorite-color.py
# Author: Vern Wolfley
# Purpose: Write a program that asks a user for their favorite color
#####

import random

print("Who am I working with today?")
userName = input(" - ")
print("Hello " + userName.capitalize()+"!")
print(userName.capitalize() + ", what is your favorite color?")
colorChoice = input(" - ")
print(colorChoice.capitalize() + ", is a great color!")

colorList = ["Blue", "Green", "Pink", "Red", "Yellow"]
print("My favorite color is", random.choice(colorList) + ".")
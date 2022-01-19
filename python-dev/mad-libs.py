#####
# Date: 2022-01-15
# Week 2 assignment
# File: mad-libs.py
# Author: Vern Wolfley
# Purpose: Create a funny story using user input
#####

import random

# stores user inputs in array
verbs = []
animals = []
adjectives =[]
exclamations = []
nouns = []

start = (f'''
Let's play a fun game!

Please enter the following:
''')

print(start)

adj1 = input("Adjective: ")
animal1 = input("Animal: ")
verb1 = input("Verb: ")
excl1 = input("Exclamation: ").capitalize()
verb2 = input("Verb: ")
verb3 = input("Verb: ")
excl2 = input("Exclamation: ").capitalize()
adj2 = input("Adjective: ")
animal2 = input("Animal: ")
verb4 = input("Verb: ")
noun1 = input("Noun: ")
adj3 = input("Adjective: ")
noun2 = input("Noun: ")
noun3 = input("Noun: ")

# pushes variables into arrays
verbs.extend([verb1, verb2, verb3, verb4])
animals.extend([animal1, animal2])
adjectives.extend([adj1, adj2, adj3])
exclamations.extend([excl1, excl2])
nouns.extend([noun1, noun2, noun3])

# creates a random choice from each array
# not a unique choice
x = random.choice

# output variable
mad_lib = (f'''
The other day, I was really in trouble. It all started when I saw a very
{x(adjectives)} {x(animals)} {x(verbs)} down the hallway. "{x(exclamations)}!" I yelled. 
But all I could think to do was to {x(verbs)} over and over. Miraculously,
that caused it to stop, but not before it tried to {x(verbs)}
right in front of my family.  So, I {x(verbs)} up a {x(adjectives)} {x(nouns)}. 
My family yelled "{x(exclamations)}!", the {x(nouns)} is for the {x(animals)}. 
Well that fixed my trouble, and I have that {x(adjectives)} {x(nouns)} to thank for it.
''')

# prints output
print(mad_lib)

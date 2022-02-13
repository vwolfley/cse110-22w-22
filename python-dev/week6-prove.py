#####
# Date: 2022-02-12
# Week 6 Prove: Milestone - Adventure Game
# File: week6-prove.py
# Author: Vern Wolfley
# Purpose: Start & finish a text-based adventure game, the user is presented a scenario with different options.
#####

import time

# Variable that decides whether the game will run again or not.
goOn = True
yes =  ['yes', 'y']
no = ['no','n']
get_weapon = True
welcome = "Welcome to the Heros Quest!"
opening = (f'''{"*":*^80}
You're about to begin a great adventure, traveling into uncharted 
territory, braving the elements, fighting evil, and righting wrongs.  
This journey will take many days, maybe even months.  It will test 
both your physical and mental strength.  Choose your path carefully 
and always stay vigilant.
{"*":*^80}''')

END = (f'''
{"*":*^80}
*{"Well that's OK not everyone is cut out to be a hero!":^78}*
*{"":^78}*
*{"--- END OF QUEST ---":^78}*
{"*":*^80}
''')

END_GAME = (f'''
{"*":*^80}
*{"Thanks for Playing!":^78}*
*{"":^78}*
*{"--- END OF GAME ---":^78}*
{"*":*^80}
''')

WIN = (f'''
{"*":*^80}
*{"Your Quest is won!":^78}*
*{"You freed the region from evil!":^78}*
*{"You better rest up for your next adventure!":^78}*
*{"--- END OF QUEST ---":^78}*
{"*":*^80}
''')
Q2 = f'''{"*":*^80}
Before you set off on this arduous journey. We need to 
know your name, so we can either sing your praises or 
mark your grave.
{"*":*^80}'''


### Weapons
sword = "Good choice the sword is a one-handed weapon that is light and fast, good for close combat."
broadsword = f'''Good choice the broad sword is a two-handed weapon 
                that when handled by the right person can go serious damage in combat.'''
battle_ax = "Good choice the battle-ax is a fierce and deadly weapon designed to deliver a heavy blow."
wand = "Good choice the wand gives you magical powers."

direction = f'What direction should we go? (NORTH, EAST, WEST, SOUTH) '

### North 
north = f'''The north is covered in a dense, dark forest.
As you enter you feel watched.
Do you slow down to be ready for battle or speed up hoping to outrun whatever it is?
'''
slow = f'''The tree elves outnumber you 10 to 1 and quickly to overtake you.  
Their poison-tipped arrows quickly find the chinks in your armor. 
No weapon other than the wand can protect you...They bring your quest to a deadly end'''

win_wand = f'''You are able to cast a spell blinding the elves to your presence.
You narrowly escape!'''

### South
south = f'''The south is filled with dangerous swamps.  
As you pick your way slowly through all the obstacles an ogre appears!  
Do you stand and fight or run away?'''

stand = f'The ogres club is no match for your weapon and you quickly eliminate him!'

orge_wand = f'''The ogre is imune to your magic! 
He grabs your wand and breaks it!  Then he breaks you!'''

run = f'''Your lack of courage leads to your downfall!  
The ogre hits you with his club as you turn to run, bringing your quest to a deadly end.'''

### East
east = f'''The east is a desert with shifting sand dunes and dangerous beasts.  
On your second day in the desert, you lose your way and wander off the safe path.  
A giant hairy beast attacks!'''

fight_beast = f'''The beast is no match for your weapon and you quickly eliminate him!'''
wand_beast = f'''The beast laughs at your puny magic and quickly devours you!'''
run_beast = f'''The beaset quickly catches you, you coward, and slowly devours you!'''

### West
west = f'''The west is a mountainous region filled with lakes and streams.  
As you travel through this region you encounter a witch.  
She asks for your help and protection.  Do you say yes or no?'''

witch_lose = f'''It was a trick!! She casts a dark spell, 
putting you in a coma, and then she cooks you and eats you.'''

witch_win = f'''It was a trick!! She casts a dark spell.
Her dark magic is powerfull, but your wand and its magic are stronger.
You cast your own spell banishing her and breaking her spells.'''


indecision = f'''Your indecision has cost you!
Your quest has failed! '''

#####
# Function return T or F for Y or N (to be used to reassign goOn var)
####
def cont(yn):
    if yn in yes:
        return True
    elif yn in no:
        print(END_GAME)
        return False
    
#######
# Directions function
# Provides choices for player picking a direction
#######
def directions(choice, weapon):
    # North
    if choice == "north":
        print(f'{choice.upper()} it is!')
        time.sleep(.5)
        print(north)
        choice = input('SLOW DOWN or SPEED UP ').lower()
        print(choice, weapon)
        if (choice == 'slow down' or choice == "speed up") and weapon == "wand":
            print(win_wand)
            time.sleep(.5)
            print(WIN)
        elif (choice == 'slow down' or choice == "speed up") and weapon != "wand":
            print(slow)
            time.sleep(.5)
            print(END)
        else:
            print("That is not a valid choice!")
            time.sleep(.5)
            print(indecision)
    # East        
    elif choice == "east":
        print(f'{choice.upper()} it is!')
        time.sleep(.5)
        print(east)
        choice = input("BATTLE or RETREAT ").lower()
        if choice == "battle" and weapon != "wand":
            print(fight_beast)
            time.sleep(.5)
            print(WIN)
        elif choice == "battle":
            print(wand_beast)
            time.sleep(.5)
            print(END)
        elif choice == "Retreat":
            print(run_beast)
            time.sleep(.5)
            print(END)
        else:
            print("That is not a valid choice!")
            time.sleep(.5)
            print(indecision)
    
    # South        
    elif choice == "south":
        print(f'{choice.upper()} it is!')
        print(south)
        choice = input('STAND or RUN ').lower()
        if choice == "stand" and weapon != "wand":
            print(stand)
            time.sleep(.5)
            print(WIN)
        elif choice == "stand" and weapon == "wand":
            print(orge_wand)
            time.sleep(.5)
            print(END)
        elif choice == "run":
            print(run)
            time.sleep(.5)
            print(END)
        else:
            print("That is not a valid choice!")
            time.sleep(.5)
            print(indecision)
    
    # West       
    elif choice == "west":
        print(f'{choice.upper()} it is!')
        print(west)
        choice = input('YES or NO ').lower()
        if weapon == "wand":
            print(witch_win)
            time.sleep(.5)
            print(WIN)
        else:
            print(witch_lose)
            time.sleep(.5)
            print(END)
    else:
        print("That is not a valid choice, and no choice is in itself a choice!")
        time.sleep(.5)
        print("Your indecision has ended your quest!")
        time.sleep(.5)
        print(END)

    
########################################################
# Main program. runs the Choose Your Own Adventure game.
########################################################
### START
while goOn == True:
    get_weapon = True
    print(welcome)
    time.sleep(.5)
    ### Question 1
    choice = input("So you want to go on a quest do you? (Y/N) ").lower()
    if choice in yes:
        print(opening)
        time.sleep(2)
        print(Q2)
        time.sleep(2)
        hero = input("What is our hero's name? ").title()
        # Pick Weapon
        while get_weapon == True:
            print(f'{hero} this is a DANGEROUS quest pick a weapon!')
            choice = input('SWORD, BATTLE AX, or WAND? ').lower()
            
            if choice == 'sword':
                weapon = 'sword'
                get_weapon = False
                print(sword)
                time.sleep(1)
                choice = input(direction).lower()
                # Pick Direction function
                directions(choice, weapon)
                
            elif choice == 'battle ax':
                weapon = 'battle ax'
                get_weapon = False
                print(battle_ax)
                time.sleep(1)
                choice = input(direction).lower()
                # Pick Direction function
                directions(choice, weapon)
            elif choice == 'wand':
                weapon = 'wand'
                get_weapon = False
                print(wand)
                time.sleep(1)
                choice = input(direction).lower()
                # Pick Direction function
                directions(choice, weapon)
            else:
                choice = input(f"{hero} are you sure you don't want a weapon? (Y/N) ").lower()
                if choice in yes:
                    print("Ok it is your life!")
                    get_weapon = False
                    time.sleep(1)
                    choice = input(direction).lower()
                    # Pick Direction function
                    directions(choice, weapon)
                else:
                    get_weapon = True
        
    else:
        print(END)
    
    
    # End of game choice
    decision = input("Do you want to play again? (Y/N) ").lower()
    print(decision)
    goOn = cont(decision)



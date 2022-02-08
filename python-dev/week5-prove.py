#####
# Date: 2022-02-05
# Week 5 Prove: Milestone - Adventure Game
# File: week5-prove.py
# Author: Vern Wolfley
# Purpose: Start a text-based adventure game, the user is presented a scenario with different options.
#####

import time

# Variable that decides whether the game will run again or not.
goOn = True
yes =  ['yes', 'y']
no = ['no','n']
get_weapon = True
welcome = "Welcome to the Heros Quest!"
opening = (f'''
-----------------------------------------------------------------
You're about to begin a great adventure, traveling into uncharted 
territory, braving the elements, fighting evil, and righting wrongs.  
This journey will take many days, maybe even months.  It will test 
both your physical and mental strength.  Choose your path carefully 
and always stay vigilant.
-----------------------------------------------------------------
''')

END = (f'''
{"*":*^80}
*{"Well that's OK not everyone is cut out to be a hero!":^78}*
*{"":^78}*
*{"--- END OF QUEST ---":^78}*
{"*":*^80}
''')

Q2 = (f'''
-----------------------------------------------------------------
Before you set off on this arduous journey. We need to 
know your name, so we can either sing your praises or 
mark your grave.
-----------------------------------------------------------------
''')

sword = "Good choice the sword is a one-handed weapon that is light and fast, good for close combat."
broadsword = "Good choice the broad sword is a two-handed weapon that when handled by the right person can go serious damage in combat."
battle_ax = "Good choice the battle-ax is a fierce and deadly weapon designed to deliver a heavy blow."
wand = "Good choice the wand gives you magical powers."

# Return T or F for Y or N (to be used to reassign goOn var).
def cont(yn):
    if yn in yes:
        return True
    elif yn in no:
        print(END)
        return False

    
########################################################
# Main program. runs the Choose Your Own Adventure game.
########################################################
### START
while goOn == True:
    print(welcome)
    time.sleep(.5)
    ### Question 1
    choice = input("So you want to go on a quest do you? (y/n)").lower()
    if choice in yes:
        print(opening)
        time.sleep(1)
        print(Q2)
        time.sleep(1)
        hero = input("What is our hero's name?").title()
        while get_weapon == True:
            print(f'{hero} this is a DANGEROUS quest pick a weapon!')
            choice = input('SWORD, BATTLE AX, or WAND? ').lower()
            if choice == 'sword':
                weapon = 'sword'
                get_weapon = False
                print(sword)
                time.sleep(1)
                choice = input(f'What direction should we go? (NORTH, EAST, WEST, SOUTH)').lower()
                print(f'{choice} it is!')
            elif choice == 'battle ax':
                weapon = 'battle ax'
                get_weapon = False
                print(battle_ax)
                time.sleep(1)
                choice = input(f'What direction should we go? (NORTH, EAST, WEST, SOUTH)').lower()
                print(f'{choice} it is!')
            elif choice == 'wand':
                weapon = 'wand'
                get_weapon = False
                print(wand)
                time.sleep(1)
                choice = input(f'What direction should we go? (NORTH, EAST, WEST, SOUTH)').lower()
                print(f'{choice} it is!')
            else:
                choice = input(f"{hero} are you sure you don't want a weapon? (y/n)").lower()
                if choice in yes:
                    print("Ok it is your life!")
                    get_weapon = False
                    time.sleep(1)
                    choice = input(f'What direction should we go? (NORTH, EAST, WEST, SOUTH)').lower()
                    print(f'{choice} it is!')
                else:
                    get_weapon = True
        
    else:
        print(END)
    
    
    # End of game choice
    decision = input("Do you want to play again? (y/n)").lower()
    print(decision)
    goOn = cont(decision)




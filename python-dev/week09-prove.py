#####
# Date: 2022-03-05
# Week 09 Prove: Milestone - Shopping Cart Program
# File: week09-prove.py
# Author: Vern Wolfley
# Purpose: Create a program that stores a list of products in a shopping cart 
#####

welcome = (f''' 
{"*":*^80}
*{"Welcome to the Shopping Cart Program":^78}*
{"*":*^80}''')

view_cart = (f''' 
{"-":-^80}
The contents of the shopping cart are:
{"-":-^80}''')

end = (f''' 
{"*":*^80}
*{"Thank you for shopping with us!":^78}*
*{"Goodbye":^78}*
{"*":*^80}''')

not_valid = (f''' 
{"*":*^80}
*{"Sorry that is not a valid choice!":^78}*
{"*":*^80}''')

options = (f'''
{"*":*^80}
Please select one of the following:
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
{"*":*^80}''')

cart = []

print(welcome)
action = None
while action != 5:
    while True:
        try:
            print(options)
            action = int(input("Please enter your choice: "))
    
            if action == 1:
                item = input(f'What item would you like to add? ').title()
                cart.append(item)
                print(f"\n*** {item} has been added to your cart. ***")
            elif action == 2:
                print(view_cart)
                for item in cart:
                    print("-",item)
            elif action == 3:
                # place action here
                break
            elif action == 4:
                # place action here
                break
            elif action == 5:
                print(end)

            while action not in [1,2,3,4,5]:
                print(not_valid)
                break
            break
        except ValueError:
            print(not_valid)
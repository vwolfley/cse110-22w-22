##### # Date: 2022-03-12
# Week 10 Prove: Milestone - Shopping Cart Program
# File: week10-prove.py
# Author: Vern Wolfley
# Purpose: Create a program that stores a list of products in a shopping cart 
#####

import time

# Bold ANSI 
bold_s = '\033[1m'
bold_e = '\033[0m'

welcome = (f''' 
{"*":*^80}
{bold_s}*{"Welcome to the Shopping Cart Program":^78}*{bold_e}
{"*":*^80}''')

view_cart = (f''' 
{"-":-^80}
{bold_s}The contents of the shopping cart are:{bold_e}
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

ct = (f'''{"-":-^20}
{bold_s}Cart Total: ''')

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
prices = []

print(welcome)
time.sleep(.3)
action = None
change = None

while action != 5:
    while True:
        try:
            print(options)
            action = int(input("Please enter your choice, (1-5): "))
    
            if action == 1:
            # Add item to cart
                item = input(f'\nWhat item would you like to add? ').title()
                price = float(input("What is the item's price? "))
                cart.append(item)
                prices.append(price)
                print(f"\n*** {item} has been added to your cart. ***")
                time.sleep(.5)
            elif action == 2:
            # View items in cart
                print(view_cart)
                for i in range(len(cart)):
                    item = cart[i]
                    price = prices[i]
                    print(f"{i+1}. {item:<12}${price:,.2f}")
                total = sum(prices)
                print(f"{ct}{'':<3}${total:,.2f}{bold_e}")
                time.sleep(.5)
            elif action == 3:
            # Remove item from cart
                print(view_cart)
                for i in range(len(cart)):
                    item = cart[i]
                    price = prices[i]
                    print(f"{i+1}. {item:<12}${price:,.2f}")
                    
                change = int(input(f"\nWhich item would you like to remove? (1-{len(cart)})) "))
                index = change - 1
                if index in range(0, len(cart)):
                    removed = cart[index]
                    # Remove item
                    cart.pop(index)
                    # Remove price
                    prices.pop(index)
                    print(f"\n*** {removed} was removed ***")
                    print(view_cart)
                    for i in range(len(cart)):
                        item = cart[i]
                        price = prices[i]
                        print(f"{i+1}. {item:<12}${price:,.2f}")
                else:
                    print(not_valid)
                time.sleep(.5)
            elif action == 4:
            # Compute total from cart
                total = sum(prices)
                print(f"{ct}{'':<3}${total:,.2f}{bold_e}")
                time.sleep(1)
            elif action == 5:
            # Quit adding items to cart
                print(end)

            while action not in [1,2,3,4,5]:
                print(not_valid)
                break
            break
        except ValueError:
            print(not_valid)
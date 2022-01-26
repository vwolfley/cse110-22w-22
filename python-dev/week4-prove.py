#####
# Date: 2022-01-29
# Week 4 Prove: Milestone - Meal Price Calculator Continued
# File: week4-prove.py
# Author: Vern Wolfley
# Purpose: Compute the price of a meal.
#####

# What is the price of a child's meal? 4.50
# What is the price of an adult's meal? 9.00
# How many children are there? 4
# How many adults are there? 2
# What is the sales tax rate? 6

# Subtotal: $36.00
# Sales Tax: $2.16
# Total: $38.16

# What is the payment amount? 40
# Change: $1.84

# Inputs
## Task 01
child_meal = float(input("What is the price of a child's meal?  "))
adult_meal = float(input("What is the price of an adult's meal?  "))
## Task 02
num_children = int(input("How many children are there?  "))
num_adults = int(input("How many adults are there?  "))

drinks_question = input("Did you purchase drinks? (Y/N)")

if drinks_question == "y":
    drinks = int(input("How many drinks were purchased?  "))
    drinks_sub = (drinks * 1.5)
    drinks_string = (f'{drinks} Drinks @ $1.50')
elif drinks_question == "n":
    drinks_sub = 0
    drinks_string = (f'No drinks purchased - ')
    
    
## Task 03
sales_tax = float(input("What is the sales tax rate?  "))


# Variables
child_sub = (child_meal * num_children)
adult_sub = (adult_meal * num_adults)

subtotal = child_sub + adult_sub + drinks_sub
tax_rate = (subtotal * sales_tax)/100
total_price = subtotal + tax_rate
tip_rate = 0.18
tip = total_price * tip_rate
total = total_price + tip

# Outputs 
child_string = (f'{num_children} Child\'s meals @ ${child_meal:.2f}')
adult_string = (f'{num_adults} Adult\'s meals @ ${adult_meal:.2f}')
## Task 04
sub_string = (f'Subtotal')
## Task 05
tax_string = (f'Sales Tax @ {sales_tax}%')
tip_string = (f'Gratuity of 18%')
## Task 06
total_string = (f'Total:')

# Bold ANSI 
bold_s = '\033[1m'
bold_e = '\033[0m'


## Task 09
## Task 10
## Task 11
## Task 12
## Task 13
bill = (f'''
{bold_s}Sales Receipt{bold_e}
--------------------------------
{child_string:<25} ${child_sub:.2f}
{adult_string:<25} ${adult_sub:.2f}
{drinks_string:<25} ${drinks_sub:.2f}
--------------------------------
{sub_string:<25} ${subtotal:.2f}
{tax_string:<25} ${tax_rate:.2f}
{tip_string:<25} ${tip:.2f}
--------------------------------
{total_string:<25} {bold_s}${total:.2f}{bold_e}
''')

print(bill)

## Task 07
payment = float(input("What is the payment tendered?  "))
## Task 08
change = abs(total - payment)
payment_string = (f'Payment tendered:')
change_string = (f'Change due:')

receipt = (f'''
{bold_s}Sales Receipt{bold_e}
--------------------------------
{child_string:<25} ${child_sub:.2f}
{adult_string:<25} ${adult_sub:.2f}
{drinks_string:<25} ${drinks_sub:.2f}
--------------------------------
{sub_string:<25} ${subtotal:.2f}
{tax_string:<25} ${tax_rate:.2f}
{tip_string:<25} ${tip:.2f}
--------------------------------
{total_string:<25} ${total:.2f}

{payment_string:<25} ${payment:.2f}
{change_string:<25} {bold_s}${change:.2f}{bold_e}

Thank You, Please come again!
''')

print(receipt)

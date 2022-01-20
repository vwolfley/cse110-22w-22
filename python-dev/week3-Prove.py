#####
# Date: 2022-01-22
# Week 3 Prove: Milestone - Meal Price Calculator
# File: prove03.py
# Author: Vern Wolfley
# Purpose: Compute the price of a meal.
#####

# Compute the price of a meal as follows by asking for:
# the price of child and adult meals, 
# the number of each, 
# and then the sales tax rate. 
# Use these values to determine the total price of the meal. 
# Then, ask for the payment amount and compute the amount of change to give back to the customer.

# Requirement 01   
child_meal = float(input("What is the price of a child's meal?  "))
num_children = int(input("How many children are there?  "))
# Requirement 02
adult_meal = float(input("What is the price of an adult's meal?  "))
num_adults = int(input("How many adults are there?  "))
# Requirement 03
sales_tax = float(input("What is the sales tax rate?  "))
    
child_sub = (child_meal * num_children)
adult_sub = (adult_meal * num_adults)
subtotal = child_sub + adult_sub
tax_rate = (subtotal * sales_tax)/100
total_price = subtotal + tax_rate
tip_rate = 0.18
tip = total_price * tip_rate
total = total_price + tip

child_string = (f'{num_children} Child\'s meals @ ${child_meal:.2f}')
adult_string = (f'{num_adults} Adult\'s meals @ ${adult_meal:.2f}')
sub_string = (f'Subtotal:')
tax_string = (f'Sales Tax:')
total_string = (f'Total:')
tip_string = (f'Gratuity of 18%')

# Requirement 04
# Requirement 05
# Requirement 06

# Requirement 08
# Requirement 09
# Requirement 10
# Requirement 11
output = (f'''
Sales Receipt
--------------------------------
{child_string:<25} ${child_sub:.2f}
{adult_string:<25} ${adult_sub:.2f}
--------------------------------
{sub_string:<25} ${subtotal:.2f}
{tax_string:<25} ${tax_rate:.2f}
{tip_string:<25} ${tip:.2f}
--------------------------------
{total_string:<25} ${total:.2f}
''')


print(output)
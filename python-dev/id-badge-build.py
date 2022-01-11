#####
# Date: 2022-01-11
# Week 2 Assignment
# File: id-badge-build.py
# Author: Vern Wolfley
# Purpose: Create a properly formatted ID badge
#####

# module provides regular expression matching operations
import re

print("Please enter the following information:")

first_name = input("First Name: ").capitalize()
last_name = input("Last Name: ").upper()
email = input("Email Address: ").lower()
phone = input("Phone Number: ")
job_title = input("Job Title: ").title()
id_number = input("ID Number: ")

hair_color = input("Hair Color: ").capitalize()
eye_color = input("Eye Color: ").capitalize()
start_month = input("What month did you start?: ").capitalize()
training = input("Have you completed training? (yes/no): ").upper()

# formats the phone number to (000) 000-0000
# .zfill() makes sure that the input is at least 10 characters, if not it adds zeros to make sure program does not break.
phone_gen = '(%s) %s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', phone.zfill(10)))

hair = (f"Hair: {hair_color}")
eyes = (f"Eyes: {eye_color}")
month = (f"Month: {start_month}")
train = (f"Training: {training}")

output = (f'''
The ID Card is:
-----------------------------------
{last_name}, {first_name}
{job_title}
ID: {id_number}

{email}
{phone_gen}

{hair:<20}{eyes}
{month:<20}{train}
-----------------------------------
''')

print(output)
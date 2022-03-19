####### 
# Date: 2022-03-15
# Week 11 Prove: Milestone
# File: week11-prove.py
# Author: Vern Wolfley
# Purpose: Analyze dataset on life expectancies
#######

# ** MILESTONE 01 **
# Path to my directory
file_path = "./assignment_files/life-expectancy.csv"
# Testing file path
# file_path = "life-expectancy.csv"
data = file_path

total = None
max_le = None
min_le = None
avg_le = None

life_info = []
entity = []
code = []
year = []
life_exp = []

# User input asks for a year
user_year = input("\nWhat year are you looking for?:  ")

# ** MILESTONE 02 **
with open(data, "r") as dataset:
    # Remove header row
    next(dataset)
    # ** MILESTONE 03 **
    for row in dataset:
        info_set = row.strip()
        # ** MILESTONE 04 **
        info = info_set.split(",")
        
        life_info.append(info)
        entity.append(info[0])
        code.append(info[1])
        year.append(info[2])
        life_exp.append(float((info[3])))
        
# print(life_info)
# print(entity) 
# print(code) 
# print(year)
# print(life_exp) 

# total = len(life_info)
max_le = max(life_exp)
min_le = min(life_exp)
# avg_le = sum(life_exp)/len(life_exp)

min_index = life_exp.index(min_le)
max_index = life_exp.index(max_le)
19
# ** MILESTONE 05 **
# Answer questions on data set
highest_le = f"From the data, the overall max life expectancy is {max_le:.1f} years, from {entity[max_index]} in {year[max_index]}."
lowest_le = f"From the data, the overall min life expectancy is {min_le:.1f} years, from {entity[min_index]} in {year[min_index]}."
questions_set1 = (f''' 
{"*":*^80}
{highest_le}
{lowest_le}
{"*":*^80}''')

print(questions_set1)

# Looks for the specified year in the data
le = []
countries = []
for index in life_info:
    if index[2] == user_year:
#         print(index)
        files = index
        le.append(float(files[3]))
        countries.append(files[0])
        
sum_le = sum(le)
avg_le = sum_le / len(le)
le_min = min(le)
le_max = max(le)
min_i = le.index(min(le))
max_i = le.index(max(le))

# Answer questions on subset of data set only
average_life = f"For the year {user_year}, the average life expectancy across all countries was {avg_le:.1f} years."
max_life = f"For the year {user_year}, the max life expectancy was in {countries[max_i]} with {le_max:.1f} years."
min_life = f"For the year {user_year}, the min life expectancy was in {countries[min_i]} with {le_min:.1f} years."
questions_set2 = (f''' 
{"*":*^80}
{average_life}
{max_life}
{min_life}
{"*":*^80}''')

print(questions_set2)


###################################
# GRAPH THE DATA
###################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Single Line Graph Only
def single_graph():
    plt.figure(figsize = (15,8))
    sns.set_theme(style="darkgrid")

    gp = sns.lineplot(x = years, y = countries_le, data = data_le, color = 'r', label = user_country1)                                 

    gp.set_title(f'Life Expectancy of {user_country1} over time')
    gp.set_ylabel('Life Expectancy in years')
    gp.set_xlabel('Years')
    plt.xticks(rotation=90)
    gp.set_xticks(gp.get_xticks()[::2])


cnty = f"\nOPTIONS\n{countries}"
print(cnty)

# User input asks for a country
user_country1 = input("\nWhat country are you looking for?:  ").title()
# ask = input("\nDo you want to compare two contries?  (y/n)  ").lower()

# if ask == "y":
#     user_country2 = input("\nWhat country are you looking for?:  ").title()
# else:
#     user_country2 = None
user_country2 = None
# Looks for the specified country in the data
countries_le = []
country_names = []
years = []
data_le = []
for index in life_info:
    if (index[0] == user_country1 and user_country2 == None):
#         print(index)
        files = index
        data_le.append([files[2], float(files[3])])
        countries_le.append(float(files[3]))
        country_names.append(files[0])
        years.append(files[2])
    elif (index[0] == user_country1 or index[0] == user_country2):
#         print(index)
        files = index
        data_le.append([files[2], float(files[3])])
        countries_le.append(float(files[3]))
        country_names.append(files[0])
        years.append(files[2])
        
header = ["Year", "Life_EXP"]
# data_le.insert(0, header)
# print(data_le)

single_graph()

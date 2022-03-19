####### 
# Date: 2022-03-19
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

life_info = []
entity = []
code = []
year = []
life_exp = []

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
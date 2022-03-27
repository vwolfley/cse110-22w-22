####### 
# Date: 2022-03-26
# Week 12 Prove: Milestone
# File: week12-prove.py
# Author: Vern Wolfley
# Purpose: Analyze dataset on life expectancies
#######

# Path to my directory
file_path = "../assignment_files/life-expectancy.csv"
data = file_path

# ###################################
# # GRAPH THE DATA Function
# ###################################
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Set Graph parameters
# # Single Line Graph Only
# def single_graph():
#     plt.figure(figsize = (15,8))
#     sns.set_theme(style="darkgrid")

#     gp = sns.lineplot(x = years, y = le, data = data_le, color = 'r', label = user_country)                                 

#     gp.set_title(f'Life Expectancy of {user_country} over time')
#     gp.set_ylabel('Life Expectancy in years')
#     gp.set_xlabel('Years')
#     plt.xticks(rotation=90)
#     gp.set_xticks(gp.get_xticks()[::2])
#     return
# ###################################
# # GRAPH THE DATA Function
# ###################################

total = None
max_le = None
min_le = None
avg_le = None

life_info = []
entity = []
code = []
year = []
life_exp = []

# Explain project
print(f"Lets look at data showing the life expectancies over the years for various countries.")

yes =["yes", "y"]
keep_asking = "y"
while keep_asking in yes:
    
    keep_asking = input("Do you want keep exploring the data?  (y/n) ").lower()
    if keep_asking in yes:
        
        user_pick = input("\n Do you want to explore by YEAR or COUNTRY? ").lower()
        
        # Read the data
        with open(data, "r") as dataset:
            # Remove header row
            next(dataset)
            for row in dataset:
                info_set = row.strip()
                info = info_set.split(",")

                life_info.append(info)
                entity.append(info[0])
                code.append(info[1])
                year.append(info[2])
                life_exp.append(float((info[3])))

#         print(life_info)
        # print(entity) 
        # print(code) 
        # print(year)
        # print(life_exp) 

        # total = len(life_info)
        max_le = max(life_exp)
        min_le = min(life_exp)
        # avg_le = sum(life_exp)/len(life_exp)

        min_index = life_exp.index(min_le )
        max_index = life_exp.index(max_le )

         # Answer questions on data set
        highest_le = f"From the data, the overall max life expectancy is {max_le:.1f} years, from {entity[max_index]} in {year[max_index]}."
        lowest_le = f"From the data, the overall min life expectancy is {min_le:.1f} years, from {entity[min_index]} in {year[min_index]}."
        questions_set1 = (f''' 
        {"*":*^80}
        {highest_le}
        {lowest_le}
        {"*":*^80}''')
        
        # Pick by YEAR
        if user_pick == "year":
            year_list = list(set(year))

            # User input asks for a year
            user_year = input("\nWhat year are you looking for?:  ")
            
            if user_year in year_list:

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

                # Output Section
                print(questions_set1)
                print(questions_set2)
            else:
                print("Year not in dataset!")
            
        elif user_pick == "country":
            entity_list = list(set(entity))
            
            for a,b,c in zip(entity_list[::3],entity_list[1::3],entity_list[2::3]):
                print('{:<30}{:<35}{:<}'.format(a,b,c))
                             
            # User input asks for a country
            user_country = input("\nWhat country are you looking for?:  ").title()
            
            # Looks for the specified country in the data
            le = []
            years = []
            data_le = []
            for index in life_info:
                if index[0] == user_country:
#                     print(index)
                    files = index
                    le.append(float(files[3]))
                    years.append(files[2])
                    data_le.append([files[2], float(files[3])])

            sum_le = sum(le)
            avg_le = sum_le / len(le)
            le_min = min(le)
            le_max = max(le)
            min_i = le.index(min(le))
            max_i = le.index(max(le))

            # Answer questions on subset of data set only
            average_life = f"For {user_country}, the average life expectancy is {avg_le:.1f} years."
            max_life = f"For {user_country}, the max life expectancy was in {years[max_i]} with {le_max:.1f} years."
            min_life = f"For {user_country}, the min life expectancy was in {years[min_i]} with {le_min:.1f} years."
            questions_set2 = (f''' 
            {"*":*^80}
            {average_life}
            {max_life}
            {min_life}
            {"*":*^80}''')
            
            # Output Section
            print(questions_set1)
            print(questions_set2)
            
            # Print Graph
            # single_graph()
            
        else:
            print(f"\n*** That is not a valid option! ***")
            
    else:   
        print(f"\n*** Ok Thanks for Playing! ***")
####### 
# Date: 2022-04-02
# Week 13 Prove: Milestone
# File: week13-prove.py
# Author: Vern Wolfley
# Purpose: Wind Chill Calculator
#######

degree_sign = u'\N{DEGREE SIGN}'

# convert from celsius to fahrenheit
def convert2fahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit

# convert from fahrenheit to celsius
def convert2celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

# calculate wind chill with temperature in F, and wind speed in mph
def wind_chill(temp, wind_speed):
    wc = 35.74 + 0.6215*temp - 35.75*(wind_speed**0.16)+0.4275*temp*(wind_speed**0.16)
    return round(wc,2)

# When user exits calculator
end = (f''' 
{"*":*^80}
*{"Thank you - Goodbye":^78}*
{"*":*^80}''')

# User feedback when given wrong choice
not_valid = (f''' 
{"*":*^80}
*{"Sorry that is not a valid choice!":^78}*
{"*":*^80}''')

    
action = None
while action != "n":
    while True:
        try:
            action = input("\nDo you want to use the wind chill calculator? (y/n) ").lower()
    
            if action == "y":
            
                # Ask user for temperature type
                temp_type = input("Is your temperature in Celsius or Fahrenheit? (C or F) ").lower()

                # Ask user for temperature   
                if temp_type == "c":
                    tp = int(input(f"\nWhat is the temperature in {degree_sign}{temp_type.upper()}?  "))
                    t = convert2fahrenheit(tp)
                elif temp_type == "f":
                    t = int(input(f"\nWhat is the temperature in {degree_sign}{temp_type.upper()}?  "))
                    tp = convert2celsius(t)

                for ws in range(5, 65, 5):
                    answer_f = wind_chill(t, ws)
                    answer_c = convert2celsius(answer_f)
                    print(f"At temperature {tp:.0f}{degree_sign}C or {t:.0f}{degree_sign}F, and {ws}mph, the windchill is: {answer_c:.0f}{degree_sign}C or {answer_f:.0f}{degree_sign}F")

            elif action == "n":
                print(end)
                break

            while action not in ["y", "n"]:
                print(not_valid)
                break
            break
        except ValueError:
            print(not_valid)   
    
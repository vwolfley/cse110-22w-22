#####
# Date: 2022-01-18
# Week 3 Team Activity
# File: area-of-shapes.py
# Author: Vern Wolfley
# Purpose: Write a program to compute the areas of three different shapes.
#####

# Core Requirements

# Square area of computation

length = input("What is the length of one side of your square? ")
sq_area = float(length)**2
print(f'The area of your square is: {sq_area}')

# Rectangle area of computation

r_len = input("What is the length of your rectangle? ")
r_wid = input("What is the width of your rectangle? ")
r_area = float(r_len) * float(r_wid)
print(f'The area of your rectangle is: {round(r_area, 3)}')

# Circle area of computation

import math

radius = input("What is the radius of your circle? ")
#
# cir_area = 3.14 * float(radius)**2
# or
#
cir_area = math.pi * float(radius)**2
print(f'The area of your circle is: {round(cir_area, 3)}')

# Stretch Challenge
## II
length = input("Pick any length: ")

area_sq = float(length)**2
area_cir = math.pi*float(length)**2
vol_cube = float(length)**3
vol_sph = (4/3) * math.pi * float(length)**3

output =(f'''
Area of a Square = {area_sq}
Area of a Circle = {area_cir:.1f}
Volume of Cube = {vol_cube}
Volume of Sphere = {vol_sph:.1f}
''')

print(output)

# Stretch Challenge
## III 

length = input("Pick any length in cm: ")
width = input("Pick any width in cm: ")
radius = input("Pick any radius in cm: ")

area_sq = float(length)**2
meters = (1/10000)
area_req = float(length) * float(width)
area_cir = math.pi * float(radius)**2

output =(f'''
Area of square with length {length}cm = {area_sq}cm^2
Area of square with length {length}cm = {area_sq * meters:.4f}m^2

Area of a rectangle with length {length}cm and width {width}cm = {area_req}cm^2
Area of a rectangle with length {length}cm and width {width}cm = {area_req * meters:.4f}m^2

Area of a circle with radius {radius}cm = {area_cir:.3f}cm^2
Area of a circle with radius {radius}cm = {area_cir * meters:.4f}m^2
''') 

print(output)
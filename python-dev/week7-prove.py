#####
# Date: 2022-02-19
# Week 7 Prove: Milestone - Pixel Pictures
# File: week7-prove.py
# Author: Vern Wolfley
# Purpose: Work with pictures and pixels
#####

from PIL import Image
# print("The Library is loaded correctly")

# Path to my directory where the images are stored
image_path = "/Users/vernwolfley/Documents/My-Education/CSE-110/assignment_files/cse110_images"

image_og = Image.open(image_path + "/beach.jpg")

# width, height = image_og.size
pixels_og = image_og.load()
# r, g, b = pixels_og[100, 200]
# pixels_og[100, 200] = (r, g, b)
# image_og.save("the_file_goes_here.jpg")

# print(image_og.size)
# print(pixels_og[100, 200])
# print(pixels_og[110, 210])
# print(pixels_og[120, 220])
# print(pixels_og[130, 230])

# Purple Square
# for y in range(100, 210):
#     for x in range(100, 200):
#         pixels_og[x, y] = (200, 8, 249) #C808F9

# change all pixel values add blue
for y in range(0, 600):
    for x in range(0, 800):
        r, g, b = pixels_og[x, y]
        pixels_og[x, y] = (r, g, 200) 

# pixels_og[100, 200] = (200, 8, 249) #C808F9
# pixels_og[101, 200] = (200, 8, 249) #C808F9
# pixels_og[102, 200] = (200, 8, 249) #C808F9
# pixels_og[103, 200] = (200, 8, 249) #C808F9
# pixels_og[104, 200] = (200, 8, 249) #C808F9
# pixels_og[105, 200] = (200, 8, 249) #C808F9
# pixels_og[100, 201] = (200, 8, 249) #C808F9
# pixels_og[101, 201] = (200, 8, 249) #C808F9
# pixels_og[102, 201] = (200, 8, 249) #C808F9
# pixels_og[103, 201] = (200, 8, 249) #C808F9
# pixels_og[104, 201] = (200, 8, 249) #C808F9
# pixels_og[105, 201] = (200, 8, 249) #C808F9
# pixels_og[100, 202] = (200, 8, 249) #C808F9
# pixels_og[101, 202] = (200, 8, 249) #C808F9
# pixels_og[102, 202] = (200, 8, 249) #C808F9
# pixels_og[103, 202] = (200, 8, 249) #C808F9
# pixels_og[104, 202] = (200, 8, 249) #C808F9
# pixels_og[105, 202] = (200, 8, 249) #C808F9
# pixels_og[100, 203] = (200, 8, 249) #C808F9
# pixels_og[101, 203] = (200, 8, 249) #C808F9
# pixels_og[102, 203] = (200, 8, 249) #C808F9
# pixels_og[103, 203] = (200, 8, 249) #C808F9
# pixels_og[104, 203] = (200, 8, 249) #C808F9
# pixels_og[105, 203] = (200, 8, 249) #C808F9

image_og.show()

file_loc = "../assignment_files/cse110_images/"
# image_og.save(file_loc + "purple_square.jpg")
# image_og.save("../assignment_files/cse110_images/blue_beach.jpg")
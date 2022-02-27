#####
# Date: 2022-02-25
# Week 8 Prove: Milestone - Pixel Pictures
# File: week8-prove.py
# Author: Vern Wolfley
# Purpose: Work with pictures and pixels
#####

import os
from PIL import Image
from PIL import ImageEnhance
# print("The Library is loaded correctly")

# Path to my directory where the images are stored
file_path = "../assignment_files/cse110_images/"

# Get the list of all files and directories
dir_list = os.listdir(file_path)

# prints all files with jpg
for x in dir_list:
    if x.endswith(".jpg"):
        # Prints only jpg files
        print(x)

# Ask user for image input
bkg_img = input("Please pick a background image to use from list:  ")
ovl_img = input("Please pick a overlay image to use from list:  ")

background_image = Image.open(file_path + "/" + bkg_img)
overlay_image = Image.open(file_path + "/" + ovl_img)

# background_image = Image.open(file_path + "/earth.jpg")
# overlay_image = Image.open(file_path + "/spaceshuttle.jpg")
# background_image = Image.open(file_path + "/field.jpg")
# overlay_image = Image.open(file_path + "/cat.jpg")

# Showing the original images
background_image.show()
overlay_image.show()

# Ask user if they want to transpose image
transpose = input("Do you want to transpose overlay image? (Y/N) ").lower

if transpose == "y":
    # Transposing image 
    transposed_img = overlay_image.transpose(Image.FLIP_LEFT_RIGHT)
    # transposed_img.show()
    overlay_pixels = transposed_img.load()

background_pixels = background_image.load()
overlay_pixels = overlay_image.load()


# Print the rgb values for the overlay pixels at point [0,0]
# print(overlay_pixels[0,0])

image_combined = Image.new("RGB", background_image.size)
combined_pixels = image_combined.load()

# Get the height and width of image
(width, height) = background_image.size

# Loop though images
for x in range(0, width):
    for y in range(0, height):
        (r_overlay, g_overlay, b_overlay) = overlay_pixels[x,y]
        (r_background, g_background, b_background) = background_pixels[x,y]
        
        if abs(r_overlay-66)< 80 and abs(g_overlay-229)<80 and abs(b_overlay- 24)<80:
            combined_pixels[x,y] = (r_background, g_background, b_background)
        else:
            combined_pixels[x,y] = (r_overlay, g_overlay, b_overlay)

# Show the newly created image
image_combined.show()

# Image enhancing
# enhanc_image = ImageEnhance.Contrast(image_combined)
# enhanc_image.enhance(1.3).show("30% more contrast")



# Save new image to this location
image_combined.save(file_path + "NEW_IMAGE.jpg")


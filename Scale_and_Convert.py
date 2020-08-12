#!/usr/bin/env python3

from PIL import Image, UnidentifiedImageError
from sys import platform
import os
import re

class scale_and_convert:
    def __init__(self):
        pass
    def image_formatting(self):
        # Acquire directory information.
        cwd = os.getcwd()
        
        # origin = cwd + "/" + input("Enter location of formatted files to be formatted: ")
        # dest = cwd + "/" + input("Enter location of formatted files to be saved: ")
        
        # origin = input("Enter location of formatted files to be formatted: ")
        # dest = input("Enter location of formatted files to be saved: ")
        
        # origin = r"C:\Users\KyleHollands\OneDrive\Education\Coursera\Google IT Automation with Python\Automating Real-World Tasks with Python\Week 1\Resources\Scale and Convert Images using PIL\Incorrectly Formatted Images/"
        # dest = r"C:\Users\KyleHollands\OneDrive\Education\Coursera\Google IT Automation with Python\Automating Real-World Tasks with Python\Week 1\Resources\Scale and Convert Images using PIL\Correctly Formatted Images/"
        
        origin = "/home/student-02-55178bc2d8eb/images/"
        dest = "/opt/icons/"
        
        # Acquire attribute information.
        rotation = int(input("Enter image rotation value (clockwise): "))
        img_width = int(input("Enter new image width: "))
        img_height = int(input("Enter new image height: "))
        ext = str(input("Enter extension to be converted to (.jpg, .png, etc): "))
        
        # Loop through all images in acquired directory, then apply modifications.
        
        # Tested to work in linux
        
        for image in os.listdir(origin):
            try:
                img = Image.open(origin + image)
                img.rotate(rotation).resize((img_width,img_height)).convert("RGB").save(dest + image.split('.')[0],ext)
                img.close()
                
            except UnidentifiedImageError:
                continue
        
        # Tested to work in Windows
        
        # for img in os.listdir(origin):
        #     try:
        #         if os.path.isdir(dest):
        #             im = Image.open(origin + "/" + img)
        #             img = re.sub(r'([.][a-z]+)',ext,img)
        #             im.rotate(rotation).resize((img_width,img_height)).convert("RGB").save(dest + "/" + img)
        #             im.close()

        #     except UnidentifiedImageError:
        #         continue
            
scale_and_convert().image_formatting()
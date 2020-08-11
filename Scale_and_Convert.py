#!/usr/bin/env python3

from PIL import Image, UnidentifiedImageError
import os
import re

class scale_and_convert:
    def __init__(self):
        pass
    def image_formatting(self):
        # Acquire directory information.
        cwd = os.getcwd()
        
        origin = cwd + "/" + input("Enter location of formatted files to be formatted: ")
        dest = cwd + "/" + input("Enter location of formatted files to be saved: ")
        
        # origin = r"C:\Users\KyleHollands\OneDrive\Education\Coursera\Google IT Automation with Python\Automating Real-World Tasks with Python\Week 1\Resources\Scale and Convert Images using PIL\Incorrectly Formatted Images/"
        # dest = r"C:\Users\KyleHollands\OneDrive\Education\Coursera\Google IT Automation with Python\Automating Real-World Tasks with Python\Week 1\Resources\Scale and Convert Images using PIL\Correctly Formatted Images/"
        
        # origin = "/home/student-04-af18cecbf8f1/images/"
        # dest = "/opt/icons/"
        
        # Acquire attribute information.
        rotation = int(input("Enter image rotation value (clockwise): "))
        img_width = int(input("Enter new image width: "))
        img_height = int(input("Enter new image height: "))
        ext = str(input("Enter extension to be converted to (.jpg, .png, etc): "))

        # If origin location exists, then loop through images to be formatted.
        
        for img in os.listdir(origin):
            try:
                if os.path.isdir(dest):
                    im = Image.open(origin + "/" + img)
                    img = re.sub(r'([.][a-z]+)',ext,img)
                    im.rotate(rotation).resize((img_width,img_height)).convert("RGB").save(dest + "/" + img)
                    im.close()

            except UnidentifiedImageError:
                continue
            
        print("Files formatted successfully.")
            
scale_and_convert().image_formatting()
#!/usr/bin/env python3

from PIL import Image
import os

class scale_and_convert:
    def __init__(self):
        pass
    def image_formatting(self):
        # Acquire directory information.
        cwd = os.getcwd()
        origin = cwd + "/" + input("Enter location of formatted files to be formatted: ")
        dest = cwd + "/" + input("Enter location of formatted files to be saved: ")
        
        # Acquire attribute information.
        rotation = int(input("Enter image rotation value (clockwise): "))
        img_width = int(input("Enter new image width: "))
        img_height = int(input("Enter new image height: "))
        ext = str(input("Enter extension to be converted to (.jpg, .png, etc): "))
        
        # Loop through images in chosen directory, then format according to information provided.
        for image in os.listdir(origin):
            try:
                img = Image.open(origin + "/" + image)
                img.rotate(rotation).resize((img_width,img_height)).convert("RGB").save(dest + "/" + image.split('.')[0] + "." + ext)
                img.close()
                
            # If a non-image file is located, skip and hide error message.
            except OSError:
                continue
            
        print("Files formatted successfully.")
        
        # Prevent window from closing immediately.
        
        k=input("press close to exit") 
        
scale_and_convert().image_formatting()
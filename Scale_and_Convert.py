from PIL import Image
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
        
        # Acquire attribute information.
        rotation = int(input("Enter image rotation value (clockwise): "))
        img_width = int(input("Enter new image width: "))
        img_height = int(input("Enter new image height: "))
        ext = input("Enter extension to be converted to (.jpg, .png, etc): ")

        # If origin location exists, then loop through images to be formatted.
        if os.path.isdir(origin):
            for img in os.listdir(origin):
                if os.path.isdir(dest):
                    im = Image.open(origin + "/" + img)
                    img_ext = re.sub(r'([.][a-z]+)',ext,img)
                    im.rotate(rotation).resize((img_width,img_height)).save(dest + "/" + "reformatted_" + img_ext)
                else:
                    print("Directory not found.")
                    break
        else:
            print("Directory not found.")
        
        print("Files formatted successfully.")
            
scale_and_convert().image_formatting()
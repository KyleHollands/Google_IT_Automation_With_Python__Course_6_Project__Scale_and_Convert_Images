from PIL import Image
import os

class scale_and_convert:
    def image_formatting(folder):
       
        for image in os.listdir(folder):
            im = Image.open(image)
            im.rotate(90).resize((640,480)).save(input("Select output folder: "))
        
    image_formatting(os.listdir(input("Select input folder: ")))
from PIL import Image
import os

class scale_and_convert:
    def image_formatting(folder):
    
        cwd = os.getcwd()
        
        if os.path.isdir(folder):
            for image in os.listdir(folder):
                if image.endswith(".jpg"):
                    im = Image(image)
                    im.rotate(90).resize((640,480)).save(cwd/input("Enter destination: "))
        else:
            return False
           
    image_formatting(input("Enter file location: "))
    
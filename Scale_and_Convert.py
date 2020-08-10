from PIL import Image
import os

class scale_and_convert:
    def __init__(self):
        pass
    def image_formatting(self, folder):
        # Acquire directory information.
        cwd = os.getcwd()
        dest = cwd + "/" + input("Enter location of formatted files to be saved: ")
        # Acquire attribute information.
        rotation = input("Enter image rotation value (clockwise): ")
        resizing = input("Enter resize values (#,#): ")
        ext = input("Enter extension to be converted to (.jpg, .png, etc): ")
                    
        # If origin location exists, then loop through images to be formatted.
        if os.path.isdir(folder):
            for img in os.listdir(folder):
                # if img.endswith(".jpg"):
                im = Image.open(folder + "/" + img)
                if os.path.isdir(dest):
                    im.rotate(90).resize((640,480)).save(dest + "/" + "reformatted_" + img)
                else:
                    print("Directory not found.")
                    break
        else:
            print("Directory not found.")
        
        print("Files formatted successfully.")
            
scale_and_convert().image_formatting(input("Enter location of files to be formatted: "))
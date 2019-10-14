#Import numpy
import numpy as np
#Import the os module, for the os.walk function
import os 
from PIL import Image

#Check the image if it is 512x512 or not
def checkImageSize512x512(image):
    width, height = image.size
    if width == 512 and height == 512:
        return 1
    else:
        return 0

#Resize the image
def resizeImage(image):
    try:
        return image.resize((512,512), Image.ANTIALIAS)
    except:
        print("Error in resizing image")

dirName, subdirList, fileList = next(os.walk("./photos"))
fileCount = len(fileList)
dictionary = np.zeros([fileCount, 512, 512, 3])

def main():
    # Set the directory you want to start from
    rootDir = '.'
    index = 0
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fileName in fileList:
            if "photos" in dirName:
                #Open image file
                image = Image.open(dirName+"/"+fileName)
                #Check image size
                if checkImageSize512x512(image) == 0:
                    #Resize image
                    image = resizeImage(image)
                dictionary[index] =  np.array(image)
                index = index + 1

if __name__ == "__main__":
    main()
    print(dictionary)
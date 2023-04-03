import sys
import os, glob
from PIL import ImageOps, Image
def main():
    folder = "Task35_P-Shirt/InputeImages"
    counter = 0
    user = sys. argv
    ext = checkExtensions(user)
    if checkArgvLen(user) == -1:
        print("Too few command-line arguments")
    elif checkArgvLen(user) == -2:
        print("Too many command-line arguments")
    elif checkArgvLen(user) == True:
        if ext == False:
            print("Input and output have different extensions")
        elif ext not in checkFileFormatsInFolder(folder):
            print("In the folder is not selected format images")
        else:
            for fileName in glob.glob(os.path.join(folder,"*."+ ext)):
                inputImage = Image.open(fileName)
                outpotImage = Image.open("Task35_P-Shirt/shirt.png")
                imageSize = outpotImage.size
                image2 = ImageOps.fit(inputImage, imageSize, bleed = 0.0, centering =(0.5, 0.5))
                image2.paste(outpotImage,outpotImage)
                counter += 1
                image2.save("Task35_P-Shirt/OutputImages/OutputImage"+str(counter)+"."+ext)

def checkArgvLen(txt):
    if len(txt) < 3:
        return -1
    elif len(txt) > 3:
        return -2
    else:
        return True

def checkFileFormatsInFolder(f):
    files = glob.glob(os.path.join(f,"*.*"))
    fileExtensions = []
    for items in files:
        ext = items.split(".")
        fileExtensions.append(ext[1])
    return fileExtensions

def checkExtensions(txt):
    allowedFormats = ["jpg","png","jpeg"]
    try:
        ext1 = txt[1].split(".")
        ext2 = txt[2].split(".")
        if ext1[1] != ext2[1]:
            return False
        elif ext1[1] == ext2[1] and ext1[1] in allowedFormats:
            return ext1[1]
    except:
        return False

if __name__ == "__main__":
    main()

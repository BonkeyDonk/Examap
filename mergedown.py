from PIL import Image
Image.MAX_IMAGE_PIXELS = 10000000000000000

import os

print("Please list all files you want to paste on top of each other, in order from bottom to top. Ex: 'bottom.png middle.png top.png'.")
print("All images will paste at the top left, because i'm lazy to implement otherwise. Please make sure all images are the same resolution! (Ex: 43200x21600)")
print("The resolution of the final image is based off of the resolution of the bottom layer.")
cool = input("Input: ")
coollist = cool.split(" ")

print(coollist[0])
getres = Image.open(coollist[0])
wid, hgt = getres.size
getres.close()

final = Image.new("RGBA", (wid,hgt), "white")

# for y in range(6):
#     for x in range(12):
#         name = str(y) + str(f"{x+1:02}") + ".png"
#         print("Processing: " + name)
#         currentImage = Image.open(name)
#         x_pos = imconst * x
#         y_pos = imconst * y
#         final.paste(currentImage,(x_pos,y_pos),currentImage)

for name in coollist:
    currentImage = Image.open(name).convert("RGBA")
    print("Pasting: ", name)
    final.paste(currentImage,(0,0),currentImage)

nameToSaveAs = input("What do you want to save the image as? (ex: combined.png): ")
final.save(nameToSaveAs)
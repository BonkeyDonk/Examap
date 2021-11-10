from PIL import Image
Image.MAX_IMAGE_PIXELS = 100000000000

import os

imconst = 3600

final = Image.new("RGBA", (43200,21600), "white")

for y in range(6):
    for x in range(12):
        name = str(y) + str(f"{x+1:02}") + ".png"
        print("Processing: " + name)
        currentImage = Image.open(name)
        x_pos = imconst * x
        y_pos = imconst * y
        final.paste(currentImage,(x_pos,y_pos),currentImage)

nameToSaveAs = input("What do you want to save the image as? (ex: combined.png): ")
final.save(nameToSaveAs)
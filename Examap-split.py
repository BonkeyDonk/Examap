from PIL import Image
Image.MAX_IMAGE_PIXELS = 100000000000

import os
if not os.path.exists('examap_output'):
    os.makedirs('examap_output')

import os

imconst = 3600

input = Image.open("final.tif").convert("RGBA")

for y in range(6):
    for x in range(12):
        name = str(y) + str(f"{x+1:02}") + ".png"
        print("Processing: " + name)
        thisRegion = Image.new("RGBA", (3600,3600), "white")
        left = imconst * x
        top = imconst * y
        right = imconst * x + imconst
        bottom = imconst * y + imconst
        cropped = input.crop((left, top, right, bottom))
        thisRegion.paste(cropped,(0,0),cropped)
        thisRegion.save("examap_output/" + name)

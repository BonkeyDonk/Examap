from PIL import Image

import os

imconst = 3600

first = input("What is the top left grid to combine? (ex: 102): ")
first = list(first)
last = input("What is the bottom right grid to combine? (ex: 306): ")
last = list(last)

top = (int) (first[0])
left = ((int) (first[1] + first[2]))
bottom = (int) (last[0])
right = ((int) (last[1] + last[2]))
print(top)
print(left)
print(bottom)
print(right)

final = Image.new("RGBA", ((right-left+1)*imconst,(bottom-top+1)*imconst), "white")

for y in range(top,bottom+1):
    for x in range(left, right+1):
        name = str(y) + str(f"{x:02}") + ".png"
        print("Processing: " + name)
        currentImage = Image.open(name)
        x_pos = imconst * (x-left)
        y_pos = imconst * (y-top)
        final.paste(currentImage,(x_pos,y_pos),currentImage)

final.save("combined_region.png")
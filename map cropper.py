from os import listdir, getcwd, mkdir
from os.path import isfile, join
from PIL import Image
Image.MAX_IMAGE_PIXELS = 10000000000000

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "cropped_output")
try: mkdir(output)
except OSError: pass

crop = input("Input the x,y coordinates of the topleft pixel, then the x,y coordinates of the bottomright pixel:")
crop = [int(c) for c in crop.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))    

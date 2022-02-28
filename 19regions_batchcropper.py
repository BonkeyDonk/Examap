from os import listdir, getcwd, mkdir
from os.path import isfile, join
from PIL import Image
Image.MAX_IMAGE_PIXELS = 10000000000000

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "Europe")
try: mkdir(output)
except OSError: pass

crop1 = "17793 1051 27859 6685"
crop1 = [int(c) for c in crop1.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop1)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "Africa")
try: mkdir(output)
except OSError: pass

crop2 = "18490 6228 28606 15426"
crop2 = [int(c) for c in crop2.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop2)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "Middle East")
try: mkdir(output)
except OSError: pass

crop3 = "25630 6008 29229 9301"
crop3 = [int(c) for c in crop3.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop3)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "Greenland")
try: mkdir(output)
except OSError: pass

crop4 = "12727 653 20411 3694"
crop4 = [int(c) for c in crop4.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop4)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))
        
path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "Central Asia")
try: mkdir(output)
except OSError: pass

crop5 = "27157 4058 32111 6594"
crop5 = [int(c) for c in crop5.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop5)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))
        
path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "Lesser Akhand Bharat")
try: mkdir(output)
except OSError: pass

crop6 = "28878 6168 33294 10968"
crop6 = [int(c) for c in crop6.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop6)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "Australia")
try: mkdir(output)
except OSError: pass

crop7 = "35064 11877 40377 16133"
crop7 = [int(c) for c in crop7.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop7)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "New Zealand")
try: mkdir(output)
except OSError: pass

crop8 = "40556 14217 43199 16486"
crop8 = [int(c) for c in crop8.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop8)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))
        
path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "Southeast Asia")
try: mkdir(output)
except OSError: pass

crop9 = "32638 7348 40166 12235"
crop9 = [int(c) for c in crop9.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop9)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "KR-JP")
try: mkdir(output)
except OSError: pass

crop10 = "36475 4133 39758 7712"
crop10 = [int(c) for c in crop10.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop10)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "China + Mongolia")
try: mkdir(output)
except OSError: pass

crop11 = "30412 4334 37812 8661"
crop11 = [int(c) for c in crop11.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop11)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "South America")
try: mkdir(output)
except OSError: pass

crop12 = "10445 9248 17531 17626"
crop12 = [int(c) for c in crop12.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop12)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "Middle America")
try: mkdir(output)
except OSError: pass

crop13 = "7340 6845 14541 9983"
crop13 = [int(c) for c in crop13.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop13)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "Canada")
try: mkdir(output)
except OSError: pass

crop14 = "4615 760 15379 5811"
crop14 = [int(c) for c in crop14.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop14)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "Beringia")
try: mkdir(output)
except OSError: pass

crop15 = "0 1984 4734 4755"
crop15 = [int(c) for c in crop15.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop15)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "United States")
try: mkdir(output)
except OSError: pass

crop16 = "6574 4842 13599 7908"
crop16 = [int(c) for c in crop16.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop16)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "Western Pacific")
try: mkdir(output)
except OSError: pass

crop17 = "0 7214 6686 16203"
crop17 = [int(c) for c in crop17.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop17)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "Eastern Pacific")
try: mkdir(output)
except OSError: pass

crop18 = "40135 8301 43199 13964"
crop18 = [int(c) for c in crop18.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop18)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))

path = getcwd()

files = [
  f for f in listdir(path)
  if isfile(join(path, f))
]

output = join(path, "Siberia")
try: mkdir(output)
except OSError: pass

crop19 = "27430 947 43199 5762"
crop19 = [int(c) for c in crop19.split(" ")]

extensions = ["jpg", "png", "jpeg", "tif","tiff"]

for file in files:
  if file.split(".")[-1] not in extensions: continue

  with Image.open(file) as image:
    cropped = image.crop(crop19)
    cropped.save(join(output, file.split(".")[0]) + ".png")
    print("Processed {}".format(file))


                                                        

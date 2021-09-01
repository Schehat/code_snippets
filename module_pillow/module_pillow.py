import os
from PIL import Image, ImageFilter

os.chdir(os.path.dirname(__file__))

SIZE_400 = (400, 400)

image1 = Image.open("picture.png")

# image1.show()
# save file but convert the extension to jpg
# image1.save("picture.jpg")

# safe all png in a separate folder as jpgs
for f in os.listdir("."):
    if f.endswith(".png"):
        i = Image.open(f)
        ftext, fext = os.path.splitext(f)
        # from jpg to png the convert step can be skipped
        # like that: i.save(f"pngs/{ftext}.png")
        i.convert("RGB").save(f"jpgs/{ftext}.jpg")

# safe all png in a separate folder in size (400, 400)
for f in os.listdir("."):
    if f.endswith(".png"):
        i = Image.open(f)
        ftext, fext = os.path.splitext(f)
        i.thumbnail(SIZE_400)
        i.save(f"400/{ftext}_400{fext}")

for f in os.listdir("."):
    if f.endswith(".png"):
        i = Image.open(f)

        # all editing is not inplace
        # argument 90° degree
        i = i.rotate(90)
        # convert color: argument L equals black & white
        i = i.convert("L")
        # default is 2
        i = i.filter(ImageFilter.GaussianBlur(1))

        i.save(f"edit_overload/{ftext}_edit{fext}")

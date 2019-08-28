# -*- coding: utf-8 -*-

from PIL import Image
img = Image.open("file.png")
print(img.size)
cropped = img.crop((800, 325, 1280, 490))  # (left, upper, right, lower)
cropped.save("file1.png")
# -*- coding: utf-8 -*-

from PIL import Image
import settings.DIR_PATH as path


def get_ROIimg():
    img = Image.open(path.src_path + "file.png")
    # print(img.size)
    cropped = img.crop((800, 325, 1280, 490))  # (left, upper, right, lower)
    cropped.save(path.src_path + "file1.png")

if __name__ == "__main__":
    get_ROIimg()
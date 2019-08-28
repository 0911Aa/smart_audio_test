# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image
import settings.DIR_PATH as path

pytesseract.pytesseract.tesseract_cmd = 'D://Program Files (x86)/Tesseract-OCR/tesseract.exe'
img = Image.open(path.src_path+'file1.png')
print(pytesseract.image_to_string(img,lang='eng'))
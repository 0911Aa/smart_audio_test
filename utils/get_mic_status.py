# -*- coding: utf-8 -*-
from utils import get_img_ROI
import cv2
import time
from skimage.measure import compare_ssim
import settings.DIR_PATH as path

def get_mic_status(driver):
    # driver.screenshot("mic.png")
    get_img_ROI.get_ROIimg(100,250,364,476)

get_mic_status(1)
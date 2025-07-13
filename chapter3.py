#!/usr/bin/env python3

################################################################################
#                                                                              #
#  Chapter 3 – Image Resizing and Cropping                                     #
#                                                                              #
#  Author : Abdelrhman Sabry Mohamed                                           #
#  Email  : abd3lrhman.sabry@gmail.com                                         #
#                                                                              #
#  Description:                                                                #
#  This script demonstrates how to resize and crop an image using OpenCV.      #
#                                                                              #
################################################################################

import cv2
import numpy as np

img = cv2.imread("Resources/lena.JPG")
if img is None:
    exit()

print(img.shape)

imgResized = cv2.resize(img, (1000, 500))
print(imgResized.shape)
imgCropped = img[0:200, 200:500]

imgGray = cv2.cvtColor(imgResized, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

cv2.imshow("Original", img)
# cv2.imshow("Resized", imgResized)
cv2.imshow("cropped", imgCropped)

cv2.waitKey(0)
cv2.destroyAllWindows()

#!/usr/bin/env python3

################################################################################
#                                                                              #
#  Chapter 2 – Edge Detection and Morphological Operations                     #
#                                                                              #
#  Author : Abdelrhman Sabry Mohamed                                           #
#  Email  : abd3lrhman.sabry@gmail.com                                         #
#                                                                              #
#  Description:                                                                #
#  This script applies grayscale, blur, edge detection, dilation, and erosion #
#  to an image using OpenCV.                                                  #
#                                                                              #
################################################################################

import cv2
import numpy as np

img = cv2.imread("Resources/lena.jpg")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgcanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgcanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgcanny)
cv2.imshow("Dial Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)

#!/usr/bin/env python3

################################################################################
#                                                                              #
#  Chapter 1 – Image Processing Basics                                         #
#                                                                              #
#  Author : Abdelrhman Sabry Mohamed                                           #
#  Email  : abd3lrhman.sabry@gmail.com                                         #
#                                                                              #
#  Description:                                                                #
#  This script loads an image, converts it to grayscale, applies Gaussian      #
#  blur, and displays both results using OpenCV.                               #
#                                                                              #
################################################################################

import cv2

img = cv2.imread("Resources/lena.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.waitKey(0)

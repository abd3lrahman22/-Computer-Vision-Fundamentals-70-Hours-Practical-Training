#!/usr/bin/env python3

################################################################################
#                                                                              #
#  Chapter 5 – Perspective Transformation                                      #
#                                                                              #
#  Author : Abdelrhman Sabry Mohamed                                           #
#  Email  : abd3lrhman.sabry@gmail.com                                         #
#                                                                              #
#  Description:                                                                #
#  This script demonstrates how to apply a perspective warp to an image        #
#  using OpenCV by defining source and destination points.                     #
#                                                                              #
################################################################################

import cv2
import numpy as np

img = cv2.imread("Resources/images.jpeg")

if img is None:
    print("Error: Image not found.")
    exit()

width, height = 250, 350

pts1 = np.float32([[70, 220], [320, 210], [80, 470], [330, 460]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Original Image", img)
cv2.imshow("Warped Output", imgOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()

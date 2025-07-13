#!/usr/bin/env python3

################################################################################
#                                                                              #
#  Chapter 6 – Stacking Images in Grids using NumPy and OpenCV                #
#                                                                              #
#  Author : Abdelrhman Sabry Mohamed                                           #
#  Email  : abd3lrhman.sabry@gmail.com                                         #
#                                                                              #
#  Description:                                                                #
#  This script demonstrates how to create image grids by stacking multiple     #
#  copies of the same image horizontally and vertically using NumPy.           #
#                                                                              #
################################################################################

import cv2
import numpy as np

img = cv2.imread('Resources/lena.jpg')
img = cv2.resize(img, (300, 300))

row1 = np.hstack((img, img, img))
row2 = np.hstack((img, img, img))
imgGrid = np.vstack((row1, row2))
cv2.imshow("3x2 Image Grid", imgGrid)

imgRow = np.hstack((img, img, img))
cv2.imshow("3 Images Horizontal", imgRow)

cv2.waitKey(0)

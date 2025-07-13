#!/usr/bin/env python3

################################################################################
#                                                                              #
#  Chapter 4 – Drawing Shapes and Text on Images                               #
#                                                                              #
#  Author : Abdelrhman Sabry Mohamed                                           #
#  Email  : abd3lrhman.sabry@gmail.com                                         #
#                                                                              #
#  Description:                                                                #
#  This script demonstrates how to draw lines, rectangles, circles, and text   #
#  on a blank image using OpenCV functions.                                    #
#                                                                              #
################################################################################

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)
cv2.putText(img, "Opencv", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3)

cv2.imshow("img", img)
cv2.waitKey(0)

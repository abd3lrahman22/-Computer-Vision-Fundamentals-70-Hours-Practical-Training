#!/usr/bin/env python3

################################################################################
#                                                                              #
#  Chapter 7 – HSV Color Detection with Trackbars                              #
#                                                                              #
#  Author : Abdelrhman Sabry Mohamed                                           #
#  Email  : abd3lrhman.sabry@gmail.com                                         #
#                                                                              #
#  Description:                                                                #
#  This script uses trackbars to dynamically adjust HSV color ranges and       #
#  filter an image in real-time to isolate specific color areas.               #
#                                                                              #
################################################################################

import cv2
import numpy as np

def empty(a):
    pass

path = 'Resources/abdo.jpg'

cv2.namedWindow("TrackBarS")
cv2.resizeWindow("TrackBarS", 640, 240)

cv2.createTrackbar("Hue Min", "TrackBarS", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBarS", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBarS", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBarS", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBarS", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBarS", 255, 255, empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_Min = cv2.getTrackbarPos("Hue Min", "TrackBarS")
    h_Max = cv2.getTrackbarPos("Hue Max", "TrackBarS")
    s_Min = cv2.getTrackbarPos("Sat Min", "TrackBarS")
    s_Max = cv2.getTrackbarPos("Sat Max", "TrackBarS")
    v_Min = cv2.getTrackbarPos("Val Min", "TrackBarS")
    v_Max = cv2.getTrackbarPos("Val Max", "TrackBarS")

    lower = np.array([h_Min, s_Min, v_Min])
    upper = np.array([h_Max, s_Max, v_Max])

    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Original Image", img)
    cv2.imshow("HSV Image", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

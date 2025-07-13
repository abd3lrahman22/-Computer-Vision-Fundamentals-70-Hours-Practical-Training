#!/usr/bin/env python3

################################################################################
#                                                                              #
#  Chapter 9 – Face Detection with Haar Cascade Classifier                     #
#                                                                              #
#  Author : Abdelrhman Sabry Mohamed                                           #
#  Email  : abd3lrhman.sabry@gmail.com                                         #
#                                                                              #
#  Description:                                                                #
#  This script uses a Haar Cascade classifier to detect faces in an image      #
#  and draw bounding boxes around them using OpenCV.                           #
#                                                                              #
################################################################################

import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread('Resources/lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)

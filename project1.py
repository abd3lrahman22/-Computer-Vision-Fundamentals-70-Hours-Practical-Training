#!/usr/bin/env python3

################################################################################
#                                                                              #
#  Project 1 – Color Detection and Drawing with Webcam                         #
#                                                                              #
#  Author : Abdelrhman Sabry Mohamed                                           #
#  Email  : abd3lrhman.sabry@gmail.com                                         #
#                                                                              #
#  Description:                                                                #
#  This project captures video from a webcam, detects specific color ranges    #
#  using HSV thresholds, and draws on the frame based on the detected object   #
#  positions. Ideal for real-time color-based tracking and virtual painting.   #
#                                                                              #
################################################################################

import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

myColors = [
    [160, 50, 200, 175, 150, 255],
    [45, 100, 100, 75, 255, 255],
    [0, 100, 100, 10, 255, 200]
]

myColorValue = [
    [255, 153, 204],
    [0, 153, 76],
    [153, 0, 0]
]

myPoints = []

def getContours(img):
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y

def findColor(img, myColors, myColorValue):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints = []
    for count, color in enumerate(myColors):
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorValue[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
    return newPoints

def drawOnCanvas(points, colors):
    for point in points:
        cv2.circle(imgResult, (point[0], point[1]), 10, colors[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValue)
    if len(newPoints) != 0:
        for point in newPoints:
            myPoints.append(point)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValue)
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

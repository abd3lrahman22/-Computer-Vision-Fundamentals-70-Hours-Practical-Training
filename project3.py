#!/usr/bin/env python3

################################################################################
#                                                                              #
#  Project 3 – Automatic Car Number Plate Detection and Cropping              #
#                                                                              #
#  Author : Abdelrhman Sabry Mohamed                                           #
#  Email  : abd3lrhman.sabry@gmail.com                                         #
#                                                                              #
#  Description:                                                                #
#  This project loads a set of car images, detects Russian-style number        #
#  plates using Haar Cascade Classifier, draws bounding boxes, and saves      #
#  the cropped plates automatically to a specified folder.                     #
#                                                                              #
################################################################################

import cv2
import os

# Full path to Resources folder
base_path = r"C:\Users\hp\PycharmProjects\OpencvPython\Resources"

# Load number plate detector
xml_path = os.path.join(base_path, "haarcascade_russian_plate_number.xml")
nPlateCascade = cv2.CascadeClassifier(xml_path)

# List of images to process
images = ["p1.jpg", "p2.jpg", "p3.jpg"]
minArea = 200
color = (255, 0, 255)
count = 0

for img_name in images:
    img_path = os.path.join(base_path, img_name)
    img = cv2.imread(img_path)

    if img is None:
        print(f"⚠️ Image not found: {img_path}")
        continue

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)

    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, "Number Plate", (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y + h, x:x + w]
            cv2.imshow("ROI", imgRoi)

            save_path = os.path.join(base_path, "Scanned", f"NoPlate_{count}.jpg")
            cv2.imwrite(save_path, imgRoi)
            count += 1

    cv2.imshow("Result", img)
    cv2.waitKey(5000)

cv2.destroyAllWindows()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import cv2
import create_fog_image

def get_visibility(test_image, clear_image):
    img = cv2.imread(test_image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
  
    yellow = cv2.inRange(hsv, [20, 100, 100], [30, 255, 255]) # For different colors, change the upper and lower limits
    white = cv2.inRange(gray, 200, 255)
    mask_one = cv2.bitwise_or(white, yellow)
    temp_image = cv2.bitwise_and(gray, mask_one)

    gauss = cv2.GaussianBlur(temp_image, kernel_size=(5, 5), 0)

    canny = cv2.Canny(gauss, 50, 150) # Threshold = 50 & 150

    """THE DISTANCE OF VISIBILITY CAN BE CHANGED USING THIS PORTION OF THE CODE"""
    imshape = canny.shape
    lower_left = [0*imshape[1],imshape[0]*0.6]
    lower_right = [0.5*imshape[1],imshape[0]*0.45]
    top_left = [0*imshape[1],imshape[0]]
    top_right = [0.8*imshape[1],imshape[0]]
    vertices = [np.array([lower_left,top_left,top_right,lower_right],dtype=np.int32)]

    empty_mask = np.zeros_like(canny)
    cv2.fillPoly(empty_mask, vertices, 255)
    interest_area = cv2.bitwise_and(canny, empty_mask)

    actual = cv2.imread(clear_image, 0)
    diff = cv2.bitwise_and(interest_area, actual)

    visibility = diff.mean()/actual.mean() * 100
    return visibility

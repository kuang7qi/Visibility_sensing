import cv2
import numpy as np

# Read Image1

def foggy_image(road, fog, fog_weight):
    road = cv2.imread(road)
    fog = cv2.imread(fog)

    img2 = cv2.resize(fog, (1200, 703))
    img = cv2.addWeighted(road, 1, img2, fog_weight, 0)

    cv2.imwrite('current_image.png', img)

import numpy as np
import cv2

image = cv2.imread('image_rue.jpg',0)

#on découpe le haut gauche de notre image
height = int(np.size(image, 0)/2)
width = int(np.size(image, 1)/3)
crop_image = image[0:0+height, 0:0+width]


_, threshold = cv2.threshold(crop_image, 100, 255, cv2.THRESH_BINARY)
_, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


for cnt in contours:

    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(image, [cnt], 0, (0), 5)

    '''
    x = cnt.ravel()[0]
    y = cnt.ravel()[1]

    if len(cnt) == 3:
        cv2.putText(image, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0))
    elif len(cnt) == 4:
        cv2.putText(image, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0))
    elif len(cnt) == 5:
        cv2.putText(image, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0))
    elif 6 < len(cnt) < 15:
        cv2.putText(image, "Ellipse", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0))
    else:
        cv2.putText(image, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0))   
'''

cv2.imshow("image",image)
cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
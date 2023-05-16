import numpy as np
import cv2
import matplotlib.pyplot as plt
import cv2
import os
import argparse

#links
#https://pyimagesearch.com/2016/10/31/detecting-multiple-bright-spots-in-an-image-with-python-and-opencv/
#https://stackoverflow.com/questions/51846933/finding-bright-spots-in-a-image-using-opencv
#https://www.programcreek.com/python/example/88833/skimage.measure.label


from imutils import contours
from skimage import measure
Image = ('testing.jpg') # save images as newimage{column index} 
read = cv2.imread(Image)#this will need to loop through all images that need to be read


#  constants
BINARY_THRESHOLD = 20
CONNECTIVITY = 8
DRAW_CIRCLE_RADIUS = 4

#  convert to gray
gray_image = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY)

#  extract edges
binary_image = cv2.Laplacian(gray_image, cv2.CV_8UC1)

#  fill in the holes between edges with dilation
dilated_image = cv2.dilate(binary_image, np.ones((5, 5)))

#  threshold the black/ non-black areas
_, thresh = cv2.threshold(dilated_image, BINARY_THRESHOLD, 255, cv2.THRESH_BINARY)

#  find connected components
components = cv2.connectedComponentsWithStats(thresh, CONNECTIVITY, cv2.CV_32S)

#  draw circles around center of components
#see connectedComponentsWithStats function for attributes of components variable
centers = components[3]
for center in centers:
    cv2.circle(thresh, (int(center[0]), int(center[1])), DRAW_CIRCLE_RADIUS, (255), thickness=-1)

cv2.imwrite("res.png", thresh)
locate = cv2.minMaxLoc(thresh)
print(locate)
cv2.imshow("res", thresh)
cv2.waitKey(0)
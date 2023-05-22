# import the necessary packages
from imutils import contours
from skimage import measure
import numpy as np
import argparse
import imutils
import cv2
import PIL

image = cv2.imread("TestingImages/testing.jpg")

# construct the argument parse and parse the arguments
BINARY_THRESHOLD = 40
CONNECTIVITY = 4
DRAW_CIRCLE_RADIUS = 4

#  convert to gray
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#  extract edges
binary_image = cv2.Laplacian(gray_image, cv2.CV_8UC1)

#  fill in the holes between edges with dilation
dilated_image = cv2.dilate(binary_image, np.ones((5, 5)))

#  threshold the black/ non-black areas
_, thresh = cv2.threshold(dilated_image, BINARY_THRESHOLD, 255, cv2.THRESH_BINARY)

erode = cv2.erode(thresh, None, iterations=2)
cv2.imshow("result", erode)
cv2.waitKey(0)
#  find connected components
components = cv2.connectedComponentsWithStats(erode, CONNECTIVITY, cv2.CV_32S)

#  draw circles around center of components
#see connectedComponentsWithStats function for attributes of components variable
centers = components[3]
for center in centers:
	DrawCircle = cv2.circle(thresh, (int(center[0]), int(center[1])), DRAW_CIRCLE_RADIUS, (255), thickness=-1)
	locate = cv2.minMaxLoc(DrawCircle)
	print(locate)

cv2.imwrite("res.png", thresh)
# cv2.imshow("result", thresh)
# cv2.waitKey(0)
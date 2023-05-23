# import the necessary packages
from imutils import contours
from skimage import measure
import numpy as np
import argparse
import imutils
import cv2
import PIL

image = cv2.imread("TestingImages/testing0.jpg")	


#~~~~~stolen code~~~~~#

# # construct the argument parse and parse the arguments
BINARY_THRESHOLD = 20
CONNECTIVITY = 4
DRAW_CIRCLE_RADIUS = 4
# #  convert to gray
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# #  extract edges
# binary_image = cv2.Laplacian(gray_image, cv2.CV_8UC1)
# #  fill in the holes between edges with dilation
# dilated_image = cv2.dilate(binary_image, np.ones((5, 5)))
# #  threshold the black/ non-black areas
# _, thresh = cv2.threshold(dilated_image, BINARY_THRESHOLD, 255, cv2.THRESH_BINARY)
# erode = cv2.erode(thresh, None, iterations=2)
# res = cv2.circle(thresh, (int(center[0]), int(center[1])), DRAW_CIRCLE_RADIUS, (255), thickness=-1)
# res = np.argwhere((thresh > 250).any(-1))


#~~~~my code~~~~~#
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #the first parameter is the image that is read by cv2	
blurred = cv2.GaussianBlur(gray, (11, 11), 0)	
thresh = cv2.threshold(blurred, 200, 250, cv2.THRESH_BINARY)[1]	
erode = cv2.erode(thresh, None, iterations=2) # perform a series of erosions and dilations to remove any small blobs of noise from the thresholded image

#  find connected components
components = cv2.connectedComponentsWithStats(erode, CONNECTIVITY, cv2.CV_32S)

CenterList = []
centers = components[3]
for center in centers:	
	CenterList.append(center)#appending center coordinates to list

CenterList.pop(0)#removing first value (first value will always be the center of the image)
print(CenterList)
cv2.imwrite("result.png", thresh)
# # cv2.imshow("result", thresh)
# cv2.waitKey(0)
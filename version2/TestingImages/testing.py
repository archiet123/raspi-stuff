import numpy as np
import cv2
import matplotlib.pyplot as plt
# from matplotlib import imread
import cv2
import os
import argparse
import PIL

Connectivity = 4

image = cv2.imread("testing.jpg")	

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #the first parameter is the image that is read by cv2	
blurred = cv2.GaussianBlur(gray, (11, 11), 0)	
thresh = cv2.threshold(blurred, 200, 250, cv2.THRESH_BINARY)[1]	
erode = cv2.erode(thresh, None, iterations=2) # perform a series of erosions and dilations to remove any small blobs of noise from the thresholded image

components = cv2.connectedComponentsWithStats(erode, Connectivity, cv2.CV_32S)

CenterList = []
centers = components[3]
for center in centers:#center is the coordinate for each component (where a pixel is greater than 255)
	print(center)
	rounded = center.round()#rounding each coordinate	
	CenterList.append(rounded)#appending center coordinates to list

CenterList.pop(0)#removing first value (first value will always be the center of the image)
print(CenterList)
listToStr = ' '.join([str(elem) for elem in CenterList])#converts CenterList from nparray to list
print(listToStr) 
ClearedString = listToStr.replace(".", "").replace("]", "").replace("[", "").replace(" ", "")#clears all unwanted characters
print(ClearedString)
newstring = ''.join(" " if i % 3 == 0 else char for i, char in enumerate(ClearedString))#removes every third number in string so only the "Y" axis remains
print(newstring)
cv2.imwrite("result.png", thresh)
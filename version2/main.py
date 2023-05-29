import numpy as np
import cv2
import matplotlib.pyplot as plt
# from matplotlib import imread
import cv2
import os
import argparse
import PIL

from backend import * #importing variables from other file
os.system('python backend.py')

Connectivity = 4

for index in range(81):      

	image = cv2.imread(f"assets/testing{index}.jpg")	
	#image = cv2.imread(f"TestingImages/testing.jpg")

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #the first parameter is the image that is read by cv2	
	blurred = cv2.GaussianBlur(gray, (11, 11), 0)	
	thresh = cv2.threshold(blurred, 200, 250, cv2.THRESH_BINARY)[1]	
	erode = cv2.erode(thresh, None, iterations=2) # perform a series of erosions and dilations to remove any small blobs of noise from the thresholded image

	components = cv2.connectedComponentsWithStats(erode, Connectivity, cv2.CV_32S)

	YCoords = []
	CenterList = []
	centers = components[3]
	for center in centers:#center is the coordinate for each component (where a pixel is greater than 255)		
		YValue = (center[1])
		YCoords.append(YValue)
	YCoords.pop(0)#removing first value (first value will always be the center of the image)
	# print(type(YCoords))
	
	RoundedYCoords = [round(num) for num in YCoords]
	#print(F"index: {index} Coord: {RoundYCoords}")

	# for i in RoundYCoords:
	# 	selector = getCharacter(RoundYCoords)
	# 	print(selector)

	def GetSelector(*params):
				
		for num in params:			
			selector = 0
			if num > 310:
				selector = 9
				print(selector)				
			elif num > 275:
				selector = 8
				print(selector)				
			elif num > 240:
				selector = 7
				print(selector)				
			elif num > 200:
				selector = 6
				print(selector)				
			elif num > 170:
				selector = 5
				print(selector)				
			elif num > 130:
				selector = 4
				print(selector)				
			elif num > 100:
				selector = 3
				print(selector)
			elif num > 60:
				selector = 2
				print(selector)
			elif num > 35:
				selector = 1
				print(selector)
			elif num > 20:
				selector = 0
				print(selector)
		return selector
			
		
			
	#input list
	my_list = [32, 137]
	#function call
	selector = GetSelector(*RoundedYCoords)
	print(f"index: {index} selector: {selector}")
	
	
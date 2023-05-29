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

def getList(final2):	
	if final2 > 20:
		#print("top row")
		return BList
	elif final2 > 1:
		#print("top row")
		
		return AList
	elif final2 == 0:
		return List
	
	else:
		return List

Connectivity = 4

FinalString = ""


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
	if RoundedYCoords == []:
		RoundedYCoords.append(500)
		print(RoundedYCoords)
	
	def GetSelector(*params):
		AList = ['&','A','B','C','D','E','F','G','H','I']
		BList = ['-','J','K','L','M','N','O','P','Q','R']
		CList = ['/','S','T','U','V','W','X','Y','Z']
		List = ['0','1','2','3','4','5','6','7','8','9',' ']
		List = List
		for num in params:			
			selector = 0
			if num > 500:
				selector = 10
				print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")
			if num > 400:
				selector = 9				
				print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")				
			elif num > 375:
				selector = 8
				print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")				
			elif num > 335:
				selector = 7
				print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")			
			elif num > 300:
				selector = 6
				print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")				
			elif num > 265:
				selector = 5
				print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")				
			elif num > 235:
				selector = 4
				print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")			
			elif num > 195:
				selector = 3
				print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")
			elif num > 165:
				selector = 2
				print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")
			elif num > 130:
				selector = 1
				print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")
			elif num > 65:
				List = BList
				selector = 0
				print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")
			elif num > 25:
				List = AList
				selector = 0
				print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")
			elif num == "":
				selector = 10
		return selector
	

			
	
	#function call
	selector = GetSelector(*RoundedYCoords)
	FinalString+=List[selector]#appends character selection to final string
	# print(f"index: {index} selector: {selector}")
	
splited_str = []
n  = 9
# looping through  example_str from 0 to length
# of example_str in a step size of 5
for index in range(0, len(FinalString), n):
	# slicing at iteration stops and storing it in splited_str
	splited_str.append(FinalString[index : index + n]) 
print(splited_str)
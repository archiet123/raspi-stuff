import numpy as np
import cv2
import matplotlib.pyplot as plt
import cv2
import os
import argparse




#importing variables from other file
print(f"\nimage to select from:")
print("abc123, abcCard, all80, card, first_image, realTest, spacedPunches\n")
#creating a parser
parser = argparse.ArgumentParser()
#adding the argument, "--name" is how this value is refered to if there are multiple arguments parsed.
parser.add_argument('--imageName', type=str, required=True)

#assigning argument to variable
value = parser.parse_args()

#assigning imageName to varible, can be accessed faster
getImage = value.imageName

img = cv2.imread(f'ImagesToRead/{getImage}.jpg')#reading init pic
#cv2.imshow('window', img)
#cv2.waitKey()

aList = ['A','B','C','D','E','F','G','H','I']
bList = ['J','K','L','M','N','O','P','Q','R']
List = []


def autoCoords():
	leftY = 468
	rightY = 480
	
	for index in range(0,81):
		
		column0 = img[280:650, leftY:rightY]
		plt.imsave(f"assets/testing{index}.jpg", column0)		

		
		leftY +=13
		rightY +=13

		if index == 0 :
			continue

		if index % 5:
			#print(index, "removing 4")
			leftY +=-1
			rightY +=-1

		if index == 38:
			#print(index, "removing 4")
			leftY +=-4
			rightY +=-4	


		# if index == 7:
		# 	#print(index, "removing 4")
		# 	leftY +=-4
		# 	rightY +=-4	
		
		# if index == 13:
		# 	#print(index, "removing 4")
		# 	leftY +=-4
		# 	rightY +=-4	

		# if index == 17:
		# 	#print(index, "removing 4")
		# 	leftY +=-4
		# 	rightY +=-4	
		
		# if index == 22:
		# 	#print(index, "removing 4")
		# 	leftY +=-4
		# 	rightY +=-4	
		
		# if index == 27:
		# 	#print(index, "removing 4")
		# 	leftY +=-6
		# 	rightY +=-6

		# if index == 30:
		# 	#print(index, "removing 4")
		# 	leftY +=-4
		# 	rightY +=-4

def topRow():
	leftY = 468
	rightY = 480
	
	for index in range(0,80):
		
		column0 = img[210:290, leftY:rightY]
		plt.imsave(f"top_row_images/testing{index}.jpg", column0)		

		# if index >= 40: 
		# 	leftY +=12
		# 	rightY +=12
		# else:
		leftY +=13
		rightY +=13

		if index == 0 or index == 72:
			continue

		if index == 7:
			#print(index, "removing 4")
			leftY +=-4
			rightY +=-4	

		if index % 8 == 0:
			#print(index, "removing 4")
			leftY +=-4
			rightY +=-4				

		if index % 22 == 0:
			#print(index, "removing 4")
			leftY +=-4
			rightY +=-4
		
		if index % 30 == 0:
			#print(index, "removing 4")
			leftY +=-4
			rightY +=-4

		if index % 38 == 0:
			#print(index, "added 4")
			leftY +=-4
			rightY +=-4

		if index % 51 == 0:
			#print(index, "added 4")
			leftY +=-4
			rightY +=-4

		if index % 78 == 0:
			#print(index, "added 4")
			leftY +=-4
			rightY +=-4

		if index % 79 == 0:
			#print(index, "added 4")
			leftY +=-4
			rightY +=-4


autoCoords()
topRow()

def getCharacter(final):	
	selector = 0
	if final > 310:
		selector = 9
	elif final > 270:
		selector = 8
	elif final > 240:
		selector = 7
	elif final > 200:
		selector = 6
	elif final > 160:
		selector = 5
	elif final > 130:
		selector = 4
	elif final > 100:
		selector = 3
	elif final > 60:
		selector = 2
	elif final > 35:
		selector = 1
	elif final > 20:
		selector = 0
	return selector



	

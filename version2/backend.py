import numpy as np
import cv2
import matplotlib.pyplot as plt
import cv2
import os
import argparse




#importing variables from other file
print(f"\nimage to select from:")
print("ABC123, All80, AlphabetTest, RandomCharacters, SpacedPunches, ZeroToNine, ZeroToZ\n")
#creating a parser
parser = argparse.ArgumentParser()
#adding the argument, "--name" is how this value is refered to if there are multiple arguments parsed.
parser.add_argument('--ImageName', type=str, required=True)

#assigning argument to variable
value = parser.parse_args()

#assigning imageName to varible, can be accessed faster
getImage = value.ImageName

img = cv2.imread(f'ImagesToRead/{getImage}.jpg')#reading init pic
#cv2.imshow('window', img)
#cv2.waitKey()

aList = ['A','B','C','D','E','F','G','H','I']
bList = ['J','K','L','M','N','O','P','Q','R']
List = []


def AutoCoords():
	leftY = 468
	rightY = 480
	
	for index in range(0,81):
		
		column0 = img[200:650, leftY:rightY]
		plt.imsave(f"assets/testing{index}.jpg", column0)
		
		leftY +=13
		rightY +=13	
		
		if index == 8:
			leftY +=-4
			rightY +=-4

		if index == 14:
			leftY +=-4
			rightY +=-4

		if index == 17:
			leftY +=-4
			rightY +=-4
		
		if index == 23:
			leftY +=-6
			rightY +=-6		

		if index == 29:
			leftY +=-4
			rightY +=-4	

		if index == 31:
			leftY +=-6
			rightY +=-6

		if index == 39:
			leftY +=-6
			rightY +=-6
		
		if index == 43:
			leftY +=-6
			rightY +=-6

		if index == 49:
			leftY +=-6
			rightY +=-6

		if index == 56:
			leftY +=-6
			rightY +=-6

		if index == 60:
			leftY +=-6
			rightY +=-6

		if index == 67:
			leftY +=-6
			rightY +=-6

		if index == 75:
			leftY +=-6
			rightY +=-6
		
		if index == 79:
			leftY +=-4
			rightY +=-4

AutoCoords()

def getCharacter(RoundYCoords):	
	selector = 0
	if RoundYCoords > 310:
		selector = 9
	elif RoundYCoords > 275:
		selector = 8
	elif RoundYCoords > 240:
		selector = 7
	elif RoundYCoords > 200:
		selector = 6
	elif RoundYCoords > 170:
		selector = 5
	elif RoundYCoords > 130:
		selector = 4
	elif RoundYCoords > 100:
		selector = 3
	elif RoundYCoords > 60:
		selector = 2
	elif RoundYCoords > 35:
		selector = 1
	elif RoundYCoords > 20:
		selector = 0
	return selector



	

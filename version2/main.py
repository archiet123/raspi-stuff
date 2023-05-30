import numpy as np
import cv2
import matplotlib.pyplot as plt
# from matplotlib import imread
import cv2
import os
import argparse
import PIL

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

def getList(ListChoice):	
	if ListChoice == 0:		
		return List
	elif ListChoice == 1:		
		return AList
	elif ListChoice == 2:
		return BList
	elif ListChoice == 3:
		return CList	
	else:
		return List

def GetList(SelectA, SelectB, SelectC, ActiveA, ActiveB, ActiveC):
	if SelectA == True and ActiveA == True:
		return AList
	elif SelectB == True and ActiveB == True:
		return BList
	elif SelectC == True and ActiveC == True:
		return CList
	else:
		return List

Connectivity = 4
AList = ['&','A','B','C','D','E','F','G','H','I']
BList = ['-','J','K','L','M','N','O','P','Q','R']
CList = ['/','S','T','U','V','W','X','Y','Z']
List = ['0','1','2','3','4','5','6','7','8','9',' ']
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
		RoundedYCoords.append(501)
		#print(RoundedYCoords)
	
	def GetSelector(*params):		
		global ListChoice		
		global SelectA 
		global SelectB 
		global SelectC 
		global ActiveA
		global ActiveB
		global ActiveC
		SelectA = False
		SelectB = False
		SelectC = False
		ActiveA = False
		ActiveB = False
		ActiveC = False
		for num in params:			
			selector = 0
			if num > 500:
				selector = 10
				#print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")
			elif num > 400:
				selector = 9
				SelectA = True
				SelectB = True
				SelectC = True				
				#print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")				
			elif num > 375:
				selector = 8
				SelectA = True
				SelectB = True
				SelectC = True
				#print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")				
			elif num > 335:
				selector = 7
				SelectA = True
				SelectB = True
				SelectC = True
				#print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")			
			elif num > 300:
				selector = 6
				SelectA = True
				SelectB = True
				SelectC = True
				#print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")				
			elif num > 265:
				selector = 5
				SelectA = True
				SelectB = True
				SelectC = True
				#print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")				
			elif num > 235:
				selector = 4
				SelectA = True
				SelectB = True
				SelectC = True
				#print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")			
			elif num > 195:
				selector = 3
				SelectA = True
				SelectB = True
				SelectC = True
				#print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")
			elif num > 165:
				selector = 2
				SelectA = True
				SelectB = True
				SelectC = True
				#print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")
			elif num > 130:
				selector = 1
				SelectA = True
				SelectB = True
				SelectC = True
				#print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")
			elif num > 100:
				
				ActiveC = True
				selector = 0
				#print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")
			elif num > 65:
				
				ActiveB = True
				selector = 0
				#print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")
			elif num > 25:
								
				ActiveA = True
				selector = 0
				#print(f" index: {index} coord: {num} numbers: {RoundedYCoords} selector: {selector}")			
		return selector
		

			
	
	#function call
	selector = GetSelector(*RoundedYCoords)
	listSelector = GetList(SelectA, SelectB, SelectC, ActiveA, ActiveB, ActiveC)#selects the list that the selector will select from
	FinalString+=listSelector[selector]#appends character selection to final string
	#print(FinalString)
	#print(f"index: {index} selector: {selector}")
	
splited_str = []
n  = 9
# looping through  example_str from 0 to length
# of example_str in a step size of 5
for index in range(0, len(FinalString), n):
	# slicing at iteration stops and storing it in splited_str
	splited_str.append(FinalString[index : index + n]) 
print(splited_str)
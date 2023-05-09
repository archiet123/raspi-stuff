import numpy as np
import cv2
import matplotlib.pyplot as plt
import cv2
import os
import argparse

from picamera import PiCamera
camera = PiCamera()
camera.rotation = -180

camera.capture(f'/home/pi/raspi-stuff/version2/ImagesToRead/currentCard.jpg')#taking init pic
#img = cv2.imread(f'ImagesToRead/freshImage.jpg')#reading init pic

from backend import * #importing variables from other file
os.system('python backend.py')


def getList(final2):	
	if final2 > 20:
		#print("top row")
		return bList
	elif final2 > 1:
		#print("top row")
		
		return aList
	elif final2 == 0:
		return List
	else:
		return List

aList = ['X','A','B','C','D','E','F','G','H','I']
bList = ['X','J','K','L','M','N','O','P','Q','R']
List = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



final_string = ""

toRemove = ["/", ")", "("]


#going to have to do everything twice in this loop, once for 0-9 and once for top rows
for index in range(80):
	imageName = (f'assets/testing{index}') # save images as newimage{column index} 
	top_row_image = (f'top_row_images/testing{index}')
 
	read = cv2.imread(f'{imageName}.jpg')#this will need to loop through all images that need to be read
	read2 = cv2.imread(f'{top_row_image}.jpg')

	gray = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY) #the first parameter is the image that is read by cv2	
	gray2 = cv2.cvtColor(read2, cv2.COLOR_BGR2GRAY)

	blurred = cv2.GaussianBlur(gray, (11, 11), 0)	
	blurred2 = cv2.GaussianBlur(gray2, (11, 11), 0)

	thresh = cv2.threshold(blurred, 200, 250, cv2.THRESH_BINARY)[1]	
	thresh2 = cv2.threshold(blurred2, 200, 250, cv2.THRESH_BINARY)[1]	

	erode = cv2.erode(thresh, None, iterations=2) # perform a series of erosions and dilations to remove any small blobs of noise from the thresholded image
	erode2 = cv2.erode(thresh2, None, iterations=2)

	#cv2.imwrite('assets/eroded.jpg', erode)#saves the eroded image to the directory
	#cv2.imshow('window', erode)	
	minMaxLoc = cv2.minMaxLoc(erode)#minMaxloc finds the darkest and brightest part of the image (varibale) 'erode'
	minMaxLoc2 = cv2.minMaxLoc(erode2)

	yRegion = str(minMaxLoc)[25:29]#just gets the Y axis 	
	yRegion2 = str(minMaxLoc2)[25:30]

	final = yRegion.replace(')', '')#replacing the bracket that is returned with tripple digit coords
	final2 = yRegion2.replace(')', '')	
	
	#print(f'the size of the image is: {shape}')	
	#print(f'the brightest part of the image, darkest part of the image, x coord, y coord{minMaxLoc}')	
	#print(f'{imageName} {final}')

	#print(final2)

	if final2 == '':
		final2 = '1'
	
	if final == '':
		final = '0'
	
	final = int(final)
	final2 = int(final2)
	selector = getCharacter(final)
		
	listSelector = getList(final2)
	
	final_string+=listSelector[selector]
	


		

print("\n")
print(f"the punchcard had {index +1} columns punched")
#print(f'The final string is: {final_string}')

splited_str = []
n  = 10
# looping through  example_str from 0 to length
# of example_str in a step size of 5
for index in range(0, len(final_string), n):
    # slicing at iteration stops and storing it in splited_str
    splited_str.append(final_string[index : index + n]) 
print(splited_str)
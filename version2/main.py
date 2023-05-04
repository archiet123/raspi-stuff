import numpy as np
import cv2
import matplotlib.pyplot as plt
import cv2
import os
import argparse

from backend import * #importing variables from other file
os.system('python backend.py')




characters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
final_string = ""

toRemove = ["/", ")", "("]

for index in range(81):
	imageName = (f'assets/testing{index}') # save images as newimage{column index}    	
	read = cv2.imread(f'{imageName}.jpg')#this will need to loop through all images that need to be read

	
	gray = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY) #the first parameter is the image that is read by cv2
	
	blurred = cv2.GaussianBlur(gray, (11, 11), 0)	
	thresh = cv2.threshold(blurred, 200, 250, cv2.THRESH_BINARY)[1]	
	erode = cv2.erode(thresh, None, iterations=2) # perform a series of erosions and dilations to remove any small blobs of noise from the thresholded image
	#cv2.imwrite('assets/eroded.jpg', erode)#saves the eroded image to the directory
	#cv2.imshow('window', erode)
	
	minMaxLoc = cv2.minMaxLoc(erode)#minMaxloc finds the darkest and brightest part of the image (varibale) 'erode' 	
	
	yRegion = str(minMaxLoc)[25:29]#just gets the Y axis 	
	final = yRegion.replace(')', '')#replacing the bracket that is returned with tripple digit coords
	
	#print(f'the size of the image is: {shape}')	
	print(f'the brightest part of the image, darkest part of the image, x coord, y coord{minMaxLoc}')	
	print(f'{imageName} {final}')

	if final == '':
		break
	else:	
		final = int(final)
		selector = getCharacter(final)
		final_string+=characters[selector]
		

print("\n")
print(f"the punchcard had {index} columns punched")
#print(f'The final string is: {final_string}')

splited_str = []
n  = 9
# looping through  example_str from 0 to length
# of example_str in a step size of 5
for index in range(0, len(final_string), n):
    # slicing at iteration stops and storing it in splited_str
    splited_str.append(final_string[index : index + n]) 
print(splited_str)
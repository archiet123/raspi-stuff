import re
import numpy as np
import cv2
#from picamera import PiCamera
from PIL import Image, ImageChops
import PIL
import matplotlib.pyplot as plt
import cv2
import math

img = cv2.imread(f'assets/all80.jpg')#reading init pic
#cv2.imshow('window', img)
#cv2.waitKey()


def autoCoords():
	leftY = 468
	rightY = 480
	
	for index in range(0,80):
		
		column0 = img[260:650, leftY:rightY]
		plt.imsave(f"assets/testing{index}.jpg", column0)		

		# if index >= 40: 
		# 	leftY +=12
		# 	rightY +=12
		# else:
		leftY +=13
		rightY +=13

		if index == 0:
			continue
		if index % 9 == 0:
			print(index, "removing 4")
			leftY +=-4
			rightY +=-4

		# if index % 30 == 0:
		# 	print(index, "removing 8")
		# 	leftY +=-8
		# 	rightY +=-8

autoCoords()

def getCharacter(final):	
	selector = 0
	if final > 320:
		selector = 9
	elif final > 285:
		selector = 8
	elif final > 265:
		selector = 7
	elif final > 230:
		selector = 6
	elif final > 190:
		selector = 5
	elif final > 165:
		selector = 4
	elif final > 125:
		selector = 3
	elif final > 95:
		selector = 2
	elif final > 55:
		selector = 1
	elif final > 20:
		selector = 0
	return selector

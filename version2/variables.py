import re
import numpy as np
import cv2
#from picamera import PiCamera
from PIL import Image, ImageChops
import PIL
import matplotlib.pyplot as plt
import cv2

def getCharacter(final):
	if final > 20 and final < 50:
		selector = 0
		return selector
	elif final > 55 and final < 90:
		selector = 1
		return selector
	elif final > 95 and final < 120:
		selector = 2
		return selector
	elif final > 125 and final < 140:
		selector = 3
		return selector
	elif final > 160 and final < 180:
		selector = 4
		return selector
	elif final > 190 and final < 210:
		selector = 5
		return selector
	elif final > 230 and final < 250:
		selector = 6
		return selector
	elif final > 265 and final < 280:
		selector = 7
		return selector
	elif final > 295 and final < 320:
		selector = 8
		return selector
	elif final > 330 and final < 350:
		selector = 9
		return selector

img = cv2.imread(f'assets/card.jpg')#reading init pic



column0 = img[260:650, 470:480]#column0 bounds  
plt.imsave("assets/testing0.jpg", column0)

column1 = img[260:650, 483:493]#column1 bounds
plt.imsave("assets/testing1.jpg", column1)

column2 = img[260:650, 496:506]#column2 bounds
plt.imsave("assets/testing2.jpg", column2)

column3 = img[260:650, 509:519]
plt.imsave("assets/testing3.jpg", column3)

column4 = img[260:650, 522:532]
plt.imsave("assets/testing4.jpg", column4)

column5 = img[260:650, 533:543]
plt.imsave("assets/testing5.jpg", column5)

column6 = img[260:650, 545:555]
plt.imsave("assets/testing6.jpg", column6)

column7 = img[260:650, 558: 568]
plt.imsave("assets/testing7.jpg", column7)

column8 = img[260:650, 571: 581]
plt.imsave("assets/testing8.jpg", column8)

column9 = img[260:650, 584: 594]
plt.imsave("assets/testing9.jpg", column9)

column10 = img[260:650, 596:606]
plt.imsave("assets/testing10.jpg", column10)


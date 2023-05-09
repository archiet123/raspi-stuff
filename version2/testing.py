import numpy as np
import cv2
import matplotlib.pyplot as plt
import cv2
import os
import argparse



def getCharacter(final):	
	selector = 0
	if final < 320:
		selector = 9
	elif final < 285:
		selector = 8
	elif final < 265:
		selector = 7
	elif final < 230:
		selector = 6
	elif final < 190:
		selector = 5
	elif final < 165:
		selector = 4
	elif final < 125:
		selector = 3
	elif final < 95:
		selector = 2
	elif final < 55:
		selector = 1
	elif final < 20:
		selector = 0
	return selector
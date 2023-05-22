import numpy as np
import cv2
import matplotlib.pyplot as plt
# from matplotlib import imread
import cv2
import os
import argparse
import PIL

#links
#https://pyimagesearch.com/2016/10/31/detecting-multiple-bright-spots-in-an-image-with-python-and-opencv/
#https://stackoverflow.com/questions/51846933/finding-bright-spots-in-a-image-using-opencv
#https://www.programcreek.com/python/example/88833/skimage.measure.label


# from imutils import contours
# from skimage import measure
# Image = ('testing.jpg') # save images as newimage{column index} 
# read = cv2.imread(Image)#this will need to loop through all images that need to be read

image = cv2.imread("eroded.jpg")
res = np.argwhere((image > 250).any(-1))

#res = np.argwhere(image[:,:,0] > 250)
# res = np.where(image > 200)

print(str(res))
print(len(res))


# np.argwhere(Image[255,255,255] > threshold)
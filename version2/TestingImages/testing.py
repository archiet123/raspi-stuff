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
CoordList = []
Result = []

image = cv2.imread("eroded.jpg")
res = np.argwhere((image > 250).any(-1))

for i in res:
    CoordList.append(i)#appending all value to list
    if len(CoordList) == 1:#if length of list is 1 then skip iteration
        continue
    else:
        PenultimateValue = CoordList[-2:][0]
        LastValue = CoordList[-1:][0]#getting last value in list
        CoordDiff = PenultimateValue - LastValue#only should append to list if the difference of last
        if CoordDiff < 30:
            continue
        else:
            Result.append(CoordDiff)
        print(LastValue)
        

# res = np.argwhere(image[:,:,0] > 250) not sure about this one

print(str(Result))

# print(str(res))




import cv2
from picamera import PiCamera
from time import sleep
from PIL import Image, ImageChops
import PIL
import matplotlib.pyplot as plt
import numpy 
import cv2
camera = PiCamera()
camera.rotation = -180

#first_image = "bob"
#camera.capture(f'/home/pi/Documents/pi programming/reading jpg/image test/testing new frame/final_program/characters/{first_image}.jpg')
#img = cv2.imread(f'/home/pi/Documents/pi programming/reading jpg/image test/testing new frame/final_program/characters/{first_image}.jpg', 0)



#column0 = img[345:670, 270:280]#column0 bounds
#zero = plt.imsave(f'/home/pi/Documents/pi programming/reading jpg/image test/testing new frame/final_program/characters/{first_image}.jpg', column0, cmap ='gray')


#column0 = img[345:650, 270:282]#column0 bounds
#zero = cv2.imshow('Grayscale',column0)
#column1 = img[345:670, 270:280]#column0 bounds
#one = plt.imsave(f'/home/pi/Documents/pi programming/reading jpg/image test/testing new frame/final_program/characters/{first_image}.jpg', column1, cmap ='gray')


img1 = cv2.imread('ghfhdfg.jpg', 0)
img2 = cv2.imread('gfhg.jpg', 0)

res = cv2.absdiff(img1, img2)

#res = res.astype(np.uint8)

percentage = (numpy.count_nonzero(res) * 100) / res.size

print (percentage)

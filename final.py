from picamera import PiCamera
from time import sleep
from PIL import Image, ImageChops
import PIL
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
camera = PiCamera()
camera.rotation = -180

#cv2.imwrite('New_Img.jpg', Old_Img)

global first_image
first_image = "og"
camera.capture(f'/home/pi/Documents/pi programming/reading jpg/image test/testing new frame/final_program/{first_image}.jpg')
global path
path = f'/home/pi/Documents/pi programming/reading jpg/image test/testing new frame/final_program/'
img = cv2.imread(f'{first_image}.jpg', 0)

#cropped = img[350:650,250:960]#bounds of whole punchcard
#New_Img = plt.imsave('Grayscale', cropped)

#definition of each column
#column0 = img[345:670, 270:280]#column0 bounds
#zero = plt.imsave("newimage0.jpg", column0, cmap ='gray')

#deletes old images
def del_old_imgs():
    for columnsIdx in range(0,10):
        if os.path.exists('/home/pi/Documents/pi programming/reading jpg/image test/testing new frame/final_program/' + f'newimage{columnsIdx}.jpg') is False:
            return True
        else:
            os.remove(path + f'newimage{columnsIdx}.jpg')

            
del_old_imgs()

'''
column0 = img[240:658,467:482]#column0 bounds
zero = cv2.imshow('Grayscale',column0)
zero = plt.imsave("column0.jpg", column0, cmap ='gray')

column1 = img[240:658,480:495]#column1 bounds
one = cv2.imshow('Grayscale',column1)
one = plt.imsave("column1.jpg", column1, cmap ='gray')
 
column2 = img[240:658,494:509]#column2 bounds
two = cv2.imshow('Grayscale',column2)
two = plt.imsave("column2.jpg", column2, cmap ='gray')
'''


column0 = img[240:658,467:482]#column0 bounds
#zero = cv2.imshow('Grayscale',column0)
zero = plt.imsave("newimage0.jpg", column0, cmap ='gray')

column1 = img[240:658,480:495]#column1 bounds
#one = cv2.imshow('Grayscale',column1)
one = plt.imsave("newimage1.jpg", column1, cmap ='gray')
 
column2 = img[240:658,494:509]#column2 bounds
#two = cv2.imshow('Grayscale',column2)
two = plt.imsave("newimage2.jpg", column2, cmap ='gray')


'''column3 = img[345:650,297:307]#column3 bounds
three = cv2.imshow('Grayscale',column3)
#three = plt.imsave("newimage3.jpg", column3, cmap ='gray')


column4 = img[345:650,305:315]#column4 bounds 
four = cv2.imshow('Grayscale',column4)
#four = plt.imsave("newimage4.jpg", column4, cmap ='gray')


column5 = img[345:650,313:323]#column 5 bounds tbc
five = cv2.imshow('Grayscale',column5)
#five = plt.imsave("newimage5.jpg", column5, cmap ='gray')


column6 = img[345:650,321:331]#column 6 bounds tbc
six = cv2.imshow('Grayscale',column6)
#six = plt.imsave("newimage6.jpg", column6, cmap ='gray')


column7 = img[345:650,329:339]#column 7 tbc (very poor card)
seven = cv2.imshow('Grayscale',column7)
#seven = plt.imsave("newimage7.jpg", column7, cmap ='gray')


column8 = img[345:650,337:347]#column 8 bounds
eight = cv2.imshow('Grayscale',column8)
#eight = plt.imsave("newimage8.jpg", column8, cmap ='gray')


column9 = img[350:670,345:355]#column 9 bounds
nine = cv2.imshow('Grayscale',column9)
#nine = plt.imsave("newimage9.jpg", column9, cmap ='gray')

'''

cv2.waitKey()
cv2.destroyAllWindows()

#column10 = img[350:650,348:357]
#a = cv2.imshow('Grayscale',column10)

#one = plt.imsave("column1.jpg", column1, cmap='gray')  
        
#loop, compare: zero, and set image. if fasle
#compare: one, and set image. if false

#b_column = img[350:650, 270:285]
#b = cv2.imshow('Grayscale', b_column)




global number
charIndex = 0
characters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
final_string = ""
#for loop loops 6 times in testing, will have to be 26 times in practice (PER CHARACTER). 26*86 loops maximum
#(26 per character in alphabet,   86 or x amount for however many holes have been punched )

for columnsIdx in range (0,3):#(0,85):
    for charIndex in range (0,3):#(0,35):
        ogColumnName = (f'newimage{columnsIdx}') # save images as newimage{column index}
        ogImage = cv2.imread(f'{ogColumnName}.jpg', 0)

        charImage = cv2.imread(f'column{charIndex}.jpg', 0)
        res = cv2.absdiff(charImage, ogImage)
        percent = (np.count_nonzero(res) * 100) / res.size
        #print (f'{percent}%')

        if percent > 95:
            print(f'There are no differences in the image: column{charIndex} & {ogColumnName}')
            final_string+=characters[charIndex]
            
    
        else:
            print(f'There are differences in the image: column{charIndex} & {ogColumnName}')
            print(f'{percent}')


print(f"The final string is: {final_string}")







# punch card has 86 columns
# 36 characters (0-9 a-z)
# column{index} contains an image which represents the character as it would be in the punch card column
# take image on pi
# save image

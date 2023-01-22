from picamera import PiCamera
from time import sleep
from PIL import Image, ImageChops
import PIL
import matplotlib.pyplot as plt
import cv2
camera = PiCamera()
camera.rotation = -180

#cv2.imwrite('New_Img.jpg', Old_Img)

global first_image
first_image = input("What do you want the first image to be saved as?")
camera.capture(f'/home/pi/Documents/pi programming/reading jpg/image test/testing new frame/final_program/{first_image}.jpg')
path = f'/home/pi/Documents/pi programming/reading jpg/image test/testing new frame/final_program/{first_image}.jpg'
img = cv2.imread(f'{first_image}.jpg', 0)

cropped = img[350:650,250:960]#bounds of whole punchcard
New_Img = plt.imsave('Grayscale', cropped)

#definition of each column
'''column0 = img[345:650, 262:272]#column0 bounds
zero = plt.imsave("column0.jpg", column0, cmap ='gray')

column1 = img[345:650,271:281]#column1 bounds
one = cv2.imshow('Grayscale',column1)
 
column2 = img[345:650,280:290]#column2 bounds
two = cv2.imshow('Grayscale',column2)

column3 = img[345:650,289:298]#column3 bounds
three = cv2.imshow('Grayscale',column3)

column4 = img[345:650,297:304]#column4 bounds (needs to go to 305 but is a bad card)
four = cv2.imshow('Grayscale',column4)

column5 = img[345:650,307:314]#column 5 bounds tbc
five = cv2.imshow('Grayscale',column5)

column6 = img[345:650,316:323]#column 6 bounds tbc
six = cv2.imshow('Grayscale',column6)

column7 = img[345:650,323:330]#column 7 tbc (very poor card)
seven = cv2.imshow('Grayscale',column7)

column8 = img[345:650,330:339]#column 8 bounds
eight = cv2.imshow('Grayscale',column8)

column9 = img[345:650,339:348]#column 9 bounds
nine = cv2.imshow('Grayscale',column9)


'''
column10 = img[345:650,348:357]
a = cv2.imshow('Grayscale',column10)

#list thing updated, need to print punch card with spaces inbetween top rows


#one = plt.imsave("column1.jpg", column1, cmap='gray')



'''global count
count = 0

#loop that checks if the desired punchcard to be read's columns match the defined columns
for i in range(2):
    column = (f"column{count}")
    print (column)
    
    img1 = Image.open(f"{column}.jpg")
    img2 = Image.open(f"actual_pc.jpg")
    
    
    diff = ImageChops.difference(img1,img2)
    
    if diff.getbbox():
        print("There are differences")
        
    else:
        print("There are no differences")
    count = count + 1
    actual_pc = img[350:650,270:280]#column0 bounds
actual = plt.imsave("actual_pc.jpg", actual_pc, cmap='gray')
    
    '''
    
#loop, compare: zero, and set image. if fasle
#compare: one, and set image. if false

#b_column = img[350:650, 270:285]
#b = cv2.imshow('Grayscale', b_column)

cv2.waitKey()
cv2.destroyAllWindows()
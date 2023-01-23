import numpy
import cv2

#--------------the loop-----------------#
def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

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
        percent, diff = mse(img1, img2)
        print("Image matching Error between the two images:",error)
        

        if percent > 0.1:#this needs to be changed to a better treashold, dont know best percentage match without testing.
            print(f'There are no differences in the image: column{charIndex} & {ogColumnName}')
            final_string+=characters[charIndex]
            
    
        else:
            print(f'There are differences in the image: column{charIndex} & {ogColumnName}')
            print(f'{percent}')


print(f"The final string is: {final_string}")


#---------new code for loop---------------#
#this code needs to be inside the main loop to compare images
# # load the input images

#img1 = cv2.imread(read original image) the program will take ONE initial image.

#column0 is then set as the variable that will look for the first character (a) on the punchcard
#this needs to be repeated for every column where the coordinates are defined.

camera.capture(f'/home/pi/Documents/pi programming/reading jpg/image test/testing new frame/final_program/{inital_image}.jpg')

column0 = inital_image[240:658,467:482]
zero = plt.imsave("newimage0.jpg", column0)

img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image1_edit.jpg')

# convert the images to grayscale


# define the function to compute MSE between two images
def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

error, diff = mse(img1, img2)
print("Image matching Error between the two images:",error)

cv2.imshow("difference", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
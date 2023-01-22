import numpy
import cv2

#--------------the loop-----------------#

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


#---------new code for loop---------------#
#this code needs to be inside the main loop to compare images
# # load the input images
img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image1_edit.jpg')

# convert the images to grayscale
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

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
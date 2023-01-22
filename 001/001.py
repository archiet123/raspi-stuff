#this script will be hard coding correct values to test if the loop made will return the correct characters if ture.

#this would normally be the code for pixel coordinates in the image.

#column0 = img[240:658,467:482]#column0 bounds
#zero = cv2.imshow('Grayscale',column0)
#zero = plt.imsave("newimage0.jpg", column0, cmap ='gray')

column0 = True



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

for columnsIdx in range (0,3):#(0,85): numbers of columns on a punchcard
    for charIndex in range (0,3):#(0,35): numbers of characters that are defined
        ogColumnName = (f'newimage{columnsIdx}') # taking new image and save image as newimage{column index}
        ogImage = cv2.imread(f'{ogColumnName}.jpg', 0) #cv2 reads image and saves as loop index

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
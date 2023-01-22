from picamera import PiCamera
from time import sleep
from PIL import Image, ImageChops
import time

#Measures the time of the program to execute
startTime = time.time()


#{this section is the character in the alphabet that is being identified, change the "yeah" file name to the saved
#letter.
global correct_img
correct_img = Image.open("image1.jpg")
#}




#import compare
global number
number = 0
global punchcardnumber
punchcardnumber = 0
global loop_counter
loop_counter = 0
#for loop loops 6 times in testing, will have to be 26 times in practice (PER CHARACTER). 26*86 loops maximum
#(26 per character in alphabet,   86 or x amount for however many holes have been punched )
for i in range (0,85  ):
    number = 0
    loop_counter = loop_counter + 1
    print (loop_counter)
    for i in range(0,26):
        number = number + 1
        name = (f"image{number}")
        img = Image.open(f"{name}.jpg")
        #img.show()
        diff = ImageChops.difference(img,correct_img)
        if diff.getbbox():
            print(f"There are differences in the image: {name} ")        
        else:
            print(f"There are no differences in the image: {name}")


#Measures time from beginning to the end
ExecutionTime = round(time.time() - startTime)
ExecutionTimeInMinutes = round(ExecutionTime / 60)
print(f"Execution time in seconds: {ExecutionTime} seconds")
print(f"Execution time in minutes: {ExecutionTimeInMinutes} minutes")

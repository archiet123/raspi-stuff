from picamera import PiCamera
from time import sleep
from PIL import Image, ImageChops


global correct_img
correct_img = Image.open("yeah3.jpg")

#import compare
global number
number = 0
for i in range(0,6):
    number = number + 1
    name = (f"yeah{number}")
    img = Image.open(f"{name}.jpg")
    #img.show()
    diff = ImageChops.difference(img,correct_img)
    if diff.getbbox():
        sleep(3)
        print(f"There are differences in the image: {name} ")        
    else:
        print(f"There are no differences in the image: {name}")
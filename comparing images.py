from picamera import PiCamera
from time import sleep
from PIL import Image, ImageChops
camera = PiCamera()
#camera.rotation = -180

def pic_one():
    global first_image
    first_image = input("What do you want the first image to be saved as?")
    camera.start_preview()
    sleep(3)
    camera.capture(f'/home/pi/Documents/pi programming/reading jpg/{first_image}.jpg')
    camera.stop_preview()
    
def pic_two():
    second = False
    while second == False:
        global second_image
        second_image = input("What do you want the second image to be saved as?")
        if second_image == first_image:
            print("You cannot pick the same name as the first image")
            second = False
        else:
            camera.start_preview()
            sleep(3)
            camera.capture(f'/home/pi/Documents/pi programming/reading jpg/{second_image}.jpg')
            camera.stop_preview()
            second = True
            
def compare_images():
    img1 = Image.open(f"{first_image}.jpg")
    img2 = Image.open(f"{second_image}.jpg")
    
    diff = ImageChops.difference(img1,img2)
    
    if diff.getbbox():
        diff.show()
        sleep(3)
        print("The differences in the images are highlighted")
        
    else:
        print("Not working")
        
pic_one()
pic_two()
compare_images()

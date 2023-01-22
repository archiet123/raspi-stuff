from picamera import PiCamera
from time import sleep
from PIL import Image, ImageChops
camera = PiCamera()
#camera.rotation = -180

def create_image():
    global image
    image = input("What do you want the image to be saved as?")
    camera.start_preview()
    sleep(3)
    camera.capture(f'/home/pi/Documents/pi programming/reading jpg/{image}.jpg')
    camera.stop_preview()
    
create_image()
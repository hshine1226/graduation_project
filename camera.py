from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()

camera.start_preview()
sleep(2)
now = time.localtime()
camera.capture('/home/pi/'+now+'image.jpg')
camera.stop_preview()

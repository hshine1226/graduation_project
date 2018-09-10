import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()

GPIO.setmode(GPIO.BCM)
PIR_PIN1 = 3 #FC-51
 
GPIO.setup(PIR_PIN1, GPIO.IN)
 
try:     
    while True:
      if (!GPIO.input(PIR_PIN1)):    
        print "FC-51 Detect"
        camera.start_preview()
        sleep(2)
        now = time.localtime()
        camera.capture('/home/pi/'+now+'image.jpg')
        camera.stop_preview()
        time.sleep(5)
 
except KeyboardInterrupt:
    print “ Quit”
    GPIO.cleanup()

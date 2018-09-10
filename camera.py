import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()

GPIO.setmode(GPIO.BCM)
PIR_PIN1 = 7 #인체감지센서1
PIR_PIN2 = 8 #인체감지센서2
 
GPIO.setup(PIR_PIN, GPIO.IN)
 
try:     
    while True:
        if GPIO.input(PIR_PIN1):
            print "Motion Sensor1 Detect"
            if GPIO.input(PIR_PIN2):
              print "Motion Sensor2 Detect"
              camera.start_preview()
              sleep(2)
              now = time.localtime()
              camera.capture('/home/pi/'+now+'image.jpg')
              camera.stop_preview()
        time.sleep(0.05)
 
except KeyboardInterrupt:
    print “ Quit”
    GPIO.cleanup()

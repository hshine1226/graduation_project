import RPi.GPIO as GPIO
from picamera import PiCamera
import time
from time import sleep
import datetime

camera = PiCamera()

GPIO.setmode(GPIO.BCM)
PIR_PIN1 = 7 #humansensor1
PIR_PIN2 = 8 #humansensor2
 
GPIO.setup(PIR_PIN1, GPIO.IN)
GPIO.setup(PIR_PIN2, GPIO.IN)
 
try:     
    while True:
        if GPIO.input(PIR_PIN1):
            print "Motion Sensor1 Detect"            
            
            if GPIO.input(PIR_PIN1):
                camera.start_preview()
                now = datetime.datetime.now()
                nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
                camera.capture('/home/pi/'+str(nowDatetime)+'.jpg')
                camera.stop_preview()
        time.sleep(2)
 
except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()

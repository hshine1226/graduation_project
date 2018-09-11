#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from picamera import PiCamera
import time
from time import sleep
import datetime

camera = PiCamera()

GPIO.setmode(GPIO.BCM)
PIR_PIN1 = 3 #FC-51
 
GPIO.setup(PIR_PIN1, GPIO.IN)
 
try:     
    while True:
        if (GPIO.input(PIR_PIN1) == 0):
            print "FC-51 Detect"
            camera.start_preview()
            sleep(2)
            now = datetime.datetime.now()
            nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
            camera.capture('/home/pi/'+nowDatetime+'.jpg')
            camera.stop_preview()
            time.sleep(5)
 
except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()

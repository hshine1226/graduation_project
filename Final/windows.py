#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import datetime
import os

GPIO.setmode(GPIO.BCM)
PIR_PIN1 = 12 #Motion Detect Sensor1
PIR_PIN2 = 8 #Motion Detect Sensor2
 
GPIO.setup(PIR_PIN1, GPIO.IN)
GPIO.setup(PIR_PIN2, GPIO.IN)

cnt = 0
try:
	while True:
		if GPIO.input(PIR_PIN1):
			print "Motion Sensor1 Detect"			
			cnt = 1
			sleep(1)
		if cnt == 1:
			if GPIO.input(PIR_PIN2):
				print "Motion Sensor2 Detect"
				print "Help~~"
				cnt = 0
				sleep(1)
                                os.system('gammu sendsms TEXT 01073205117 -unicode -textutf8 "[SOS]\n창문으로 누군가 들어왔습니다.\n주소 : 한국기술교육대학교\n2공학관 119호"')
 
except KeyboardInterrupt:
	print "Quit"
	GPIO.cleanup()

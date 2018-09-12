#-*- coding: utf-8 -*-
# test BLE Scanning software
# jcs 6/8/2014
# doorsensor

# hciconfig
#sudo hciconfig hci0 up!!!!!!

import blescan
import sys
import time
import os
import bluetooth._bluetooth as bluez
import RPi.GPIO as GPIO
from picamera import PiCamera
import datetime

dev_id = 0

camera = PiCamera()

GPIO.setmode(GPIO.BCM)
PIR_PIN1 = 3 #FC-51
 
GPIO.setup(PIR_PIN1, GPIO.IN)

try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)
door_sensor = "ac:9a:22:9b:02:61"

while True:
	
	returnedList = blescan.parse_events(sock, 1)
	#print "----------"
	for beacon in returnedList:
		#print beacon
		if str(beacon) == door_sensor:
                    print("door sensor dectection")
                    os.system('gammu sendsms TEXT 01073205117 -unicode -text "[SOS]\n도어락이 파손되었습니다.\n주소 : 한국기술교육대학교\n2공학관 119호"')
                    time.sleep(1)
                    
                if (GPIO.input(PIR_PIN1) == 0):
                    print "FC-51 Detect"
                    camera.start_preview()
                    time.sleep(2)
                    now = datetime.datetime.now()
                    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
                    camera.capture('/home/pi/Documents/Final/photo/'+nowDatetime+'.jpg')
                    camera.stop_preview()
                    time.sleep(5)

#-*- coding: utf-8 -*-
# test BLE Scanning software
# jcs 6/8/2014
# doorsensor

# hciconfig
#sudo hciconfig hci0 up!!!!!!

import pyrebase
import blescan
import sys
import time
import os
import bluetooth._bluetooth as bluez
import RPi.GPIO as GPIO
from picamera import PiCamera
import datetime
from subprocess import call  #prompt


config={         #firebase config
    "apiKey": "AIzaSyBS6YDrKmtt7n0e32iovczfhIFpNHAKW8I", #webkey
    "authDomain": "howon-1547f.firebaseapp.com",   #project id
    "databaseURL": "https://howon-1547f.firebaseio.com/",  #databaseurl
    "storageBucket": "howon-1547f.appspot.com"  #storage
    }

firebase = pyrebase.initialize_app(config)

dev_id = 0

camera = PiCamera()
camera.rotation = 180

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
                    os.system('gammu sendsms TEXT 01073205117 -unicode -textutf8 "[SOS]\n도어락이 파손되었습니다.\n주소 : 한국기술교육대학교\n2공학관 119호"')
                    #time.sleep(1)
                
                    camera.start_preview()
                    #time.sleep(1)
                    nowDatetime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                    basename='video'
                    filename="_".join([basename, nowDatetime])
                    
                    
                    camera.start_recording('/home/pi/Documents/Final/video/'+filename+'.h264')
                    time.sleep(5)
                    camera.stop_recording()
                    camera.stop_preview()
                    call('MP4Box -add /home/pi/Documents/Final/video/'+filename+'.h264 /home/pi/Documents/Final/video/'+filename+'.mpeg', shell=True)
                    uploadfile = '/home/pi/Documents/Final/video/'+filename+'.mpeg'  #upload file name
                    s = os.path.splitext(uploadfile)[1]  #upload file type
                    fileN = nowDatetime + s
                    
                    #upload files to firebase
                    storage = firebase.storage()

                    file_upload = storage.child("videos/"+fileN).put(uploadfile)
                    fileUrl = storage.child("videos/"+fileN).get_url(file_upload['downloadTokens']) 
                    print("Storage upload Complete!!!!\nurl : " + fileUrl)
                    
                    db = firebase.database()
                    result = db.child("files").push(filename+".mpeg,"+fileUrl)
                    print("DB upload Complete!!!!")
                    
                if (GPIO.input(PIR_PIN1) == 0):
                    print "FC-51 Detect"
                    camera.start_preview()
                    #time.sleep(1)
                    now = datetime.datetime.now()
                    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
                    basename='photo'
                    filename="_".join([basename, nowDatetime])
                    
                    camera.capture('/home/pi/Documents/Final/photo/'+filename+'.png')
                    camera.stop_preview()
                    uploadfile = '/home/pi/Documents/Final/photo/'+filename+'.png'  #upload file name
                    s = os.path.splitext(uploadfile)[1]  #upload file type
                    fileN = nowDatetime + s
                    
                    #upload files to firebase
                    storage = firebase.storage()

                    file_upload = storage.child("photo/"+fileN).put(uploadfile)
                    fileUrl = storage.child("photo/"+fileN).get_url(file_upload['downloadTokens']) 
                    print("Storage upload Complete!!!!\nurl : " + fileUrl)
                    
                    db = firebase.database()
                    result = db.child("photo").push(filename+".png,"+fileUrl)
                    print("DB upload Complete!!!!")
                    
                    #time.sleep(1)
                    

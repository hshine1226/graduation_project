#-*- coding: utf-8 -*-
# test BLE Scanning software
# jcs 6/8/2014
# doorsensor

# hciconfig
#sudo hciconfig hci0 up!!!!!!

import blescan
import sys
import time

import bluetooth._bluetooth as bluez

dev_id = 0
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
                    time.sleep(1)
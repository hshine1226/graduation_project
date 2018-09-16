import socket
import blescan
import sys
import time
import datetime
import bluetooth._bluetooth as bluez

dev_id = 0
isOpen = 1
#msg = "s"

HOST=""
PORT=8012
BUFSIZE=1024
ADDR=(HOST, PORT)
tcpSersock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSersock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpSersock.bind(ADDR)
#tcpSersock.listen(5)

print 'waiting for connection...'
#tcpCliSock,addr = tcpSersock.accept()   # wait till get connected
print 'connected'

try:
	bSock = bluez.hci_open_dev(dev_id)
	tcpSersock.listen(5)
        tcpCliSock,addr = tcpSersock.accept()   # wait till get connected
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(bSock)
blescan.hci_enable_le_scan(bSock)
door_sensor2 = "ac:9a:22:9b:02:32"

while True:
    '''msg = tcpCliSock.recv(4)
    if str(msg) == "f":
        print 'waiting for connection...'
        tcpCliSock,addr = tcpSersock.accept()   # wait till get connected
        msg = tcpCliSock.recv(1)
        print 'connected'''

    #else :
    #print "1"
    returnedList = blescan.parse_events(bSock, 1)

    #print returnedList
    #print "2"
    #print "----------"
    for beacon in returnedList:
        #print beacon
        if str(beacon) == door_sensor2:
            if(isOpen == 1):
                print("door Opened")
                #if(tcpCliSock.recv(BUFSIZE) == "signal"):
                tcpCliSock.send("o\n")
                #msg = tcpCliSock.recv(1)
                #print(tcpCliSock.recv(BUFSIZE))
                isOpen = -isOpen
                time.sleep(0.7)
            else :
                print("door Closed")
                #if(tcpCliSock.recv(BUFSIZE) == "signal"):
                tcpCliSock.send("c\n")
                #print(tcpCliSock.recv(BUFSIZE))
                isOpen = -isOpen
                time.sleep(0.7)
    
#tcpSersock.close()
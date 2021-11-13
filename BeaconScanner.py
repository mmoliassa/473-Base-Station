#This is a working prototype. DO NOT USE IT IN LIVE PROJECTS

import ScanUtility
import PublishData
import bluetooth._bluetooth as bluez

#Set bluetooth device. Default 0.
dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print ("\n *** Looking for BLE Beacons ***\n")
	print ("\n *** CTRL-C to Cancel ***\n")
except:
	print ("Error accessing bluetooth")

ScanUtility.hci_enable_le_scan(sock)
#Scans for iBeacons

mqtt_connection = PublishData.initialize_resources()

try:
	while True:
		returnedList = ScanUtility.parse_events(sock, 10)
		if returnedList is None:
			continue
		print(returnedList)
		PublishData.publishMessage(mqtt_connection, returnedList)
		for item in returnedList:
			print(item)
			print("")
except KeyboardInterrupt:
	PublishData.disconnect(mqtt_connection)
	pass

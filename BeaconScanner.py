#This is a working prototype. DO NOT USE IT IN LIVE PROJECTS
import sys
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
while True:
	try:
		#print("test1")
		mqtt_connection = PublishData.initialize_resources()
		#print("test2")
		break
	except KeyboardInterrupt:
		sys.exit()
	except:
		#print("testing")
		continue

try:
	while True:
		returnedList = ScanUtility.parse_events(sock, 10)
		if returnedList is None:
			continue
		for item in returnedList:
			PublishData.publishMessage(mqtt_connection, item)
			print(item)
			print("")
except KeyboardInterrupt:
	PublishData.disconnect(mqtt_connection)
	pass
except:
	PublishData.disconnect(mqtt_connection)
	pass

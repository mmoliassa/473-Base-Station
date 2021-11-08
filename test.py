import PublishData
from datetime import datetime

uuid = '78e3b374-a079-4011-a999-62da95809bba'
majorVal = 12345
minorVal = 67890
device_id = '123456789'
occupied_data = 0
date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

testArray = [{"uuid": uuid, "major": majorVal, "minor": minorVal, "device_id": device_id, "occupied_data": occupied_data, "date_time": date_time}]

mqtt_connection = PublishData.initialize_resources()
PublishData.publishMessage(mqtt_connection, testArray)
PublishData.disconnect(mqtt_connection)


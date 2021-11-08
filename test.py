import PublishData

device_id = 12345

testArray = [{"device_id": device_id, "occupied_data": 0}]

mqtt_connection = PublishData.initialize_resources()
PublishData.publishMessage(mqtt_connection, testArray)
PublishData.disconnect(mqtt_connection)


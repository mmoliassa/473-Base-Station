
import boto3

import time

promptText = "Select an option\n 1. Register a device\n 2. Remove a device\n 3. Assign a device\n 4. Create a room\n"
db = boto3.resource('dynamodb', region_name="us-west-2")


def query_rooms():
    db = boto3.resource('dynamodb', region_name="us-west-2")
    tables = list(db.tables.all())
    #print(tables)
    return tables

def device_registration():
    roomNames = query_rooms()
    roomNameList = []
    for name in roomNames:
        roomNameList.append(name.name)
    #print('\n'.join(str(p) for p in roomNameList))
    room_name = input("Choose Room: \n " + '\n '.join(str(p) for p in roomNameList) + '\n\n')
    table = db.Table(room_name)
    device_id = input('Device ID?\n')
    device_name = input('Device Name?\n')

    table.put_item(
        Item={
            'device_id': device_id,
            'device_name': device_name,
            'occupied_data': 0,
            'timestamp': int(time.time())
        }
    )

while 1==1:
    inputStr = input(promptText)
    selection = int(inputStr)
    if selection not in [1,2,3,4]:
        continue
    if selection == 1:
        device_registration()
    elif selection == 2:
        print(2)
    elif selection == 3:
        print(3)
    elif selection == 4:
        print(4)
    break



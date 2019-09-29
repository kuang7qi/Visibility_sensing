import paho.mqtt.client as mqtt #import the client1
import time
import datetime
import numpy as np
import csv

ROWS = ['DATE', 'TIME', 'VISIBILITY']
with open("output.csv",'w') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerow(ROWS)
resultFile.close()
list_temp = []

def on_subscribe(client, userdata, mid, granted_qos):
    print('Subscribed')

def on_message(client, userdata, message):
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M")
    msg = str(message.payload.decode("utf-8"))
    with open("output.csv",'a') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerow([date, time, msg])
    resultFile.close()

#broker_address="192.168.1.184"
broker_address="test.mosquitto.org"
client = mqtt.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect('test.mosquitto.org')
client.subscribe('Visibility')
client.loop_forever()

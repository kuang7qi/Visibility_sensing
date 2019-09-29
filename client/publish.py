import paho.mqtt.client as mqtt

def message(visibility):
    #broker_address="192.168.1.184"
    broker_address="test.mosquitto.org" #use external broker

    client = mqtt.Client("krish")
    client.connect(broker_address)
    msg = (str)(visibility) + "%"
    client.publish("Visibility", msg)

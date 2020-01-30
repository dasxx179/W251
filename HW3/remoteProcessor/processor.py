import paho.mqtt.client as mqtt
import random

MQTT_HOST="169.61.184.60"
MQTT_PORT=1883
MQTT_TOPIC="facedetection"

def onConnect(client, userdata, flags, rc):
    print("Connected With Result Code " (rc))


def onMessage(client, userdata, msg):
    print("on message received")
    num = random.randint(1,10000)

    path = '/mnt/w251-bucket-sayan' + str(num) +'.png'
    imagefile = open(path, 'wb')
    imagefile.write(msg.payload)
    imagefile.close()


mqttclient = mqtt.Client()
mqttclient.onConnect = onConnect
mqttclient.onMessage = onMessage

mqttclient.connect(MQTT_HOST,MQTT_PORT,60)
mqttclient.subscribe(MQTT_TOPIC, qos=1)

mqttclient.loop_forever()  # Start networking daemon

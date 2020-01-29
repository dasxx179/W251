import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST="172.19.0.2"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="HW03"

def onConnectLocal(client, userdata, flags, rc):
    print("Connected to jetson!")

def onConnectCloud(client, userdata, flags, rc):
    print("Connected to cloud!")

def onMessage(client, userdata, msg):
    print("on message received!")
    cloudmqttclient.publish("detector",payload=msg.payload,qos=1,retain=False)

cloudmqttclient = mqtt.Client()
cloudmqttclient.connect("169.61.184.60",1883,60)
cloudmqttclient.onConnect = onConnectCloud

mqttclient = mqtt.Client()
mqttclient.onConnectLocal = onConnectLocal
mqttclient.onMessage = onMessage

mqttclient.connect(LOCAL_MQTT_HOST,LOCAL_MQTT_PORT,60)
mqttclient.subscribe(LOCAL_MQTT_TOPIC, qos = 1)

mqttclient.loop_forever()

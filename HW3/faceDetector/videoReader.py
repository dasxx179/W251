import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST="mosquitto"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="hw03"

def onConnect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc))) 

mqttclient=mqtt.Client()
mqttclient.onConnect = onConnect
mqttclient.connect(LOCAL_MQTT_HOST,LOCAL_MQTT_PORT,60)

face_cascade = cv.CascadeClassifier('./haarcascadeFiles/haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)

while(True):

    ret,frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        face = frame[y:y+h,x:x+w]
        print("face detected ",face.shape,face.dtype)
        rc,jpg = cv.imencode(".png",fce)
        msg = jpg.tobytes()
        mqttclient.publish(LOCAL_MQTT_TOPIC,payload=msg,qos=1,retain=False)
    
# When everything is done, release the capture
video_capture.release()
cv.destroyAllWindows()

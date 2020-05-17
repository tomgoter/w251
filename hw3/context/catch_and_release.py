import paho.mqtt.client as mqtt
import os 
import io
from PIL import Image

LOCAL_MQTT_HOST="mqtt_cloud"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="cloud_topic"

def readimage(path):
  count = os.stat(path).st_size / 2
  with open(path, "rb") as f:
    return bytearray(f.read())

def on_connect_local(client, userdata, flags, rc):
  client.subscribe(LOCAL_MQTT_TOPIC)
  print("connected to local broker with rc: " + str(rc))
counter = 1	

def on_message(client,userdata, msg):
  try:
    print(f"{counter} message received!")	
    #bytes = readimage(msg.payload)
    #image = Image.open(io.BytesIO(bytes))
    #image.save(f'/images/image{counter}', "PNG")
    #print("data stored")
    counter += 1
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()


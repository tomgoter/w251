import paho.mqtt.client as mqtt


LOCAL_MQTT_HOST="mosquitto"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="hw3_topic"
REMOTE_HOST="52.117.100.124"
REMOTE_MQTT_TOPIC = "cloud_topic"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)

def on_connect_remote(client, userdata, flags, rc):
        print("connected to remote broker with rc: " + str(rc))
        
def on_message(client,userdata, msg):
  try:
    print("message received!")	
    # if we wanted to re-publish this message, something like this should work
    msg = msg.payload
    remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
remote_mqttclient = mqtt.Client("cloud_client")
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
remote_mqttclient.on_connect = on_connect_remote
remote_mqttclient.connect(REMOTE_HOST, LOCAL_MQTT_PORT,60)
local_mqttclient.on_message = on_message


# go into a loop
local_mqttclient.loop_forever()

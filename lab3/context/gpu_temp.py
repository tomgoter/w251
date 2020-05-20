import os
import paho.mqtt.client as mqtt

client = mqtt.Client("gpuTemp")
client.connect('mosquitto',port=1883)

os.system("tegrastats --logfile stats.out &")
os.system('sleep 2')

while(True):
  with open('stats.out', 'r') as file_in:
    latest = file_in.readlines()[-1]
    msg = latest[latest.find('GPU@')+4:latest.find('BCPU')-1]
  client.publish('lab3_topic', payload = msg.encode('utf-8'))
  os.system("sleep 1")
  


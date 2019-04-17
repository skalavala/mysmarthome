import os
import time
import paho.mqtt.client as mqtt

MQTT_SERVER = "192.168.xxx.xxx"
MQTT_SERVER_PORT = 1883
MQTT_TOPIC = "/garage/motion"
MQTT_USERNAME = "xxx"
MQTT_PASSWORD = "xxx"

# Define event callbacks
def on_connect(mosq, obj, rc):
    print("Return Code On Connect: " + str(rc))

def on_log(mosq, obj, level, string):
    print(string)

mqttc = mqtt.Mosquitto()

# Assign event callbacks
mqttc.on_connect = on_connect

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Connect
mqttc.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttc.connect(MQTT_SERVER, MQTT_SERVER_PORT)

# publish the message
mqttc.publish(MQTT_TOPIC, 'on')
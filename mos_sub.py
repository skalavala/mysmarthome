import mosquitto
import os
import urlparse

# External module imports
import RPi.GPIO as GPIO
import time

led = 12
MQTT_SERVER = "x.x.x.xxx"
MQTT_SERVER_PORT = xxx
MQTT_TOPIC = "/home/tv/backlight"
MQTT_USERNAME = "mosquitto"
MQTT_PASSWORD = "xxx"

# Pin Setup:
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT)

# Define event callbacks
def on_connect(mosq, obj, rc):
    print("Return Code On Connect: " + str(rc))

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    if (str(msg.payload) == "on" or str(msg.payload) == "ON"):
        #os.system('python on.py')
        GPIO.output(led, GPIO.LOW)
        time.sleep(1)
    else:
        if (str(msg.payload) == "off" or str(msg.payload) == "OFF"):
            #os.system('python off.py')
            GPIO.output(led, GPIO.HIGH)
            time.sleep(1)
        else:
            if (str(msg.payload) == "FLICKER_TV_OFF"):
                for x in range(0, 3):
                    GPIO.output(led, GPIO.HIGH)
                    time.sleep(0.25)
                    GPIO.output(led, GPIO.LOW)
                    time.sleep(0.25)
            else:
                if (str(msg.payload) == "FLICKER"):
                    for x in range(0, 3):
                        GPIO.output(led, GPIO.LOW)
                        time.sleep(0.25)
                        GPIO.output(led, GPIO.HIGH)
                        time.sleep(0.25)
                    time.sleep(1.00)
                else:
                    print("Unknown command")


def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)

mqttc = mosquitto.Mosquitto()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Connect
mqttc.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttc.connect(MQTT_SERVER, MQTT_SERVER_PORT)

# Start subscribe, with QoS level 0
mqttc.subscribe(MQTT_TOPIC, 0)

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("MQTT Return Code: " + str(rc))

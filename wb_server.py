#!/usr/bin/python

import socket
import asyncore
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

MQTT_SERVER_HOST = "192.168.xxx.xxx"
MQTT_SERVER_PORT = 1883
MQTT_USERNAME = "username"
MQTT_PASSWORD = "letmein"
MQTT_TOPIC = "/wallbox/data"

UDP_SERVER_PORT = 7090
DEFAULT_RECV_BYTES = 2048

client = mqtt.Client("udp-server")
#client.tls_set('/home/pi/certs/ca-certificates.crt')
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.connect(MQTT_SERVER_HOST, MQTT_SERVER_PORT)
client.loop_start()

class AsyncoreServerUDP(asyncore.dispatcher):
    def __init__(self):
        asyncore.dispatcher.__init__(self)

        # Bind to port 7090 on all interfaces
        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bind(('', UDP_SERVER_PORT))

    # Even though UDP is connectionless this is called when it binds to a port
    def handle_connect(self):
        print("Server Started...")

    # This is called everytime there is something to read
    def handle_read(self):
        data, addr = self.recvfrom(DEFAULT_RECV_BYTES)
        client.publish(MQTT_TOPIC, data, retain=False)
        print(str(addr) + " >> " + data)


    # This is called all the time and causes errors if you leave it out.
    def handle_write(self):
        pass

AsyncoreServerUDP()
asyncore.loop()

print("continue")

---
layout: page
title: DIY Camera with Raspberry PI & WebCam
description: The article below explains how you can use USB based camera and integrate with Home Assistant
---

# USB Camera /Using Webcam in Home Assistant 

This article explains how you can connect a USB based camera module to your Raspberry Pi, and bring in motion sensing capabilities/real-time streaming into your home automation system. The software used to interact with USB camera is `motion`. The `motion` program has so many features - including saving images when there is motion detected, run an external program indicating the same, create video clips of all recordings (by stitching all the images together), make time-lapse pictures, and also has a built-in web server for easier access to the camera via a web url...and more! There are so many advanced features that are available, unfortunately this article covers only some of it.

The design goes something like the following picture. The camera is connected to a Raspberry Pi using USB interace, and the Raspberry Pi will be running `motion` program. The program is run as `daemon`, so that when Raspberry Pi boots, the program starts automatically. The `motion` program will be constantly streaming the video (via Web URL) and whenever the program detects significant movement (difference between frames), it not only saves the images, but also calls an external python program - which in turn drops a message into MQTT signaling that the motion has been detected. The home automation system (Home Assistant) allows for easy integration with MQTT, and has the capability to create automatic `binary_sensor`s and automations. In this case, MQTT makes it easy to integrate between `motion` and `Home Assistant`.

![Camera Setup]({{site.url}}/images/camera-1.jpg "Camera Setup")

Now that you know how this will all come together, it is time to install and configure basic Raspberry Pi stuff. If you are unfamiliar with setting up Raspberry Pi, you can find it online at [Raspberry Pi](https://www.raspberrypi.org)'s web site. After installing Raspbian Operating System on your Raspberry Pi, connect USB camera to Raspberry Pi and run the following command. 

```
lsusb
```

The above command shows you a list of USB devices connected to your Raspberry Pi. If you see the camera there, you are good to go. If you don't your camera may not be supported.

Now that you know the camera is recognized by your Raspberry Pi, it is timeto install software. The sofware that is commonly used is called `Motion`. To install, run the command.

```
sudo apt-get install motion
```

After the installation, you need make a few modifications to the settings, and the configuration settings for `motion` is in `/etc/motion/motion.conf` file. So, go ahead and open the file.

*    Make sure `daemon` is ON.
*    Set `framerate` anywhere in between 1000 to 1500.
*    Keep `stream_port` to 8081.
*    `stream_quality` should be 100.
*    Change `stream_localhost` to OFF.
*    Change `webcontrol_localhost` to OFF.
*    Set `quality` to 100.
*    Set `width` & `height` to 640 & 480.
*    Set `pre_capture` to 2.
*    Set `post_capture` to 5.
*    set `target_directory` to the location of your choice - I use `/home/pi/Pictures`

Save and exit the file. By the way, you can change the resolution to what ever you need depending on your camera's maximum supported resolution.

After making changes, you also need to make changes to one more file. Type in the command `sudo nano /etc/default/motion` and press enter.

```
sudo vi /etc/default/motion
``` 

*   Set `start_motion_daemon` to `yes`. Save and exit.

Use the folowing commands to start, stop, and restart `motion` service. 

To start `motion` service, run the following command.
```
sudo service motion start
```

To stop `motion` service, run the following command.
```
sudo service motion stop
```

To restart `motion` service, run the following command.
```
sudo service motion restart
```

To check the status of `motion` service, run the following command:

```
sudo systemctl status motion
```

After running the service using `sudo motion`, if you run into any errors, it may be the permissions error. See Permissions section below.

## Checking the camera images online:

Go to the ip address of the Raspberry Pi, and access the url as below:

```
http://192.168.x.xxx:8081
```

The port number `8081` can be changed to whatever you need. It is specified in the `/etc/motion/motion.conf` file.

## Permissions

The `motion` service requires write access to several folders. The service also runs under user `motion` and group `motion`. Make sure you give the following folders access by running the command.

```
sudo chown motion:motion /var/run/motion
sudo chown motion:motion /var/log/motion
sudo chown motion:motion /var/log/motion/motion.log
sudo chown motion:motion /var/lib/motion 
```

Since I used `/home/pi/Pictures` folder as the `target_directory`, I had to give permissions to the folder using the following command.

```
sudo chown motion:motion /home/pi/Pictures
sudo service motion restart
```

I also installed Samba on the Raspberry Pi and shared the `/home` as a share, so that I can access the images and the videos using UNC path from Windows. for ex: `\\192.168.xxx.xxx\pi\Pictures\`

## Home Assistant Integration

When you use the platform `mjpeg` in Home Assistant,  by default, it is only limited to bringing camera image into the Home Assistant UI/dashboard. To bring the camera image into Home Assistant, add the following to your `configuation.yaml` file. This should show you the camera image on the Home Assistant dashboard.

```
camera:
  - platform: mjpeg
    mjpeg_url: http://192.168.xxx.xxx:8081
    name: Garage Camera
```

## Creating [Motion] Sensors in Home Assistant

To create sensors/alerts whenever motion is detected in Home Assistant, we need to configure some things. The `motion` component has built-in hooks that you can leverage to identify when the motion is detected. Please note that it is not a PIR (passive infra red) sensor, it only checks for differences from frame to frame, and whenever there is a "significant" difference is noticed, the software can notify you in the form of hooks. The `/etc/motion/motion.conf` file contains those hooks. The `on_motion_detected` is a hook, where you can run your own command, and `motion` makes sure it runs it. In this case, we will write a python code that simply drops "on" message into a mqtt topic whenever there is a motion detected.

The configuration goes as below:

```
 on_motion_detected /usr/bin/python3 /home/pi/motion_on_mqtt.py
```

The python component that publishes "on" message to a specified mqtt topic is below:

```python
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
``` 
before you move on, make sure you change the ip address, port, username and password of your MQTT server in the above code.

Copy the contents above and place in a file `motion_on_mqtt.py` and place that file in `/home/pi` folder. Since the `motion` program runs under `motion` user, you need to give permissions to that file for `motion` user. You can do so by running:

```
sudo chown motion:motion /home/pi/motion_on_mqtt.py
``` 

If you do not have MQTT python libraries (not the MQTT client software) installed, you might need that for your python program to work. The following commands will let you install `paho mqtt` libraries on your machine.
 
```
sudo apt-get install mosquitto mosquitto-clients -y
pip install paho-mqtt
pip3 install paho-mqtt python-etcd
sudo -u motion pip install paho-mqtt
```

After installing the software, make sure you restart `motion` program by running the command
```
sudo service motion restart
```

You can now switch the context to Home Assistant. In Home Assistant code, add the following code:

```yaml
binary_sensor:
  - platform: mqtt
    state_topic: "/garage/motion"
    name: "Garage Motion"
    device_class: occupancy
    payload_on: 'on'
    payload_off: 'off'
    value_template: "{% raw %}{{ value }}{% endraw %} "

automation:

  - alias: Garage Motion Reset
    trigger:
      - platform: state
        entity_id: binary_sensor.garage_motion
        to: 'on'
        from: 'off'
    action:
      - delay: '00:00:30'
      - service: mqtt.publish
        data:
          topic: "/garage/motion"
          payload: 'off'
          retain: false
```
Save the changes, and restart Home Assistant. That should show you a binary sensor on you dashboard, that will change its status whenever the camera detects motion. 

## Troubleshooting

There are many places where things can go wrong, please be careful in ensuring you have the software installed and configured properly. Also make sure the `motion` program that rung under `motion` user has access to the folders, paths, files. 

### The python program doesn't seem to be working
The python program requires `Paho MQTT` libraries installed on the system, and the user `motion` should be able to run it without any problems. If you can make sure the user `motion` can run the python program in the CLI (Command Line Interface), it should work as a `daemon`. To verify that, run the program as following:

```
sudo -u motion /usr/bin/python3 /home/pi/motion_on_mqtt.py
```

The command above should run successfully and you should see a "on" message in the MQTT - provided you configured MQTT server settings correctly.

### MQTT Server 

In case of not seeing messages in MQTT, make sure the MQTT server is set up and configured correctly. The user name, password, server Ip address, port all should be double checked. 

If possible, run a test command where you can drop a simple message into your mqtt using the following command.
```
mosquitto_pub -h 192.168.xxx.xxx -p 1883 -t /test -m "on" -u USERNAME -P PASSWORD
```

## Still having issues?

Instead of running the python program, try running a shell script that internaly calls the python program. Inside the shell script, put `>/tmp/motion.log 2>&1` at the end of command to log all the error messages and direct them into a log file. for ex:

Before running the command, make sure the user `motion` has write access to the `/tmp/mtion.log` file. If not,  run the command `sudo chown motion:motion /tmp/motion.log`

Sample `script.sh` contents
```
#!/bin/sh

echo "Running python program" >> /tmp/motion.log
/usr/bin/python3 /home/pi/motion_on_mqtt.py >> /tmp/motion.log 2>&1

```

Run the script as follows, and check the `/tmp/motion.log` for any errors.

```
sudo chown motion:motion script.sh
sudo chmod +x script.sh

sudo -u motion script.sh
```

Some things to remember: 
* Make sure you pay extra attention to the permissions!
* Restart motion service after every change to the `/etc/motion/motion.conf` file

Hope by now, you got it all working...

After making changes, restart the Home Assistant, and if everything runs as expected, enjoy! If not, you may want to go back to googling stuff!

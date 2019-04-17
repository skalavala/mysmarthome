---
layout: page
title: MQTT Cheat Sheet
description: "A bunch of commands to get you started using MQTT. Don't forget to install MQTTfx tool - a graphical ui to connect and manage mqtt (requires java)."
---

# MQTT Setup

By default, Home Assistant comes with a built-in MQTT server. If you want to install MQTT (either on a different Raspberry Pi or on the same server), follow the steps below.

```
wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key

sudo apt-key add mosquitto-repo.gpg.key

cd /etc/apt/sources.list.d/

sudo wget http://repo.mosquitto.org/debian/mosquitto-wheezy.list
```

Installation of Mosquitto requires root privileges. 
```
sudo -i	
```

The above command is not mandatory, it is if you wish to use root or you will need to prefix each below command with sudo. For e.g. sudo apt-get update

First, update all the source list
```
apt-get update
apt-get upgrade
```

After updating the source list, you are ready to install Mosquitto

```
apt-get install mosquito
```

Mosquitto is controlled in two ways. First, the default configuration is in `/etc/mosquitto/mosquitto.conf`. It is recommended not edit this file. Instead, make a copy of it with a `.conf` extension in `/etc/mosquitto/conf.d` folder. For e.g., if you create a file called `mosquitto.conf`, the full path to the local configuration file would be `/etc/mosquitto/conf.d/mosquitto.conf`.

Add the following in the `mosquitto.conf` file:

```
user mosquitto
max_queued_messages 200
message_size_limit 0
allow_zero_length_clientid true
allow_duplicate_messages false

listener 1883
autosave_interval 900
autosave_on_changes false
persistence true
persistence_file mosquitto.db
allow_anonymous true
password_file /etc/mosquitto/passwd
```

After updating the file, it is required to restart mosquitto. Run the following command to restart the mosquitto.
```
sudo systemctl restart mosquitto
```

You are required to provide a password for mosquitto. To create a password for mosquitto, run the following command
```
sudo mosquitto_passwd -c /etc/mosquitto/passwd <username>
```

You are required to restart mosquitto to refresh the settings.
```
sudo systemctl restart mosquitto
```

To make a system service to run Mosquitto automatically on boot, create a file ‘mosquitto.service’ in /etc/system/system folder.
```
sudo vi /etc/systemd/system/mosquitto.service
```

And, enter the following in the file and save.

```
[Unit]

Description=Mosquitto MQTT Broker daemon
ConditionPathExists=/etc/mosquitto/mosquitto.conf
After=network.target
Requires=network.target

[Service]
Type=forking
RemainAfterExit=no
StartLimitInterval=0
PIDFile=/run/mosquitto.pid
ExecStart=/usr/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf -d
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=2

[Install]
WantedBy=multi-user.target
```

Now enable the service, start it and look into the status:
```
sudo systemctl enable mosquitto.service
sudo systemctl start mosquitto.service
sudo systemctl status mosquitto.service -l
```
A successful start will show a green Mosquitto service. Note that the config and service definition are interlinked via the path of the PID file.

## Bridging MQTT with CloudMQTT

To bride Local MQTT Server with CloudMqtt, use the following. The following will pull all the messages from cloudmqtt to local mqtt server. Not the other way around.
 
Edit the `/etc/mosquitto/mosquitto.conf` file and add the following content

Just make sure you replace `XXX_*_XXX` with your details

```
# Place your local configuration in /etc/mosquitto/conf.d/
#
# A full description of the configuration file is at
# /usr/share/doc/mosquitto/examples/mosquitto.conf.example

pid_file /var/run/mosquitto.pid

persistence true
persistence_location /var/lib/mosquitto/

log_dest file /var/log/mosquitto/mosquitto.log

include_dir /etc/mosquitto/conf.d

connection cloudmqtt
start_type automatic
address m12.cloudmqtt.com:14093
#bridge_cafile /etc/ssl/certs/ca-certificates.crt
try_private true
bridge_attempt_unsubscribe true
cleansession true
clientid XXX_SOMENAME_XXX

remote_username XXX_CLOUD_MQTT_USERNAME_XXX
remote_password XXX_CLOUD_MQTT__PASSWORD_XXX
topic # in 0
```

## Remove an MQTT Topic Permanently from MQTT

```
 mosquitto_pub -h MQTT_SERVER_NAME -p PORT -t TOPIC_NAME -r -n -u USERNAME -P PASSWORD
```

## Publish a message to MQTT

```
mosquitto_pub -h 127.0.0.1 -t home/bedroom/switch1 -m "ON"
```

[Read more on publishing messages](https://mosquitto.org/man/mosquitto_pub-1.html)

## Read messages on a topic

```
mosquitto_sub -v -t 'test/topic'
```

or

```
mosquitto_sub -h 127.0.0.1 -t topic
```

[Read more on subscribing to messages](https://mosquitto.org/man/mosquitto_sub-1.html)


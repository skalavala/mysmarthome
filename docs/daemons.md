---
layout: page
title: Daemons, systemd services
description: "Auto Start applications on boot. Auto Running Home Assistant, Mosquitto, Home Bridge and App Daemon...etc"
---

# Auto-Starting Services on Boot

Newer Linux distributions are trending towards using systemd for managing daemons. Typically, systems based on Fedora, ArchLinux, or Debian (8 or later) use systemd. This includes Ubuntu releases including and after 15.04, CentOS, and Red Hat. If you are unsure if your system is using systemd, you may check with the following command:

```
$ ps -p 1 -o comm=
```
If the preceding command returns the string `systemd`, continue with the instructions below.

## Running Mosquitto as Service

Creaate a file with the name `mosquitto.service` in either`/etc/systemd/system` or `/lib/systemd/system` folder. You might need `sudo` access to be able to create the file. After creating the file, add te following content in there. 

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

## The HomeBridge Service
The homebridge.service is in `/etc/systemd/system/` folder, and the contents are:

```
[Unit]
Description=Homebridge
BindsTo=home-assistant.service
After=home-assistant.service

[Service]
Type=simple
User=homeassistant
ExecStartPre=/bin/sleep 60
ExecStart=/usr/bin/homebridge -U /home/mahasri/.homebridge/
RestartSec=10
Restart=on-failure
```

## The home-assistant Service

The file is in `/etc/systemd/system/` folder, and the contents are:

```
[Unit]
Description=Home Assistant
Wants=mosquitto.service homebridge.service
Before=homebridge.service
After=network.target mosquitto.service

[Service]
Type=simple
User=%i
ExecStart=/srv/homeassistant/bin/hass -c "/home/homeassistant/.homeassistant"

[Install]
WantedBy=multi-user.target
```

## AppDaemon Service

For the App Daemon Service to work, please make sure the following are correct:
* User - Double check the user name - some systems it will be `hass`, some systems it will be `homeassistant`...etc
* Exec Start - > check the path, and run the command! It should work outside first before it runs as a service  
* After - > make sure the name matches exactly.... do a `ls -al /etc/systemd/system/home*.*` to get the actual file name

```
[Unit]
Description=AppDaemon
After=home-assistant.service
[Service]
Type=simple
User=homeassistant
ExecStart=/usr/local/bin/appdaemon -c /home/homeassistant/conf
[Install]
WantedBy=multi-user.target
```

## Glances Service
To get stats about your machine, install `glances` on your linux machine, and run it as a service, so that you can query stats using web URL.

To see the available commands via api, go to `http://192.168.x.xxx:61208/api/2/pluginslist`. That should give you a JSON with a bunch of commands available for you to query using web URL... You can then make a query using the url `http://192.168.x.xxx:61208/api/2/COMMAND_HERE`

for ex: To get memory, go to the URL `http://192.168.x.xxx:61208/api/2/mem`. If you just want to get available memory without having to parse JSON, you can call `http://192.168.x.xxx:61208/api/2/mem/available`

Once you have the API, you can call it from Home Assistant using a `curl` command inside a commandline sensor.

To run the Glances as a `systemd` service, create a file with a name `glances.service` in `/etc/systemd/system` folder with the following contents

```
[Unit]
Description=Glances
After=network.target

[Service]
ExecStart=/usr/bin/glances -w
Restart=on-abort

[Install]
WantedBy=multi-user.target

```

Additional commands for you to consider:

After making changes to the service, always run the command to reload the new services
```
$ sudo systemctl --system daemon-reload
```

To enable service
```
$ sudo systemctl enable glances.service
```

To start Glances service automatically
```
$ sudo systemctl start glances.service
```

To restart Glances service
``` 
$ sudo systemctl restart glances.service
```

To Check the status
```
$ sudo systemctl status glances.service
```

---
layout: page
title: Setup UPS Battery on Ubuntu
description: Got a battery backup? Here is how you can set it up...
---

<h1>Introduction</h1>

<p>The package apcupsd provides a daemon which will monitor your APC UPS, and shutdown the system when power is no longer being supplied to the UPS.</p>

<h2>Prerequisites</h2>

<p>An APC UPS. The apcupsd daemon works with most APC Smart-UPS models, as well as most simple signaling models, such as Back-UPS, and BackUPS-Office.</p>

<h2>Installation</h2>

<h3>When using systemd</h3>

<p>This example assumes you are using a APC Smart-UPS 750 via USB.</p>

<p>First, install the apcupsd package via a terminal: </p>

```
sudo apt-get -y install apcupsd
```

Next, backup the original configuration files:
```
sudo cp /etc/apcupsd/apcupsd.conf /etc/apcupsd/apcupsd.conf.bak
```

Next, edit the configuration files: 
```
sudo nano /etc/apcupsd/apcupsd.conf
```

```
UPSNAME smartups750
UPSCABLE usb
UPSTYPE usb
DEVICE 
POLLTIME 60
```

```
sudo cp /etc/default/apcupsd /etc/default/apcupsd.bak
```

```
sudo nano /etc/default/apcupsd
```

```
ISCONFIGURED=yes
```

 <p>Now one may check the status of the UPS via a terminal: </p>
 ```
 apcaccess status
 ```

 When you run the command, you will see something like this...

```
APC      : 001,027,0660
DATE     : 2015-09-26 18:39:09 -0500  
HOSTNAME : pc
VERSION  : 3.14.12 (29 March 2014) debian
UPSNAME  : smartups750
CABLE    : USB Cable
DRIVER   : USB UPS Driver
UPSMODE  : Stand Alone
STARTTIME: 2015-09-26 18:39:08 -0500  
MODEL    : Smart-UPS 750 
STATUS   : ONLINE 
BCHARGE  : 100.0 Percent
TIMELEFT : 51.0 Minutes
MBATTCHG : 5 Percent
MINTIMEL : 3 Minutes
MAXTIME  : 0 Seconds
ALARMDEL : 30 Seconds
BATTV    : 27.1 Volts
NUMXFERS : 0
TONBATT  : 0 Seconds
CUMONBATT: 0 Seconds
XOFFBATT : N/A
STATFLAG : 0x05000008
MANDATE  : 2010-07-08
SERIALNO : XXXXXXXXXXXX
NOMBATTV : 24.0 Volts
FIRMWARE : COM 02.1 / UPS.05.D
END APC  : 2015-09-26 18:39:19 -0500
```

In order to run `apctest`, one must first stop apcupsd via a terminal: 

```
sudo systemctl stop apcupsd
```

Otherwise, one may see the following error: 
```
sudo apctest
2015-09-26 18:57:38 apctest 3.14.12 (29 March 2014) debian
Checking configuration ...
sharenet.type = Network & ShareUPS Disabled
cable.type = USB Cable
mode.type = USB UPS Driver
apctest FATAL ERROR in apctest.c at line 335
Unable to create UPS lock file.
  If apcupsd or apctest is already running,
  please stop it and run this program again.
apctest error termination completed
```

Then execute the collowing command: 
```
sudo apctest
```

That will show the following output:
```
2015-09-26 18:59:38 apctest 3.14.12 (29 March 2014) debian
Checking configuration ...
sharenet.type = Network & ShareUPS Disabled
cable.type = USB Cable
mode.type = USB UPS Driver
Setting up the port ...
Doing prep_device() ...

You are using a USB cable type, so I'm entering USB test mode
Hello, this is the apcupsd Cable Test program.
This part of apctest is for testing USB UPSes.

Getting UPS capabilities...SUCCESS

Please select the function you want to perform.

1)  Test kill UPS power
2)  Perform self-test
3)  Read last self-test result
4)  View/Change battery date
5)  View manufacturing date
6)  View/Change alarm behavior
7)  View/Change sensitivity
8)  View/Change low transfer voltage
9)  View/Change high transfer voltage
10) Perform battery calibration
11) Test alarm
12) View/Change self-test interval
 Q) Quit

Select function number:
```

 Once done, start apcupsd: 

 ```
 sudo systemctl start apcupsd
 ```

 You can also check the status by running:

 ```
 sudo systemctl status apcupsd
 ```

 
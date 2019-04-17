---
layout: page
title: Raspberry Pi Basic Setup
description: "Highlights some of the steps involved in setting up Raspberry Pi to run Home Assistant and other applications."
---

## Downloading Rasbian Image
<p>Go to <a target="_blank" href="https://www.raspberrypi.org/">Raspberry Pi's</a> web site and click on Downloads, and there you will find a bunch of images that you can install on Raspberry Pi. After downloading the image, flash the Raspberry Pi using <a target="_blank" href="https://sourceforge.net/projects/win32diskimager/">Win32 DiskImager software</a>.</p>

<p>After flashing the software on the SD card, insert it in Raspberry Pi and connect a keyboard, mouse and monitor and power Raspberry Pi to boot.</p>

<p>If you did all correctly, the Raspberry Pi should boot properly and should show you a desktop. Once you see desktop, you need to setup some basic stuff by going to Raspberry Pi icon -> Preferences -> Raspberry Pi Configuration.</p>

* Setup Hostname
* Setup Wi-Fi
* Change Default Password
* Set Time Zone
* Set Locale
* Set keyboard
* Set WiFi Country (optional)
* Enable VNC Server (if you want to have remove desktop, if not SSH is fine)

You can also access some of this information by going to command line interface, and typing the following command:

```
sudo raspi-command
```

As soon as you set up the commands above, you may want to restart by running `sudo reboot now` before you move onto the next steps:

Run the follwing command to update and upgrade
```
sudo apt-get update && sudo apt-get upgrade -y
```

Since some of the updates require disk space, it will ask you to confirm, just type ‘y’ and hit ‘enter’ to continue. It may ask you multiple times depending upon number of packages being updated. Optionally, you can also run the command with ‘-y’ option.

You may also want to update the firmware to ensure you are using the latest one. To update the firmware, run the following command(s) in the same order.

```
sudo apt-get install rpi-update
sudo rpi-update
sudo reboot
```

While you are at it, run the following commands to update the time server and install ca-certificates.
```
sudo apt-get install ca-certificates
sudo apt-get install ntpdate
sudo ntpdate -u ntp.ubuntu.com
```

Optionally, you can run the following command to clean up any packages

```
sudo apt-get clean
```
or

```
sudo apt-get autoremove 
sudo apt-get autoclean
sudo apt-get remove <application_name>
sudo apt-get purge package
```

## Setup Samba - File Sharing

Samba allows you to share folders, and when you are on Windows machines, you will be able to look up RPi by host name.

```
sudo apt-get update
sudo apt-get -y install samba
sudo reboot
```

After installing Samba and rebooting the RPi, you need to set default password and update the configuration file to enable sharing of files. The password is not required, but it is always a good practice to secure folders from unauthorized users.

```
sudo smbpasswd -a pi
```

Make configuration changes by running the command below

```
sudo vi /etc/samba/smb.conf
```

Go to the bottom of the file, and enter the following

```
[Home]
 comment=Home Directory Share
 path=/home
 browseable=Yes
 writeable=Yes
 read only = false
 only guest=no
 create mask=0777
 directory mask=0777
 public=no
```

You can have as many shares as you want. There is virtually no limit on the number of shares.
To restart Samba, execute the following command

```
sudo service smbd restart
```

Run the following command to test and verify the samba configuration
```
testparm 
```

## The .profile file

The .profile file comes in handy when you want to set user specific environmental variables, and run some basic scripts to help you keep things going for that specific user session. The following script adds `.`  (current folder) to the path, so that when you run any command, it first looks within the current folder first before looking into other folders as specified in the `$PATH`. 

To show you the currently logged in machine's host name and IP addresses when logged in, add the commands to the .profile file.

You can also create aliases as shortcuts.

```
PATH=./:$PATH
echo "---------------------------------------------------------"
echo "Host name:  " $HOSTNAME
echo "---------------------------------------------------------"

alias h="cd /home/homeassistant/.homeassistant"
alias cls="/usr/bin/clear"
```

Run `hostname -I` to see the list of IP addresses assigned. 

After making changes to the .profile file, ensure the file has “execute” permissions. If the file does not have “execute” permissions, it will not execute. To give “execute” permission, you can run the following command in the home directory.

`chmod +x ~/.profile`

You can also explicitly run the .profile file by using the following command

`source ~/.profile`


## Restarting Raspberry Pi every night at 4:05 AM

Why 4:05AM? I don't know! You can pick whatever the time you want...

If you are not running anything critical on your Raspberry Pi, and you are okay with it automatically restart every now and then, the following script is for you. I like to restart my RPi every day at 4:05 in the morning. I like the idea of resetting everything back to “normal” on a more frequent basis to run things smoother.

Type the following command in the console 
```
sudo crontab –e
```

And enter the following line 
```
0 4   *   *   *    /sbin/shutdown -r +5
```

What the above lines means, it basically the following:
```
minute hour dayOfMonth Month dayOfWeek commandToRun
```

## Setting up Gstreamer

Run the following command to install GStreamer
```
sudo apt-get install python3-gst-1.0 \
    gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0 \
    gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly \
    gstreamer1.0-tools
```

Run the following command to link gsp/gi path to HA for Gstreamer to function properly    

BEFORE you run the following command, make sure the path to the virtal environment is correct

```
sudo ln -s /usr/lib/python3/dist-packages/gi /srv/homeassistant/homeassistant_venv/lib/python3.4/site-packages
```

Make sure the homeassistant user is added to the audio group by running the following command.

```
sudo usermod -a -G audio homeassistant
```

## Respberry Pi GPIO Access

If you are using GPIOs on Raspberry Pi, you need to give access to `homeassistant` user to the GPIO. You can do that by running the following command:

```
sudo usermod -G gpio -a homeassistant
```

## Removing unwanted apps on Raspberry Pi

When you download the images from RaspberryPi.org web site, the image contains a bunch of stuff that you may not need. You can simply uninstall the unwanted stuff by running the following command:

```
sudo apt-get purge wolfram-engine greenfoot nodered bluej nuscratch scratch sonic-pi libreoffice claws-mail claws-mail-i18n minecraft-pi python-pygame -y
sudo apt-get clean
sudo apt-get autoremove
```

You can change the command and add any other software/packages you like

Note, you may still see some shortcuts on the desktop, you may want to manually delete them. The following deletes some of the shortcuts.
You may want to check if there any other shortcuts you need to delete in `/usr/share/raspi-ui-overrides/applications` folder.

```
sudo rm /usr/share/raspi-ui-overrides/applications/wolfram-language.desktop
sudo rm /usr/share/raspi-ui-overrides/applications/wolfram-mathematica.desktop
sudo rm /usr/share/raspi-ui-overrides/applications/bluej.desktop
sudo rm /usr/share/raspi-ui-overrides/applications/greenfoot.desktop
sudo rm /usr/share/raspi-ui-overrides/applications/bluej.desktop
sudo rm /usr/share/raspi-ui-overrides/applications/libreoffice-draw.desktop
sudo rm /usr/share/raspi-ui-overrides/applications/libreoffice-math.desktop
sudo rm /usr/share/raspi-ui-overrides/applications/libreoffice-startcenter.desktop
sudo rm /usr/share/raspi-ui-overrides/applications/minecraft-pi.desktop
sudo rm /usr/share/raspi-ui-overrides/applications/python-games.desktop
sudo rm /usr/share/raspi-ui-overrides/applications/scratch.desktop
```

After removing the files, do an update to update any dependencies.

```
sudo apt-get update && sudo apt-get upgrade -y
```

## Raspberry Pi Configuration

For more about configuration of boot, HDMI CEC, and or advanced options, please visit [https://elinux.org/RPiconfig](https://elinux.org/RPiconfig)

## File Access to Home Assistant

HA requires the `homeassistat` user to have read, write access to the config folder. If for any reason, the access gets messed up, you can run the following command to list all the files that are not owned by `homeassistant` user.

```
find /home/homeassistant/.homeassistant ! -user homeassistant -print
```

## skalavala's Home Automation/Smart Home

Here you will find a bunch of scripts that I use to automate my home.

I have a bunch of Raspberry Pi's, and Pi Zeros at home along with a bunch of "smart" devices of various brands. All these smart devices work great independently but not together. My goal is to bring all of them together and have them talk to each other with a little bit of programming and make them really smarter as a whole! I also want to be able to run all the software on Raspberry Pi's only.

The primary Home Automation software/platform that I use is [Home Assistant](https://home-assistant.io/) (HA). It is an open-source home automation platform written by a bunch of smart individuals. HA allows you to track and control devices easily with simple configuration and with a little bit of scripting, you can do wonders. It is also a perfect piece of software to run entirely on a single Raspberry Pi.

The following picture shows high level architecture of my home network, and what I use for basic automation stuff.
![My Home Automation Setup](https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/smart-home.jpg)

Please feel free to let me know if you find any issues with my code, and/or have any suggestions. Thank you!

## My Smart Devices

<p>
The following are some of the smart devices that I use for my current Smart Home setup. Please feel free to reach out to me or check my repository on how to configure them.
</p>
<h2>Smart Lights & Switches</h2>
<TABLE>
<TR>
    <TD>
    <a href="http://amzn.to/2pTWaNm"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/lifx-bulb.jpg" alt="Lifx Light Bulb" /></a><br/>
        Lifx Light Bulb
    </TD>
    <TD>
    <a href="http://amzn.to/2DI7i4P"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/lifx-led-strip.jpg" alt="Lifx LED Strip" /></a><br/>
        Lifx LED Strip
    </TD>
    <TD>
    <a href="http://amzn.to/2DLfuBi"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/philips-hue-bulbs.jpg" alt="Philips Hue Bulbs" /></a><br/>
        Philips Hue Bulbs
    </TD>
    <TD>
    <a href="http://amzn.to/2mH7bi8"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/philips-hue-hub.jpg" alt="Philips Hue Hub & Bulbs" /></a><br/>
        Philips Hue Hub & Bulbs
    </TD>
</TR>
<TR>
    <TD>
    <a href="http://amzn.to/2qeilPx"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/tplink-smart-switches.jpg" alt="TP-Link Smart Switches" /></a><br/>
        TP-Link Smart Switches
    </TD>
    <TD>
    <a href="http://amzn.to/2pairYc"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/wemo-light-switches.jpg" alt="Wemo Switches" /></a><br/>
        Wemo Switches
    </TD>
    <TD>
    <a href="http://amzn.to/2DK11G5"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/wall-mote.jpg" alt="ZWave Wallmotes" /></a><br/>
        ZWave Wallmotes
    </TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
</TR>
</TABLE>
<h2>Smart Outlets</h2>
<TABLE>
<TR>
    <TD>
    <a href="http://amzn.to/2FKtegl"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/aeltec-smart-outlet.jpg" alt="Aeotec Smart Outlet" /></a><br/>
        Aeotec Smart Outlet
    </TD>
    <TD>
    <a href="http://amzn.to/2pTIDFA"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/eteccity-rf-outlets.jpg" alt="Eteckcity RF Outlets" /></a><br/>
        Eteckcity RF Outlets
    </TD>
    <TD>
    <a href="http://amzn.to/2qe8PMo"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/rf-transeivers.jpg" alt="RF Transmitters & Receivers" /></a><br/>
        RF Transmitters & Receivers
    </TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
</TR>
</TABLE>
<h2>Home Securty System</h2>
<TABLE>
<TR>
    <TD>
    <a href="http://amzn.to/2pVmS6y"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/ring-doorbell-pro.jpg" alt="Ring Doorbell Pro" /></a><br/>
        Ring Doorbell Pro
    </TD>
    <TD>
    <a href="http://amzn.to/2pTIpyv"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/simplisafe-home-security.jpg" alt="SimpliSafe Home Security System" /></a><br/>
        SimpliSafe Home Security System
    </TD>
    <TD>
    <a href="http://amzn.to/2uOJxSX"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/ubiquity-poe-switch.jpg" alt="Ubiquity 8-port PoE Switch" /></a><br/>
        Ubiquity 8-port PoE Switch
    </TD>
    <TD>
    <a href="http://amzn.to/2suiPhT"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/hikvision-bullet-cameras.jpg" alt="HikVision Bullet IP Cameras" /></a><br/>
        HikVision Bullet IP Cameras
    </TD>
</TR>
<TR>
    <TD>
    <a href="http://amzn.to/2papVuj"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/leeo-smoke-alert.jpg" alt="Leeo Smoke Alert" /></a><br/>
        Leeo Smoke Alert
    </TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
</TR>
</TABLE>
<h2>Motion Sensors</h2>
<TABLE>
<TR>
    <TD>
    <a href="http://amzn.to/2pV6SkH"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/in-wall-motion-sensors.jpg" alt="In Wall Motion Sensors" /></a><br/>
        In Wall Motion Sensors
    </TD>
    <TD>
    <a href="http://amzn.to/2DI5TeJ"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/ecolink-motion-sensors.jpg" alt="Ecolink Motion Sensor" /></a><br/>
        Ecolink Motion Sensor
    </TD>
    <TD>
    <a href="http://amzn.to/2DKO7aN"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/xiaomi-motion-sensor.jpg" alt="Xiaomi Motion Sensors" /></a><br/>
        Xiaomi Motion Sensors
    </TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
</TR>
</TABLE>
<h2>ZWave Devices</h2>
<TABLE>
<TR>
    <TD>
    <a href="http://amzn.to/2pa9uhO"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/aeltec-zwave-stick.jpg" alt="Aeotec ZWave Gen5 Stick" /></a><br/>
        Aeotec ZWave Gen5 Stick
    </TD>
    <TD>
    <a href="http://amzn.to/2DKyxvU"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/aeotec-energy-meter.jpg" alt="Aeotec Energy Meter" /></a><br/>
        Aeotec Energy Meter
    </TD>
    <TD>
    <a href="http://amzn.to/2qdYUqa"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/aeotec-multi-sensor.jpg" alt="Aeotec Multi Sensor 5" /></a><br/>
        Aeotec Multi Sensor 5
    </TD>
    <TD>
    <a href="http://amzn.to/2pV5yOT"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/aeotec-multi-sensor6.jpg" alt="Aeotec Multi Sensor 6" /></a><br/>
        Aeotec Multi Sensor 6
    </TD>
</TR>
<TR>
    <TD>
    <a href="http://amzn.to/2DKz7cK"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/range-extender.jpg" alt="Aeotec Range Extender" /></a><br/>
        Aeotec Range Extender
    </TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
</TR>
</TABLE>
<h2>Door & Window Sensors</h2>
<TABLE>
<TR>
    <TD>
    <a href="http://amzn.to/2DKYfjJ"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/door-sensors.jpg" alt="Ecolink Door Sensors" /></a><br/>
        Ecolink Door Sensors
    </TD>
    <TD>
    <a href="http://amzn.to/2DKzHHM"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/door-window-sensors.jpg" alt="Door & Window Sensors" /></a><br/>
        Door & Window Sensors
    </TD>
    <TD>
    <a href="http://amzn.to/2FLRnTI"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/window-sensor.jpg" alt="Window Sensors" /></a><br/>
        Window Sensors
    </TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
</TR>
</TABLE>
<h2>Multimedia Stuff</h2>
<TABLE>
<TR>
    <TD>
    <a href="http://amzn.to/2pU2V1Y"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/bluetooth-speaker.jpg" alt="Bluetooth Speakers" /></a><br/>
        Bluetooth Speakers
    </TD>
    <TD>
    <a href="http://amzn.to/2tVYN4b"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/denon-receiver.jpg" alt="DENON Receiver" /></a><br/>
        DENON Receiver
    </TD>
    <TD>
    <a href="http://amzn.to/2tVYN4b"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/denon-receiver.jpg" alt="ONKYO Receiver" /></a><br/>
        ONKYO Receiver
    </TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
</TR>
</TABLE>
<h2>Garage Door Devices</h2>
<TABLE>
<TR>
    <TD>
    <a href="http://amzn.to/2DHQNWu"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/garage-tilt-sensor.jpg" alt="Garage Door Tilt Sensors" /></a><br/>
        Garage Door Tilt Sensors
    </TD>
    <TD>
    <a href="http://amzn.to/2pV2wu1"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/garage-relay.jpg" alt="ZWave Garage Relay" /></a><br/>
        ZWave Garage Relay
    </TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
</TR>
</TABLE>
<h2>Servers and Computers</h2>
<TABLE>
<TR>
    <TD>
    <a href="http://amzn.to/2DMx2gN"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/apcups-1500va.jpg" alt="UPS Battery" /></a><br/>
        UPS Battery
    </TD>
    <TD>
    <a href="http://amzn.to/2DI8Coj"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/qnap-nas.jpg" alt="NAS Storage" /></a><br/>
        NAS Storage
    </TD>
    <TD>
    <a href="http://amzn.to/2p9RVhQ"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/raspberry-pi3.jpg" alt="Raspberry PI 3" /></a><br/>
        Raspberry PI 3
    </TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
</TR>
</TABLE>
<h2>Smart Thermostat</h2>
<TABLE>
<TR>
    <TD>
    <a href="http://amzn.to/2FQCsaX"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/ecobee4-thermostat.jpg" alt="Ecobee Thermostat" /></a><br/>
        Ecobee Thermostat
    </TD>
    <TD>
    <a href="http://amzn.to/2uuPAgl"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/ecobee-room-sensors.jpg" alt="Ecobee Room Sensors" /></a><br/>
        Ecobee Room Sensors
    </TD>
    <TD>
    <a href="http://amzn.to/2Dgt3rv"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/nest-thermostat.jpg" alt="Nest Thermostat" /></a><br/>
        Nest Thermostat
    </TD>
    <TD>
    <a href="http://amzn.to/2FQDgN1"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/xiaomi-temp-sensor.jpg" alt="Xiaomi Temperature Sensor" /></a><br/>
        Xiaomi Temperature Sensor
    </TD>
</TR>
</TABLE>
<h2>DIY Stuff</h2>
<TABLE>
<TR>
    <TD>
    <a href="http://amzn.to/2pTQ1kv"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/relay.jpg" alt="Relays" /></a><br/>
        Relays
    </TD>
    <TD>
    <a href="http://amzn.to/2pV60wx"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/esp8266.jpg" alt="NodeMUC/ESP8266" /></a><br/>
        NodeMUC/ESP8266
    </TD>
    <TD>
    <a href="http://amzn.to/2qe8PMo"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/rf-transeivers.jpg" alt="RF Transmitters & Receivers" /></a><br/>
        RF Transmitters & Receivers
    </TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
</TR>
</TABLE>
<h2>Smart Hubs</h2>
<TABLE>
<TR>
    <TD>
    <a href="http://amzn.to/2FQmFsz"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/xiaomi-gateway-kit.jpg" alt="Xiaomi Aqara Gateway" /></a><br/>
        Xiaomi Aqara Gateway
    </TD>
    <TD>
    <a href="http://amzn.to/2mH7bi8"><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/philips-hue-hub.jpg" alt="Philips Hue Hub" /></a><br/>
        Philips Hue Hub
    </TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
    <TD><img src="https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/blank.jpg"/><br/>&nbsp;</TD>
</TR>
</TABLE>

## Here is a sample view of my dashboard

<img src="https://github.com/skalavala/smarthome/blob/master/images/skalavala-smarthome-dashboard.jpg" alt="Home Assistat" />

## Custom Components:

### Custom Variables:

I called it `input_label`, it is basically a `label` type component, where you can store any value you want, and can be used in automations, scripts and more. [check out the code here](https://github.com/skalavala/smarthome/blob/master/custom_components/input_label.py). Search for [input_label](https://github.com/skalavala/smarthome/search?utf8=%E2%9C%93&q=input_label) in my repo on how to use it.

### Life360 Custom Component:

The Life360 component uses Life360 API and retrieves information about the circle you created in the same format as OwnTracks. You just ned to setup OwnTracks, and drop-in the custom component, and you are all set!

[Click Here](https://github.com/skalavala/smarthome/blob/master/custom_components/sensor/life360.py) for the Life360 custom component code. Make sure you check out the [Packages](https://github.com/skalavala/smarthome/blob/master/packages/life360.yaml) section on how to use the Life360 Component.

### Palo Alto Component:

I wrote a Palo Alto component to keep an eye on who is logging into my firewall and VPN at home. Below is the screenshot and you can find the code in the `custom_components` folder and corresponding `Packages` folder.

<img src="https://raw.githubusercontent.com/skalavala/smarthome/master/images/paloalto.png"/>

### Tesla 

<img src="https://raw.githubusercontent.com/skalavala/smarthome/master/images/Tesla.png" />

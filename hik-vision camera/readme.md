## The following are the screenshots of HikVision camera setup.
</br>

### If you get "Parameter Error" when saving the settings, that means you are not using the right browser with correct plug-in.

The HikVision cameras work best on IE11 browsers, where it will install an active-x plug-in. This plug-in lets you see the live view, and also lets you play the recorded content. HikVision requires that plug-in to be installed to save settings. If you are on Windows 10, just go to run command, and type `iexplore.exe` to open old internet explorer, and go to your camera URL. It will then ask you to install that active-x plugin.

Also, for the text overlay to work, the authentication for web must be digest/basic. 

<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_001.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_002.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_003.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_004.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_005.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_006.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_007.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_008.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_009.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_010.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_011.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_012.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_013.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_014.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_015.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_016.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_017.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_018.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_019.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_020.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_021.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_022.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_023.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_024.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_025.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_026.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_026a.jpg"></img></br>
The "Integration Protocol" under Advanced settings is only visible if you have the latest firmware. The reason you don't see that option in the above screenshots is because I had older version of firmware, and I updated it to enable text overlay feature.

The following is the Home Assistant REST API sensor that sets a given text to the camera.  For more information, go to
[https://github.com/skalavala/mysmarthome/blob/master/packages/cameras.yaml#L141](https://github.com/skalavala/mysmarthome/blob/master/packages/cameras.yaml#L141)

```
rest_command:
  set_camera_textoverlay_left_bottom:
    url: http://192.168.xxx.xxx/Video/inputs/channels/1/overlays/text/1
    username: !secret camera_username
    password: !secret camera_password
    method: PUT
    content_type: 'text/xml'
    payload: >-
      <?xml version="1.0" encoding="UTF-8"?>
      <TextOverlay version="1.0" xmlns="http://www.hikvision.com/ver10/XMLSchema">
      <id>1</id><enabled>true</enabled>
      <posX>45</posX><posY>520</posY>
      <message>{{ message }} </message>
      </TextOverlay>
```

<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_027.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_028.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_029.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_030.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_031.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_032.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_033.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_034.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_035.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_036.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_037.jpg"></img></br>

Make sure you check the "1" checkbox under **Text Overlay**, enter some text and save settings if you want to update the text programmatically. 
Also, if you get the "Parameter Error" while saving, that means you are using wrong browser! 

**Make sure you use IE11 browser with the ActiveX plugin installed.**

**Hikvision settings are best updated using IE11 browser!**

<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_038.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_039.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_040.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_041.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_042.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_043.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_044.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_045.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_046.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_047.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_048.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_049.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_050.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_051.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_052.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_053.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_054.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_055.jpg"></img></br>
<img src="https://raw.githubusercontent.com/skalavala/mysmarthome/master/hik-vision%20camera/images/screenshot_056.jpg"></img></br>

---
layout: page
title: Jinja Scripts for Curious Minds
description: "Bunch of Jinja2 scripts to help you understand your way around Home Assistant"
---

# Jinja code for Ninjas

## 1. To see which entities are exposed to your alexa platform, run the following script

The following entities are exposed to Alexa platform via `emulated_hue_hidden`:

{% raw %}
```
{{ "-".ljust(50, '-') }} {{ "-".ljust(30, '-') }}
{{ "Entity ID".ljust(50, ' ') }} {{ "Name".ljust(30, ' ') }}
{{ "-".ljust(50, '-') }} {{ "-".ljust(30, '-') }}
{%- for item in states-%}
{%- if item.attributes.emulated_hue_hidden %}
{{ item.entity_id.ljust(50, ' ') }} {{ item.name }}
{%- endif -%}
{%- endfor %}
{{ "-".ljust(50, '-') }} {{ "-".ljust(30, '-') }}
```
{% endraw %}

### Here is the sample output of the above script:

```
-------------------------------------------------- ------------------------------
Entity ID                                          Name                          
-------------------------------------------------- ------------------------------
input_boolean.do_not_disturb                       Do Not Disturb
input_boolean.home_assistant_restart               Home Assistant
light.dinette                                      Kitchen Light
light.family_room                                  Family Room Lights
light.master_bedroom                               Master Bedroom Lights
light.office_room_light                            Office Room Light
switch.wemobackyardlightswitch                     Backyard Lights
switch.wemofrontporchlightswitch                   Front Porch Lights
switch.wemoswitch1                                 Front Room Light
-------------------------------------------------- ------------------------------
```


## 2. To generate template sensors based on the device_trackers,  run the following script and copy the output and use it in your code

Copy the output of the code in your dev-templates, and use it in your code directly


```
{% raw %}
- platform: template
  sensors:
{% for state in states.device_tracker -%}
  {% if loop.first %}{% elif loop.last %}
{% else %}
{% endif %}    {{state.entity_id|replace("device_tracker.","") -}}_template:
      value_template: {{ '"{% if is_state' }}('{{-state.entity_id -}}', 'home') {{'%}online{% else %}offline{% endif %}"'}}
      friendly_name: "{{ state.attributes.friendly_name|title|replace("_"," ",) if state.attributes.friendly_name is defined else state.name|title|replace("_"," ",) }}"
      icon_template: {{ '"{% if is_state' }}('{{-state.entity_id -}}', 'home') {{'%}mdi:check-circle{% else %}mdi:alert-circle{% endif %}"'}}
{% endfor %}
{% endraw %}
```

### Here is the sample output of the above script:

```
{% raw %}
    suresh_suresh_template:
      value_template: "{% if is_state('device_tracker.suresh_suresh', 'home') %}online{% else %}offline{% endif %}"
      friendly_name: "Suresh"
      icon_template: "{% if is_state('device_tracker.suresh_suresh', 'home') %}mdi:check-circle{% else %}mdi:alert-circle{% endif %}"

    srinika_srinika_template:
      value_template: "{% if is_state('device_tracker.srinika_srinika', 'home') %}online{% else %}offline{% endif %}"
      friendly_name: "Srinika"
      icon_template: "{% if is_state('device_tracker.srinika_srinika', 'home') %}mdi:check-circle{% else %}mdi:alert-circle{% endif %}"
{% endraw %}
    ...more entries!    
```


## 3. Group & Entities:

To see the list of `groups`,  and the entities that belong to the group, run this script

```
{% raw %}
{% for group in states.group%}
Group Name: {{ group.name }}, Entity ID: {{ group.entity_id }}
{{ "-".ljust(50, '-') }} {{ "-".ljust(30, '-') }}
{% for entity in group.attributes.entity_id|list() %}
{{- entity }}
{% endfor %}
{% endfor %}
{% endraw %}
```

### Here is the sample output of the above script:

```
Group Name: Date Time, Entity ID: group.date_time
-------------------------------------------------- ------------------------------
sensor.time
sensor.date
binary_sensor.workday_sensor
sensor.ha_installed_version
sensor.ha_current_version
sensor.ha_last_restart


Group Name: Door Sensors, Entity ID: group.door_sensors
-------------------------------------------------- ------------------------------
binary_sensor.ecolink_door_sensor_sensor
binary_sensor.ecolink_door_sensor_sensor_2

...more entries!
```

## 4. To see all the Entities and corresponding attributes all in one place, run this script:

```
{% raw %}
{{ "_".ljust(90, "_") }}
{{ "Entity ID".ljust(50) }}{{ "Entity Name" }}
  {{ "Attribute Name".ljust(50) }}{{ "Attribute Value" }}

{% for item in states %}
{{ "_".ljust(90, "_") }}
{{ item.entity_id.ljust(50) }}
  {{ "State".ljust(50) }}: {{ item.state}}
  {{ "Domain".ljust(50) }}: {{ item.domain}}
  {{ "Object ID".ljust(50) }}: {{ item.object_id}}
  {{ "Last Updated".ljust(50) }}: {{ item.last_updated}}
  {{ "Last Changed".ljust(50) }}: {{ item.last_changed}}
{%- for attrib in item.attributes|sort() %}
{%- if attrib is defined %} 
  {{attrib.ljust(50)}}: {{ item.attributes[attrib] }} 
{%- endif %}
{%- endfor %}
{%- endfor %}
{% endraw %}
```

### The following is the sample output of the above script:

```
__________________________________________________________________________________________
automation.alert_low_battery_level_of_sensors     
  State                                             : on
  Domain                                            : automation
  Object ID                                         : alert_low_battery_level_of_sensors
  Last Updated                                      : 2017-09-14 00:19:00.697024+00:00
  Last Changed                                      : 2017-09-14 00:19:00.697024+00:00 
  friendly_name                                     : Alert Low Battery Level of Sensors 
  icon                                              : mdi:arrow-right-drop-circle 
  last_triggered                                    : None
__________________________________________________________________________________________
automation.alert_super_heavy_winds                
  State                                             : on
  Domain                                            : automation
  Object ID                                         : alert_super_heavy_winds
  Last Updated                                      : 2017-09-14 00:19:00.739659+00:00
  Last Changed                                      : 2017-09-14 00:19:00.739659+00:00 
  friendly_name                                     : Alert Super Heavy Winds 
  hidden                                            : True 
  icon                                              : mdi:arrow-right-drop-circle 
  last_triggered                                    : None

  ...more entries!
```

## 5. Temperature Conversion

Sample code that uses macros to convert temperature from Fahrenheit to Centigrade and vice versa

```
{% raw %}
{%- macro F2C(temperature) -%}
{% set tmp = (((temperature - 32) *5)/9) %}
{{- " %0.2f" % tmp }}
{%- endmacro -%}

{%- macro C2F(temperature) -%}
{% set tmp = (((temperature *9) /5) + 32) %}
{{- " %0.2f" % tmp -}}
{%- endmacro -%}

75.00 degrees of Fahrenheit is equal to: {{- F2C(75.00) }} Centigrade
23.89 degrees of Centigrade is equal to: {{- C2F(23.89) }} Fahrenheit
{% endraw %}
```


## 5.a Humidex Calculation
You can calculate the humidex based on Temperature and Relative Humidity using the following jinja macro

```
{% raw %}
{% macro humidex(T, H) %}
  {% set t = 7.5*T/(237.7+T) %}
  {% set et = 10**t %}
  {% set e= 6.112 * et * (H/100) %}
  {% set humidex = T+(5/9)*(e-10) %}
  {% if humidex < T %}
    {% set humidex = T %}
  {% endif %}
  {{humidex}}
{% endmacro %}

{{ humidex(23,45) }}
{% endraw %}
```

### Here is the output of the above script:

```
75.00 degrees of Fahrenheit is equal to: 23.89 Centigrade
23.89 degrees of Centigrade is equal to: 75.00 Fahrenheit
```

## 6. Trigger Data in Automations

Ever wondered what trigger data is available for you when writing automations? Just copy the mqtt.publish service below 
and put it in **any** of your automation action section, and <b>it will dump all the attributes and information related to trigger, and state into your mqtt with a topic name "/dump/platform" </b>.

Pre-requisite is to have MQTT configured in your Home Assistant. Use tools like `mqttfx` to browse mqtt data.

Hope you find it useful!

```
{% raw %}
  - alias: Light Bulb State Change 
    trigger:
      platform: state
      entity_id: light.dinette
    action:        
      - service: mqtt.publish
        data_template:
          topic: '/dump/{{ trigger.platform }}'
          retain: false
          payload: >-
            {%- macro dumpState(statePrefix, stateObj) -%}
              {{statePrefix ~ ": "}} {{- stateObj.state }}{{- "\n" -}}
              {{statePrefix ~ ".entity_id: "}} {{- stateObj.entity_id }}{{- "\n" -}}
              {{statePrefix ~ ".domain: "}} {{- stateObj.domain }}{{- "\n" -}}
              {{statePrefix ~ ".object_id: "}} {{- stateObj.object_id }}{{- "\n" -}}
              {{statePrefix ~ ".name: "}} {{- stateObj.name }}{{- "\n" -}}
              {{statePrefix ~ ".last_updated: "}} {{- stateObj.last_updated }}{{- "\n" -}}
              {{statePrefix ~ ".last_changed: "}} {{- stateObj.last_changed }}{{- "\n" -}}
              {%- for attrib in stateObj.attributes | sort() %}
                {%- if attrib is defined -%} 
                {{- statePrefix ~ ".attributes." ~ attrib ~ ": " -}} {{- stateObj.attributes[attrib] -}}
                {{- "\n" -}}
                {%- endif -%}
              {%- endfor -%}
            {%- endmacro -%}
            
            {% set p = trigger.platform %}
            {{"trigger.platform: "}} {{ p }}{{- "\n" -}}
            
            {%- if p == "mqtt" -%}
            {{"trigger.topic: "}} {{ trigger.topic }}{{- "\n" -}}
            {{"trigger.payload: "}} {{ trigger.payload }}{{- "\n" -}}
            {{"trigger.payload_json: "}} {{ trigger.payload_json }}{{- "\n" -}}
            {{"trigger.qos: "}} {{ trigger.qos }}{{- "\n" -}}
            {%- endif -%}
            
            {%- if p == "event" or p == "sun" or p == "zone" -%}
            {{"trigger.event: "}} {{ trigger.event }}{{- "\n" -}}
            {%- endif -%}
            
            {%- if p == "numeric_state" -%}
            {{"trigger.above: "}} {{ trigger.above }}{{- "\n" -}}
            {{"trigger.below: "}} {{trigger.below }}{{- "\n" -}}
            {%- endif -%}
            
            {%- if p == "state" -%}
            {{"trigger.for: "}} {{ trigger.for }}{{- "\n" -}}
            {%- endif -%}
            
            {%- if p == "time" -%}
            {{"trigger.now: "}} {{ trigger.now }}{{- "\n" -}}
            {%- endif -%}
            
            {%- if p == "zone" -%}
            {{"trigger.zone: "}} {{ trigger.zone }}{{- "\n" -}}
            {%- endif -%}
            
            {%- if p == "state" or p == "numeric_state" or p == "template" or p == "zone" -%}
            {{"trigger.entity_id: "}} {{ trigger.entity_id }}{{- "\n" -}}{{- "\n" -}}
            {{"trigger.from_state: "}} {{- "\n" -}}
            -------------------{{- "\n" -}}
            {{ dumpState("trigger.from_state", trigger.from_state) }} {{- "\n" -}}
            trigger.to_state:{{- "\n" -}}
            -----------------{{- "\n" -}}
            {{ dumpState("trigger.to_state", trigger.to_state) }}            
            {%- endif -%}
{% endraw %}            
```

## 7. List every possible entity and corresponding attributes

You can pick and choose which entity you want to get attributes by changing the domains list. For ex, to see camera related entries, just add `states.camera` to the list.

```
{% raw %}
{{ "_".ljust(90, "_") }}
{%- set domains = [states.light, states.switch, states.automation, states.device_tracker, states.group, states.media_player, states.proximity, states.script, states.zone, states.zwave, states.sensor, states.calendar ] %}
{{ "Entity ID".ljust(50) }}{{ "Entity Name" }}
{%- for domain in domains -%}
{% for item in domain %}
{{ "_".ljust(90, "_") }}
{{ item.entity_id.ljust(50) }}{{ item.name }}
{% for attrib in item.attributes %}
{%- if attrib is defined %}
  {{attrib.ljust(50)}}: {{ item.attributes[attrib] }}
{%- endif %}
{%- endfor %}
{%- endfor %}
{%- endfor %}
{% endraw %}
```

## 8. Find out which zwave device checked in at when

To find out when was the last time a zwave device has communicated with the controller, run the script below
```
{% raw %}
{%- macro zwave_check() -%}
{% for item in states.zwave %}
{%- set seconds = (((as_timestamp(now()) | int) - as_timestamp(strptime(item.attributes.receivedTS | string | truncate(19,True,'',0),'%Y-%m-%d %H:%M:%S:%f')) | int)) %}
{%- set minutes = (seconds /60) -%}
{%- set hours = (seconds /3600) -%}
{%- if seconds < 60 %}
{{ item.name.ljust(40) }} - {{ seconds }} seconds ago
{%- elif seconds > 60 and  seconds  <= 3600 %}
{{ item.name.ljust(40) }} - {{ '%0.2f' % minutes }} minutes ago
{%- elif seconds > 3600 %}
{{ item.name.ljust(40) }} - {{ '%0.2f' % (hours) }} hours ago
{%- endif %}
{%- endfor %}
{%- endmacro -%}
{% set output = zwave_check() %}
{% if output | trim == "" %}
No device has checked in the last 10 minutes.
{% else %}
Here are the devices that have checked in the last 10 minutes:
{{ output }}
{% endif %}
{% endraw %}
```

## 9. Word Wrapping long text into multiple lines:
To wrap text to a certain number of characters, use the following script:

```
{% raw %}
{% set long_text = "this is a long text. I mean it is a really really really long text. The code below should create multiple lines with each line length is limited to 32 characters." %}
{%- for item in (long_text | wordwrap(32, true, "|")).split("|") %}
{{item}}
{%- endfor %}
{% endraw %}
```

## 10. To get attrbutes of a given entity_id

Fun stuff...

```
{% raw %}
{% set entity_id = "automation.alarm_clock" %}

{{ entity_id }}

{{ states[entity_id.split('.')[0]] }}
{{ states[entity_id.split('.')[0]] | list }}
{{ states[entity_id.split('.')[0]][entity_id.split('.')[1]] }}

{{ (states[entity_id.split('.')[0]][entity_id.split('.')[1]]).attributes.friendly_name }}
{{ (states[entity_id.split('.')[0]][entity_id.split('.')[1]]).attributes["friendly_name"] }}
{% endraw %}
```

## 11. To get the current list of domains you use in your Home Assistant Setup, run the script below:

```
{% raw %}
{{ states | map(attribute='domain') |list | unique | list}}
{% endraw %}
```

The way the above script works is it iterates through all the entities, and retrieves the `domain` attribute of each of the entity, and makes it a list by removing duplicate items - by doing so, you will get unique list of domains that your Home Assistant uses :smile:

## 12. Automatic `Group` creator

Run the following script to automatically create groups sorted by the domain

```yaml
{% raw %}
{%- macro plural(name) -%}
  {%- if name[(name|length|int -1):] == "y" -%}
  {{- name[:-1] -}}ies
{%- else -%}
  {{- name -}}s
{%- endif -%}
{%- endmacro -%}

group:
{% for item in states | map(attribute='domain') |list | unique | list %}
  {{ plural(item) }}:
    entities:
  {%- for x in states if x.domain == item %}
      {{ x.entity_id }}
  {%- endfor %}
{% endfor %}
{% endraw %}
```

## 12. To sum up list of attribute values in a list

```
something like this will work: ```
{% raw %}
{% set people = [{'name':'john', 'experience':15}, {'name':'steve', 'experience':10}, {'name':'will', 'experience':12}, {'name':'tinkerer', 'experience':25}] %}
Combined experience: {{ people | sum(attribute='experience') }} years
{% endraw %}
```

It returns `Combined experience: 62 years`

Got any questions or found issues, let me know! Thanks!
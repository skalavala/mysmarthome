# Jinja code for Ninjas

There are two ways you can test the Jinja code:

<p>
1. Using Template editor in Home Assistant Web UI. You can do that by clicking on the hamburger icon on the top left of the page, under Developer Tools, Click on Templates icon. You will see a page with some code. You can delete that code and paste any jinja2 code there, it should render the output on thr right side of the page. 
</p>

<p>
2. Go to command line, and run inside python evvironment. Here is an example:
</p>

```
$ python3
>>> from jinja2 import Template

>>> s = "{% for element in elements %}{{loop.index}} {% endfor %}"
>>> Template(s).render(elements=["a", "b", "c", "d"])
1 2 3 4
>>>
>>> Template("{{ var }}").render(var=25)
'25'
>>>
>>> Template("{{ var }}").render(var="hello world!")
'hello world!'
>>>
```
## Basics of Jinja

### Basic String Manipulation
`{{ "hello this is a test" | upper }}` returns `HELLO THIS IS A TEST`

`{{ "HELLO THIS IS A TEST" | lower }}` returns `hello this is a test`

`{{ "hello this is a test" | capitalize }}` returns `Hello this is a test`

`{{ "hello this is a test" | title }}`  returns `Hello This Is A Test`

`{{ "Hello & World" | safe }}` returns `Hello & World`

`{{ "Hello & World" | escape }}` returns `Hello &amp; World`

`{{ "Hello & World" | length }}`  returns `13`

`{{ "Hello & World" | count }}`  returns `13`

`{{ " Hello & World " | trim}}` returns `Hello & World` by removing spaces before and after

`{{ ["a", "b", "c", "d", "e"] | random }}` returns a random element from the array

## Setting Variables

To have a varibale with a name `val` and with value `hello`, use the following:
```
{% set val = "hello" %}
```

### Loops and Loop Indexes

Iterate/Loop thru an array in reverse order
```
{% set values = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"] %}
{% for item in values %}
{{ values[loop.revindex] }}
{%- endfor %}
```
prints the following:
```
k
j
i
h
g
f
e
d
c
b
```
Other noteworthy loop properties you may want to know:
```
loop.index0 - zero based index of elements in a loop
loop.revindex - reverse indexing of loop with index starting at one
loop.revindex0 - reverse indenxing of loop with index starting at zero 
loop.first - to check if the current index in the loop is the first one
loop.last - to check if the current index in the loop is the last item
loop.length - loop length
```
### Maintaining state in a loop

The loops in Jinja are different from other programming languages, where you can't maintain state. For ex: you can define a variable, and if you try to increment, decrement or change the value in a loop, and after the loop, you will notice the value hasn't changed. Reason being, there is something called `scoping` in Jinja. You can read more about scoping on Jinja's official documentation, and if you are looking for a quick way to do this, you need to use `namespace`. With the namespace, you can create a scope and update the variable from within the loops.  Here is how you define a namespace with a variable in it, called `numberFiveFound` and you can set the default value by assigning directly as follows.

```
{% set ns = namespace(numberFiveFound=false) %}
```
You can then easily change the value from a loop and still able to access the updated value as follows:

```
{% set ns = namespace(numberFiveFound=false) %}
{% set numbers  = [1, 2, 3, 4, 5, 6, 7 ] %}
{% for number in numbers if number == 5 %}
  {% set ns.numberFiveFound = true %}
{% endfor %}
{{ ns.numberFiveFound }}
```

The above script loops through a bunch of numbers, and if it finds the number "5", it will set the value to true. The value can then be accessed even after the loop, and it prints the value of `True`.

If you do not use namespace and try to do the same thing using simple variables, it will not work - due to scoping issue. **The following code WILL NOT WORK :)**

```
{% set numberFiveFound = false %}
{% set numbers  = [1, 2, 3, 4, 5, 6, 7 ] %}
{% for number in numbers if number == 5 %}
  {% set numberFiveFound = true %}
{% endfor %}
{{ numberFiveFound }}
```
It will return `False` even though the number "5" exists in the loop.

## 1. To see which entities are exposed to your alexa platform, run the following script

The following entities are exposed to Alexa platform via `emulated_hue_hidden`:

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
```

### Here is the sample output of the above script:

```
    suresh_suresh_template:
      value_template: "{% if is_state('device_tracker.suresh_suresh', 'home') %}online{% else %}offline{% endif %}"
      friendly_name: "Suresh"
      icon_template: "{% if is_state('device_tracker.suresh_suresh', 'home') %}mdi:check-circle{% else %}mdi:alert-circle{% endif %}"

    srinika_srinika_template:
      value_template: "{% if is_state('device_tracker.srinika_srinika', 'home') %}online{% else %}offline{% endif %}"
      friendly_name: "Srinika"
      icon_template: "{% if is_state('device_tracker.srinika_srinika', 'home') %}mdi:check-circle{% else %}mdi:alert-circle{% endif %}"

    ...more entries!    
```

## 3. Group & Entities:

To see the list of `groups`,  and the entities that belong to the group, run this script

```
{% for group in states.group%}
Group Name: {{ group.name }}, Entity ID: {{ group.entity_id }}
{{ "-".ljust(50, '-') }} {{ "-".ljust(30, '-') }}
{% for entity in group.attributes.entity_id|list() %}
{{- entity }}
{% endfor %}
{% endfor %}
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
```

### Here is the output of the above script:

```
75.00 degrees of Fahrenheit is equal to: 23.89 Centigrade
23.89 degrees of Centigrade is equal to: 75.00 Fahrenheit
```

## 5.a Humidex Calculation
You can calculate the humidex based on Temperature and Relative Humidity using the following jinja macro

```
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
```

The output of that would be `24.455823489173447`.

## 6. Trigger Data in Automations

Ever wondered what trigger data is available for you when writing automations? Just copy the mqtt.publish service below 
and put it in **any** of your automation action section, and <b>it will dump all the attributes and information related to trigger, and state into your mqtt with a topic name "/dump/platform" </b>.

Pre-requisite is to have MQTT configured in your Home Assistant. Use tools like `mqttfx` to browse mqtt data.

Hope you find it useful!

```
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
```

### 6a. Here is another version of the same from [@dale3h](https://github.com/dale3h)

```
{%- for prop in trigger|sort if prop not in ['to_state', 'from_state'] -%}
  trigger.{{ prop }}: {{ trigger[prop] }}{{ '\n' }}
{%- endfor -%}

{%- for state in ['to_state', 'from_state'] if trigger[state] is defined -%}
  {{- '-' * 20 -}}{{ '\n' }}
  {%- for prop in ['state', 'entity_id', 'domain', 'object_id', 'name', 'last_updated', 'last_changed']|sort -%}
    trigger.{{ state }}.{{ prop }}: {{ trigger[state][prop] }}{{ '\n' }}
  {%- endfor -%}
  {%- for attr in trigger[state].attributes -%}
    trigger.{{ state }}.attributes.{{ attr }}: {{ trigger[state].attributes[attr] }}{{ '\n' }}
  {%- endfor -%}
{%- endfor -%}
```

## 7. List every possible entity and corresponding attributes

You can pick and choose which entity you want to get attributes by changing the domains list. For ex, to see camera related entries, just add `states.camera` to the list.

```
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
```

## 8. Find out which zwave device checked in at when

To find out when was the last time a zwave device has communicated with the controller, run the script below
```
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
```
### Here is the output of the above script:

```
Here are the devices that have checked in the last 10 minutes:

Aeotec Water Sensor                      - 8.82 minutes ago
Audio Detector                           - 8.82 minutes ago
Back Door Sensor                         - 8.82 minutes ago
Basement Door Sensor                     - 8.82 minutes ago
Downstairs Multi Sensor                  - 8.82 minutes ago
Energy Meter                             - 1.75 minutes ago
Front Door Sensor                        - 8.82 minutes ago
Front Room Multi Sensor                  - 3.87 minutes ago
Front Room Window Sensor                 - 8.82 minutes ago
Garage Door Sensor                       - 8.82 minutes ago
Guest Bedroom Multi Sensor               - 7.05 minutes ago
Kitchen Motion Sensor                    - 2.52 minutes ago
Kitchen Siren                            - 6.28 minutes ago
1-Car Garage Door Sensor                 - 8.82 minutes ago
Stairs Motion Sensor                     - 8.22 minutes ago
TV Multi Sensor                          - 5.83 minutes ago
2-Car Garage Door Sensor                 - 8.82 minutes ago
Upstairs Multi Sensor                    - 8.82 minutes ago
Wallmote                                 - 8.82 minutes ago
ZWave Repeater                           - 6.30 minutes ago
ZWave Smart Switch                       - 5.93 minutes ago
ZWave Stick                              - 8.82 minutes ago
```

## 9. Word Wrapping long text into multiple lines:
To wrap text to a certain number of characters, use the following script:

```
{% set long_text = "this is a long text. I mean it is a really really really long text. The code below should create multiple lines with each line length is limited to 32 characters." %}
{%- for item in (long_text | wordwrap(32, true, "|")).split("|") %}
{{item}}
{%- endfor %}
```

### Here is the output of the above script:
```
this is a long text. I mean it
is a really really really long
text. The code below should
create multiple lines with each
line length is limited to 32
characters.
```

## 10. To get attrbutes of a given entity_id

Fun stuff...

```
{% set entity_id = "automation.alarm_clock" %}

{{ entity_id }}

{{ states[entity_id.split('.')[0]] }}
{{ states[entity_id.split('.')[0]] | list }}
{{ states[entity_id.split('.')[0]][entity_id.split('.')[1]] }}

{{ (states[entity_id.split('.')[0]][entity_id.split('.')[1]]).attributes.friendly_name }}
{{ (states[entity_id.split('.')[0]][entity_id.split('.')[1]]).attributes["friendly_name"] }}
```

## 11. To get the current list of domains you use in your Home Assistant Setup, run the script below:

```
{{ states | map(attribute='domain') |list | unique | list}}
```

### Here is the sample output of the above script... you may see a different output based on the components that are being used
```
['alarm_control_panel', 'automation', 'binary_sensor', 'calendar', 'camera', 'climate', 'device_tracker', 'group', 'input_boolean', 'input_datetime', 'input_label', 'input_number', 'input_select', 'input_text', 'light', 'media_player', 'proximity', 'script', 'sensor', 'sun', 'switch', 'timer', 'zone', 'zwave']
```

The way the above script works is it iterates through all the entities, and retrieves the `domain` attribute of each of the entity, and makes it a list by removing duplicate items - by doing so, you will get unique list of domains that your Home Assistant uses :smile:

## 11a. To get the current list of domains and the number of entities in each domain:


```
{%- set unique_domains = states | map(attribute='domain') |list | unique | list -%}
[{%- for domain in unique_domains -%}
{%- if loop.first %}{% elif loop.last %}, and {% else %}, {% endif -%}
{%- for item in states[domain] -%}
{%- if loop.last %}{{domain}} ({{ loop.index}})
{%- endif -%}
{%- endfor -%}
{%- endfor -%}]
```

### Here is the output of the above script... you may see a different output based on the components that are being used
```
[alarm_control_panel (1), automation (176), binary_sensor (59), calendar (4), camera (7), climate (2), device_tracker (10), group (106), image_processing (8), input_boolean (42), input_datetime (8), input_label (32), input_number (3), input_select (6), input_text (1), light (8), lock (1), media_player (13), proximity (2), script (26), sensor (330), sun (1), switch (28), timer (9), zone (24), and zwave (24)]
```


## 12. Automatic `Group` creator

Run the following script to automatically create groups sorted by the domain

```yaml
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
```

## 13. To sum up list of attribute values in a list

```
something like this will wok: ```
{% set people = [{'name':'john', 'experience':15}, {'name':'steve', 'experience':10}, {'name':'will', 'experience':12}, {'name':'tinkerer', 'experience':25}] %}
Combined experience: {{ people | sum(attribute='experience') }} years
```

### The above script returns `Combined experience: 62 years`

## 14. To get list of attribute values as a string
```
{%set value_json = {
  "success": true,
  "tags": [
    {
      "tag": "Sea",
      "confidence": 0.6716686487197876
    },
    {
      "tag": "Coast",
      "confidence": 0.6598936915397644
    },
    {
      "tag": "Beach",
      "confidence": 0.4576399624347687
    },
    {
      "tag": "Shore",
      "confidence": 0.4436204433441162
    }
  ],
  "custom_tags": []
} %}

{%- set comma = joiner(', ') -%}
{%- for item in value_json.tags -%}
  {{- comma() -}}
  {{- item.tag -}}
{%- endfor %}

Or 

{{ value_json.tags|map(attribute='tag')|join(', ') }}

```
## 15. Convert a given "Number" to "Words"

```
{%- macro num2word(number) -%}
{%- set words = "" -%}
{%- set unitsMap = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ] -%}
{%- set tensMap = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"] -%}
{%- if number | int == 0 %}
  {% set words = " zero " %}
{%- endif -%}
{%- if number | int < 0 %}
  {% set words = " negative " + num2word(number|int * -1) %}
{%- endif -%}
{%- if ((number / 1000000000) | int > 0) %}
  {%- set words = words + num2word((number/1000000000) |int) + " billion " -%}
  {%- set number = (number%1000000000) |int -%}
{%- endif -%}
{%- if ((number / 1000000) | int > 0) %}
  {%- set words = words + num2word((number/1000000) |int) + " million " -%}
  {%- set number = (number%1000000) |int -%}
{%- endif -%}
{%- if ((number / 1000) | int > 0) %}
  {%- set words = words + num2word((number / 1000) |int) + " thousand " -%}
  {%- set number = (number%1000) |int -%}
{%- endif -%}
{%- if ((number / 100) | int > 0) %}
  {%- set words = words + num2word((number / 100) |int) + " hundred " -%}
  {%- set number = (number%100)|int -%}
{%- endif -%}
{%- if number | int > 0 -%}
  {%- if words != "" -%}
    {%- set words = words + "and " -%}
  {%- endif -%}
  {%- if number|int < 20 -%}
    {%- set words = words + unitsMap[number|int] -%}
  {%- else %}
    {%- set words = words + tensMap[(number/10)|int] -%}
    {%- if (number%10) | int > 0 %}
      {%- set words = words + "-" + unitsMap[(number%10)|int] -%}
    {%- endif -%}
  {%- endif -%}
{%- endif -%}
{{ words }}
{%- endmacro -%}

{{ num2word(-123456789) }}
```

The above returns `negative one hundred and twenty-three million four hundred and fifty-six thousand seven hundred and eighty-nine`.


## 16. Positive Subtraction using nines

The following code is written by [@dale3h](https://github.com/dale3h), I thought it would make perfect sense to keep it in here.

```
{%- macro nines(number) -%}
  {{ ('9' * number|string|length)|int - number|int }}
{%- endmacro -%}
```

The following is an example on how to use the nines macro:
```
873 - 218 = 655

{{ nines(nines(873)|int + 218)|int }}
```

## 17. List devices that are home, list lights that are ON, list anything in a group with a specific state
The following code lists all the entity friendly names in a group that has a specific state. Just change the group, and the desired state.

```
{{ dict((states|selectattr('entity_id', 'in', state_attr('group.all_devices', 'entity_id'))|list)|groupby('state'))['home']|map(attribute='name')|list|join(', ') }}
```

```
{{ dict((states|selectattr('entity_id', 'in', state_attr('group.all_lights', 'entity_id'))|list)|groupby('state'))['on']|map(attribute='name')|list|join(', ') }}
```

The same code can also be written in different ways:

```
{% set desired_group = 'group.all_lights' %}
{% set desired_state = 'on' %}

{%- for e in state_attr(desired_group, 'entity_id') if states[e.split('.')[0]][e.split('.')[1]].state == desired_state -%}
  {{ states[e.split('.')[0]][e.split('.')[1]].name }}
{% endfor -%}
```

Or

```
{{ states | selectattr('entity_id', 'in', state_attr('group.all_doors','entity_id')) | selectattr('state','in',['on','open']) | list | length >= 1 }}
{% set open_doors = {{ states | selectattr('entity_id', 'in', state_attr('group.all_doors','entity_id')) | selectattr('state','in',['on','open']) | list | map(attribute='name') |join(', ') }}
The following doors are open: {{ open_doors }}
```
## 18. Check Battery Levels of ALL devices using one script:

You can also use this in your automations to alert you when a specific device's battery level goes below certain threshold.
```
{%- for item in states -%}
{%- for attrib in item.attributes|sort() if 'battery' in attrib %}
{{ item.name }} Battery: {{ item.attributes[attrib] }}
{%- endfor -%}
{%- endfor -%}
```

The output should be something like:
```
Dining Room Motion Sensor Battery: 45.0
Front Room Motion Sensor Battery: 51.0
Family Room Motion Sensor (xiaomi) Battery: 47.0
Kitchen Motion Sensor Battery: 45.0
Aeotec Water Sensor Battery: 100
Audio Detector Battery: 100
Back Door Sensor Battery: 100
Basement Door Sensor Battery: 100
Downstairs Multi Sensor Battery: 100
Front Door Sensor Battery: 100
Front Room Multi Sensor Battery: 100
Front Room Window Sensor Battery: 89
Garage Door Sensor Battery: 100
Guest Bedroom Multi Sensor Battery: 0
Kitchen Motion Sensor Battery: 99
1-Car Garage Door Sensor Battery: 100
Stairs Motion Sensor Battery: 100
TV Multi Sensor Battery: 100
2-Car Garage Door Sensor Battery: 100
Upstairs Multi Sensor Battery: 49
Wallmote Battery: 100
```

## 19. Difference between Two Lists:

Assume you have two lists (before and after), and if you want to find out the difference between the lists, follow the code below:
In this case, the list one (before_list) has `Whiskey`, and in the list two (after_list), the `Whiskey` is removed and `Beer` is added. 

```
{% set before_list = ['Cup', 'Drink', 'Coffee cup', 'Coffee', 'Espresso', 'Caffeine', 'Latte', 'Whiskey'] %}
{% set after_list =  ['Cup', 'Drink', 'Coffee cup', 'Coffee', 'Espresso', 'Caffeine', 'Latte', 'Beer'] %}

{% macro ItemdAdded(beforeList, afterList) %}
  {%- for item in afterList if item != 'None' and item not in beforeList%}
	{%- if loop.first %}{% elif loop.last %} and{% else %},{% endif -%}
	  {{ item }}
  {%- endfor -%}
{%- endmacro -%}

{% macro ItemsRemoved(beforeList, afterList) %}
  {%- for item in beforeList if item != 'None' and item not in afterList %}
	{%- if loop.first %}{% elif loop.last %} and{% else %},{% endif -%}
	  {{ item }}
  {%- endfor -%}
{%- endmacro -%}

{%- macro list_diff(beforeList, afterList) -%}
  {%- set added = ItemdAdded(beforeList, afterList) -%}
  {%- set removed = ItemsRemoved(beforeList, afterList) -%}
  {% if added | trim != "" %}
Added: {{ added }}
  {%- endif -%}
  {% if removed | trim != "" %}
Removed: {{ removed |title }}
  {% endif %}
  {%- if removed == "" and added == "" -%}
    None.
  {%- endif -%}
{%- endmacro -%}

{{ list_diff(before_list, after_list) }}

```
The output should be something like:

```
Added: Beer
Removed: Whiskey
```
It will show `None.` when there are no changes between the lists. If you are wondering where you would need this script, imagine a scenario where you are feeding your camera image to a machine learning program (like machinebox/tagbox), and you get a list of tags in return. You can then use this script to check the differences between images by comparing tags. Item #14 is a sample output of tagbox for given image. You can use that code to generate list from a given JSON.

## 20. Concatenating Two Lists

```
{% set list1= [1, 2, 3] %}
{% set list2 = [4, 5, 6] %}
{%- for item in list1|list + list2|list %}
{{ item }}
{%- endfor -%}
```

The output would be 
```
1
2
3
4
5
6
```

## 21. Date Format - using "st", "nd", "rd", "th"

If you want the date to be more readable for display, you can use the script below. It formats the date in the format of `1st October 2018` or `2nd September 2018` or `3rd September 2018` or `16th September 2018`.

```
{%- macro get_date(dt) %}
  {%- set date_suffix = ["th", "st", "nd", "rd"] -%}
  {{ dt.day }}
  {%- if dt.day % 10 in [1, 2, 3] and dt.day not in [11, 12, 13] -%}
    {{ date_suffix[dt.day%10] }}
  {%- else -%}
    {{ date_suffix[0] }}
  {%- endif %} {{ dt.strftime("%B %Y")}}
{%- endmacro -%}

{{ get_date(now()) }}
```

Feel free to modify the `strftime` format that fits your need. You can also pass your sensor value - ex: `{{ get_date(states.sensor.mysensor.last_updated) }}`.


## 22. BANNER/ASCII Text Command in Jinja

Ever wondered how you can create ASCII Text using Jinja? I wrote this code while teaching programming to my kids, and I thought I'd add it to my jinja collection. If you are familiar with the `banner` command in unix/linux, this is very similar!

```
{{- '{author: skalavala}' -}}
{%- set alphabets = "   #     # #   #   # #     #########     ##     ####### #     ##     ####### #     ##     #######  ##### #     ##      #      #      #     # ##### ###### #     ##     ##     ##     ##     ####### ########      #      #####  #      #      ###############      #      #####  #      #      #       ##### #     ##      #  #####     ##     # ##### #     ##     ##     #########     ##     ##     #  ###     #      #      #      #      #     ###        #      #      #      ##     ##     # ##### #    # #   #  #  #   ###    #  #   #   #  #    # #      #      #      #      #      #      ########     ###   ### # # ##  #  ##     ##     ##     ##     ###    ## #   ##  #  ##   # ##    ###     #########     ##     ##     ##     ##     ############## #     ##     ####### #      #      #       ##### #     ##     ##     ##   # ##    #  #### ####### #     ##     ####### #   #  #    # #     # ##### #     ##       #####       ##     # ##### #######   #      #      #      #      #      #   #     ##     ##     ##     ##     ##     # ##### #     ##     ##     ##     # #   #   # #     #   #     ##  #  ##  #  ##  #  ##  #  ##  #  # ## ## #     # #   #   # #     #     # #   #   # #     ##     # #   #   # #     #      #      #      #   #######     #     #     #     #     #     #######" -%}

{% macro print_horizontal(name) -%}
{% for row in range(7) %}
{%- set outer_loop = loop %}
{%- for alphabet in name |list -%}
{%- set startIndex = "abcdefghijklmnopqrstuvwxyz".find(alphabet|lower) * 49 %}
{%- set begin = startIndex + outer_loop.index0*7 -%}{%- set end = begin+7 -%}
{{ alphabets[begin:end]|replace('#', '#')|replace(' ',' ') }} {% endfor %}
{% endfor %}
{% endmacro %}

{% macro print_vertical(name) -%}
{%- for alphabet in name |list -%}
{% set startIndex = "abcdefghijklmnopqrstuvwxyz".find(alphabet|lower) * 49 %}
{%- for row in range(7) %}
{%- set begin = startIndex +loop.index0*7 -%}{%- set end = begin+7 %}
{{ alphabets[begin:end]|replace('#', '#')|replace(' ',' ') -}}
{%- endfor %}
{% endfor %}
{%- endmacro %}

{%- set banner = "skalavala" -%}
{{ print_horizontal(banner) }}
```

The above code outputs:

```
 #####  #    #     #    #          #    #     #    #    #          #    
#     # #   #     # #   #         # #   #     #   # #   #         # #   
#       #  #     #   #  #        #   #  #     #  #   #  #        #   #  
 #####  ###     #     # #       #     # #     # #     # #       #     # 
      # #  #    ####### #       #######  #   #  ####### #       ####### 
#     # #   #   #     # #       #     #   # #   #     # #       #     # 
 #####  #    #  #     # ####### #     #    #    #     # ####### #     #
```

You can also print vertical text by calling `{{ print_vertical() }}`

### How does this code work?

The `alphabets` variable holds a long string of characters that represent all alphabets (a to z). Each alphabet is a 7x7 size fixed text, straightned. That means each letter is about 49 characters in length, which renders to 7x7 glyph. For each letter within the banner string, it gets the index within the alphabet string, and prints that 7x7 in either horizontal or vertical fashion. You can go and try to understand the code now ;)

### How can I change from `#` with other characters like `*`?

Very simple, just replace the command in the code:  
from `{{ alphabets[begin:end]|replace('#', '#')|replace(' ',' ') -}}` 
to   `{{ alphabets[begin:end]|replace('#', '*')|replace(' ',' ') -}}`

### How do I add more characters?

You can add other characters or numbers by simply appending to the existing `alphabets` string. For ex: If you want to add an empty space, just append 49 empty spaces and add a space to the `abcdefghijklmnopqrstuvwxyz` string for index/lookup.

```
####### #     #       # ####### #     # 
#       ##    #       # #     #  #   #  
#       # #   #       # #     #   # #   
#####   #  #  #       # #     #    #    
#       #   # # #     # #     #    #    
#       #    ## #     # #     #    #    
####### #     #  #####  #######    #
```

## 23. Parsing ImageProcessing JSON data and making sense for your automations

When you have an image_processing component in your setup, chances are it gives you the following JSON based on the camera feed. Often times people wonder how they can retrive relevant information from the JSON into a variable or a sensor to use in automations. The following JSON is a sample from image_processing component.

```
{% set value_json = 
{
	'car': [{
		'score': 99.01034832000732,
		'box': [0.14889374375343323, 0.21685060858726501, 0.23301419615745544, 0.3547678291797638]
	}, {
		'score': 98.71577620506287,
		'box': [0.14932020008563995, 0.3567427694797516, 0.22214098274707794, 0.4808700978755951]
	}]
}
%}
```

The following code shows all the tags that are found in the JSON that have the box size more than 0.5 in a much more readable fashion. This is a sample code I wrote for [@arsaboo](https://github.com/arsaboo)

```
{%- set camera = 'driveway' -%}
{%- set tags = value_json.keys()|list -%}

{%- macro get_list(obj) -%}
{%- for x in value_json[obj]|list if x.box[0]  > 0.05 -%}
{%- if loop.first %}{% elif loop.last %},{% else %},{% endif -%}{{ obj }} 
{%- endfor -%}{%- endmacro -%}

{%- macro run() -%}
{%- for object in tags -%}
{%- if loop.first %}{% elif loop.last %}, {% else %}, {% endif -%}{{ obj }} 
{{- get_list(object).split(',')|list|unique|list|join|title }}
{%- endfor -%}
{% endmacro -%}

{%- set output = run() -%}
{{- output ~ ' detected in ' ~ camera if output != '' -}}
```

The output is something like the folowing, that can used to announce using TTS or even send a text message to your cell phone. 

```
Car detected in Backyard
```

## 24 English to Morse Code Conversion

For those ham radio buffs out there, here is a way you can convert english to morse code. 

```
{% set input = "hello morse" %}
{% set morse = ".-   -... -.-. -..  .    ..-. --.  .... ..   .--- -.-  .-.. --   -.   ---  .--. --.- .-.  ...  -    ..-  ...- .--  -..- -.-- --.. -----.----..---...--....-.....-....--...---..----." %}
{%- for x in input.replace(' ', '/')|list %}
{%- set start = "abcdefghijklmnopqrstuvwxyz0123456789".find(x|lower) * 5  %}
{{- morse[start:start+5]|trim ~ ' ' if start >= 0 else '/' -}}
{%- endfor %}
```

This gives you the following output

```
.... . .-.. .-.. --- /-- --- .-. ... .
```

Compare the output with [Morse code translator here](https://morsecode.scphillips.com/translator.html)

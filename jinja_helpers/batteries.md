If you are using OwnTracks and have ZWave Devices, use the following script to create battery card:

1. Copy `input_label.yaml` and `services.yaml` from my `custom_components` folder into your `custom_components` folder.

2. Run the following script in your dev-templates editor, and copy the output and paste the output into `batteries.yaml` file

3. Copy and paste the below automations code **as-is** in your `batteries.yaml` file.

4. Restart HA

```

input_label:
{%- for state in states.zwave if state.attributes.battery_level | trim != "" %}
  {{ state.entity_id.split('.')[1] }}:
{%- endfor %}

{% for state in states.device_tracker if '_' in state.entity_id.split('.')[1] %}
  {{ state.entity_id.split('.')[1].split('_')[0] }}_battery:
  {{ state.entity_id.split('.')[1].split('_')[0] }}_wifi:
{%- endfor %}

group:
  ZWave Batteries:
    entities:
{%- for state in states.zwave %}
      - input_label.{{ state.entity_id.split('.')[1] }}
{%- endfor %}

  Phone Batteries:
    entities:
{%- for state in states.device_tracker if '_' in state.entity_id.split('.')[1] %}
      - {{ state.entity_id.split('.')[1].split('_')[0] }}_battery
{%- endfor %}

  Phone WiFi:
    entities:
{%- for state in states.device_tracker if '_' in state.entity_id.split('.')[1] %}
      - {{ state.entity_id.split('.')[1].split('_')[0] }}_wifi
{%- endfor %}

```

Copy the following automations as-is in your `batteries.yaml` file:

```

automation:
  - alias: Update ZWave Battery Levels
    trigger:
      - platform: event
        event_type: state_changed
    condition:
      - condition: template
        value_template: "{{ trigger.event.data.entity_id is not none }}"
      - condition: template
        value_template: "{{ trigger.event.data.entity_id.split('.')[0] == 'zwave' }}"
      - condition: template
        value_template: "{{ trigger.event.data.new_state.attributes is not none }}"
      - condition: template
        value_template: "{{ trigger.event.data.new_state.attributes.battery_level | trim != '' }}"
      - condition: template
        value_template: "{{ trigger.event.data.new_state.attributes.battery_level | default(999) | int != 999 }}"
    action:
      - service: input_label.set_value
        data_template:
          entity_id: "input_label.{{- trigger.event.data.entity_id.split('.')[1] -}}"
          value: "{{ trigger.event.data.new_state.attributes.battery_level }}"
      - service: input_label.set_name
        data_template:
          entity_id: "input_label.{{- trigger.event.data.entity_id.split('.')[1] -}}"
          value: "{{ trigger.event.data.new_state.attributes.friendly_name }}'s Battery"
      - service: input_label.set_icon
        data_template:
          entity_id: "input_label.{{- trigger.event.data.entity_id.split('.')[1] -}}"
          value: >
            {% set battery_level = trigger.event.data.new_state.attributes.battery_level | int %}
            {% set battery_round = (battery_level / 10)|int * 10 %}
            {% if battery_round >= 100 %}
              mdi:battery
            {% elif battery_round > 0 %}
              mdi:battery-{{ battery_round }}
            {% else %}
              mdi:battery-alert
            {% endif %}

  - alias: Update Phone Battery Levels
    initial_state: true
    trigger:
      platform: mqtt
      topic: "owntracks/+/+"
    action:
      - service: input_label.set_value
        data_template:
          entity_id: "input_label.{{trigger.topic.split('/')[-1]}}_wifi"
          value: "{{ 'Yes' if trigger.payload_json.conn == 'w' else 'No' }}"
      - service: input_label.set_icon
        data_template:
          entity_id: "input_label.{{trigger.topic.split('/')[-1]}}_wifi"
          value: "{{ 'mdi:wifi' if trigger.payload_json.conn == 'w' else 'mdi:wifi-off' }}"
      - service: input_label.set_name
        data_template:
          entity_id: "input_label.{{trigger.topic.split('/')[-1]}}_wifi"
          value: "{{trigger.topic.split('/')[-1] | title }}'s phone wifi enabled?"
          
      - service: input_label.set_value
        data_template:
          entity_id: "input_label.{{trigger.topic.split('/')[-1]}}_battery"
          value: '{{ trigger.payload_json.batt | int }}'
      - service: input_label.set_name
        data_template:
          entity_id: "input_label.{{trigger.topic.split('/')[-1]}}_battery"
          value: "{{trigger.topic.split('/')[-1] | title }}'s Battery"
      - service: input_label.set_icon
        data_template:
          entity_id: "input_label.{{trigger.topic.split('/')[-1]}}_battery"
          value: >
              {% set battery_level = trigger.payload_json.batt | int %}
              {% set battery_round = (battery_level / 10)|int * 10 %}
              {% if trigger.payload_json.charging == 1 %}
                {% if battery_round >= 100 %}
                  mdi:battery-charging-100
                {% elif battery_round > 0 %}
                  mdi:battery-charging-{{ battery_round }}
                {% else %}
                  mdi:battery-alert
                {% endif %}
              {% else %}
                {% if battery_round >= 100 %}
                  mdi:battery
                {% elif battery_round > 0 %}
                  mdi:battery-{{ battery_round }}
                {% else %}
                  mdi:battery-alert
                {% endif %}
              {% endif %}
```

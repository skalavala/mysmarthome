""" 
Author      : Suresh Kalavala
Date        : 02/09/2017
Description : Returns the appripriate icon for the entity
File        : batteries.py - python_script for batteries
"""
def get_icon(bat_level):
    icon = "mdi-unknown"
    battery_round = round(int(bat_level)/10)*10
    if battery_round >= 100:
        icon = "mdi:battery"
    elif battery_round > 0:
        icon = "mdi:battery-{}".format(str(battery_round))
    else:
        icon = "mdi:battery-alert"
    return icon

try:
    attribs = {}
    entity_id = data.get('entity_id')
    battery_value = data.get('battery_value', 0)

    attribs["icon"] = get_icon(battery_value)
    attribs["unit_of_measurement"] = "%"
    attribs["friendly_name"] = entity_id.split('.')[1].replace("_", " ").title() + "'s Battery"

    hass.states.set(entity_id, battery_value, attributes=attribs)
except Exception as ex:
    logger.error(str(ex))

"""
  - alias: Update ZWave Battery Levels
    initial_state: true
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
      - service: python_script.batteries
        data_template:
          entity_id: "input_label.{{- trigger.event.data.entity_id.split('.')[1] -}}"
          battery_value: '{{ trigger.event.data.new_state.attributes.battery_level }}'
"""    
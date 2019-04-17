## Auomatically hide/show media players based on their state. If the media player is ON, it will be visible, otherwise it will be hidden from the view... you can also modify to check its status and show only if it is playing...etc


```
#########################################################################
# Author: Suresh Kalavala
# Date: 1/11/2018
#########################################################################

homeassistant:
  customize:
{%- for item in states.media_player %}
    {{ item.entity_id }}:
      hidden: true
{%- endfor %}

# Create Groups
group:
{%- for item in states.media_player %}
  group_{{ item.entity_id.split('.')[1] }}:
    entities:
      - {{ item.entity_id }}
{%- endfor %}

# Shows the media player if it is on, else hides it
####################################################
automation:
  - alias: Set Media Player Visibility
    trigger:
      platform: state
      entity_id: 
{%- for item in states.media_player %}
        - group.group_{{ item.entity_id.split('.')[1] }}
{%- endfor %}
    action:
      service: group.set_visibility
      data_template:
        entity_id: '{{- '{{' }} "group_" ~ trigger.entity_id.split(".")[1] {{ '}}' }}'
        visible: '{{- '{{' }} trigger.to_state.state | lower == "on" {{ '}}' }}'
```

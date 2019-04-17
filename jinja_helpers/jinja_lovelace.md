# Lovelace Cards Using Jinja2 Scripting

## 1. This script auto generates Lovelace Entity Cards

```
{# @Author: Mahasri Kalavala (a.k.a @skalavala #}

{%- macro plural(name) -%}
  {%- if name[(name|length|int -1):] == "y" -%}
  {{- name[:-1] -}}ies
{%- else -%}
  {{- name -}}s
{%- endif -%}
{%- endmacro -%}

title: My Lovely Home Automation
views:
  - title: Home
    cards:
{%- set domains = states | map(attribute='domain') |list | unique | list %}
{%- for item in states['camera'] %}
      - type: picture-entity
        title: {{ item.name }}
        entity: {{ item.entity_id }}
        camera_image: {{ item.entity_id }}
        show_info: true
        tap_action: dialog
{% endfor %}
{%- for item in states['media_player'] %}
      - type: media-control
        entity: {{ item.entity_id }}
{% endfor %}
{%- for item in domains if item != "camera" and item != "media_player" %}
      - type: {% if item == "device_tracker" -%}
        entity-filter
        {%- elif item == "camera" -%}
        picture-entity
        {%- else -%}
          entities
        {%- endif %}
{%- if states[item]|list |length|default(0)|int > 1 %}
        title: {{ plural(item.replace('_', ' ') | title)  }}
{%- else %}
        title: {{ item.replace('_', ' ') | title }}
{%- endif %}
        show_header_toggle: true
        entities:
{%- for e in states[item] %}
          - {{ e.entity_id }}
{%- endfor %}
{%- if item == "device_tracker" %}
        state_filter:
          - 'home'
        card:
          type: glance
          title: My Device Trackers
{% endif %}
{% endfor -%}
```

The output of the above script would look like the following:

```
# This script auto generates Lovelace Entity Cards

- type: entities
  title: Alarm Control Panel
  show_header_toggle: true
  entities:
    - alarm_control_panel.simplisafe
      name: Home Security System

- type: entities
  title: Sun
  show_header_toggle: true
  entities:
    - sun.sun
      name: Sun
      
- type: entities
  title: Proximity
  show_header_toggle: true
  entities:
    - proximity.home
      name: home
    - proximity.work
      name: work

...
```

## 2. This script auto generates Lovelace Entity-Filter Card for your Device Trackers

```
{% for item in states['device_tracker'] -%}
- type: entity-filter
  state_filter:
    - 'home'
  card:
    type: glance
    title: My Device Trackers
  entities:
{%- for e in states[item] %}
    - {{ e.entity_id }}
{%- endfor %}
{% endfor %}
```
The output of above would look something like:

```
- type: entity-filter
  state_filter:
    - 'home'
  card:
    type: glance
    title: My Device Trackers
  entities:
    - device_tracker.hasika_hasika
    - device_tracker.ipad
    - device_tracker.mallika_mallika
    - device_tracker.srinika_srinika
    - device_tracker.suresh_suresh
    - device_tracker.tesla_model_3_5yj3e1ea8jf010610_location_tracker
```

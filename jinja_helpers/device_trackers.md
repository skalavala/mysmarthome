# Device Trackers

## To create the device tracker code automatically for you, run this script in `dev-templates` page, copy the output and paste it in `device_tracker.yaml` file under packages folder.

```
{% set domain = states.device_tracker %}

homeassistant:
  customize:
{% for state in domain %} 
    {{ state.entity_id }}: 
      friendly_name: '{{ state.attributes.friendly_name if state.attributes.friendly_name is defined else state.attributes.friendly_name.replace("_", " ") |title }}'
      {{ 'icon: '+ state.attributes.icon if state.attributes.icon is defined }}
      emulated_hue_hidden: {{state.attributes.emulated_hue if state.attributes.emulated_hue is defined else 'False' }} 
      hidden: {{state.attributes.hidden if state.attributes.hidden is defined else "False"}}
{% endfor -%}

{{" "}}
sensor:
  - platform: template
    sensors:
{% for state in states.device_tracker -%}
  {% if loop.first %}{% elif loop.last %}
{% else %}
{% endif %}      {{state.entity_id|replace("device_tracker.","") -}}_template:
        value_template: {{ '"{% if is_state' }}('{{-state.entity_id -}}', 'home') {{'%}online{% else %}offline{% endif %}"'}}
        friendly_name: "{{ state.attributes.friendly_name|title|replace("_"," ",) if state.attributes.friendly_name is defined else state.name|title|replace("_"," ",) }}"
        icon_template: {{ '"{% if is_state' }}('{{-state.entity_id -}}', 'home') {{'%}mdi:check-circle{% else %}mdi:alert-circle{% endif %}"'}}
{% endfor %}

{{" "}}
group:
  {{ (domain|list)[0].entity_id.split('.')[0].replace('_', ' ') |title}}:
    entities:
{%- for state in domain %} 
      - {{ state.entity_id }}
{%- endfor %}
```

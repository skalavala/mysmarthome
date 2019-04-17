```
###############################################################################
#   @author         :   Mahasri Kalavala
#   @date           :   {{ now().month  ~ '/' ~ now().day ~ '/' ~ now().year }}
#   @package        :   Cameras
#   @description    :   Cameras, Cameras, and Cameras!
###############################################################################
homeassistant:
  customize:

    ################################################
    ## Node Anchors
    ################################################

    package.node_anchors:
      customize: &customize
        package: 'cameras'

      exposed: &exposed
        <<: *customize
        emulated_hue_hidden: true
        homebridge_hidden: false

      not_exposed: &not_exposed
        <<: *customize
        emulated_hue_hidden: false
        homebridge_hidden: true

      hidden: &hidden
        <<: *customize
        hidden: true

# friendly names
{% for item in states.binary_sensor if 'camera' in item.entity_id %}
{%- if loop.first %}{% elif loop.last %}{% else %}{% endif %}
    {{ item.entity_id }}:
      friendly_name: {{ item.entity_id.split('.')[1].replace('_', ' ')|title}}
{% endfor %}

group:
  Frontyard Cameras:
    entities:
      - camera.frontdoor_camera
      - camera.driveway_camera

  Backyard Cameras:
    entities:
      - camera.patio_camera
      - camera.playarea_camera

  Camera Motion:
{% for item in states.binary_sensor if 'camera_motion' in item.entity_id %}
{%- if loop.first %}    entities:{% elif loop.last %}{% else %}{% endif %}
      - {{ item.entity_id }}{% endfor %}

  Camera Field Detection:
{% for item in states.binary_sensor if '_field_detection' in item.entity_id %}
{%- if loop.first %}    entities:{% elif loop.last %}{% else %}{% endif %}
      - {{ item.entity_id }}{% endfor %}

  Camera Line Crossing:
{% for item in states.binary_sensor if '_line_crossing' in item.entity_id %}
{%- if loop.first %}    entities:{% elif loop.last %}{% else %}{% endif %}
      - {{ item.entity_id }}{% endfor %}

  Camera Tamper Detection:
{% for item in states.binary_sensor if '_tamper_detection' in item.entity_id %}
{%- if loop.first %}    entities:{% elif loop.last %}{% else %}{% endif %}
      - {{ item.entity_id }}{% endfor %}

# camera platforms
camera:
{% for item in states.camera if 'doppler' not in item.entity_id and 'usps' not in item.entity_id %}
{%- if loop.first %}  entities:{% elif loop.last %}{% else %}{% endif %}
    - platform: generic
      name: {{ item.entity_id.split('.')[1].split('_')[0] | title}} Camera
      still_image_url: !secret {{ item.entity_id.split('.')[1].split('_')[0]}}_camera_url
{% endfor %}

# binary sensors
binary_sensor:
{% for item in states.camera if 'doppler' not in item.entity_id and 'usps' not in item.entity_id %}
{%- if loop.first %}{% elif loop.last %}{% else %}{% endif %}
    - platform: hikvision
      name: {{ item.entity_id.split('.')[1].split('_')[0] | title}} Camera
      host: !secret {{ item.entity_id.split('.')[1].split('_')[0]}}_camera_ip
      username: !secret camera_username
      password: !secret camera_password
{% endfor %}
```
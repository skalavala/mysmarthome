"""
{"entity_id":"light.hue_color_lamp_2", "rgb_color": [254, 0, 0] }
"""

entity_id = data.get('entity_id')
rgb_color = data.get('rgb_color', [255, 255, 255])
if entity_id is not None:
    service_data = {"entity_id": entity_id, "rgb_color": rgb_color, "brightness": 255 }
    hass.services.call("light", "turn_on", service_data, False)
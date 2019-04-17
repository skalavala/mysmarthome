home = 0
for entity_id in hass.states.entity_ids('device_tracker'):
    state = hass.states.get(entity_id)
    if state.state == 'home':
        home = home + 1

hass.states.set('sensor.people_home', home, {
    'unit_of_measurement': 'people',
    'friendly_name': 'People home'
})
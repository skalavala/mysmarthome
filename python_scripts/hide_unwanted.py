'''
@Author         :       Mahasri Kalavala
@Date           :       08/27/2017
@Description    :       This python script hides all the sensors that are Online, so that 
                        ONLY the Offline sensors are visible in the UI
'''
for entity_id in hass.states.entity_ids('sensor'):
    entity_state_object = hass.states.get(entity_id)
    attributes = entity_state_object.attributes.copy()

    """ Hide all the entities that have 'Online' Status """
    if entity_state_object.state == 'Online':
        attributes['hidden'] = True
    else:
        attributes['hidden'] = False

    hass.states.set(entity_id, entity_state_object.state, attributes=attributes)

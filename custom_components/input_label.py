"""
@ Author      : Suresh Kalavala
@ Date        : 09/14/2017
@ Description : Input Label  - A label that holds data

@ Notes:        Copy this file and services.yaml files and place it in your 
                "Home Assistant Config folder\custom_components\" folder

                To use the component, have the following in your .yaml file:
                The 'value' is optional, by default, it is set to 0 

input_label:
  some_string1:
    name: Some String 1 
    icon: mdi:alphabetical

  input_label:
    name: Some String 2
    value: 'Hello, Home Assistant!'
    icon: mdi:alphabetical

"""
"""
Component to provide input_label.

For more details about this component, please contact Suresh Kalavala
"""
import logging

import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.const import (ATTR_ENTITY_ID, CONF_ICON, CONF_NAME)
from homeassistant.helpers.entity_component import EntityComponent
from homeassistant.helpers.restore_state import RestoreEntity

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'input_label'
ENTITY_ID_FORMAT = DOMAIN + '.{}'

CONF_INITIAL = 'initial'
ATTR_VALUE   = "value"
DEFAULT_ICON = "mdi:label"

SERVICE_SETNAME  = 'set_name'
SERVICE_SETVALUE = 'set_value'
SERVICE_SETICON  = 'set_icon'

SERVICE_SCHEMA = vol.Schema({
    vol.Optional(ATTR_ENTITY_ID): cv.entity_ids,
    vol.Optional(ATTR_VALUE): cv.string,
    vol.Optional(CONF_NAME): cv.icon,
    vol.Optional(CONF_ICON): cv.icon,
})

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        cv.slug: vol.Any({
            vol.Optional(CONF_ICON, default=DEFAULT_ICON): cv.icon,
            vol.Optional(ATTR_VALUE, ''): cv.string,
            vol.Optional(CONF_NAME): cv.string,
        }, None)
    })
}, extra=vol.ALLOW_EXTRA)

async def async_setup(hass, config):
    """Set up a input_label."""
    component = EntityComponent(_LOGGER, DOMAIN, hass)

    entities = []

    for object_id, cfg in config[DOMAIN].items():
        if not cfg:
            cfg = {}
        name = cfg.get(CONF_NAME)
        initial = cfg.get(ATTR_VALUE)
        icon = cfg.get(CONF_ICON)

        entities.append(InputLabel(object_id, name, initial, icon))

    if not entities:
        return False

    component.async_register_entity_service(
        SERVICE_SETNAME, SERVICE_SCHEMA,
        'async_set_name'
    )

    component.async_register_entity_service(
        SERVICE_SETVALUE, SERVICE_SCHEMA,
        'async_set_value'
    )

    component.async_register_entity_service(
        SERVICE_SETICON, SERVICE_SCHEMA,
        'async_set_icon'
    )

    await component.async_add_entities(entities)
    return True

class InputLabel(RestoreEntity):
    """Representation of a input_label."""

    def __init__(self, object_id, name, initial, icon):
        """Initialize a input_label."""
        self.entity_id = ENTITY_ID_FORMAT.format(object_id)
        self._name = name
        self._current_value = initial
        self._icon = icon
 
    @property
    def should_poll(self):
        """If entity should be polled."""
        return False

    @property
    def name(self):
        """Return name of the input_label."""
        return self._name

    @property
    def icon(self):
        """Return the icon to be used for this entity."""
        return self._icon

    @property
    def state(self):
        """Return the current value of the input_label."""
        return self._current_value

    @property
    def state_attributes(self):
        """Return the state attributes."""
        return {
            ATTR_VALUE: self._current_value,
        }

    async def async_added_to_hass(self):
        """Run when entity about to be added to hass."""

        await super().async_added_to_hass()
        if self._current_value is not None:
            return

        state = await self.async_get_last_state()
        value = state and state.state
        self._current_value = value

    async def async_set_name(self, value):
        self._name = value
        await self.async_update_ha_state()

    async def async_set_icon(self, value):
        self._icon = value
        await self.async_update_ha_state()

    async def async_set_value(self, value):
        self._current_value = value
        await self.async_update_ha_state()

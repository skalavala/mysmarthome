name = data.get('name', 'world')
logger.info("Hello {}".format(name))
hass.bus.fire(name, { "wow": "from a Python script!" })

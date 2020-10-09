"""Constants for localtuya integration."""

ATTR_CURRENT = "current"
ATTR_CURRENT_CONSUMPTION = "current_consumption"
ATTR_VOLTAGE = "voltage"

CONF_LOCAL_KEY = "local_key"
CONF_PROTOCOL_VERSION = "protocol_version"
CONF_DPS_STRINGS = "dps_strings"

# switch
CONF_CURRENT = "current"
CONF_CURRENT_CONSUMPTION = "current_consumption"
CONF_VOLTAGE = "voltage"

# cover
CONF_OPENCLOSE_CMDS = "open_close_cmds"
CONF_POSITIONING_MODE = "positioning_mode"
CONF_CURRENT_POSITION_DP = "current_position_dp"
CONF_SET_POSITION_DP = "set_position_dp"
CONF_SPAN_TIME = "span_time"

# sensor
CONF_SCALING = "scaling"

# climate
CONF_TARGET_TEMPERATURE_DP = "target_temperature_dp"
CONF_CURRENT_TEMPERATURE_DP = "current_temperature_dp"
CONF_MAX_TEMP_DP = "max_temperature_dp"
CONF_MIN_TEMP_DP = "min_temperature_dp"
CONF_FAN_MODE_DP = "fan_mode_dp"
CONF_HVAC_MODE_DP = "hvac_mode_dp"
CONF_PRECISION = "precision"
CONF_CELSIUS = "celsius"
CONF_FAHRENHEIT = "fahrenheit"

DOMAIN = "localtuya"

# Platforms in this list must support config flows
PLATFORMS = ["binary_sensor", "climate", "cover", "fan", "light", "sensor", "switch"]

TUYA_DEVICE = "tuya_device"

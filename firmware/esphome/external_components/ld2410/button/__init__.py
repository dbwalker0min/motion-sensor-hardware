import esphome.codegen as cg
from esphome.components import button
import esphome.config_validation as cv
from esphome.const import (
    CONF_FACTORY_RESET,
    CONF_RESTART,
    DEVICE_CLASS_RESTART,
    ENTITY_CATEGORY_CONFIG,
    ENTITY_CATEGORY_DIAGNOSTIC,
    ICON_DATABASE,
    ICON_RESTART,
    ICON_RESTART_ALERT,
)

from .. import CONF_LD2410_ID, LD2410Component, ld2410_ns

FactoryResetButton = ld2410_ns.class_("FactoryResetButton", button.Button)
QueryButton = ld2410_ns.class_("QueryButton", button.Button)
RestartButton = ld2410_ns.class_("RestartButton", button.Button)
AutocalibrateButton = ld2410_ns.class_("AutocalibrateButton", button.Button)

ICON_PLAY_CIRCLE = "mdi:play-circle"

CONF_QUERY_PARAMS = "query_params"
CONF_AUTOCALIBRATE = "autocalibrate"

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_LD2410_ID): cv.use_id(LD2410Component),
    cv.Optional(CONF_FACTORY_RESET): button.button_schema(
        FactoryResetButton,
        device_class=DEVICE_CLASS_RESTART,
        entity_category=ENTITY_CATEGORY_CONFIG,
        icon=ICON_RESTART_ALERT,
    ),
    cv.Optional(CONF_RESTART): button.button_schema(
        RestartButton,
        device_class=DEVICE_CLASS_RESTART,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        icon=ICON_RESTART,
    ),
    cv.Optional(CONF_QUERY_PARAMS): button.button_schema(
        QueryButton,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        icon=ICON_DATABASE,
    ),
    cv.Optional(CONF_AUTOCALIBRATE): button.button_schema(
        AutocalibrateButton,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        icon=ICON_PLAY_CIRCLE,
    ),
}


async def to_code(config):
    ld2410_component = await cg.get_variable(config[CONF_LD2410_ID])
    if factory_reset_config := config.get(CONF_FACTORY_RESET):
        b = await button.new_button(factory_reset_config)
        await cg.register_parented(b, config[CONF_LD2410_ID])
        cg.add(ld2410_component.set_factory_reset_button(b))
    if restart_config := config.get(CONF_RESTART):
        b = await button.new_button(restart_config)
        await cg.register_parented(b, config[CONF_LD2410_ID])
        cg.add(ld2410_component.set_restart_button(b))
    if query_params_config := config.get(CONF_QUERY_PARAMS):
        b = await button.new_button(query_params_config)
        await cg.register_parented(b, config[CONF_LD2410_ID])
        cg.add(ld2410_component.set_query_button(b))
    if autocalibrate_config := config.get(CONF_AUTOCALIBRATE):
        b = await button.new_button(autocalibrate_config)
        await cg.register_parented(b, config[CONF_LD2410_ID])
        cg.add(ld2410_component.set_autocalibrate_button(b))

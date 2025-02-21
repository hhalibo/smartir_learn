from typing import Final

DOMAIN: Final = "smartir_learn"
MOCK_DATA: Final = True
LEARN_TIMEOUT = 60

# 设备类型列表
DEVICE_TYPES: Final = {
    "climate": "Climate",
    "media_player": "Media Player",
    "fan": "Fan",
    "light": "Light"
}

DEVICE_TEMPLATE = {
    "climate": {
        "Template1": "climate1.json",
        "DEBUG": "climate2.json"
    },
    "media_player": {
        "Template1": "media1.json"
    },
    "fan": {
        "Template1": "fan1.json"
    },
    "light": {
        "Template1": "light1.json"
    }
}

# Translation Keys
TRANSLATION_KEY_DEVICE_IP_MODE: Final = f"component.{DOMAIN}.common.device_ip_mode"
TRANSLATION_KEY_TEMPLATE_FROM_FILE: Final = f"component.{DOMAIN}.common.template_from_file"
TRANSLATION_KEY_COMMAND_REPLACE_MAP: Final = f"component.{DOMAIN}.common.command_replace_map"
TRANSLATION_KEY_DEVICE_TEMPLATE_NAME: Final = f"component.{DOMAIN}.common.device_template_name"

import json
from enum import IntEnum

from workers import ClassicWorker


class SettingType(IntEnum):
    CLASSIC = 1
    COLORED = 2
    TREE = 3


class Settings:
    """
    Базовый объект настроек
    """
    def __init__(self):
        self.type = None
        self.props = {}
        self.worker = None

    @staticmethod
    def create_from_json(json_data):
        """
        Создание объекта настроек из json
        """
        data = json.load(json_data)
        if data["type"] == SettingType.CLASSIC:
            settings = ClassicSettings()
        elif data["type"] == SettingType.COLORED:
            settings = ColoredSettings()
        elif data["type"] == SettingType.TREE:
            settings = TreeSettings()
        else:
            raise ValueError("Несуществующее значение типа настроек")

        for prop in settings.props:
            settings.props[prop]["value"] = data["props"].get(prop) or ""

        return settings

    def json(self):
        """
        Создание json для сохранения настроек
        """
        out = {
            "type": int(self.type),
            "props": {}
        }
        for prop_name in self.props:
            out["props"][prop_name] = self.props[prop_name]["value"]
        return json.dumps(out)


class ClassicSettings(Settings):
    """
    Настройки для классических l-систем
    """
    def __init__(self):
        super(ClassicSettings, self).__init__()
        self.type = SettingType.CLASSIC
        self.worker = ClassicWorker
        self.props = {
            "axiom": {
                "name": "Axiom",
                "value": ""
            },
            "rule": {
                "name": "Rule",
                "value": ""
            },
            "start_angle": {
                "name": "Start Angle",
                "value": ""
            },
            "angle": {
                "name": "Angle",
                "value": ""
            },
            "nesting": {
                "name": "Nesting",
                "value": ""
            },
            "length": {
                "name": "Length",
                "value": ""
            },
            "width": {
                "name": "Width",
                "value": ""
            },
            "start_x": {
                "name": "Start x",
                "value": ""
            },
            "start_y": {
                "name": "Start y",
                "value": ""
            },
            "color": {
                "name": "Color",
                "value": "#000000"
            }
        }


class ColoredSettings(Settings):
    """
    Настройки для цветных l-систем
    """
    def __init__(self):
        super(ColoredSettings, self).__init__()
        self.type = SettingType.COLORED
        self.worker = ClassicWorker
        self.props = {
            "axiom": {
                "name": "Axiom",
                "value": ""
            },
            "rule": {
                "name": "Rule",
                "value": ""
            },
            "start_angle": {
                "name": "Start Angle",
                "value": ""
            },
            "angle": {
                "name": "Angle",
                "value": ""
            },
            "nesting": {
                "name": "Nesting",
                "value": ""
            },
            "length": {
                "name": "Length",
                "value": ""
            },
            "width": {
                "name": "Width",
                "value": ""
            },
            "start_x": {
                "name": "Start x",
                "value": ""
            },
            "start_y": {
                "name": "Start y",
                "value": ""
            },
            "color1": {
                "name": "Color 1",
                "value": ""
            },
            "color2": {
                "name": "Color 2",
                "value": ""
            },
            "color3": {
                "name": "Color 3",
                "value": ""
            }
        }


class TreeSettings(Settings):
    """
    Настройки для цветных l-систем
    """
    def __init__(self):
        super(TreeSettings, self).__init__()
        self.type = SettingType.TREE
        self.worker = ClassicWorker
        self.props = {
            "axiom": {
                "name": "Axiom",
                "value": ""
            },
            "rule": {
                "name": "Rule",
                "value": ""
            },
            "start_angle": {
                "name": "Start Angle",
                "value": ""
            },
            "angle": {
                "name": "Angle",
                "value": ""
            },
            "nesting": {
                "name": "Nesting",
                "value": ""
            },
            "length": {
                "name": "Length",
                "value": ""
            },
            "width": {
                "name": "Width",
                "value": ""
            },
            "width_dec": {
                "name": "Decreasing width",
                "value": ""
            },
            "start_x": {
                "name": "Start x",
                "value": ""
            },
            "start_y": {
                "name": "Start y",
                "value": ""
            },
            "color1": {
                "name": "Color 1",
                "value": ""
            },
            "color2": {
                "name": "Color 2",
                "value": ""
            }
        }

import json
from enum import IntEnum

from workers import ClassicWorker, ColoredWorker, TreeWorker


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
        self.interpretation = ""

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
        self.interpretation = "F - forward\n" \
                              "b - forward no color\n" \
                              "+ - rotate random 45\n" \
                              "- - rotate random 45\n" \
                              "[ - save\n" \
                              "] - restore\n"
        self.type = SettingType.CLASSIC
        self.worker = ClassicWorker
        self.props = {
            "axiom": {
                "name": "Axiom",
                "value": ""
            },
            "rule": {
                "name": "F ->",
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
        self.interpretation = "F - forward\n" \
                              "b - forward no color\n" \
                              "+ - rotate random 45\n" \
                              "- - rotate random 45\n" \
                              "[ - save\n" \
                              "] - restore\n" \
                              "1 - color 1\n" \
                              "2 - color 2\n" \
                              "3 - color 3"
        self.type = SettingType.COLORED
        self.worker = ColoredWorker
        self.props = {
            "axiom": {
                "name": "Axiom",
                "value": ""
            },
            "rule": {
                "name": "F ->",
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
                "value": "#000000"
            },
            "color2": {
                "name": "Color 2",
                "value": "#000000"
            },
            "color3": {
                "name": "Color 3",
                "value": "#000000"
            }
        }


class TreeSettings(Settings):
    """
    Настройки для цветных l-систем
    """
    def __init__(self):
        super(TreeSettings, self).__init__()
        self.interpretation = "F - forward\n" \
                              "X - forward\n" \
                              "+ - rotate random 45\n" \
                              "- - rotate random 45\n" \
                              "[ - save\n" \
                              "] - restore\n" \
                              "@ - dec width\n"
        self.type = SettingType.TREE
        self.worker = TreeWorker
        self.props = {
            "axiom": {
                "name": "Axiom",
                "value": ""
            },
            "rule": {
                "name": "X ->",
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
            "length_dec": {
                "name": "Decreasing ratio length",
                "value": ""
            },
            "width": {
                "name": "Width",
                "value": ""
            },
            "width_dec": {
                "name": "Decreasing ratio width",
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
                "name": "Trunk color",
                "value": "#000000"
            },
            "color_dec": {
                "name": "Decreasing ratio trunk color",
                "value": ""
            },
            "color2": {
                "name": "Leaf color 1",
                "value": "#000000"
            },
            "color3": {
                "name": "Leaf color 2",
                "value": "#000000"
            },
            "color4": {
                "name": "Leaf color 3",
                "value": "#000000"
            },
            "length_leaf": {
                "name": "Leaf length",
                "value": ""
            },
            "width_leaf": {
                "name": "Leaf width",
                "value": ""
            }
        }

from enum import Enum

from workers import ClassicWorker


class SettingType(Enum):
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
            }
        }

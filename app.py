import pickle
import os
import copy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy import platform
from kivy.uix.filechooser import FileChooser

from common import apply_rules, create_lines


class BaseSettings:
    """
    Базовый объект настроек
    """
    def __init__(self):
        self.axiom = "F+F-FF"
        self.rule = "-F+[FF++FF++FF]-F+"
        self.start_angle = 60
        self.angle = 12
        self.nesting = 4
        self.length = 5
        self.width = 1
        self.start_x = 100
        self.start_y = 100


class Painter(Widget):
    def __init__(self, **kwargs):
        super(Painter, self).__init__(**kwargs)

    def draw(self, settings):
        self.canvas.clear()
        axiom = apply_rules(settings.axiom, settings.rule, settings.nesting)
        lines = create_lines(axiom, settings)

        self.canvas.add(Color(0, 1, 0, 1))
        # добавление линий на canvas
        for line in lines:
            self.canvas.add(line)


class LSystemApp(App):

    def build(self):
        self.root = BoxLayout(orientation="horizontal")
        self.settings_layout = Builder.load_file('./templates/settings.kv')

        painter = Painter()
        self.root.add_widget(painter)
        self.root.add_widget(self.settings_layout)

        self.settings_layout.ids.start.bind(on_press=lambda a: self.start(painter))
        self.settings_layout.ids.save.bind(
            on_press=lambda a: self.save_settings(self.settings_layout.ids.config_save_name.text)
        )
        self.load_config_list()
        return self.root

    def start(self, painter):
        # настройки введёные пользователем
        settings = self.create_settings_from_layout()
        painter.draw(settings)

    def create_settings_from_layout(self):
        settings = BaseSettings()
        settings.axiom = self.settings_layout.ids.axiom.text
        settings.rule = self.settings_layout.ids.rule.text
        settings.start_angle = float(self.settings_layout.ids.start_angle.text)
        settings.angle = float(self.settings_layout.ids.angle.text)
        settings.nesting = int(self.settings_layout.ids.nesting.text)
        settings.length = float(self.settings_layout.ids.length.text)
        settings.start_x = int(self.settings_layout.ids.start_x.text)
        settings.start_y = int(self.settings_layout.ids.start_y.text)
        settings.width = float(self.settings_layout.ids.width.text)
        return settings

    def load_config_list(self):
        configs = os.listdir(os.path.dirname(__file__)+"/configs")

        # без данного приёма вылетает ошибка
        for child in [child for child in self.settings_layout.ids.configs.children]:
            self.settings_layout.ids.configs.remove_widget(child)

        for config in configs:
            button = Button(text=config, size_hint_y=None, height=100)
            button.bind(on_press=lambda a: self.select_file(a.text))

            self.settings_layout.ids.configs.add_widget(button)

    def select_file(self, name):
        """
        Выбор фалйа
        """
        try:
            with open(os.path.dirname(__file__)+"/configs/"+name, 'rb') as f:
                settings = pickle.load(f)
                self.settings_layout.ids.axiom.text = str(settings.axiom)
                self.settings_layout.ids.rule.text = str(settings.rule)
                self.settings_layout.ids.start_angle.text = str(settings.start_angle)
                self.settings_layout.ids.angle.text = str(settings.angle)
                self.settings_layout.ids.nesting.text = str(settings.nesting)
                self.settings_layout.ids.length.text = str(settings.length)
                self.settings_layout.ids.start_x.text = str(settings.start_x)
                self.settings_layout.ids.start_y.text = str(settings.start_y)
                self.settings_layout.ids.width.text = str(settings.width)

        except FileNotFoundError:
            print("Файл не был найдён")

    def save_settings(self, name):
        """
        Сохранение конфигурации в файл
        """
        settings = self.create_settings_from_layout()
        with open(os.path.dirname(__file__)+"/configs/"+name, 'wb') as f:
            pickle.dump(settings, f)

        self.load_config_list()


if __name__ == "__main__":  
    LSystemApp().run()

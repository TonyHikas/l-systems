import pickle
import os
import copy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy import platform
from kivy.uix.filechooser import FileChooser

from settings import ClassicSettings


class Painter(Widget):
    def __init__(self, **kwargs):
        super(Painter, self).__init__(**kwargs)
        self.canvas.before.add(Color(255, 255, 255, 1))
        self.canvas.before.add(Rectangle(size=(4000, 4000)))

    def draw(self, settings):
        self.canvas.clear()
        axiom = settings.worker.apply_rules(settings)
        lines = settings.worker.create_lines(axiom, settings)

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

        default_settings = ClassicSettings()
        self.create_props_widgets(default_settings)

        return self.root

    def start(self, painter):
        # настройки введёные пользователем
        settings = self.create_settings_from_layout()
        painter.draw(settings)

    def create_props_widgets(self, settings):
        """
        Создание виджетов для отображдения параметров
        """
        for prop_name, prop_value in settings.props.items():
            label = Label(text=prop_value["name"], size_hint_y=None, height=50)
            text_input = TextInput(id=prop_name, text=str(prop_value["value"]), size_hint_y=None, height=40)
            self.settings_layout.ids.props.add_widget(label)
            self.settings_layout.ids.props.add_widget(text_input)

    def create_settings_from_layout(self):
        settings = ClassicSettings()
        for child in [child for child in self.settings_layout.ids.props.children]:
            if child.id is not None:
                settings.props[child.id]["value"] = child.text
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

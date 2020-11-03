from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

from common import apply_rules, create_lines


# class BaseSettings:
#     axiom = "F++F++F"
#     rule = "-2F3F-"
#     start_angle = 60
#     angle = 60
#     nesting = 12
#     length = 15

class BaseSettings:
    def __init__(self):
        self.axiom = "F+F-FF"
        self.rule = "-F+[FF++FF++FF]-F+"
        self.start_angle = 60
        self.angle = 12
        self.nesting = 4
        self.length = 5


class Painter(Widget):
    def __init__(self, **kwargs):
        super(Painter, self).__init__(**kwargs)

    def draw(self, settings):
        self.canvas.clear()
        axiom = apply_rules(settings.axiom, settings.rule, settings.nesting)
        lines = create_lines(axiom, settings)
        # print(axiom)
        self.canvas.add(Color(0, 1, 0, 1))
        for line in lines:
            self.canvas.add(line)


class LSystemApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="horizontal")
        settings_layout = Builder.load_file('./templates/settings.kv')
        start_button = Button(text="Start")
        settings_layout.add_widget(start_button)
        painter = Painter()
        main_layout.add_widget(painter)
        main_layout.add_widget(settings_layout)

        start_button.bind(on_press=lambda a: self.start(painter, settings_layout))
        return main_layout

    def start(self, painter, settings_layout):
        settings = BaseSettings()
        settings.axiom = settings_layout.ids.axiom.text
        settings.rule = settings_layout.ids.rule.text
        settings.start_angle = float(settings_layout.ids.start_angle.text)
        settings.angle = float(settings_layout.ids.angle.text)
        settings.nesting = int(settings_layout.ids.nesting.text)
        settings.length = float(settings_layout.ids.length.text)
        painter.draw(settings)


if __name__ == "__main__":  
    LSystemApp().run()

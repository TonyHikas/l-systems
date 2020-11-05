import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scatter import Scatter, ScatterPlane
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.graphics.transformation import Matrix
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from settings import ClassicSettings, Settings, ColoredSettings, TreeSettings


class Painter(Widget):
    """
    Canvas для рисования систем
    """
    def __init__(self, **kwargs):
        super(Painter, self).__init__(**kwargs)

    def draw(self, settings):
        self.canvas.clear()
        axiom = settings.worker.apply_rules(settings)
        lines = settings.worker.create_lines(axiom, settings)
        self.canvas.add(Color(0, 1, 0, 1))
        # добавление линий на canvas
        for line in lines:
            self.canvas.add(line)


class LSystemApp(App):
    """
    Главное приложение
    """
    def __init__(self):
        super(LSystemApp, self).__init__()
        self.settings_layout = None
        self.settings = None
        self.scatter = None
        self.draw_layout = None

    def build(self):
        self.root = BoxLayout(orientation="horizontal")
        self.settings_layout = Builder.load_file('./templates/settings.kv')

        self.draw_layout = RelativeLayout()
        self.draw_layout.canvas.before.add(Color(255, 255, 255, 1))
        self.draw_layout.canvas.before.add(Rectangle(size=(4000, 4000)))
        self.scatter = ScatterPlane()
        painter = Painter()
        self.scatter.add_widget(painter)
        self.draw_layout.add_widget(self.scatter)
        self.root.add_widget(self.draw_layout)
        self.root.add_widget(self.settings_layout)

        self.settings_layout.ids.start.bind(
            on_press=lambda a: self.start(painter)
        )
        self.settings_layout.ids.save.bind(
            on_press=lambda a: self.save_settings(self.settings_layout.ids.config_save_name.text)
        )
        self.settings_layout.ids.switch_classic.bind(
            on_press=lambda a: self.new_settings(ClassicSettings())
        )
        self.settings_layout.ids.switch_colored.bind(
            on_press=lambda a: self.new_settings(ColoredSettings())
        )
        self.settings_layout.ids.switch_tree.bind(
            on_press=lambda a: self.new_settings(TreeSettings())
        )
        self.settings_layout.ids.scale_up.bind(
            on_press=lambda a: self.scale_up()
        )
        self.settings_layout.ids.scale_down.bind(
            on_press=lambda a: self.scale_down()
        )
        self.draw_layout.bind(
            on_touch_down=lambda obj, touch: self.scale(touch)
        )

        self.load_config_list()

        self.settings = ClassicSettings()
        self.create_settings_widgets()

        return self.root

    def start(self, painter):
        """
        Запуск отрисовки
        """
        self.create_settings_from_layout()
        painter.draw(self.settings)

    def new_settings(self, settings):
        """
        Создание новой настройки
        """
        self.settings = settings
        self.create_settings_widgets()
        self.settings_layout.ids.config_save_name.text = "new_config"

    def create_settings_widgets(self):
        """
        Создание виджетов для отображдения настройки
        """
        for child in [child for child in self.settings_layout.ids.props.children]:
            self.settings_layout.ids.props.remove_widget(child)
        for prop_name, prop_value in self.settings.props.items():
            label = Label(text=prop_value["name"], size_hint_y=None, height=50)
            text_input = TextInput(id=prop_name, text=str(prop_value["value"]), size_hint_y=None, height=40)
            self.settings_layout.ids.props.add_widget(label)
            self.settings_layout.ids.props.add_widget(text_input)

    def create_settings_from_layout(self):
        """
        Парсинг параметров, введённых пользователем в объект настроек
        """
        for child in [child for child in self.settings_layout.ids.props.children]:
            if child.id is not None:
                self.settings.props[child.id]["value"] = child.text

    def load_config_list(self):
        """
        Загрузка списка сохранённых конфигурация
        """
        configs = sorted(os.listdir(os.path.dirname(__file__)+"/configs"))

        for child in [child for child in self.settings_layout.ids.configs.children]:
            self.settings_layout.ids.configs.remove_widget(child)

        for config in configs:
            button = Button(text=config, size_hint_y=None, height=50)
            button.bind(on_press=lambda a: self.select_file(a.text))

            self.settings_layout.ids.configs.add_widget(button)

    def select_file(self, name):
        """
        Выбор фалйа
        """
        try:
            with open(os.path.dirname(__file__)+"/configs/"+name, 'r') as f:
                self.settings = Settings.create_from_json(f)
                self.create_settings_widgets()
                self.settings_layout.ids.config_save_name.text = name

        except FileNotFoundError:
            print("Файл не был найдён")

    def save_settings(self, name):
        """
        Сохранение конфигурации в файл
        """
        self.create_settings_from_layout()
        json_data = self.settings.json()
        with open(os.path.dirname(__file__)+"/configs/"+name, 'w') as f:
            f.write(json_data)
        self.create_settings_widgets()
        self.load_config_list()

    def scale(self, touch):
        """
        Масштабирование колесом мыши
        """
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                self.scale_up(touch.pos)
            elif touch.button == 'scrollup':
                self.scale_down(touch.pos)

    def scale_up(self, anchor=None):
        """
        Увеличение кнопкой
        """
        if not anchor:
            anchor = self.draw_layout.center
        self.scatter.apply_transform(Matrix().scale(1.1, 1.1, 1.1), anchor=anchor)

    def scale_down(self, anchor=None):
        """
        Уменьшение кнопкой
        """
        if not anchor:
            anchor = self.draw_layout.center
        self.scatter.apply_transform(Matrix().scale(0.9, 0.9, 0.9), anchor=anchor)


if __name__ == "__main__":  
    LSystemApp().run()

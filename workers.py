from kivy.graphics import Color, Line
import math


class Worker:
    """
    Базовай класс воркера
    """
    @staticmethod
    def apply_rules(settings) -> str:
        """
        Применяет правала к аксиоме
        """
        axiom = settings.props["axiom"]["value"]
        for j in range(int(settings.props["nesting"]["value"])):
            out = ""
            for i in axiom:
                if i == "F":
                    out += settings.props["rule"]["value"]
                else:
                    out += i
            axiom = out
        return axiom

    @staticmethod
    def create_lines(axiom: str, settings):
        """
        Создание линий по строке
        """
        pass


def hex_to_color(hex_str: str):
    """
    Преобразование hex в rgb
    """
    hex_str = hex_str.lstrip('#')
    return Color(*tuple(int(hex_str[i:i + 2], 16)/255 for i in (0, 2, 4)))


def new_line(width):
    """Создание новой линии"""
    return Line(points=(), width=float(width), cap="round", joint="round", close=False)


class ClassicWorker(Worker):
    @staticmethod
    def create_lines(axiom: str, settings):
        resp = []
        x = float(settings.props["start_x"]["value"])
        y = float(settings.props["start_y"]["value"])
        heading = -float(settings.props["start_angle"]["value"]) + 90

        resp.append(hex_to_color(settings.props["color"]["value"]))

        line = new_line(settings.props["width"]["value"])
        line.points += (x, y)
        stack = []
        for i in axiom:
            if i == "F":
                x1 = float(settings.props["length"]["value"])*math.sin(math.radians(heading))
                y1 = float(settings.props["length"]["value"])*math.cos(math.radians(heading))
                x += x1
                y += y1
                line.points += (x, y)
            elif i == "b":
                resp.append(line)
                line = new_line(settings.props["width"]["value"])
                x1 = float(settings.props["length"]["value"]) * math.sin(math.radians(heading))
                y1 = float(settings.props["length"]["value"]) * math.cos(math.radians(heading))
                x += x1
                y += y1
                line.points += (x, y)
            elif i == "[":
                stack.append(x)
                stack.append(y)
                stack.append(heading)
            elif i == "]":
                heading = stack.pop()
                y = stack.pop()
                x = stack.pop()
                resp.append(line)
                line = new_line(settings.props["width"]["value"])
                line.points += (x, y)
            elif i == "+":
                heading += float(settings.props["angle"]["value"])
            elif i == "-":
                heading -= float(settings.props["angle"]["value"])
        resp.append(line)
        return resp


class ColoredWorker(Worker):
    @staticmethod
    def create_lines(axiom: str, settings):

        resp = []
        x = float(settings.props["start_x"]["value"])
        y = float(settings.props["start_y"]["value"])
        heading = -float(settings.props["start_angle"]["value"]) + 90

        resp.append(hex_to_color(settings.props["color1"]["value"]))

        line = new_line(settings.props["width"]["value"])
        line.points += (x, y)
        stack = []
        for i in axiom:
            if i == "F":
                x1 = float(settings.props["length"]["value"])*math.sin(math.radians(heading))
                y1 = float(settings.props["length"]["value"])*math.cos(math.radians(heading))
                x += x1
                y += y1
                line.points += (x, y)
            elif i == "b":
                resp.append(line)
                line = new_line(settings.props["width"]["value"])
                x1 = float(settings.props["length"]["value"]) * math.sin(math.radians(heading))
                y1 = float(settings.props["length"]["value"]) * math.cos(math.radians(heading))
                x += x1
                y += y1
                line.points += (x, y)
            elif i == "[":
                stack.append(x)
                stack.append(y)
                stack.append(heading)
            elif i == "]":
                heading = stack.pop()
                y = stack.pop()
                x = stack.pop()
                resp.append(line)
                line = new_line(settings.props["width"]["value"])
                line.points += (x, y)
            elif i == "+":
                heading += float(settings.props["angle"]["value"])
            elif i == "-":
                heading -= float(settings.props["angle"]["value"])
            elif i == "1":
                resp.append(line)
                resp.append(hex_to_color(settings.props["color1"]["value"]))
                line = new_line(settings.props["width"]["value"])
                line.points += (x, y)
            elif i == "2":
                resp.append(line)
                resp.append(hex_to_color(settings.props["color2"]["value"]))
                line = new_line(settings.props["width"]["value"])
                line.points += (x, y)
            elif i == "3":
                resp.append(line)
                resp.append(hex_to_color(settings.props["color3"]["value"]))
                line = new_line(settings.props["width"]["value"])
                line.points += (x, y)
        resp.append(line)
        return resp

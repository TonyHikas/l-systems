from kivy.graphics import Color, Line
import math
import random


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


def hex_to_rgb(hex_str: str):
    """
    Преобразование hex в rgb
    """
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i + 2], 16) / 255 for i in (0, 2, 4))


def hex_to_color(hex_str: str):
    """
    Преобразование hex в Color объект
    """
    return Color(*hex_to_rgb(hex_str))


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
        width = float(settings.props["width"]["value"])
        length = float(settings.props["length"]["value"])
        angle = float(settings.props["angle"]["value"])

        resp.append(hex_to_color(settings.props["color"]["value"]))

        line = new_line(settings.props["width"]["value"])
        line.points += (x, y)
        stack = []
        for i in axiom:
            if i == "F":
                x1 = length * math.sin(math.radians(heading))
                y1 = length * math.cos(math.radians(heading))
                x += x1
                y += y1
                line.points += (x, y)
            elif i == "b":
                resp.append(line)
                line = new_line(settings.props["width"]["value"])
                x1 = length * math.sin(math.radians(heading))
                y1 = length * math.cos(math.radians(heading))
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
                line = new_line(width)
                line.points += (x, y)
            elif i == "+":
                heading += angle
            elif i == "-":
                heading -= angle
        resp.append(line)
        return resp


class ColoredWorker(Worker):
    @staticmethod
    def create_lines(axiom: str, settings):

        resp = []
        x = float(settings.props["start_x"]["value"])
        y = float(settings.props["start_y"]["value"])
        heading = -float(settings.props["start_angle"]["value"]) + 90
        width = float(settings.props["width"]["value"])
        length = float(settings.props["length"]["value"])
        angle = float(settings.props["angle"]["value"])

        resp.append(hex_to_color(settings.props["color1"]["value"]))

        line = new_line(settings.props["width"]["value"])
        line.points += (x, y)
        stack = []
        for i in axiom:
            if i == "F":
                x1 = length * math.sin(math.radians(heading))
                y1 = length * math.cos(math.radians(heading))
                x += x1
                y += y1
                line.points += (x, y)
            elif i == "b":
                resp.append(line)
                line = new_line(width)
                x1 = length * math.sin(math.radians(heading))
                y1 = length * math.cos(math.radians(heading))
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
                line = new_line(width)
                line.points += (x, y)
            elif i == "+":
                heading += angle
            elif i == "-":
                heading -= angle
            elif i == "1":
                resp.append(line)
                resp.append(hex_to_color(settings.props["color1"]["value"]))
                line = new_line(width)
                line.points += (x, y)
            elif i == "2":
                resp.append(line)
                resp.append(hex_to_color(settings.props["color2"]["value"]))
                line = new_line(width)
                line.points += (x, y)
            elif i == "3":
                resp.append(line)
                resp.append(hex_to_color(settings.props["color3"]["value"]))
                line = new_line(width)
                line.points += (x, y)
        resp.append(line)
        return resp


class TreeWorker(Worker):
    @staticmethod
    def apply_rules(settings) -> str:
        axiom = settings.props["axiom"]["value"]
        for j in range(int(settings.props["nesting"]["value"])):
            out = ""
            for i in axiom:
                if i == "X":
                    if random.randint(0, 5) == 0:
                        out += i
                    else:
                        out += settings.props["rule"]["value"]
                else:
                    out += i
            axiom = out
        return axiom

    @staticmethod
    def create_lines(axiom: str, settings):
        resp = []
        x = float(settings.props["start_x"]["value"])
        y = float(settings.props["start_y"]["value"])
        heading = -float(settings.props["start_angle"]["value"]) + 90
        width = float(settings.props["width"]["value"])
        width_dec = float(settings.props["width_dec"]["value"])
        length = float(settings.props["length"]["value"])
        length_dec = float(settings.props["length_dec"]["value"])
        angle = float(settings.props["angle"]["value"])
        opacity = 1
        color = hex_to_rgb(settings.props["color1"]["value"])
        color_dec = float(settings.props["color_dec"]["value"])

        resp.append(hex_to_color(settings.props["color1"]["value"]))

        stack = []
        for i in axiom:
            if i == "F":
                resp.append(Color(color[0]/opacity, color[1]/opacity, color[2]/opacity))
                line = new_line(width)
                line.points += (x, y)
                x1 = length*math.sin(math.radians(heading))
                y1 = length*math.cos(math.radians(heading))
                x += x1
                y += y1
                line.points += (x, y)
                resp.append(line)
            elif i == "X":
                rand = random.randint(0, 2)
                if rand == 0:
                    resp.append(hex_to_color(settings.props["color2"]["value"]))
                if rand == 1:
                    resp.append(hex_to_color(settings.props["color3"]["value"]))
                if rand == 2:
                    resp.append(hex_to_color(settings.props["color4"]["value"]))
                line = new_line(float(settings.props["width_leaf"]["value"]))
                line.points += (x, y)
                x1 = float(settings.props["length_leaf"]["value"]) * math.sin(math.radians(heading))
                y1 = float(settings.props["length_leaf"]["value"]) * math.cos(math.radians(heading))
                x += x1
                y += y1
                line.points += (x, y)
                resp.append(line)
            elif i == "[":
                stack.append(x)
                stack.append(y)
                stack.append(heading)
                stack.append(width)
                stack.append(length)
                stack.append(opacity)
            elif i == "]":
                opacity = stack.pop()
                length = stack.pop()
                width = stack.pop()
                heading = stack.pop()
                y = stack.pop()
                x = stack.pop()
                resp.append(line)
                line = new_line(width)
                line.points += (x, y)
            elif i == "+":
                heading += random.randint(0, angle)
            elif i == "-":
                heading -= random.randint(0, angle)
            elif i == "@":
                width *= width_dec
                opacity *= color_dec
                length *= length_dec
                length *= random.randint(99, 110)/100

        return resp

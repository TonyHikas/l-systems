from kivy.graphics import Color, Line
from typing import List
import math


class Worker:
    """
    Базовай класс воркера
    """
    @staticmethod
    def apply_rules(settings):
        pass

    @staticmethod
    def create_lines(axiom: str, settings):
        pass


class ClassicWorker(Worker):
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
    def create_lines(axiom: str, settings) -> List[Line]:
        """
        Создание линий по строке
        """
        resp = []
        x = float(settings.props["start_x"]["value"])
        y = float(settings.props["start_y"]["value"])
        heading = -float(settings.props["start_angle"]["value"]) + 90
        # преобразование hex в rgb
        color_hex = settings.props["color"]["value"].lstrip('#')
        resp.append(Color(*tuple(int(color_hex[i:i + 2], 16) for i in (0, 2, 4))))
        line = Line(points=(), width=float(settings.props["width"]["value"]), cap="round", joint="round", close=False)
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
                line = Line(
                    points=(),
                    width=float(settings.props["width"]["value"]),
                    cap="round",
                    joint="round",
                    close=False
                )
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
                line = Line(
                    points=(),
                    width=float(settings.props["width"]["value"]),
                    cap="round",
                    joint="round",
                    close=False
                )
                line.points += (x, y)
            elif i == "+":
                heading += float(settings.props["angle"]["value"])
            elif i == "-":
                heading -= float(settings.props["angle"]["value"])
        resp.append(line)
        return resp

from kivy.graphics import Color, Line
from typing import List
import math


def apply_rules(axiom: str, rule: str, nesting: int) -> str:
    """
    Применяет правала к аксиоме
    """
    for j in range(nesting):
        out = ""
        for i in axiom:
            if i == "F":
                out += rule
            else:
                out += i
        axiom = out
    return axiom


def create_lines(axiom: str, settings) -> List[Line]:
    """
    Создание линий по строке
    """
    resp = []
    x = settings.start_x
    y = settings.start_y
    heading = -settings.start_angle + 90
    line = Line(points=(), width=settings.width, cap="round", joint="round", close=False)
    line.points += (x, y)
    stack = []
    for i in axiom:
        if i == "F":
            x1 = settings.length*math.sin(math.radians(heading))
            y1 = settings.length*math.cos(math.radians(heading))
            x += x1
            y += y1
            line.points += (x, y)
        elif i == "b":
            resp.append(line)
            line = Line(points=(), width=settings.width, cap="round", joint="round", close=False)
            x1 = settings.length * math.sin(math.radians(heading))
            y1 = settings.length * math.cos(math.radians(heading))
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
            line = Line(points=(), width=settings.width, cap="round", joint="round", close=False)
            line.points += (x, y)
        elif i == "+":
            heading += settings.angle
        elif i == "-":
            heading -= settings.angle
    resp.append(line)
    return resp

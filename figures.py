# Классы фигур (наследование)
# Родительский (базовый) класс (superclass)
# Дочерний (производный, наследник) класс
from math import pi


class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return round((self.width + self.height) * 2, 1)

    # Геттер
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    # Cеттер
    def set_width(self, new_w):
        self.width = new_w

    def set_height(self, new_h):
        self.height = new_h

    def __str__(self):
        return f'Это фигура со стороной {self.side}'

    def __eq__(self, other):
        return self.side == other.side

    def __gt__(self, other):
        return self.side > other.side

    def __ge__(self, other):
        return self.side >= other.side

    def __add__(self, other):
        return Square(self.side + other.side)

    def __sub__(self, other):
        return Square(self.side - other.side)

    def __repr__(self):
        return f'Квадрат со стороной {self.side}'

    def __del__(self):
        print(f'Квадрат со стороной {self.side} стёрт!')


class Square(Rectangle):
    def __init__(self, s=1):
        super().__init__(s, s)  # вызов конструктора базового класса
        self.side = s


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return round(2 * pi * self.radius, 1)

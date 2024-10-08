# Объектно-ориентированный подход
# Полиморфизм
from math import pi


class Square:
    def __init__(self, s):
        self.side = s

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return float(round(self.side * 4, 2))


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return round(2 * pi * self.radius, 1)


class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return round((self.width + self.height) * 2, 1)


circle = Circle(5)
square = Square(5)
rect = Rectangle(5, 7)

print(circle.perimeter())
print(square.perimeter())
print(rect.perimeter())

if circle.__class__.__name__ == 'Circle':
    print('Это экземпляр класса Circle')










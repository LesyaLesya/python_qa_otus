import math


class Figure:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError('Имя должно быть строкой')
        self.__name = name
        self.__angles = None
        self.__area = None
        self.__perimeter = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, figure_name):
        if not isinstance(figure_name, str):
            raise TypeError('Новое имя должно быть строкой')
        self.__name = figure_name

    @property
    def angles(self):
        if isinstance(self, (Square, Rectangle)):
            self.__angles = 4
        elif isinstance(self, Triangle):
            self.__angles = 3
        elif isinstance(self, Circle):
            self.__angles = 0
        return self.__angles

    @angles.setter
    def angles(self, value):
        self.__angles = value

    @property
    def area(self):
        if self.__area is None:
            if isinstance(self, Square):
                self.__area = self.side ** 2
            if isinstance(self, Rectangle):
                self.__area = self.width * self.height
            if isinstance(self, Triangle):
                p = float((self.a + self.b + self.c) / 2)
                self.__area = round(((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5), 4)
            if isinstance(self, Circle):
                self.__area = round((math.pi * (self.radius ** 2)), 4)
        return self.__area

    @area.setter
    def area(self, value):
        self.__area = value
        self.__area = None

    @property
    def perimeter(self):
        if self.__perimeter is None:
            if isinstance(self, Triangle):
                self.__perimeter = self.a + self.b + self.c
            if isinstance(self, Square):
                self.__perimeter = 4 * self.side
            if isinstance(self, Rectangle):
                self.__perimeter = 2 * (self.width + self.height)
            if isinstance(self, Circle):
                self.__perimeter = round((2 * math.pi * self.radius), 4)
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, value):
        self.__perimeter = value
        self.__perimeter = None

    def add_square(self, figure):
        if not isinstance(figure, (Rectangle, Circle, Square, Triangle)):
            raise Exception("Передан неправильный класс")
        return round((self.area + figure.area), 4)


class Square(Figure):
    def __init__(self, name, side):
        super().__init__(name)
        if type(side) not in (float, int):
            raise TypeError("Длина стороны должна быть числом")
        if side <= 0:
            raise ValueError("Длина стороны должна быть больше ноля")
        self.side = side

    def __str__(self):
        return "Квадрат"


class Triangle(Figure):
    def __init__(self, name, a, b, c):
        super().__init__(name)
        if type(a) not in (float, int) or type(b) not in (float, int) \
                or type(c) not in (float, int):
            raise TypeError("Длина стороны должна быть числом")
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Длина стороны должна быть больше ноля")
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "Треугольник"


class Rectangle(Figure):
    def __init__(self, name, width, height):
        super().__init__(name)
        if type(width) not in (float, int) or type(height) not in (float, int):
            raise TypeError("Длина стороны должна быть числом")
        if width <= 0 or height <= 0:
            raise ValueError("Длина стороны должна быть больше ноля")
        self.width = width
        self.height = height

    def __str__(self):
        return "Прямоугольник"


class Circle(Figure):
    def __init__(self, name, radius):
        if type(radius) not in (float, int):
            raise TypeError("Радиус должен быть числом")
        if radius <= 0:
            raise ValueError("Радиус должен быть больше ноля")
        super().__init__(name)
        self.radius = radius

    def __str__(self):
        return "Круг"

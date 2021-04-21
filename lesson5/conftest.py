import pytest
from lesson5.figures import Square, Circle, Triangle, Rectangle


@pytest.fixture(autouse=True)
def setup_fixture():
    print("\nStart test.... ")
    yield
    print("\nStop test....")


# Тестовый класс фигуры Square
class TestClassSquare:
    def check_name(self, value):
        figure = Square(value, 10)
        return figure.name

    def check_angles(self):
        figure = Square("квадрат", 10)
        return figure.angles

    def check_area(self, value):
        figure = Square("квадрат", value)
        return figure.area

    def check_perimeter(self, value):
        figure = Square("квадрат", value)
        return figure.perimeter

    def check_add_square(self, value1, value2):
        figure_1 = Square("квадрат", value1)
        figure_2 = Circle("круг", value2)
        return round((figure_1.area + figure_2.area), 4)

# Фикстуры Square
@pytest.fixture
def fixture_square():
    return TestClassSquare()


# Тестовый класс фигуры Circle
class TestClassCircle:
    def check_name(self, value):
        figure = Circle(value, 5)
        return figure.name

    def check_angles(self):
        figure = Circle("круг", 5)
        return figure.angles

    def check_area(self, value):
        figure = Circle("круг", value)
        return figure.area

    def check_perimeter(self, value):
        figure = Circle("круг", value)
        return figure.perimeter

    def check_add_square(self, value1, value2, value3):
        figure_1 = Circle("круг", value1)
        figure_2 = Rectangle("прямоугольник", value2, value3)
        return round((figure_1.area + figure_2.area), 4)


# Фикстуры Circle
@pytest.fixture
def fixture_circle():
    return TestClassCircle()


# Тестовый класс фигуры Rectangle
class TestClassRectangle:
    def check_name(self, value):
        figure = Rectangle(value, 5, 10)
        return figure.name

    def check_angles(self):
        figure = Rectangle("прямоугольник", 5, 10)
        return figure.angles

    def check_area(self, value1, value2):
        figure = Rectangle("прямоугольник", value1, value2)
        return figure.area

    def check_perimeter(self, value1, value2):
        figure = Rectangle("круг", value1, value2)
        return figure.perimeter

    def check_add_square(self, value1, value2, value3):
        figure_1 = Rectangle("прямоугольник", value1, value2)
        figure_2 = Square("квадрат", value3)
        return round((figure_1.area + figure_2.area), 4)

# Фикстуры Rectangle
@pytest.fixture
def fixture_rectangle():
    return TestClassRectangle()


# Тестовый класс фигуры Triangle
class TestClassTriangle:
    def check_name(self, value):
        figure = Triangle(value, 5, 5, 5)
        return figure.name

    def check_angles(self):
        figure = Triangle("треугольник", 5, 5, 5)
        return figure.angles

    def check_area(self, value1, value2, value3):
        figure = Triangle("треугольник", value1, value2, value3)
        return figure.area

    def check_perimeter(self, value1, value2, value3):
        figure = Triangle("треугольник", value1, value2, value3)
        return figure.perimeter

    def check_add_square(self, value1, value2, value3, value4):
        figure_1 = Triangle("треугольник", value1, value2, value3)
        figure_2 = Circle("круг", value4)
        return round((figure_1.area + figure_2.area), 4)

# Фикстуры Triangle
@pytest.fixture
def fixture_triangle():
    return TestClassTriangle()

import pytest


# Тесты для фигуры класса Square
class TestSquare:
    # Проверка имени фигуры - позитивная
    @pytest.mark.parametrize("value", ["КваДраТ", "квадрат", "square", "abcd", "12345"])
    def test_square_check_name(self, fixture_square, value):
        assert fixture_square.check_name(value) == value, \
            "Имя Квадрата неправильное"

    # Проверка имени фигуры - негативная - не строка
    @pytest.mark.parametrize("value", [123, True])
    def test_square_check_name_negative(self, fixture_square, value):
        try:
            fixture_square.check_name(value)
            assert False, "Передана строка"
        except TypeError:
            assert True, "Допустимо имя типа string"

    # Проверка углов
    def test_square_check_angles(self, fixture_square):
        assert fixture_square.check_angles() == 4, "У квадрата не 4 угла"

    # Проверка площади фигуры - позитивная
    @pytest.mark.parametrize("value, expected", [(20, 400), (30, 900),
                                                 (5, 25), (12, 144),
                                                 (100, 10000)])
    def test_square_check_area(self, fixture_square, value, expected):
        assert fixture_square.check_area(value) == expected, "Неправильная площадь квадрта"

    # Проверка площади фигуры - негативная - стороны не числа
    @pytest.mark.parametrize("value", ["test", True, "123"])
    def test_square_check_area_negative_not_number(self, fixture_square, value):
        try:
            fixture_square.check_area(value)
            assert False, "Переданы числа"
        except TypeError:
            assert True, "Переданы числа"

    # Проверка площади фигуры - негативная - стороны отрицательные числа/ ноль
    @pytest.mark.parametrize("value", [-1, 0])
    def test_square_check_area_negative_less_zero(self, fixture_square, value):
        try:
            fixture_square.check_area(value)
            assert False, "Переданы положительные числа"
        except ValueError:
            assert True, "Переданы положительные числа"

    # Проверка периметра фигуры
    @pytest.mark.parametrize("value, expected", [(2, 8), (18, 72),
                                                 (43, 172), (29, 116),
                                                 (1000, 4000)])
    def test_square_check_perimeter(self, fixture_square, value, expected):
        assert fixture_square.check_perimeter(value) == expected, \
            "Неправильный периметр квадрата"

    # Проверка метода add_square()
    @pytest.mark.parametrize("value1, value2, expected", [(10, 35, 3948.451),
                                                          (11, 64, 12988.9635),
                                                          (1, 1, 4.1416)])
    def test_square_add_square(self, fixture_square, value1, value2, expected):
        assert fixture_square.check_add_square(value1, value2) == expected, \
            "Сумма площадей Квадрата и Круга неверная"


# Тесты для фигуры класса Circle
class TestCircle:
    # Проверка имени фигуры - позитивная
    @pytest.mark.parametrize("value", ["Круг", "krug", "круг", "Тест", "7892734"])
    def test_circle_check_name(self, fixture_circle, value):
        assert fixture_circle.check_name(value) == value, \
            "Имя Круга неправильное"

    # Проверка имени фигуры - негативная - не строка
    @pytest.mark.parametrize("value", [123, True])
    def test_circle_check_name_negative(self, fixture_circle, value):
        try:
            fixture_circle.check_name(value)
            assert False, "Передана строка"
        except TypeError:
            assert True, "Допустимо имя типа string"

    # Проверка углов
    def test_circle_check_angles(self, fixture_circle):
        assert fixture_circle.check_angles() == 0, \
            "У круга не 0 углов"

    # Проверка площади фигуры - позитивная
    @pytest.mark.parametrize("value, expected", [(5, 78.5398), (13, 530.9292),
                                                 (54, 9160.8842), (86, 23235.2193),
                                                 (100, 31415.9265)])
    def test_circle_check_area(self, fixture_circle, value, expected):
        assert fixture_circle.check_area(value) == expected, "Неправильная площадь круга"

    # Проверка площади фигуры - негативная - стороны не числа
    @pytest.mark.parametrize("value", ["test", True, "123"])
    def test_circle_check_area_negative_not_number(self, fixture_circle, value):
        try:
            fixture_circle.check_area(value)
            assert False, "Переданы числа"
        except TypeError:
            assert True, "Переданы числа"

    # Проверка площади фигуры - негативная - стороны отрицательные числа/ ноль
    @pytest.mark.parametrize("value", [-1, 0])
    def test_circle_check_area_negative_less_zero(self, fixture_circle, value):
        try:
            fixture_circle.check_area(value)
            assert False, "Переданы положительные числа"
        except ValueError:
            assert True, "Переданы положительные числа"

    # Проверка периметра фигуры
    @pytest.mark.parametrize("value, expected", [(2, 12.5664), (16, 100.531),
                                                 (22, 138.2301), (54, 339.292),
                                                 (1000, 6283.1853)])
    def test_circle_check_perimeter(self, fixture_circle, value, expected):
        assert fixture_circle.check_perimeter(value) == expected, "Неправильный периметр круга"

    # Проверка метода add_square()
    @pytest.mark.parametrize("value1, value2, value3, expected",
                             [(2, 5, 10, 62.5664), (10, 15, 20, 614.1593), (33, 2, 19, 3459.1944)])
    def test_circle_add_square(self, fixture_circle, value1, value2, value3, expected):
        assert fixture_circle.check_add_square(value1, value2, value3) == expected, \
            "Сумма площадей Прямоугольника и Круга неверная"


# Тесты для фигуры класса Rectangle
class TestRectangle:
    # Проверка имени фигуры - позитивная
    @pytest.mark.parametrize("value", ["Прямоугольник", "прямоугольник",
                                       "123", "Rectangle", "rect"])
    def test_rect_check_name(self, fixture_rectangle, value):
        assert fixture_rectangle.check_name(value) == value, \
            "Имя Прямоугольника неправильное"

    # Проверка имени фигуры - негативная - не строка
    @pytest.mark.parametrize("value", [123, True])
    def test_rect_check_name_negative(self, fixture_rectangle, value):
        try:
            fixture_rectangle.check_name(value)
            assert False, "Передана строка"
        except TypeError:
            assert True, "Допустимо имя типа string"

    # Проверка углов
    def test_rect_check_angles(self, fixture_rectangle):
        assert fixture_rectangle.check_angles() == 4, "У прямоугольника не 4 угла"

    # Проверка площади фигуры - позитивная
    @pytest.mark.parametrize("value1, value2, expected",
                             [(2, 10, 20), (13, 14, 182),
                              (43, 56, 2408), (90, 100, 9000),
                              (61, 9, 549)])
    def test_rect_check_area(self, fixture_rectangle, value1, value2, expected):
        assert fixture_rectangle.check_area(value1, value2) == expected, \
            "Неправильная площадь прямоугольника"

    # Проверка площади фигуры - негативная - стороны не числа
    @pytest.mark.parametrize("value1, value2", [("test", True), ("123", False)])
    def test_rect_check_area_negative_not_number(self, fixture_rectangle, value1, value2):
        try:
            fixture_rectangle.check_area(value1, value2)
            assert False, "Переданы числа"
        except TypeError:
            assert True, "Переданы числа"

    # Проверка площади фигуры - негативная - стороны отрицательные числа/ ноль
    @pytest.mark.parametrize("value1, value2", [(-1, 0), (1, -10)])
    def test_rect_check_area_negative_less_zero(self, fixture_rectangle, value1, value2):
        try:
            fixture_rectangle.check_area(value1, value2)
            assert False, "Переданы положительные числа"
        except ValueError:
            assert True, "Переданы положительные числа"

    # Проверка периметра фигуры
    @pytest.mark.parametrize("value1, value2, expected",
                             [(6, 12, 36), (111, 14, 250), (34, 44, 156),
                              (7, 26, 66), (100, 100, 400)])
    def test_rect_check_perimeter(self, fixture_rectangle, value1, value2, expected):
        assert fixture_rectangle.check_perimeter(value1, value2) == expected, \
            "Неправильный периметр прямоугольника"

    # Проверка метода add_square()
    @pytest.mark.parametrize("value1, value2, value3, expected",
                             [(6, 12, 5, 97), (13, 26, 1, 339), (37, 200, 1000, 1007400)])
    def test_rect_add_square(self, fixture_rectangle, value1, value2, value3, expected):
        assert fixture_rectangle.check_add_square(value1, value2, value3) == expected, \
            "Сумма площадей Прямоугольника и Квадрата неверная"


# Тесты для фигуры класса Triangle
class TestTriangle:
    # Проверка имени фигуры - позитивная
    @pytest.mark.parametrize("value", ["Треугольник", "тРеуГольник",
                                       "triangle", "some_name", "3-angle"])
    def test_triangle_check_name(self, fixture_triangle, value):
        assert fixture_triangle.check_name(value) == value, \
            "Имя Треугольника неправильное"

    # Проверка имени фигуры - негативная - не строка
    @pytest.mark.parametrize("value", [123, True])
    def test_triangle_check_name_negative(self, fixture_triangle, value):
        try:
            fixture_triangle.check_name(value)
            assert False, "Передана строка"
        except TypeError:
            assert True, "Допустимо имя типа string"

    # Проверка углов
    def test_triangle_check_angles(self, fixture_triangle):
        assert fixture_triangle.check_angles() == 3, "У треугольника не 3 угла"

    # Проверка площади фигуры - позитивная
    @pytest.mark.parametrize("value1, value2, value3, expected",
                             [(200, 300, 400, 29047.3751), (5, 5, 5, 10.8253),
                              (7, 8, 9, 26.8328), (3, 7, 9, 8.7856), (4, 5, 6, 9.9216)])
    def test_triangle_check_area(self, fixture_triangle, value1, value2, value3, expected):
        assert fixture_triangle.check_area(value1, value2, value3) == expected, \
            "Неправильная площадь треугольника"

    # Проверка площади фигуры - негативная - стороны не числа
    @pytest.mark.parametrize("value1, value2, value3",
                             [("test", True, "123"), ("123", False, "some")])
    def test_triangle_check_area_negative_not_number(self, fixture_triangle,
                                                     value1, value2, value3):
        try:
            fixture_triangle.check_area(value1, value2, value3)
            assert False, "Переданы числа"
        except TypeError:
            assert True, "Переданы числа"

    # Проверка площади фигуры - негативная - стороны отрицательные числа/ ноль
    @pytest.mark.parametrize("value1, value2, value3", [(-1, -10, 0), (0, 1, -7)])
    def test_triangle_check_area_negative_less_zero(self, fixture_triangle, value1, value2, value3):
        try:
            fixture_triangle.check_area(value1, value2, value3)
            assert False, "Переданы положительные числа"
        except ValueError:
            assert True, "Переданы положительные числа"

    # Проверка периметра фигуры
    @pytest.mark.parametrize("value1, value2, value3, expected",
                             [(200, 300, 400, 900), (5, 5, 5, 15),
                              (7, 8, 9, 24), (3, 7, 9, 19), (4, 5, 6, 15)])
    def test_triangle_check_perimeter(self, fixture_triangle, value1, value2, value3, expected):
        assert fixture_triangle.check_perimeter(value1, value2, value3) == expected, \
            "Неправильный периметр треугольника"

    # Проверка метода add_square()
    @pytest.mark.parametrize("value1, value2, value3, value4, expected",
                             [(200, 300, 400, 3, 29075.6494),
                              (5, 5, 5, 24, 1820.3827),
                              (7, 8, 9, 55, 9530.1506)])
    def test_triangle_add_square(self, fixture_triangle, value1, value2, value3, value4, expected):
        assert fixture_triangle.check_add_square(value1, value2, value3, value4) == expected, \
            "Сумма площадей Круга и Треугольника неверная"

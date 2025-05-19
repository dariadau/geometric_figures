import doctest
from math import pi


class Circle:
    def __init__(self, radius):
        """
        Создание и подготовка к работе объекта "Окружность"

        :param radius: радиус окружности

        Примеры:
        >>> circ = circle_formulas(2)  # инициализация экземпляра класса
        """

        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус должен быть типа int или float")
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def circ_area(self):
        """
        Данная функция определяет площадь прямоугольника

        :return: Площаль окружности

        Примеры:
        >>> circ_a = circle_formulas(2)
        >>> circ_a.circ_area()
        25.132741228718345
        """

        return 2 * pi * self.radius ** 2

    def circ_perimeter(self):
        """
        Данная функция определяет периметр окружности

        :return: Периметр окружности

        Примеры:
        >>> circ_b = circle_formulas(2)
        >>> circ_b.circ_perimeter()
        12.566370614359172
        """

        return pi * self.radius ** 2

    def circ_sector_area(self, angle):
        """
        Данная функция определяет Площадь сектора (часть круга, которая ограничена двумя
        радиусами и дугой между этими радиусами)

        :return: Площадь сектора

        Примеры:
        >>> circ_с = circle_formulas(2)
        >>> circ_с.circ_sector_area(30)
        1.0471975511965976
        """

        if not isinstance(angle, (int, float)):
            raise TypeError("Угол сектора должен быть типа int или float")
        if angle <= 0:
            raise ValueError("Угол сектора должен быть положительным числом")
        self.angle = angle

        return (pi * self.radius ** 2) / 360 * self.angle


doctest.testmod()  # тестирование примеров, которые находятся в документации

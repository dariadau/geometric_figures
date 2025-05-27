import doctest
from math import pi


class Circle:
    def __init__(self, radius, angle=0):
        """
        Создание и подготовка к работе объекта "Окружность"

        Примеры:
        >>> circ_a = Circle(5)  # инициализация экземпляра класса
        >>> circ_b = Circle(5, 30)    # инициализация экземпляра класса
        """

        self.radius = None
        self.angle = None
        self.define_values(radius, angle)

    def define_values(self, radius, angle=0):
        """
        Функция для задания и согласования аргументов для присваивания атрибутов экземпляров класса

        :param radius: радиус окружности
        :param angle: угол окружности

        Пример:
        >>> circ_c = Circle(-3)
        Traceback (most recent call last):
        ...
        ValueError: Радиус должен быть положительным числом
        >>> circ_c = Circle(3, -30)
        Traceback (most recent call last):
        ...
        ValueError: Угол сектора должен быть положительным числом
        >>> circ_c = Circle('3', 30)
        Traceback (most recent call last):
        ...
        TypeError: Радиус должен быть типа int или float
        >>> circ_c = Circle(3, '30')
        Traceback (most recent call last):
        ...
        TypeError: Угол сектора должен быть типа int или float
        """

        if radius:
            if not isinstance(radius, (int, float)):
                raise TypeError("Радиус должен быть типа int или float")
            if radius <= 0:
                raise ValueError("Радиус должен быть положительным числом")
            self.radius = radius

        if angle:
            if not isinstance(angle, (int, float)):
                raise TypeError("Угол сектора должен быть типа int или float")
            if angle <= 0:
                raise ValueError("Угол сектора должен быть положительным числом")
            self.angle = angle

    def circ_area(self):
        """
        Данная функция определяет площадь окружности

        :return: Площаль окружности

        Примеры:
        >>> circ_a = Circle(2)
        >>> circ_a.circ_area()
        25.132741228718345
        """

        return 2 * pi * self.radius ** 2

    def circ_perimeter(self):
        """
        Данная функция определяет периметр окружности

        :return: Периметр окружности

        Примеры:
        >>> circ_b = Circle(2)
        >>> circ_b.circ_perimeter()
        12.566370614359172
        """

        return pi * self.radius ** 2

    def circ_sector_area(self):
        """
        Данная функция определяет Площадь сектора (часть круга, которая ограничена двумя
        радиусами и дугой между этими радиусами)

        :return: Площадь сектора

        Примеры:
        >>> circ_с = Circle(2, 30)
        >>> circ_с.circ_sector_area()
        1.0471975511965976
        """

        return (pi * self.radius ** 2) / 360 * self.angle


doctest.testmod()  # тестирование примеров, которые находятся в документации

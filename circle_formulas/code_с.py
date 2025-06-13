import doctest
from math import pi


class Circle:
    def __init__(self, radius: float, angle: float = 0):
        """
        Создание и подготовка к работе объекта "Окружность"

        Примеры:
        >>> circ_a = Circle(5)  # инициализация экземпляра класса
        >>> circ_b = Circle(5, 30)    # инициализация экземпляра класса
        """

        self.radius = None
        self.angle = None
        self.define_values(radius, angle)

    def define_values(self, radius: float, angle: float = 0):
        """
        Метод для задания и согласования аргументов для присваивания атрибутов экземпляров класса

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
        ValueError: Угол сектора должен быть неотрицательным числом
        >>> circ_c = Circle('3', 30)
        Traceback (most recent call last):
        ...
        TypeError: Радиус должен быть типа int или float
        >>> circ_c = Circle(3, '30')
        Traceback (most recent call last):
        ...
        TypeError: Угол сектора должен быть типа int или float
        """

        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус должен быть типа int или float")
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

        if not isinstance(angle, (int, float)):
            raise TypeError("Угол сектора должен быть типа int или float")
        if angle < 0:
            raise ValueError("Угол сектора должен быть неотрицательным числом")
        self.angle = angle

    def __str__(self):
        return f'Класс для использования формул окружности. Угол = {self.angle}, радиус = {self.radius}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.radius}, {self.angle})'

    def change_radius(self, x):
        """
        Метод для замены значения радиуса окружности

        :param x: новое значение для радиуса окружности

        Примеры:
        >>> rec_c = Circle(1, 2)
        >>> rec_c.change_radius(3)
        """
        if not isinstance(x, (int, float)):
            raise TypeError("Радиус окружности должен быть типа int или float")
        if x <= 0:
            raise ValueError("Радиус окружности должен быть положительным числом")
        self.radius = x

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

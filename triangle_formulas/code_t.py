import doctest
from math import sqrt


class Triangle:
    triangle_counter = 0  # счетчик созданных фигур

    def __init__(self, x, y, z):
        """
        Создание и подготовка к работе объекта "Треугольник"

        Примеры:
        >>> tri = Triangle(1, 2, 4)  # инициализация экземпляра класса
        """

        self.x = None
        self.y = None
        self.z = None
        self.value_check(x, y, z)

    def value_check(self, x, y, z):
        """
        Создание и подготовка к работе объекта "Треугольник"

        :param x: 1 сторона треугольника
        :param y: 2 сторона треугольника
        :param z: 3 сторона треугольника

        Примеры:
        >>> tri_a = Triangle(0, 1, 2)
        Traceback (most recent call last):
        ...
        ValueError: Сторона треугольника должна быть положительным числом
        >>> tri_b = Triangle(1, '2', 4)
        Traceback (most recent call last):
        ...
        TypeError: Сторона треугольника должна быть типа int или float
        """

        if not isinstance(x, (int, float)):
            raise TypeError("Сторона треугольника должна быть типа int или float")
        if x <= 0:
            raise ValueError("Сторона треугольника должна быть положительным числом")

        if not isinstance(y, (int, float)):
            raise TypeError("Сторона треугольника должна быть типа int или float")
        if y <= 0:
            raise ValueError("Сторона треугольника должна быть положительным числом")

        if not isinstance(z, (int, float)):
            raise TypeError("Сторона треугольника должна быть типа int или float")
        if z <= 0:
            raise ValueError("Сторона треугольника должна быть положительным числом")

        if not (x + y > z or x + z > y or z + y > x):
            raise ValueError('''Сумма длин двух любых сторон треугольника должна быть больше длины 
                оставшейся стороны''')

        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Класс для использования формул треугольника. Треугольник имеет следующие стороны: x = {self.x}, y = {self.y}, z = {self.z}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y}, {self.z})'

    @classmethod
    def incr_counter(cls):
        """
        Метод, который увеличивает число уже созданных треугольников
        """

        cls.triangle_counter += 1

    def change_side_x(self, x):
        """
        Метод для замены длины стороны x

        :param x: новое значение для стороны x

        Примеры:
        >>> rec_c = Triangle(1, 2, 3)
        >>> rec_c.change_side_x(4)
        """
        if not isinstance(x, (int, float)):
            raise TypeError("Сторона x должна быть типа int или float")
        if x <= 0:
            raise ValueError("Сторона x должна быть положительной")
        self.x = x

    def tri_area(self):
        """
        Данная функция определяет площадь треугольника

        :return: Площаль треугольника

        Примеры:
        >>> tri_a = Triangle(1, 2, 3)
        >>> tri_a.tri_area()
        0.0
        """

        p = (self.x + self.y + self.z) / 2
        return sqrt(p * (p - self.x) * (p - self.y) * (p - self.z))

    def tri_perimeter(self):
        """
        Данная функция определяет периметр треугольника

        :return: Периметр треугольника

        Примеры:
        >>> tri_b = Triangle(1, 2, 3)
        >>> tri_b.tri_perimeter()
        6
        """

        return self.x + self.y + self.z

    def tri_type(self):
        """
        Данная функция определяет тип треугольника: разносторонний, равнобедренный
        или равносторонним

        :return: Тип треугольника

        Примеры:
        >>> tri_c = Triangle(1, 2, 3)
        >>> tri_c.tri_type()
        'Разносторонний'
        """

        if self.x == self.y == self.z:
            result = 'Равносторонний'
        elif (self.x == self.y and self.x != self.z) or (self.x == self.z and self.x != self.y) or (
                self.z == self.y and self.z != self.x):
            result = 'Равнобедренный'
        else:
            result = 'Разносторонний'

        return result


doctest.testmod()  # тестирование примеров, которые находятся в документации

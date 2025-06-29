import doctest


class Rectangle:
    rectangle_counter = 0  # счетчик созданных фигур

    def __init__(self, length: float, width: float):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        Примеры:
        >>> rec = Rectangle(1, 2)  # инициализация экземпляра класса
        """

        self.length = None
        self.width = None
        self.values(length, width)

    def values(self, length, width):
        """
        Функция для задания и согласования аргументов для присваивания атрибутов экземпляров класса

        :param length: длина прямоугольника
        :param width:  ширина прямоугольника

        Примеры:
        >>> rec = Rectangle('1', 2)
        Traceback (most recent call last):
        ...
        TypeError: Длина прямоугольника должна быть типа int или float
        >>> rec = Rectangle(-1, 2)
        Traceback (most recent call last):
        ...
        ValueError: Длина прямоугольника должен быть положительным числом
        >>> rec = Rectangle(1, '2')
        Traceback (most recent call last):
        ...
        TypeError: Ширина прямоугольника должна быть int или float
        >>> rec = Rectangle(1, -2)
        Traceback (most recent call last):
        ...
        ValueError: Ширина прямоугольника не может быть отрицательным числом
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина прямоугольника должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина прямоугольника должен быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина прямоугольника должна быть int или float")
        if width < 0:
            raise ValueError("Ширина прямоугольника не может быть отрицательным числом")
        self.width = width

    def __str__(self):
        return f'Класс для использования формул прямоугольника. Параметры: длина = {self.length}, ширина = {self.width}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.length}, {self.width})'

    def change_length(self, changer):
        """
        Метод для замены значения длины прямоугольника

        :param changer: новое значение для длины прямоугольника

        Примеры:
        >>> rec_a = Rectangle(1, 2)
        >>> rec_a.change_length(3)
        """
        if not isinstance(changer, (int, float)):
            raise TypeError("Длина прямоугольника должна быть типа int или float")
        if changer <= 0:
            raise ValueError("Длина прямоугольника должен быть положительным числом")
        self.length = changer

    def rec_area(self):
        """
        Данная функция определяет площадь прямоугольника

        :return: Площаль прямоугольника

        Примеры:
        >>> rec_a = Rectangle(1, 2)
        >>> rec_a.rec_area()
        2
        """

        return self.length * self.width

    def rec_perimeter(self):
        """
        Данная функция определяет периметр прямоугольника

        :return: Периметр прямоугольника

        Примеры:
        >>> rec_b = Rectangle(1, 2)
        >>> rec_b.rec_perimeter()
        6
        """

        return 2 * (self.length + self.width)

    def rec_diagonal(self):
        """
        Данная функция определяет диаметр прямоугольника

        :return: Диаметр прямоугольника

        Примеры:
        >>> rec_c = Rectangle(4, 3)
        >>> rec_c.rec_diagonal()
        5.0
        """

        return ((self.length ** 2) + (self.width ** 2)) ** (1 / 2)

    @classmethod
    def incr_counter(cls):
        """
        Метод, который увеличивает число уже созданных прямоугольников
        """

        cls.rectangle_counter += 1


doctest.testmod()  # тестирование примеров, которые находятся в документации

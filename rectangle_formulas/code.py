import doctest


class Rectangle:
    def __init__(self, length: float, width: float):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param length: длина прямоугольника
        :param width: ширина прямоугольника

        Примеры:
        >>> rec = rectangle_formulas(1, 2)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина прямоугольника должна быть типа int или float")
        if length < 0:
            raise ValueError("Длина прямоугольника должен быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина прямоугольника должно быть int или float")
        if width < 0:
            raise ValueError("Ширина прямоугольника не может быть отрицательным числом")
        self.width = width

    def rec_area(self):
        """
        Данная функция определяет площадь прямоугольника

        :return: Площаль прямоугольника

        Примеры:
        >>> rec_a = rectangle_formulas(1, 2)
        >>> rec_a.rec_area()
        2
        """

        return self.length * self.width

    def rec_perimeter(self):
        """
        Данная функция определяет периметр прямоугольника

        :return: Периметр прямоугольника

        Примеры:
        >>> rec_b = rectangle_formulas(1, 2)
        >>> rec_b.rec_perimeter()
        6
        """

        return 2 * (self.length + self.width)

    def rec_diagonal(self):
        """
        Данная функция определяет диаметр прямоугольника

        :return: Диаметр прямоугольника

        Примеры:
        >>> rec_c = rectangle_formulas(4, 3)
        >>> rec_c.rec_diagonal()
        5.0
        """

        return ((self.length ** 2) + (self.width ** 2)) ** (1 / 2)


doctest.testmod()  # тестирование примеров, которые находятся в документации
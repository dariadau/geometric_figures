# geometric_figures
В данной библиотеке представлены формулы для окружности, прямоугольника и треугольника

## Структура проекта
```bash
circle_formulas/  
     ├── __init__.py  
     └── code_с.py  
rectangle_formulas/  
     ├── __init__.py  
     └── code_r.py  
triangle_formulas/  
     ├── __init__.py  
     └── code_t.py  
__init__.py  
README.md
```

## 🟠circle_formulas

В данном пакете содержатся формулы для окружности:  
* circ_area() → площадь окружности
* circ_perimeter() → длина окружности
* sector_area() → площадь сектора
Все вышеперечисленные формулами являются методами класса Circle

Требуемые аргументы для работы класса:
* radius - радиус окружности
  Поддерживаемый тип данных: int, float (требуется для расчета площади сектора)
* angle - угол в градусах __(только для работы метода sector_area)__
  Поддерживаемый тип данных: int, float


Пример: __Площадь окружности__

```bash
from geometric_figures import Circle

radius = 5
c = Circle(radius)
print("Площадь окружности:", c.circ_area())  # Вывод: 78.5
```  

Пример: __Периметр окружности__
```bash
from geometric_figures import Circle

print("Периметр окружности:", c.circ_perimeter())  # Вывод: 31.4
```


Пример: __Площадь сектора окружности__
```bash
from geometric_figures import Circle

angle = 90
print("Площадь сектора:", c.sector_area(angle))  # Вывод: 19.625
```

## 🟩 rectangle_formulas

В данном пакете содержатся формулы для прямоугольника:  
* rectangle_area() → площадь прямоугольника
* rectangle_perimeter() → периметр прямоугольника
* rectangle_diagonal() → длина диагонали
  Все вышеперечисленные формулами являются методами класса Rectangle

Требуемые аргументы для работы класса:
* width - ширина прямоугольника  
  Поддерживаемый тип данных: int, float
* length - длина прямоугольника  
  Поддерживаемый тип данных: int, float

__Площадь прямоугольника__

```bash
from geometric_figures import Rectangle

width, length = 4, 5
r = Rectangle(width, length)
print("Площадь прямоугольника:", r.rectangle_area())  # Вывод: 20
```  

Пример: __Периметр прямоугольника__
```bash
from geometric_figures import Rectangle

print("Периметр прямоугольника:", r.rectangle_perimeter())  # Вывод: 18
```

Пример: __Диагональ прямоугольника__
```bash
from geometric_figures import Rectangle

print("Диагональ прямоугольника:", r.rectangle_diagonal())  # Вывод: ~6.4
```

## 🔺triangle_formulas

В данном пакете содержатся формулы для треугольника:  

* triangle_area() → площадь треугольника
* triangle_perimeter() → периметр треугольника
* triangle_type() → определяет тип треугольника (равносторонний, равнобедренный, разносторонний)
  Все вышеперечисленные формулами являются методами класса Triangle

Требуемые аргументы для работы класса:
* a, b, c - стороны треугольника 
  Поддерживаемый тип данных: int, float

> [!WARNING]
> Сумма длин двух любых сторон треугольника больше длины оставшейся стороны:  
> a + b > c  
> b + c > a  
> c + a > b  

Пример: __Площадь треугольника__
```bash
from geometric_figures import Triangle

base, height = 6, 4
t = Triangle(base, height, 5)
print("Площадь треугольника:", t.triangle_area())  # Вывод: 12.0
```

Пример: __Периметр треугольника__
```bash
from geometric_figures import Triangle

a, b, c = 3, 4, 5
t = Triangle(a, b, c)
print("Периметр треугольника:", t.triangle_perimeter(a, b, c))  # Вывод: 12
```

Пример: __Тип треугольника__
```bash
from geometric_figures import Triangle

print("Тип треугольника:", t.triangle_type(5, 5, 5))  # Вывод: Равносторонний
print("Тип треугольника:", t.triangle_type(5, 5, 6))  # Вывод: Равнобедренный
print("Тип треугольника:", t.triangle_type(3, 4, 5))  # Вывод: Разносторонний
```

## Установка

```bash
git clone https://github.com/dariadau/geometric_figures.git

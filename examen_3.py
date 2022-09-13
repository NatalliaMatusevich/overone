from abc import ABC, abstractmethod
import math


# 1
# Напишите функцию, которая
# # будет принимать номер
# # кредитной карты и показывать
# # только последние 4 цифры.
# # Остальные цифры должны
# # заменяться звездочками

def card_hide(num):
    num_ls = [int(i) for i in str(num)]
    ls_4 = num_ls[-4:]
    s = ''.join(str(x) for x in ls_4)
    return '*' * len(num_ls[:-4]) + s[-4:]

print(card_hide(5456789515658562))

# 2
# Напишите функцию, которая
# проверяет: является ли слово
# палиндромом

def is_palindrom(s):
    if len (s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrom(s[1:-1])

print(is_palindrom('summer'))
print(is_palindrom('шалаш'))

# 3
# Напишите классы Круг,
# Прямоугольник, Квадрат.
# Каждый класс должен
# содержать метод нахождения
# площади фигуры.
# Используйте
# :
# - Наследование - Абстрактный класс
# и методы
# - Округлите площадь круга до 2х чисел после запятой -
# Число π возьмите из модуля math

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Figure):
    def __init__(self, a):
        self.a = a

    def area(self):
        return f'Площадь квадрата = {4 * self.a}'


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return f'Площадь прямоугольника = {self.a * self.b}'


class  Circle(Figure):
    def __init__(self, r):
        self.r = r

    def area(self):
        return f'Площадь круга = {round(math.pi * self.r ** 2, 2)}'


square = Square(4)
rectangle = Rectangle(2,6)
circle = Circle(3)

figures =[square, rectangle, circle]
for i in figures:
    print(i.area())
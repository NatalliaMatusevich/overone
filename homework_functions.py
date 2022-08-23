# задача 1
# Из полученного списка чисел
# создайте список с суммами
# этих чисел, отсортированными
# по возрастанию

# ls = []
#
# def summ(nums):
#     for i in nums:
#         while i != 0:
#             summm = 0
#             i = i % 10
#             summm += i
#             ls.append(summm)
#             i // 10
#     return ls
#
# nums = [int(i) for i in input().split()]
# print(summ(nums))

#
# задача 2
# Напишите функцию которая
# принимает на вход список
# целых чисел, удаляет из него
# все нечётные значения, а
# чётные нацело делит на два.
#
# ls = []
#
# def even_nums(numbers):
#     for i in numbers:
#         if i % 2 == 0:
#             ls.append(int(i / 2))
#     return ls
#
# numbers = [int(i) for i in input().split()]
# print(even_nums(numbers))

# задача 3

# Напишите функцию f(x), которая
# возвращает значение следующей
# функции, определённой на всей
# числовой прямой:
# def f(x):
#     if x <= -2:
#         return 1 - (x + 2) ** 2
#     elif -2 < x <= 2:
#         return -(x / 2)
#     elif 2 < x:
#         return (x - 2) ** 2 + 1
#
# print(f(4.5))


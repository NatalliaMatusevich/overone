# задание 4_1
num = int(input())
if num < 0:
    print('отрицательное число')
elif num > 0:
    print('положительное число')
elif num == 0:
    print('Запрос отклонен, нужно было вводить любое число, кроме "0"')
# задание 4_2
t = float(input('Введите температуру: '))
degree = input('Введите вид градусов:\nC - по Цельсию, F - по Форенгейту: ')
if degree == 'F':
    print((t-32) * 5 / 9, '°C')
elif degree == 'C':
    print(9 / 5 * t + 32, '°F')
elif degree != 'F' and degree != 'C':
    print('У Вас осталась одна попытка, внимательно вводите данные')
    t = float(input('Введите температуру: '))
    degree_2 = input('Введите вид градусов:\nC - по Цельсию, F - по Форенгейту: ')
    if degree_2 == 'F':
        print((t - 32) * 5 / 9, '°C')
    elif degree_2 == 'C':
        print(9 / 5 * t + 32, '°F')
    else:
        print('Извините, запрос отклонен')
# задание 4_3
num_1 = float(input())
num_2 = float(input())
oper = input()
if oper == "+":
    print(num_1 + num_2)
elif oper == "-":
    print(num_1 - num_2)
elif oper == "/":
    print(num_1 / num_2)
elif oper == "*":
    print(num_1 * num_2)
# задание 4_4
w_1 = list(input())
w_2 = list(input())
if (sorted(w_1)) == (sorted(w_2)):
    print('anagram')
else:
    print('just words')
# задача 4_5
age = int(input())
yasli = ["Анна", "Мария", "Инна", "Петр", "Иван"]
srednyaa = ["Артем", "Кирилл", "Светлана", "Алексей"]
starshaya = ["Наталья", "Денис", "Даниил"]
if age < 1:
    print("Заведующая сказала: 'Вам еще очень рано в детский сад!'")
if 1 <= age < 3:
    print("Максим принят в ясельную группу")
    yasli_2 = yasli.append('Максим')
    yasli_3 = yasli.sort()
    print(yasli)
    print(len(yasli))
if 3 <= age < 5:
    print("Максим принят в среднюю группу")
    srednyaa_2 = srednyaa.append('Максим')
    srednyaa_3 = srednyaa.sort()
    print(srednyaa)
    print(len(srednyaa))
if 5 <= age < 7:
    print("Максим принят в старшую группу")
    starshaya_2 = starshaya.append('Максим')
    starshaya_3 = starshaya.sort()
    print(starshaya)
    print(len(starshaya))
if age >= 7:
    print("Заведующая сказала: 'Вы что? Вам пора уже в школу!!!'")

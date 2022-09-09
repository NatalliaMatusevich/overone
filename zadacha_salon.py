# 14_8
# Создайте класс для салона красоты, чтобы можно было
# создавать дома с салоном красоты.
# Методы:
# - Маникюр
# - Стрижка
# Методы прописывать не надо, просто поставьте заглушку.

# 14_9
# Добавьте в салон красоты метод salon_opening_hours,
# который сообщает салон открыт или закрыт.
# Создайте дом с салоном красоты.
# Атрибуты:
# Час открытия салона
# Час закрытия салона
# Посмотрите работает ли салон в
# 13 часов, а в 23?

# 14_11
# Установите статичечкий атрибут
# мин цена в салоне красоты.
# Допишите методы:
# Маникюр стоит на 20% больше
# Стрижка зависит от длины волос:
# меньше 30см - +20%,
# От 30 до 50 см - +50%
# Свыше 50 см - +80%

class Building:
    def __init__(self, doors, windows, floors):
        self.doors = doors
        self.windows = windows
        self.floors = floors

    def build(self):
        print('The building was build')

    def destroy(self):
        print('The building was destroyed')


class SalonMixin:
    min_price = 20

    def manikur(self):
        return self.min_price + (self.min_price * 20 / 100)

    def strizhka(self, hair_length):
        if hair_length < 30:
            return self.min_price * 1.2
        elif hair_length >= 30 and hair_length <= 50:
            return self.min_price * 1.5
        elif hair_length > 50:
            return self.min_price * 1.8

    def salon_opening_hours(self, open_time, close_time, now_time=None):
        if now_time < open_time or now_time > close_time:
            print(f'Салон закрыт.')
        else:
            print(f'Салон открыт.')


class HouseWithSalon(Building, SalonMixin):
    def __init__(self, doors, windows, floors):
        super().__init__(doors, windows, floors)

dom = HouseWithSalon(10, 30, 3)
dom.salon_opening_hours(8, 22, 13)
print(dom.manikur())
print(dom.strizhka(31))
# 14_8 14_9
# класс салон красоты - миксин
# методы:
# - маникюр
# - стрижка
# - время работы
#
# создать класс дом с салоном красоты (наслелование)
# атрибуты:
# - время открытия
# - время закрытия
#
# вызвать метод в 13 часов, в 23

class Building:
    def __init__(self, doors, windows, floors):
        self.doors = doors
        self.windows = windows
        self.floors = floors

    def build(self):
        print('The building was build')

    def destroy(self):
        print('The building was destroyed')


class SalonBeautyMixin:
    pass

    def manikur(self):
        pass

    def strizhka(self):
        pass

    def time(self):
        pass

class HouseBeauty(Building, SalonBeautyMixin):
    def __init__(self, doors, windows, floors, open, close):
        super().__init__(doors, windows, floors)
        self.open = open
        self.close = close


    def salon_opening_hours(self, open, close):
        if open >= 8 and close < 22:
            print(f'Салон открыт')
        else:
            print(f'Салон закрыт')



dom = HouseBeauty(10, 30, 3, 8, 22)
dom.salon_opening_hours(9, 23)
# Создать три класса: Dog, Cat, Parrot.
# Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор
# и методы: run, jump, birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный метод fly,
# Cat - meow, Dog - bark.

# Создать родительский класс Pet,
# содержащий все общие методы классов
# Dog, Cat, Parrot.
# Унаследовать Dog, Cat, Parrot от класса Pet.
# Удалить в дочерних классах те методы, которые
# имеются у родительского класса.
# Создать объект каждого класса и
# вызвать все его методы.
#
class Pet:

    def run(self):
        print('Бегать!')

    def jump(self):
        print('Прыгать!')

    def birthday(self):
        print(self.age + 1)

    def sleep(self):
        print('Спать!')

class Dog(Pet):

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def bark(self):
        print('Лаять!')

class Cat(Pet):

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def meow(self):
        print('Мяукать!')

class Parrot(Pet):

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def fly(self):
        print('Летать!')

beagle = Dog('Lucky', 2, 'Dasha')
beagle.run(), beagle.jump(), beagle.birthday(), beagle.sleep(), beagle.bark()
print('**********')
siamese = Cat('Sima', 1, 'Danik')
siamese.run(), siamese.jump(), siamese.birthday(), siamese.sleep(), siamese.meow()
print('**********')
cockatiel = Parrot('Kesha', 3, 'Inna')
cockatiel.run(), cockatiel.jump(), cockatiel.birthday(), cockatiel.sleep(), cockatiel.fly()


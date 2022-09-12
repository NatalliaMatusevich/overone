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


class NonNegativeValue:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.name} cannot be negative")
        instance.__dict__[self.name] = value

class String:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if len(value) == 0:
            raise TypeError(f'Expected {self.name} cannot be empty')
        for i in value:
            if i.isalpha() == False:
                raise TypeError(f'Expected {self.name} to be from letters')
            instance.__dict__[self.name] = value



class Pet:
    age = NonNegativeValue()
    name = String()
    master = String()

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

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
        super().__init__(name, age, master)


    def bark(self):
        print('Лаять!')

class Cat(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def meow(self):
        print('Мяукать!')

class Parrot(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def fly(self):
        print('Летать!')


beagle = Dog('ggg', 5, '11')
beagle.run(), beagle.jump(), beagle.birthday(), beagle.sleep(), beagle.bark()
print('**********')
siamese = Cat('Sima', 1, 'Danik')
siamese.run(), siamese.jump(), siamese.birthday(), siamese.sleep(), siamese.meow()
print('**********')
cockatiel = Parrot('Kesha', 5, 'Inna')
cockatiel.run(), cockatiel.jump(), cockatiel.birthday(), cockatiel.sleep(), cockatiel.fly()

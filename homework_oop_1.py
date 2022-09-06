# 14/1
class Dog:

    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        return print('Прыгай!')

    def run(self):
        return print('Беги!')

    def back(self):
        return print('Назад!')

    def change_name(self):    # дополнение по задаче 14/2
        self.name = new_name


pug = Dog(2, 4, 'Lucky', 1)
pug.jump()
pug.run()
pug.back()
print(pug.__dict__)
# дополнение по задаче 14/2
new_name = input('Введите новое имя: ')
pug.change_name()
print(pug.name)




# Домашнее задание по теме "Зачем нужно наследование"

# Задача "Съедобное, несъедобное":
# 2 класса родителя: Animal, Plant
# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
# Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения
# 4 класса наследника:
# Mammal, Predator для Animal.
# Flower, Fruit для Plant.
# У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
# eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
# В данном случае можно использовать принцип наследования, чтобы не дублировать код.
# Метод eat должен работать следующим образом:
# Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
# Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
# Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.
# У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
# Пункты задачи:
# 1 Создайте классы Animal и Plant с соответствующими атрибутами и методами
# 2 Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами.
#   При необходимости переопределите значения атрибутов.
# 3 Создайте объекты этих классов.



class Animal:
    alive = True    # (живой)
    fed = False     # (накормленный)
    def __init__(self, name):
        self.name = name

class Plant:
    edible = False  # (съедобность)
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел(а) {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал(а) есть {food.name}')
            self.alive = False

class Predator(Animal):

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел(а) {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал(а) есть {food.name}')
            self.alive = False

class Flower(Plant): #Цветы
    pass
 #   edible = True

class Fruit(Plant):
    edible = True



animal1 = Predator('Волк')
animal2 = Mammal('Мартышка')
plant1 = Plant('Тюльпан')
plant2 = Fruit('Банан')

print(animal1.name)
print(plant1.name)

print(animal1.alive, f'- {animal1.name} живой')
print(animal2.fed, f'- {animal2.name} голоден(а)')

animal1.eat(plant1)
animal2.eat(plant2)
print(animal1.alive, f'- {animal1.name} помер(ла)')
print(animal2.fed, f'- {animal2.name} сыт(а)')
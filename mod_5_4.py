
# Домашняя работа по уроку "Различие атрибутов класса и экземпляра"

# Задача "История строительства":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
#
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
#
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса
# используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
#
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
#
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__,
# а также значение атрибута houses_history.


class House:
    houses_history = []     # атрибут будет хранить названия созданных объектов
    
    def __new__(cls, *args, **kwargs): # ,*args, **kwargs
        cls.houses_history.append(args[0])
        #print(*cls.houses_history)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
       self.name = name
       self.number_of_floors = number_of_floors

    def __len__(self):
         return self.number_of_floors
    
    def __add__(self, value):
        if type(value) in (int, float):
            return self.__class__(self.name, self.number_of_floors + value)
         

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):    # 1
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors == other

    def __lt__(self, other):    # 2
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors <= other


    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif type(other) in (int, float):
            return self.number_of_floors > other

   
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other.number_of_floors, (int, float)):
            return self.number_of_floors != other
                        

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self
    
    def __del__(self):
        print(self.name, ' снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(*House.houses_history)
h2 = House('ЖК Акация', 20)
print(*House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(*House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)


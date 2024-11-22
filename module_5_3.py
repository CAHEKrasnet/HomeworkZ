# Задача "Нужно больше этажей":

# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".

# Необходимо дополнить класс House следующими специальными методами:
# 1 __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# 2 Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. 
# Как и в методе __eq__ в сравнении участвует кол-во этажей.
# 3 __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# 4 __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
# Остальные методы арифметических операторов, где self - x, other - y:
# Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
# Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми действиями 
# лучше убедиться в принадлежности к типу при помощи функции isinstance:
# isinstance(other, int) - other указывает на объект типа int.
# isinstance(other, House) - other указывает на объект типа House.

# other может быть не только числом, но и вообще любым объектом другого класса.
# Для более точной логики работы методов __eq__, __add__ и других методов сравнения и арифметики перед выполняемыми действиями лучше убедиться 
# в принадлежности к типу при помощи функции isinstance
# Благодаря данной проверке, мы можем сравнивать как 2 объекта класса, в данном случае их этажи, так и объект класса с целым числом.
# def __eq__(self, other):
# if isinstance(other, House):
# return self.number_of_floors == other.number_of_floors
# elif isinstance(other, int):
# return self.number_of_floors == other
#  Так же метод __add__ должен возвращать объект класса.
# def __add__(self, value):
# if isinstance(value, int):
# return House(self.name, self.number_of_floors + value)

class House:
    def __init__(self, name, number_of_floors):
       self.name = name
       self.number_of_floors = number_of_floors

    def __len__(self):
         return self.number_of_floors
    
    def __add__(self, value):
        if type(value) in (int, float):
            return self.__class__(self.name, self.number_of_floors + value)
         

    def __str__(self):
       title = str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
       return title

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


hightower = House('Башня', 19)
warehouse = House('Склад', 2)

print(hightower)
print(warehouse)
# 1
print(hightower == warehouse)
# 3
print(warehouse.__add__(4))
print(hightower == warehouse)
# 2
print(hightower < warehouse)
print(hightower <= warehouse)
print(hightower > warehouse)
print(hightower >= warehouse)
print(hightower != warehouse)
# 5
print(hightower.__radd__(7))
print(warehouse.__iadd__('8')) # не прибавляется
print(warehouse.__iadd__(8))

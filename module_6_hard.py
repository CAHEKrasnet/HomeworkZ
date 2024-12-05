# Задание "Они все так похожи":
# Общее ТЗ:
# Реализовать классы Figure(родительский),
# Circle, Triangle и Cube, объекты которых будут обладать методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия
# (методы) - геттеры и сеттеры.
# Атрибуты класса Figure: sides_count = 0
# Каждый объект класса Figure должен обладать следующими атрибутами:
# Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
# Атрибуты(публичные): filled(закрашенный, bool)
# И методами:
# Метод get_color, возвращает список RGB цветов.
# Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: 
# все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
# Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. 
# Если введены некорректные данные, то цвет остаётся прежним.
# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон 
# совпадает с текущим, False - во всех остальных случаях.
# Метод get_sides должен возвращать значение атрибута __sides.
# Метод __len__ должен возвращать периметр фигуры.
# Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.

from turtle import color
from math import pi, sqrt




class Figure:
    sides_count = 0

    def __init__(self, color, *sides):

        self.__color = color        # список цветов в формате RGB
        self.__sides = sides        # Список сторон целые числа
        self.filled = False        #закрашенный, bool 
        

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):

        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255:  # Цвет корректный
            return True
        else:
            return False  # Цвет некорректный

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = []
            self.__color.append(r)
            self.__color.append(g)
            self.__color.append(b)
            
        return self.__color

    def __is_valid_sides(self, *new_sides):
        
        new_sides_list = []
        for i in new_sides:
            if type(i) == tuple:
                for j in i:
                    new_sides_list.append(j)
        
        for i in range(0, len(new_sides_list)):
            if new_sides_list[i] <= 0:
                print(f'Мы в цикле {i}')
                new_sides_list.pop(new_sides_list[i])
                
        
        if len(new_sides_list) == self.sides_count:
            
            return True
        else:
            
            return False


    def get_sides(self):
        if isinstance(self, Cube):
            #self.__sides = self.cube_sides
            return self.__sides
        elif isinstance(self, Triangle):
            return self.__sides
        else:
            return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        print("Мы в функции SET")
        print(type(new_sides))
        print(new_sides)
        new_sides_list = []
        for i in new_sides:
            print(f'Тип элемента в new_sides: {type(i)}')
            if type(i) == tuple or type(i) == list:
                for j in i:
                    print(f'Тип элемента j = {j} = {type(j)}')
                    new_sides_list.append(j)
            elif type(i) == int:
                new_sides_list = new_sides
                
        
        print(f'Список new_sides_list in SET = {new_sides_list}')
        
        if self.__is_valid_sides(new_sides):
            print("Мы в функции SET, проверка __is_valid_sides")
            self.__sides = new_sides
            print(f'new self sides SET: {self.__sides}')    
        return self.__sides


class Circle(Figure):
    sides_count = 1  #Список сторон целые числа

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = sides
        self.__radius = self.__sides[0] / (2 * pi)

    def get_square(self):
        s = (self.__radius ** 2) * pi
        return s


class Cube(Figure):
    sides_count = 12
    cube_sides = []

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = [sides[0]] * self.sides_count # переопределение __sides
        for i in range(0, self.sides_count):
            self.cube_sides.append(sides[0])
        self.__sides = self.cube_sides
        

    def get_volume(self):
        print(self.__sides[0])
        print(self.cube_sides[0])
        V = self.__sides[0] ** 3
        return V


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides = sides
        p = (self.sides[0] + self.sides[1] + self.sides[2]) / 2
        self.__height = 2 * (sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))) / self.sides[0]
        

    def get_square(self):
        St = (self.__height * self.sides[0]) / 2
        return St


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
triangle1 = Triangle((155, 56, 30), 8, 3, 6)
cube1 = Cube((222, 35, 130), 6)
print(circle1.get_sides()) 
print(triangle1.get_sides())
print(cube1.get_sides())





# Проверка на изменение цветов:

circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())

cube1.set_color(77, 500, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:

cube1.set_sides(7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7)
print(cube1.get_sides())

triangle1.set_sides(1, 2, 3)
print(triangle1.get_sides())

# # Изменится
print(circle1.get_sides())

# Проверка периметра:
print(len(circle1))

# Проверка объёма:
print(cube1.get_sides())
print(cube1.get_volume())

# площадь
print(triangle1.get_sides())
print(circle1.get_square())
print(triangle1.get_square())

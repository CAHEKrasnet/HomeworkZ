# Домашнее задание по теме "Множественное наследование"

# Задача "Ошибка эволюции":

from random import randint as rnd

# 
class Animal:                # класс описывающий животных.
    live = True             # живой/неживой.
    sound = None            # звук (изначально отсутствует).
    _DEGREE_OF_DANGER = 0   # степень опасности существа.

    def __init__(self, speed):  
        self.speed = speed
        self._cords = [0, 0, 0]

    def move(self, dx, dy, dz):             # изменение дистанции в зависисости от скорости
        if self._cords[2] + dz*self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed
        
        #print(f'Стало: {self._cords[0]}: <координаты по x>, {self._cords[1]}: <координаты по y>, {self._cords[2]}: <координаты по z>')

    def get_cords(self):
        print(f'{self._cords[0]}: <координаты по x>, {self._cords[1]}: <координаты по y>, {self._cords[2]}: <координаты по z>')        
        
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print( "Be careful, i'm attacking you 0_0" )   
            
    def speak(self):
        print(self.sound)        
            


class Bird(Animal):            # класс описывающий птиц
    
    beak = True                 # вналичии клюв
    
    # def __init__(self, speed):  
    #     super().__init__(speed)
    #     self.speed = speed
        
    
    def lay_eggs(self):         # откладка яйца
        egg_count = rnd(1, 4)
        print(f"Here are(is) {egg_count} eggs for you")
        
class AquaticAnimal(Animal):  #  класс описывающий плавающего животного.
# Объект такого класса должен обладать атрибутами класса наследования.
# Также обладает методами:
    _DEGREE_OF_DANGER = 3
    
    # def __init__(self, speed):
    #      super().__init__(speed)
    #      self._cords = super()._cords
    #      self.speed = speed
         

    def dive_in(self, dz):      # изменение координаты z в _cords
        self._cords[2] -= abs(dz)*(self.speed//2)
        
        
class PoisonousAnimal(Animal):      # класс описывающий ядовитых животных. Наследуется от Animal.
    _DEGREE_OF_DANGER = 8
    
    # def __init__(self, speed):
    #      super().__init__(speed)
    #      self.sound = super().sound
    #      self.speed = speed

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
     
    
    def __init__(self, speed):
         super().__init__(speed)
         self.sound = "Click-click-click"
         
# print(PoisonousAnimal.mro())
# print(Duckbill.mro())
# print(Bird.mro())
# db = Animal(10)
db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()


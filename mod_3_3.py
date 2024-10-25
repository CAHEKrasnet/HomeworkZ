# Домашнее задание по уроку "Распаковка параметров и параметры функции"

# Задача "Распаковка":
# 1.Функция с параметрами по умолчанию:
# Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию
# (например сейчас это: 1, 'строка', True).
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)      # Функция должна выводить эти параметры.

# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(999, 'Be happy')
print_params(111, None, False)
print_params(9999999)
print_params()

# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b=25)
print('Функция print_params(b=25) работает')
print_params(c = [1,2,3])
print('Функция print_params(c = [1,2,3]) работает')
# Распаовка параметров
# Создайте список values_list с тремя элементами разных типов.
values_list = [333, None, 'Питон']
# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
values_dict = {'a': 99.999, 'b': "Зима близко", 'c': False}
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)
# 3.Распаковка + отдельные параметры:
# Создайте список values_list_2 с двумя элементами разных типов
values_list_2 = ['Красноярск', 24]
# Проверьте, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 42)
print('Функция print_params(*values_list_2, 42) работает')
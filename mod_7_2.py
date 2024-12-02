# Домашнее задание по теме "Позиционирование в файле".

# Задача "Записать и запомнить":

# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи,
#   strings - список строк для записи.
# Функция должна:
# 1 Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# 2 Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением -
#   записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
from pprint import pprint

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    # определяем начальные значения
    string_positions = {}   # задаём словарь
    str_num = 0
    str_start_byte = file.seek(0)   # байт начала первой строки
    for string_ in strings:
        file.write(string_+'\n')
        str_num += 1
        key = (str_num, str_start_byte) # задаём ключи словаря
        string_positions[key]= string_  # добавляем значения в словарь
        str_start_byte = file.tell()
    file.close()
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    '',
    'Спасибо!'
    ]

file_name = 'myfile.txt'   # задаём имя нашего файла

result = custom_write(file_name, info)
pprint(result)  # выводим результат для проверки


# Примечания:
# 1 Не забывайте при записи в файл добавлять спец. символ перехода на следующую строку в конце - '\n'.
# 2 Не забывайте закрывать файл вызывая метод close() у объектов файла.
# 3 Помните, что при использовании символов не принадлежащих таблице ASCII, вы используете больше байт для записи
#   символа. Соответственно для чтения и записи информации из/в файл(-f) потребуется другая кодировка - utf-8.
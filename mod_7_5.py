# Домашнее задание по теме "Файлы в операционной системе".

# Цель задания:
#
# Освоить работу с файловой системой в Python, используя модуль os.
# Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize
# и использование модуля time для корректного отображения времени.
#
# Задание:
#
# Создайте новый проект или продолжите работу в текущем проекте.
# 1. Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
# 2. Примените os.path.join для формирования полного пути к файлам.
# 3. Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# 4. Используйте os.path.getsize для получения размера файла.
# 5. Используйте os.path.dirname для получения родительской директории файла.

import os, time
from os.path import join, getmtime, getsize, dirname
directory = "."     # тестировать будем в папке проекта
for root, dirs, files in os.walk(directory):    # 1
    for file in files:
        filepath = os.path.join(root, file)     # 2
        filetime = os.path.getmtime(file)       # 3
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)        # 4
        parent_dir = os.path.dirname(os.path.abspath(file)) # полный путь
        #parent_dir = os.path.dirname(directory)  # относительный путь # 5
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
              f'Родительская директория: {parent_dir}')
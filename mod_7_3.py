# Домашнее задание по теме "Оператор "with".

# Задача "Найдёт везде":

# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt', 'file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут
# file_names в виде списка или кортежа.
#
# Также объект класса WordsFinder должен обладать следующими методами:
# get_all_words - подготовительный метод, который возвращает словарь следующего вида:
#   {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
#   Где:
#   'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
#   ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.

    # Алгоритм получения словаря такого вида в методе get_all_words:
    # 1 Создайте пустой словарь all_words.
    # 2 Переберите названия файлов и открывайте каждый из них, используя оператор with.
    # 3 Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
    # 4 Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке.
    #   (тире обособлено пробелами, это не дефис в слове).
    # 5 Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
    # 6 В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

# find(self, word) - метод, где word - искомое слово.
#   Возвращает словарь, где ключ - название файла, # значение - позиция первого такого слова в списке слов этого файла.
# count(self, word) - метод, где word - искомое слово.
#   Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
# В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла
# и списка его слов.
# Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться
# методом словаря - item().
    # for name, words in get_all_words().items():
    # Логика методов find или count

import pprint
word = 'teXT'   # искомое слово
class WordsFinder:
    res = {}    #  для вывода результатов
    def __init__(self, *file_names):
        self.file_names = list(file_names)    # атрибут file_names в виде списка
#        self.file_names = file_names         # или кортежа.

    def get_all_words(self):
        all_words = {}  # 1 Создайте пустой словарь all_words
        punctuation = ',.=!?;:' # 4 Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке.
        

        for filename in self.file_names:  # 2 Переберите названия файлов и открывайте каждый из них, используя with.
            words = []  # обнуляем список слов
            clear_line = '' # обнуляем строки
            with open(filename, "r", encoding='utf-8') as file:
                for line in file:
                    line = line.lower()  # Для каждого файла считывайте единые строки, переводя их в нижний регистр
                    while line.find(' — ') != -1:             # 4 Избавьтесь от пунктуации [' — '] в строке.
                        line = line.replace(' — ', " ")  # (тире обособлено пробелами, это не дефис в слове)
                        continue
                    for char in line:   # 4 Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':'] в строке.
                        if not char in punctuation:
                            clear_line += char
                words = clear_line.split()        #  Разбейте эту строку на элементы списка методом split().
                #print(f'Количество слов в файле {filename} равно {len(words)}')
            all_words[filename] = words   #  В словарь all_words запишите полученные данные,
                                          #   ключ - название файла, значение - список из слов этого файла.
            self.res.clear()    # очищаем словарь результатов
        return all_words

    def find(self, word):    # - метод поиска первого вхождения слова, где word - искомое слово.
        # f_dict = {}
        
        for names, words in self.get_all_words().items():
            place = 0
            if word.lower() in words:
                place = words.index(word.lower())+1
                self.res[names] = place
            continue
        return self.res

    def count(self, word):    # count(self, word) - метод поиска количества вхождений, где word - искомое слово.
        for names, words in self.get_all_words().items():
            counter = 0
            if word.lower() in words:
                counter = words.count(word.lower())
                self.res[names] = counter
        return self.res

myfinder = WordsFinder('test_file.txt')
print(myfinder.get_all_words())
print(myfinder.find(word), f' # Позиция первого искомого слова "{word}" в списке:', *myfinder.res.values())
print(myfinder.count(word), f' # Количество повторений найденного слова "{word}": ', *myfinder.res.values(), '\n')


finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'), '\n')

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'), '\n')

finder2 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder2.get_all_words())
print(finder2.find('if'))
print(finder2.count('if'), '\n')

finder3 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt', 'Rudyard Kipling - If.txt', 'Mother Goose - Monday’s Child.txt')
#pprint.pprint(finder3.get_all_words())
print(finder3.get_all_words())
print(finder3.find('THE'))
print(finder3.count('the'))

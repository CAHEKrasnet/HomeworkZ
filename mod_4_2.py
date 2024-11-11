# Домашнее задание по уроку "Пространство имен"
#
# 1 Создайте новый проект в PyCharm
# 2 Запустите созданный проект

# Ваша задача:
# 1 Создайте новую функцию test_function
# 2 Создайте внутри функции inner_function, функция должна печатать значение "Я в области видимости функции test_function"
# 3 Вызовите функцию inner_function внутри функции test_function
# 4 Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
# 5 Полученный код напишите в ответ к домашнему заданию

def test_function():        # 1
    def inner_function():   # 2
        print("Я в области видимости функции test_function")

    inner_function()        # 3 - здесь ничего не возвращает

inner_function()  # (ошибка)
# Вызов функци inner_function() вне функции test_function приводит к появлению ошибки -
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?


test_function()     # Здесь происходит корректный вызов 
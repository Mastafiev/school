import random

a = []
for i in range(10):
    a.append(random.randint(1, 100))
s = 0
c = 0
for b in a:
    if((b % 5 == 0) and (b % 10 == 0)):
        s = s + b
        c = c + 1
print(s, c)


# Импортировать библиотеку random
#
# Создать пустой массив a
# Для i в промежутке 0 - 9 (отсчитываем десять повторений)
#   Добавить в конец массива a значение (Случайное число в диапозоне от 1 до 100)
# Создать переменную s (читай сумма)
# Создать переменную c (читай счётчик)
# Для b в массиве a (Перебираем все элементы массива)
#   Если((Остаток от деления на 5 равен 0) И (Остаток от деления на 10 равен 0))
#     К переменной s прибавить значение текущего элемента
#     Переменную c увеличить на 1
# Напечатать значенине переменных s и c

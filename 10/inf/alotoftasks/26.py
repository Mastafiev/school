import random # Импортировать библиотеку random

k1 = int(input("k1: ")) # Запросить у пользователя ввод k1
k2 = int(input("k2: ")) # Запросить у пользователя ввод k2

a = [] # Создать пустой массив a
for i in range(10): # Для i в промежутке 0 - 9 (отсчитываем десять повторений)
    a.append(random.randint(1, 100)) # Добавить в конец массива a значение (Случайное число в диапозоне от 1 до 100)
s = 0 # Создать переменную s (читай сумма)
c = 0 # Создать переменную c (читай счётчик)
for b in a: # Для b в массиве a (Перебираем все элементы массива)
    if((b % k1 == 0) and (b % k2 == 0)): # Если((Остаток от деления на k1 равен 0) И (Остаток от деления на k2 равен 0))
        s = s + b # К переменной s прибавить значение текущего элемента
        c = c + 1 # Переменную c увеличить на 1
print(s, c) # Напечатать значение переменных s и c
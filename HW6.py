# Task 30:  
# Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения 
# n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


el1 = int(input('Введите первый элемент прогрессии: '))
differ = int(input('Введите разность элементов прогрессии: '))
count = int(input('Введите количество элементов прогрессии: '))
for i in range(count):
    print(el1 + i * differ)


# Task 32:
# Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = [2, 10, 15, 6, 32, -5, -4, 0, 7, -12]
min_value = int(input('Введите минимальное значение диапазона: '))
max_value = int(input('Введите максимальное значение диапазона: '))
for i in range(len(list_1)):
    if min_value <= list_1[i] <= max_value:
        print(i)      

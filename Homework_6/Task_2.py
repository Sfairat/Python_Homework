# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

N = int(input('Введите число элементов массива: '))
min = int(input('Введите минимальное значение заданного диапазона: '))
max = int(input('Введите максимальное значение заданного диапазона: '))

import random
my_list = []
for i in range(N):
    my_list.append(random.randint(-10, 11))
print(my_list)

index_list = []
for i in range(len(my_list)):
    if my_list[i] >= min and my_list[i] <= max:
        index_list.append(i)
        
print(index_list)
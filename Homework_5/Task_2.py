# Задача 2
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def sum(x, y):
    if x == 1:
        return x + y
    return sum(x - 1, y + 1)

a = abs(int(input('Введите число A: ')))
b = abs(int(input('Введите число B: ')))

print(sum(a, b))
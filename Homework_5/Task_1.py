# Задача 1
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def exponent(x, y):
    if y == 1:
        return x
    return x * exponent(x, y - 1)

a = int(input('Введите число A: '))
b = abs(int(input('Введите число B: ')))

print(exponent(a, b))
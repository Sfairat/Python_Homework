# Задача 2.
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 6
# -> 5

N = int(input('Введите число элементов списка: '))

A = []
for i in range(N + 1):
    A.append(i)
    
X = int(input('Введите число, X: '))

diff = abs(X - A[0])
for i in range(1, len(A)):
    temp = X - A[i]
    if temp < diff and temp > 0:
        diff = temp
        
if X > N:
    print(f'Самый близкий элемент к числу {X} равен {X - diff}.')
elif X == 1:
    print(f'Самый близкий элемент к числу {X} равен 2.')
elif X <= 0:
    print(f'Самый близкий элемент к числу {X} равен 1.')
else:
    print(f'Самые близкие элементы к числу {X} равны {X - diff} и {X + diff}.')
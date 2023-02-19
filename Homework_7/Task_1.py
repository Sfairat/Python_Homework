# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, 
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.
# Ввод:

# пара-ра-рам рам-пам-папам па-ра-па-да

# Вывод:
# Парам пам-пам

input_str = input('Введите стихотворение: ')
phrases = input_str.split()
print(phrases)

letters = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
sum_list = []

for i in phrases:
    sum = 0
    for j in i:
        if j in letters:
            sum += 1
    sum_list.append(sum)
    
if len(set(sum_list)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
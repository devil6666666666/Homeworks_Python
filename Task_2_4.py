# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import os
import random
N = abs(int(input('Введите целое число N: ')))
lst = []
for i in range(N):
    lst.append(random.randint(-N, N))
print(lst)
with open(os.path.dirname(os.path.abspath(__file__))
          + "\positions.txt", "r", encoding='utf-8') as data:
    tmp = data.read()
num = [int(x) for x in tmp.split() if x.isdigit()]
print(num)
res = 1
for j in num:
    res *= lst[j]
print(f'Произведение элементов на указанных позициях равно {res}')

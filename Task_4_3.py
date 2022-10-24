# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов 
# исходной последовательности.

import random
lst = []
for i in range(10):
    lst.append(random.randint(0, 10))
print(lst)
print(list(set(lst)))

#  Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным
#  значением дробной части элементов.

from decimal import Decimal, getcontext
l = [1.1, 1.2, 3.1, 5, 10.01]
getcontext().prec = 2
l1 = [Decimal(i % 1) for i in l if i % 1 != 0]
print(max(l1)-min(l1))

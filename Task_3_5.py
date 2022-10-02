# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

a = int(input('Введите целое число: '))
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == -1:
        return 1
    elif n == -2:
        return -1
    elif n>0:
        return fibonacci(n - 1) + fibonacci(n - 2)
    elif n<0:
        return fibonacci(n + 2) - fibonacci(n + 1)

l = [fibonacci(i) for i in range(-a, a+1)]
print(l)

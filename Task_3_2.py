# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т. д.

l = [2, 3, 4, 5, 6]
com = [l[j] * l[len(l) - 1 - j] for j in range(len(l) // 2 + len(l) % 2)]
print(com)
# Дана последовательность чисел. Получить список уникальных
# элементов заданной последовательности, список повторяемых
# и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

my_list = [1, 2, 3, 5, 1, 1, 5, 3, 10]
print ("Оригинальный список : " + str(my_list))
li = []
[li.append(x) for x in my_list if x not in li]
print (f"Список после удаления дубликатов : {li}")

dup = {x for x in my_list if my_list.count(x) > 1}
print(f'Список повторяемых элементов: {dup}')
uniqe = [x for x in my_list if my_list.count(x) == 1]
print(f'Список уникальных элементов: {uniqe}')
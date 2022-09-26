# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = input('Введите X: ')
Y = input('Введите Y: ')
Z = input('Введите Z: ')
if (X or Y or Z) == (X and Y and Z):
    print('True')
else:
    print('False')

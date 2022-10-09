#  Напишите программу, которая принимает на вход
#  вещественное число и показывает сумму его цифр.

def sum (input_number):
    sum_digit = 0
    while input_number != 0:
        sum_digit += input_number % 10
        input_number //= 10
    return sum_digit


number = input('Введите число: ')
number = number.replace('-', '').replace('.', '').replace(',', '')

if number.isdigit():
    sum_digits = sum (int(number))
    print(f'Сумма цифр числа равна {sum_digits}')
else:
    print('Недопустимый ввод. Можно вводить только числа.')
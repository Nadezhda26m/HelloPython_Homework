# Вводим с клавиатуры целое число X. Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное
# число из введенных чисел.
#
# Алгоритм
# 1. Ввести целое число number
# 2. Ввести number раз целые числа для выборки
# 3. Первое число из выборки становится максимальным
# 4. Второе число сравниваем с первым, если оно больше, то становится
# максимальным, а первое - вторым максимальным, иначе наоборот
# 5. Каждое следующее число сравниваем со вторым максимальным. Если больше него,
# то сравниваем с максимальным, делаем соответствующие замены
# 6. Выводим максимальное и второе максимальное число

import math

print('Данная программа находит максимальное и второе максимальное число '
      'из введенных целых чисел')
count_numbers = int(input('Введите количество чисел для ввода: '))

# # duplicate_numbers = [] # для сравнения двух решений

## Решение 1, с возможным совпадением
# for i in range(count_numbers):
#     number = int(input(f'Введите {i + 1} число: '))
#     # duplicate_numbers.insert(i, number)
#     if i == 0:
#         maximum = number
#     elif i == 1:
#         second_max = number
#         if second_max > maximum:
#             maximum, second_max = second_max, maximum
#     elif number > second_max:
#         if number > maximum:
#             second_max = maximum
#             maximum = number
#         else:
#             second_max = number
#
# if count_numbers < 1:
#     print('Некорректный ввод')
# elif count_numbers == 1:
#     print(f'Max = {maximum}, введите больше чисел для поиска '
#           f'второго максимального числа')
# else:
#     print(f'Max = {maximum}, second max = {second_max}')

## Решение 2, без совпадения
for i in range(count_numbers):
    number = int(input(f'Введите {i + 1} число: '))
    # number = duplicate_numbers[i]
    # print(f'Введите {i + 1} число: {number}')
    if i == 0:
        maximum2 = number
        second_max2 = -math.inf
    elif number > second_max2 and number != maximum2:
        if number > maximum2:
            second_max2 = maximum2
            maximum2 = number
        else:
            second_max2 = number

if count_numbers < 1:
    print('Некорректный ввод')
elif count_numbers == 1:
    print(f'Max(2) = {maximum2}, введите больше чисел для поиска '
          f'второго максимального числа')
elif second_max2 == -math.inf:
    print(f'Max(2) = {maximum2}, вводите разные числа для поиска '
          f'второго по величине максимального числа')
else:
    print(f'Max(2) = {maximum2}, second max(2) = {second_max2}')

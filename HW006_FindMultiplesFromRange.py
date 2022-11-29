# Вводим с клавиатуры целое число X и У. Выводим на экран
# количество чисел между Х и У, которые делятся на 2 и 3.
#
# Алгоритм
# 1. Ввести два целых числа
# 2. Определить минимальное из них
# 3. В диапазоне от минимального до максимального (не включительно)
# найти числа, которые делятся на 2 и 3 одновременно
# 4. Вывести количество этих чисел

num_min = int(input('Введите первое число (целое): '))
num_max = int(input('Введите второе число (целое): '))
if num_min > num_max:
    num_min, num_max = num_max, num_min
print(f'Количество чисел между {num_min} и {num_max}, которые делятся на 2 и 3:')

# Решение 1
count1 = 0
for i in range(num_min + 1, num_max):
    if not i % 2 and not i % 3:
        count1 += 1
print(f'count1 = {count1}')

# Решение 2
count2 = 0
low_common_multiple = 2 * 3 # НОК
for k in range(num_min + 1, num_min + low_common_multiple + 1):
    if not k % low_common_multiple:
        break
for j in range(k, num_max, low_common_multiple):
    count2 += 1
print(f'count2 = {count2}')

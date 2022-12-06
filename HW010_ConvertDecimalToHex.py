# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести
# его в шестнадцатиричную систему счисления.

# Алгоритм
# 1. Ввести целое неотрицательное число, проверить корректность ввода
# 2. Получить остатки от деления числа на 16, записать через разделитель в строку
# 3. Числа больше 9 заменить на соответствующие символы, записать результат без разделителей
# 4. Для получения ответа в 16-ной СС перевернуть строку, полученную в пункте 3
# 5. Выдать результат преобразования

print('***Преобразование чисел из 10-ной системы счисления в 16-ную***\n')
stop = ''
while stop == '':
    number_input = int(input('Введите целое неотрицательное число: '))
    if number_input > -1:
        number = number_input
        hex_raw = ''  # получим набор чисел в обратном порядке
        while number > 15:
            num = number % 16
            hex_raw += str(num) + ','
            number //= 16
        hex_raw += str(number)

        hex_reverse = ''  # преобразуем числа 10 - 15 в буквы
        size_raw = len(hex_raw) - 1
        i_next = False
        for i in range(size_raw + 1):
            if i_next:
                i_next = False
                continue
            elif hex_raw[i] == '1' and i < size_raw:
                if hex_raw[i + 1] == ',':
                    hex_reverse += hex_raw[i]
                elif hex_raw[i + 1] == '0':
                    hex_reverse += 'A'
                elif hex_raw[i + 1] == '1':
                    hex_reverse += 'B'
                elif hex_raw[i + 1] == '2':
                    hex_reverse += 'C'
                elif hex_raw[i + 1] == '3':
                    hex_reverse += 'D'
                elif hex_raw[i + 1] == '4':
                    hex_reverse += 'E'
                elif hex_raw[i + 1] == '5':
                    hex_reverse += 'F'
                i_next = True
            elif hex_raw[i] != ',':
                hex_reverse += hex_raw[i]

        hex_finish = ''  # перевернем строку для получения ответа
        size_reverse = len(hex_reverse) - 1
        for i in range(size_reverse, -1, -1):
            hex_finish += hex_reverse[i]

        print(f'{number_input}(10) = {hex_finish}(16)')
    else:
        print('Некорректный ввод')
    stop = input('Нажмите Enter для продолжения или отправьте любой '
                 'символ для остановки\n')

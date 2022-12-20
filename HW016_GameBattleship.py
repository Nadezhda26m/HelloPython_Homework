# Сделать игру морской бой

# Алгоритм
# 1. Создаем пустое игровое поля заданного размера, список списков,
# по умолчанию заполняем нулями
# 2. Расставляем длинный корабль, вертикально или горизонтально,
# он не должен выезжать за границы поля
# 3. Расставляем однопалубный корабль, он не должен сокасаться с первым кораблем
# даже по диагонали. Отмечаем расставленные корабли *
# 4. На новом поле рандомно расставляем по тем же правилам корабли компьютера
# 5. Создаем третье пустое поле, на котором будет играть пользователь.
# Определяем рандомно первого игрока
# 6. Игрок должен каждый раз вводить валидные данные строки и столбца. Если он
# промахнулся, то ход передается противнику, а выбранная ячейка отмечается знаком ~.
# Если игрок попал в цель, то подбитый корабль отмечается #, затем проверяется количество
# сбитых кораблей. Если сбиты еще не все, то игрок снова делает ход, пока не
# промахнется или не выиграет игру.
# 7. Аналогично при передачи хода компьютеру рандомно выбирается валидная ячейка,
# проверяется статус хода
# 8. Когда одна из сторон сбивает все расставленные цели, то объявляется победитель

# TODO
# расширить поле +
# добавить 1 корабль ++
# ранил / потопил
# проверка ввода вертикали / горизонтали
# комп ищет раненый корабль
# добавить словарь фраз
# вокруг потопленного корабля комп не ищет

from random import randint
import time

# вывести игровое поле с нумерацией
def print_field_square(field):
    size_field = len(field)
    for i in range(-1, size_field):
        if i == -1:
            print(' ', end=' ')
            for p in range(1, size_field + 1):
                print(p, end=' ')
            print()
        else:
            print(f'{i + 1}', end=' ')
            for k in range(0, size_field):
                print(field[i][k] if field[i][k] != 0 else '.', end=' ')
            print()

# проверить корректность ввода пользователя
def check_input_user(field):
    size = len(field)
    while True:
        row = int(input('Введите номер строки: '))
        col = int(input('Введите номер столбца: '))
        if not (1 <= row <= size and 1 <= col <= size):
            print('Мимо поля, повторите ввод')
        elif field[row - 1][col - 1] != 0:
            print('Туда уже стреляли, повторите ввод')
        else:
            return (row, col)

# создать пустое игровое поле заданного размера
def create_field(size, char=0):
    field = []
    for i in range(size):
        field.append([])
        for k in range(size):
            field[i].append(char)
    return field

# проверить, соприкасается ли указанная ячейка с уже заполненной, в т.ч. по диагонали
def check_space_around(row, col, field):
    size = len(field)
    while True:
        if field[row][col] != 0:
            break
        if row > 0:
            if field[row - 1][col] != 0:
                break
            if col > 0 and (field[row][col - 1] != 0 or field[row - 1][col - 1] != 0):
                break
            if col < size - 1 and (field[row][col + 1] != 0 or field[row - 1][col + 1] != 0):
                break
        if row < size - 1:
            if field[row + 1][col] != 0:
                break
            if col > 0 and (field[row][col - 1] != 0 or field[row + 1][col - 1] != 0):
                break
            if col < size - 1 and (field[row][col + 1] != 0 or field[row + 1][col + 1] != 0):
                break
        return True

# вывести рядом два поля
def print_fields_nearby(field_left, field_right):
    size = len(field_left)
    for i in range(-1, size):
        if i == -1:
            print(' ', end=' ')
            for p in range(1, size + 1):
                print(p, end=' ')
            print('         ', end=' ')
            for p in range(1, size + 1):
                print(p, end=' ')
            print()
        else:
            print(f'{i + 1}', end=' ')
            for k in range(0, size):
                print(field_left[i][k] if field_left[i][k] != 0 else '.', end=' ')
            print(f'        {i + 1}', end=' ')
            for k in range(0, size):
                print(field_right[i][k] if field_right[i][k] != 0 else '.', end=' ')
            print()

# разместить рандомно корабль с указанием количества палуб
def put_ship_random(check_space, field, count_decks):
    size = len(field)
    horiz_vertic = randint(1, 2)
    while True:
        ship_row = randint(0, size - 1)
        ship_col = randint(0, size - 1)
        if check_space(ship_row, ship_col, field):
            if horiz_vertic == 1:
                if ship_col <= size - count_decks:
                    if check_space(ship_row, ship_col + count_decks - 1, field):
                        for i in range(count_decks):
                            field[ship_row][ship_col + i] = '*'
                        break
            else:
                if ship_row <= size - count_decks:
                    if check_space(ship_row + count_decks - 1, ship_col, field):
                        for i in range(count_decks):
                            field[ship_row + i][ship_col] = '*'
                        break

# разместить рандомно однопалубный корабль (меньше проверок)
def put_decks_random_1decks(check_space, field):
    size = len(field)
    while True:
        ship_row = randint(0, size - 1)
        ship_col = randint(0, size - 1)
        if check_space(ship_row, ship_col, field):
            field_comp[ship_row][ship_col] = '*'
            break


size_field = 7  # Задаем размер игрового поля, квадратного
print('Добро пожаловать в игру Морской бой!\n'
      'Правила игры доступны по ссылке [тык]\n')

# /Расставляем корабли пользователя
print('Сперва расставьте корабли на своем поле, один двухпалубный и один однопалубный')
field_user = create_field(size_field)
print_field_square(field_user)
print('Начнем с двухпалубного, чтобы расположить его горизонтально, '
      'нажмите 1, вертикально - 2')
while True:
    horiz_vertic = int(input('> '))
    if horiz_vertic == 1 or horiz_vertic == 2:
        break
    else:
        print('Неверные данные, повторите ввод')

if horiz_vertic == 1:
    print('Введите координаты левой части корабля')
    while True:
        ship_row = int(input('Строка: '))
        ship_col = int(input('Столбик: '))
        if 0 < ship_row <= size_field and 0 < ship_col <= size_field:
            if ship_col == size_field:
                print('Справа не хватает места для корабля, повторите ввод')
            else:
                field_user[ship_row - 1][ship_col - 1] = "*"
                field_user[ship_row - 1][ship_col] = "*"
                break
        else:
            print('Неверные данные, повторите ввод')
else:
    print('Введите координаты верхней части корабля')
    while True:
        ship_row = int(input('Строка: '))
        ship_col = int(input('Столбик: '))
        if 0 < ship_row <= size_field and 0 < ship_col <= size_field:
            if ship_row == size_field:
                print('Снизу не хватает места для корабля, повторите ввод')
            else:
                field_user[ship_row - 1][ship_col - 1] = "*"
                field_user[ship_row][ship_col - 1] = "*"
                break
        else:
            print('Неверные данные, повторите ввод')
print_field_square(field_user)  # здесь будет двухпалубный кораблик игрока

print('Введите координаты однопалубного корабля, он не должен '
      'соприкасаться с двухпалубным')
while True:
    ship_row = int(input('Строка: '))
    ship_col = int(input('Столбик: '))
    if 0 < ship_row <= size_field and 0 < ship_col <= size_field:
        if check_space_around(ship_row - 1, ship_col - 1, field_user):
            field_user[ship_row - 1][ship_col - 1] = '*'
            break
        else:
            print('Сюда нельзя ставить корабль, повторите ввод')
    else:
        print('Неверные данные, повторите ввод')

print('Ваши корабли >')
print_field_square(field_user)

# комп прячет кораблики
field_comp = create_field(size_field)
put_ship_random(check_space_around, field_comp, 4)
put_ship_random(check_space_around, field_comp, 3)
put_ship_random(check_space_around, field_comp, 2)
put_ship_random(check_space_around, field_comp, 2)
put_decks_random_1decks(check_space_around, field_comp)
put_decks_random_1decks(check_space_around, field_comp)
put_decks_random_1decks(check_space_around, field_comp)

print('Корабли противника >')
print_field_square(field_comp)  # не подсматривайте за кораблями противника!

# кто ходит первым
time.sleep(2)
print('\nНачинаем игру')
print('(вы играете на левом поле)')
user_goal = create_field(size_field)  # на этом поле играет игрок
print_fields_nearby(user_goal, field_user)
step_now = randint(1, 2)
if step_now == 1:
    print('Первый ход делает игрок')
else:
    print('Первый ход делает компьютер')

# подсчитываем сбитые корабли
user_win = 0
comp_win = 0

# !!!!!!!!!!!!!!!!!!!
max_ships = 3  # 3 ячейки с кораблями
while True:

    # Ход игрока
    if step_now == 1:
        print('\nВаш ход >>>>>')
        target = check_input_user(user_goal)
        step_row = target[0]
        step_col = target[1]
        time.sleep(1)
        if field_comp[step_row - 1][step_col - 1] == 0:
            user_goal[step_row - 1][step_col - 1] = '~'
            print('Мимо')
            step_now = 2
        else:
            user_goal[step_row - 1][step_col - 1] = '#'
            print('Попал!')
            user_win += 1
        print_fields_nearby(user_goal, field_user)

    # Ход компьютера
    else:
        time.sleep(1)
        print('\nХод противника >>>>>')
        time.sleep(2)
        while True:
            step_row = randint(0, size_field - 1)
            step_col = randint(0, size_field - 1)
            if field_user[step_row][step_col] == 0:
                field_user[step_row][step_col] = '~'
                print(f'Строка: {step_row + 1}\nСтолбик: {step_col + 1}')
                time.sleep(1)
                print('Мимо')
                step_now = 1
                break
            elif field_user[step_row][step_col] == '*':
                field_user[step_row][step_col] = '#'
                print(f'Строка: {step_row + 1}\nСтолбецик: {step_col + 1}')
                time.sleep(1)
                print('Противник попал в ваш корабль!')
                comp_win += 1
                break
        print_fields_nearby(user_goal, field_user)

    if user_win == max_ships:
        print('\nВы выиграли!!!')
        break
    elif comp_win == max_ships:
        print('\nВы проиграли (:')
        break

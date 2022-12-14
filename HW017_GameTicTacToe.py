# Сделать игру крестики-нолики

from random import randint
import time

# Чтобы могли играть Маша и Саша, например
dict_players = \
    {
        'player1': 'user',
        'player2': 'comp'
    }

# Быстрая замена символа на пустую ячейку или ходы игроков
dict_value = \
    {
        'not': '-',
        'player1': 'X',
        'player2': 'O'
    }

# создание пустого поля заданного размера (квадратного)
size_row = 3
size_col = size_row
field = []
for i in range(size_row):
    field.append([])
    for k in range(size_col):
        field[i].append(dict_value['not'])

# Печать игрового поля с нумерацией
for i in range(-1, size_row):
    if i == -1:
        print(' ', end=' ')
        for p in range(1, size_col + 1):
            print(p, end=' ')
        print()
    else:
        print(f'{i + 1}', end=' ')
        for k in range(0, size_col):
            print(field[i][k], end=' ')
        print()

# кто ходит первым
first_step = randint(1, 2)
if first_step == 1:
    step = dict_players.get('player1')
    print(f"Начинает игрок: {dict_players.get('player1')}")
else:
    step = dict_players.get('player2')
    print(f"Начинает игрок: {dict_players.get('player2')}")

# сколько раз делать ход
steps_max = size_row * size_col  # максимальное количество шагов (клеток)
while steps_max > 0:

    # передача хода
    if step == dict_players.get('player1'):
        user_step_ok = False

        # сделать ход игроку
        while not user_step_ok:
            pos_row = int(input('Строка: '))
            pos_col = int(input('Столбец: '))
            if not (1 <= pos_row <= size_row and 1 <= pos_col <= size_col):
                print('Неверные данные, повторите ввод')
            elif field[pos_row - 1][pos_col - 1] == dict_value['not']:
                field[pos_row - 1][pos_col - 1] = dict_value['player1']
                user_step_ok = True
            else:
                print('Ячейка занята, повторите ввод')

        print(dict_players.get('player1'))
        # Печать игрового поля с нумерацией
        for i in range(-1, size_row):
            if i == -1:
                print(' ', end=' ')
                for p in range(1, size_col + 1):
                    print(p, end=' ')
                print()
            else:
                print(f'{i + 1}', end=' ')
                for k in range(0, size_col):
                    print(field[i][k], end=' ')
                print()
        step = dict_players.get('player2')

    else:
        # Ход компьютера
        comp_step_ok = False

        while not comp_step_ok:
            pos_row = randint(0, size_row - 1)
            pos_col = randint(0, size_col - 1)
            if field[pos_row][pos_col] == dict_value['not']:
                field[pos_row][pos_col] = dict_value['player2']
                comp_step_ok = True
        time.sleep(1)

        print(dict_players.get('player2'))
        # Печать игрового поля с нумерацией
        for i in range(-1, size_row):
            if i == -1:
                print(' ', end=' ')
                for p in range(1, size_col + 1):
                    print(p, end=' ')
                print()
            else:
                print(f'{i + 1}', end=' ')
                for k in range(0, size_col):
                    print(field[i][k], end=' ')
                print()
        step = dict_players.get('player1')

    steps_max -= 1

    winner = []
    # проверка заполнения строки
    for i in range(size_row):
        if field[i][0] != dict_value['not']:
            win_char = field[i][0]
            win = True
            for k in range(1, size_col):
                if field[i][k] != win_char:
                    win = False
                    break
            if win:
                winner.append((i, win_char))

    if len(winner) > 0:
        print('Есть победитель')
        for d in range(len(winner)):
            print(f'Победила строка {winner[d][0] + 1}\nПобедитель {winner[d][1]}')
        steps_max = 0

    winner = []
    # проверка заполнения столбца
    for i in range(size_col):
        if field[0][i] != dict_value['not']:
            win_char = field[0][i]
            win = True
            for k in range(1, size_row):
                if field[k][i] != win_char:
                    win = False
                    break
            if win:
                winner.append((i, win_char))

    if len(winner) > 0:
        print('Есть победитель')
        for d in range(len(winner)):
            print(f'Победил столбик {winner[d][0] + 1}\nПобедитель {winner[d][1]}')
        steps_max = 0

    winner = []
    # проверка заполнения диагонали ↘ !!! для квадратного поля
    if field[0][0] != dict_value['not']:
        win_char = field[0][0]
        win = True
        for k in range(1, size_row):  # в правый нижний угол
            if field[k][k] != win_char:
                win = False
                break
        if win:
            winner.append(('↘', win_char))

    if len(winner) > 0:
        print('Есть победитель')
        for d in range(len(winner)):
            print(f'Победила диагональ {winner[d][0]}\nПобедитель {winner[d][1]}')
        steps_max = 0

    winner = []
    # проверка заполнения диагонали ↗ !!! для квадратного поля
    if field[size_row - 1][0] != dict_value['not']:
        win_char = field[size_row - 1][0]
        win = True
        for k in range(1, size_row):  # в правый нижний угол
            if field[size_row - 1 - k][k] != win_char:
                win = False
                break
        if win:
            winner.append(('↗', win_char))

    if len(winner) > 0:
        print('Есть победитель')
        for d in range(len(winner)):
            print(f'Победила диагональ {winner[d][0]}\nПобедитель {winner[d][1]}')
        steps_max = 0

game_over = True
for i in range(size_row):
    if dict_value['not'] in field[i]:
        game_over = False
        break
if game_over:
    print('Ничья')

# ! Ошибка, не так сработает, если победитель определился в последнем ходе
# user
#   1 2 3
# 1 O X O
# 2 X - X
# 3 O X O
# comp
#   1 2 3
# 1 O X O
# 2 X O X
# 3 O X O
# Есть победитель
# Победила диагональ ↘
# Победитель O
# Есть победитель
# Победила диагональ ↗
# Победитель O
# Ничья

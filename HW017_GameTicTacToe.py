# Сделать игру крестики-нолики
#
# Алгоритм
# 1. Создаем пустое игровое поля заданного размера, список списков,
# заполняем значением по умолчанию (-)
# 2. Определяем игроков, их роли (символ) и кто ходит первым
# 3. Игра продолжается до тех пор, пока не объявится победитель или
# не исчерпаются все ходы, максимальное количество ходов - количество ячеек
# 4. Игрок и компьютер по очереди выбирают ячейку, она должна быть внутри поля
# и не занятой
# 5. После каждого хода проверяются все условия победы, так как их может быть
# больше одного. Ищем строку, столбик или диагональ, заполненную целиком 'O' или 'X'.
# Когда хотя бы одно условие победы выполняется, выводим выигрышную комбинацию
# (или несколько) и победителя. Завершаем игру выходом из цикла
# 6. Если в конце игры победитель не определился, то объявляется ничья

from random import randint
import time

# Печать квадратного игрового поля с нумерацией
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
                print(field[i][k], end=' ')
            print()

def find_win_row(field, value_default):
    size_field = len(field)
    for i in range(size_field):
        if field[i][0] != value_default:
            for k in range(1, size_field):
                if field[i][k] != field[i][0]:
                    break
            else:
                return (f'строка {i + 1}', field[i][0])

def find_win_col(field, value_default):
    size_field = len(field)
    for i in range(size_field):
        if field[0][i] != value_default:
            for k in range(1, size_field):
                if field[k][i] != field[0][i]:
                    break
            else:
                return (f'столбик {i + 1}', field[0][i])

def find_win_diagonal_down(field, value_default):
    if field[0][0] != value_default:
        size_field = len(field)
        for i in range(1, size_field):
            if field[i][i] != field[0][0]:
                break
        else:
            return ('диагональ ↘', field[0][0])

def find_win_diagonal_up(field, value_default):
    size_field = len(field)
    if field[size_field - 1][0] != value_default:
        for k in range(1, size_field):
            if field[size_field - 1 - k][k] != field[size_field - 1][0]:
                break
        else:
            return ('диагональ ↗', field[size_field - 1][0])

def check_victory(conditions, field, value_default, char_player_1, player1, player2):
    item = conditions(field, value_default)
    if item:
        if item[1] == char_player_1:
            print(f'Победа, {item[0]}\nПобедитель {player1}')
        else:
            print(f'Победа, {item[0]}\nПобедитель {player2}')
        return True

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

# создание пустого поля (квадратного) заданного размера
size_field = 3
field = []
for i in range(size_field):
    field.append([])
    for k in range(size_field):
        field[i].append(dict_value['not'])

# Печать игрового поля с нумерацией
print('Играем в игру Крестики-Нолики)')
print(f'Размер игрового поля {size_field}x{size_field}')
print_field_square(field)

print(f"{dict_players['player1']} - {dict_value['player1']}\n"
      f"{dict_players['player2']} - {dict_value['player2']}")

# кто ходит первым
step_now = randint(1, 2)
print(f'Начинает игрок: ', end='')
if step_now == 1:
    print(dict_players.get('player1'))
else:
    print(dict_players.get('player2'))

# сколько раз делать ход
steps_max = size_field ** 2  # максимальное количество шагов (ячеек)
while steps_max > 0:

    if step_now == 1:
        # ход игрока
        user_step_ok = False
        while not user_step_ok:
            pos_row = int(input('Строка: '))
            pos_col = int(input('Столбик: '))
            if not (1 <= pos_row <= size_field and 1 <= pos_col <= size_field):
                print('Неверные данные, повторите ввод')
            elif field[pos_row - 1][pos_col - 1] == dict_value['not']:
                field[pos_row - 1][pos_col - 1] = dict_value['player1']
                user_step_ok = True
            else:
                print('Ячейка занята, повторите ввод')
        step_now = 2

        print(dict_players.get('player1'))
        print_field_square(field)

    else:
        # Ход компьютера
        comp_step_ok = False
        while not comp_step_ok:
            pos_row = randint(0, size_field - 1)
            pos_col = randint(0, size_field - 1)
            if field[pos_row][pos_col] == dict_value['not']:
                field[pos_row][pos_col] = dict_value['player2']
                comp_step_ok = True
        step_now = 1
        time.sleep(1)

        print(dict_players.get('player2'))
        print_field_square(field)

    # может быть больше одной победной комбинации
    a = check_victory(find_win_row, field, dict_value['not'], dict_value['player1'],
                      dict_players['player1'], dict_players['player2'])
    b = check_victory(find_win_col, field, dict_value['not'], dict_value['player1'],
                      dict_players['player1'], dict_players['player2'])
    c = check_victory(find_win_diagonal_down, field, dict_value['not'], dict_value['player1'],
                      dict_players['player1'], dict_players['player2'])
    d = check_victory(find_win_diagonal_up, field, dict_value['not'], dict_value['player1'],
                      dict_players['player1'], dict_players['player2'])
    if a or b or c or d:
        steps_max = -1
    else:
        steps_max -= 1

if steps_max == 0:
    print('Ничья')

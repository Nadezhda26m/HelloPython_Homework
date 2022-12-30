import HW019_mode_read as mr
import HW019_mode_write as mw
import HW019_file_add_record as fadd

# выбрать номер записи и изменить ее
def change_record(file_name):
    data = mr.read_all_lines_with_numb(file_name)
    size = len(data)
    record_num = 0
    while not 0 < record_num <= size:
        record_num = int(input('Введите номер записи для переписывания: '))
    data[record_num - 1][1] = input('Введите новое событие: ') + '\n'
    mw.overwrites_file(file_name, data)
    print(f'Изменена запись в файле {file_name}')
    print(f'> {data[record_num - 1][0]} {data[record_num - 1][1]}', end='')

# удалить запись из файла и перенести ее в правую колонку
def move_record_right(file_name, next_file):
    data = mr.read_all_lines_with_numb(file_name)
    size_data = len(data)
    record_num = 0
    while not 0 < record_num <= size_data:
        record_num = int(input('Введите номер записи для переноса: '))
    data_move = data[record_num - 1][1]
    data.pop(record_num - 1)
    data = mw.correct_numb_strings(data)
    mw.overwrites_file(file_name, data)
    fadd.add_remove_record_at_end(next_file, data_move)
    print(f'Вы перенесли запись:\n> {data_move}из файла {file_name} в файл {next_file}')

# удалить запись из файла и откорректировать номера
def delete_record(file_name):
    data = mr.read_all_lines_with_numb(file_name)
    size_data = len(data)
    record_num = 0
    while not 0 < record_num <= size_data:
        record_num = int(input('Введите номер записи для удаления: '))
    del_data = data.pop(record_num - 1)
    data = mw.correct_numb_strings(data)
    mw.overwrites_file(file_name, data)
    print(f'Вы удалили запись из файла {file_name}:\n> {del_data[1]}', end='')

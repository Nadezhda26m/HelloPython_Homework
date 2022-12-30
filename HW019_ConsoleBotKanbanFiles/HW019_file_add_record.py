import HW019_mode_read as mr
import HW019_mode_append as ma

# добавить запись в конец списка, определив номер записи
def add_record_at_end(file_name):
    data = mr.read_all_lines_with_numb(file_name)  #
    size = len(data)
    event = input('Введите событие: ')
    if size > 0:
        last_num = int(data[size - 1][0])  # выцепить последний номер
        new_num = '{:03}'.format(last_num + 1)
        ma.append_new_record(file_name, event, new_num)
    else:
        ma.append_new_record(file_name, event)
        new_num = '001'
    print(f'Вы добавили в файл {file_name} событие:\n{new_num} {event}')

# поместить запись в конец списка, с определением номера новой записи
def add_remove_record_at_end(file_name, data_move):
    data = mr.read_all_lines_with_numb(file_name)
    size = len(data)
    if size > 0:
        last_num = int(data[size - 1][0])  # выцепить последний номер
        new_num = '{:03}'.format(last_num + 1)
        ma.append_remove_record(file_name, data_move, new_num)
    else:
        ma.append_remove_record(file_name, data_move)

import HW019_file_show as fshow
import HW019_file_add_record as fadd
import HW019_file_move_change as fmove
import HW019_mode_read as mr

files = ['HW019_to_do.txt', 'HW019_doing.txt',
         'HW019_check.txt', 'HW019_done.txt']

print('Данная программа работает как kanban-доска с 4 колонками:\n'
      '1 колонка - TO DO\n2 колонка - DOING (5)\n'
      '3 колонка - CHECK (5)\n4 колонка - DONE\n'
      'Новые записи можно добавлять только в 1 колонку,\n'
      'далее вы можете последовательно передвигать записи из 1 колонки к 4.\n'
      'Когда запись перемещена в колонку DONE, ее уже нельзя двигать дальше.\n'
      'Также для колонок 2 и 3 существует ограничение по количеству задач.\n'
      'Пустые колонки не доступны для выбора режима\n'
      '(исключение - добавление новой записи в первую колонку)')

progress = ''
while progress != 'end':
    # выбрать режим работы
    flag = True
    while flag:
        now = input('\nВыберите режим работы с kanban-доской:\n'
                    '1 - считать данные с файла\n'
                    '2 - добавить новую запись (только для колонки TO DO)\n'
                    '3 - перенести запись в столбик справа '
                    '(не доступно для колонки DONE)\n'
                    '4 - изменить запись (исправить опечатки)\n'
                    '5 - удалить запись\n'
                    'Введите номер режима: ')
        if not '0' < now[:] <= '5':
            print('Неверные данные, повторите ввод')
        else:
            flag = False
            now = int(now)

    # выбрать колонку (файл) (не пустую)
    # для режима записи доступен только один файл
    next_now = False
    if now != 2:
        count_todo = mr.count_records(files[0])
        count_doing = mr.count_records(files[1])
        count_check = mr.count_records(files[2])
        count_done = mr.count_records(files[3])
        choose = []
        print('\nВыберите доступную колонку:')
        if count_todo > 0:
            print(f'1 - TO DO ({count_todo} шт)')
            choose.append('1')
        else:
            print('1 - TO DO (пустая)')
        if count_doing > 0:
            print(f'2 - DOING (5) ({count_doing} шт)')
            choose.append('2')
        else:
            print('2 - DOING (5) (пустая)')
        if count_check > 0:
            print(f'3 - CHECK (5) ({count_check} шт)')
            choose.append('3')
        else:
            print('3 - CHECK (5) (пустая)')
        if count_done > 0 and now != 3:
            print(f'4 - DONE ({count_done} шт)')
            choose.append('4')
        elif now != 3:
            print('4 - DONE (пустая)')
        if len(choose) == 0:
            print('Все колонки пустые, сначала заполните их')
            next_now = True
        else:
            while not flag:
                col_num = input('> ')
                if not col_num in choose:
                    print('Неверные данные, повторите ввод')
                else:
                    if now == 3 and ((col_num == '1' and count_doing == 5)
                                     or (col_num == '2' and count_check == 5)):
                        print('Соседняя колонка забита, сначала освободите ее')
                        next_now = True  # если забита, то можно сменить режим
                        break
                    else:
                        flag = True
                        col_num = int(col_num)
    if next_now:  # сменить режим
        continue

    if now == 1:  # чтение и вывод
        fshow.show_file_fully(files[col_num - 1])
    elif now == 2:  # добавить запись в конец
        print('Вы можете добавить запись в колонку TO DO')
        fadd.add_record_at_end(files[0])
    elif now == 3:  # вывести файл и отправить вправо выбранную запись
        fshow.show_file_fully(files[col_num - 1])
        fmove.move_record_right(files[col_num - 1], files[col_num])
    elif now == 4:  # вывести файл и изменить выбранную запись
        fshow.show_file_fully(files[col_num - 1])
        fmove.change_record(files[col_num - 1])
    elif now == 5:  # вывести файл и удалить запись
        fshow.show_file_fully(files[col_num - 1])
        fmove.delete_record(files[col_num - 1])

    progress = input('\nДля завершения отправьте "end", '
                     'для продолжения - любой символ (или нажмите Enter)\n> ')

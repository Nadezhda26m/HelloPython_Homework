# добавить запись в конец файла, в пустом файле начать по умолчанию с 001
def append_new_record(file_name, data, num='001'):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{num} {data}\n')

# без перехода на новую строку в конце записи
def append_remove_record(file_name, data, num='001'):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{num} {data}')

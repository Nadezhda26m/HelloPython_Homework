# записать весь файл (список) в переменную
def read_all_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

# разбить даные над подсписки с номером и текстом
def read_all_lines_with_numb(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.readlines()
        size = len(data)
        new_data = []
        for i in range(size):
            new_data.append([])
            new_data[i].append(data[i][:3])
            new_data[i].append(data[i][4:])
    return new_data

# посчитать количество строк в файле
def count_records(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.readlines()
        count = len(data)
    return count

# записать данные из списка, содержащего подсписки с номерами
def overwrites_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        size = len(data)
        for i in range(size):
            file.write(f'{data[i][0]} {data[i][1]}')

# откорректировать номера в списке по возрастанию
def correct_numb_strings(data):
    size = len(data)
    new_data = []
    for i in range(size):
        new_data.append([])
        new_data[i].append('{:003}'.format(i+1))
        new_data[i].append(data[i][1])
    return new_data

def read_all_file_string(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.readlines()
        size = len(data)
        message = ''
        for i in range(size):
            message += data[i]
    return message

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

def append_new_record(file_name, data, num='001'):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{num} {data}\n')

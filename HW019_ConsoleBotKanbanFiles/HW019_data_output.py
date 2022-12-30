# распечатать построчно список, содержащий строки из файла (целиком)
def print_data_list_elementwise(data_list):
    size = len(data_list)
    for i in range(size):
        print(data_list[i], end='')

# распечать список с номерами
# def print_new_data_list_elementwise(data_list):
#     size = len(data_list)
#     for i in range(size):
#         print(data_list[i][0], end=' ')
#         print(data_list[i][1], end='')

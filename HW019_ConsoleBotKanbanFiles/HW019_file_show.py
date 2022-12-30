import HW019_mode_read as mr
import HW019_data_output as out

# вывести построчно файл на экран
def show_file_fully(file_name):
    data = mr.read_all_file(file_name)
    out.print_data_list_elementwise(data)

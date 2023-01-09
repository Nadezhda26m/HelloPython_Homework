# Написать простой парсер для извлечения информации с любого сайта.
# Например - новость, или погоду с сайта mail.ru

import requests
from bs4 import BeautifulSoup as bs

# считать данные с сайта в формате данных soup
def soup_parse(url):
    response = requests.get(url).text
    soup = bs(response, 'html.parser')
    return soup

# получить заголовки таблицы
def get_table_head(soup):
    p_name = soup.find('th', class_='views-field views-field-title active')\
        .find('a', class_='active').text
    p_protein = soup.find('th', class_='views-field views-field-field-protein-value')\
        .find('a', class_='active').text
    p_fat = soup.find('th', class_='views-field views-field-field-fat-value')\
        .find('a', class_='active').text
    p_carbs = soup.find('th', class_='views-field views-field-field-carbohydrate-value')\
        .find('a', class_='active').text
    p_kcal = soup.find('th', class_='views-field views-field-field-kcal-value')\
        .find('a', class_='active').text
    return (p_name, p_protein, p_fat, p_carbs, p_kcal)

# перенести значения из тела таблицы в список
def get_all_value(soup):
    c_page = soup.find_all(['td', 'a'],
                           class_=['views-field views-field-title active',
                                   'views-field views-field-field-protein-value',
                                   'views-field views-field-field-fat-value',
                                   'views-field views-field-field-carbohydrate-value',
                                   'views-field views-field-field-kcal-value'])
    # выбрать теги и классы с нужными ячейками
    size = len(c_page)
    data_table = []
    for i in range(0, size, 5):  # можно сделать выборку короче (заменить size)
        position = []
        name = str(c_page[i])
        name_left = name.rfind('">')
        name_right = name.find('</a>')
        position.append(name[name_left + 2:name_right])
        for j in range(1, 5):
            name = str(c_page[i + j])
            name_left = name.find('">')
            name_right = name.find('</td>')
            position.append(name[name_left + 3:name_right - 1])
        data_table.append(position)
    return data_table

# вывод данных из таблицы с названием каждой ячейки
def show_table(table_head, data_table):
    size = len(table_head)
    count = len(data_table)
    for i in range(count):
        for j in range(size):
            print(table_head[j], end=': ')
            print(data_table[i][j])
        print()

# найти фрукт по первым буквам
def find_fruit_by_first_symb(data_table, name_fruit):
    name_fruit = name_fruit.title()
    count = len(data_table)
    find_index = []
    for i in range(count):
        if name_fruit in data_table[i][0]:
            find_index.append(data_table[i])
    return find_index


url = 'https://calorizator.ru/product/fruit'
soup = soup_parse(url)
table_head = get_table_head(soup)  # заголовки
my_list = get_all_value(soup)  # тело таблицы
while True:
    mode_now = input('Отправьте 1, чтобы просмотреть всю таблицу калорийности, \n'
                     'или 2, чтобы найти определенный фрукт\n> ')
    while True:
        if mode_now != '1' and mode_now != '2':
            print('Введено неверное значение, повторите ввод')
            mode_now = input('> ')
        else:
            break

    if mode_now == '1':
        print('Таблица калорийности продуктов » Фрукты\n')
        show_table(table_head, my_list)
    else:
        # find_fruit = 'манГО'  # манго, мангостан
        find_fruit = input('Введите полное название фрукта или первые буквы (от А до С): ')
        print()
        find_all = find_fruit_by_first_symb(my_list, find_fruit)
        if find_all:
            show_table(table_head, find_all)
        else:
            print('Не найдено')

    farther = input('Нажмите Enter для продолжения либо '
                    'отправьте любой символ для завершения\n> ')
    if farther != '':
        print('\nВы вышли из программы')
        break



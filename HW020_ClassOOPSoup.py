# Написать программу, где создадим класс Soup (для определения типа супа),
# принимающий 1 аргумент - который отвечает за основной продукт к выбираемому супу.
# В этом классе создать метод show_my_soup(), выводящий на печать
# «Суп - {Основной продукт}» в случае наличия добавки
# Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»

class Soup:
    def __init__(self, main_ingr=''):
        self.main_ingr = main_ingr

    def show_my_soup(self):
        if self.main_ingr:
            print(f'Суп - {self.main_ingr}')
        else:
            print('Обычный кипяток')

food1 = Soup('капуста')
food1.show_my_soup()

food2 = Soup()
food2.show_my_soup()

# Нужно написать программу
# В ней используем классы - имя студента name, номер группы group и список
# полученных оценок progress.
# В самой программе вводим список всех студентов.
# В программе нужно вывести список студентов, отсортированный по имени,
# А так же студентов, у которых низкие оценки

class Students:
    def __init__(self, name, group, progress=[], avg=0):
        self.name = name
        self.group = group
        self.progress = progress
        self.avg = avg

    def get_avg_grade(self):
        size = len(self.progress)
        if size > 0:
            sum = 0
            for i in range(size):
                sum += self.progress[i]
            self.avg = round(sum / size, 2)
        return self.avg

    def add_progress(self, grades):
        size = len(grades)
        for i in range(size):
            self.progress.append(grades[i])
        return self.progress

    def show_student(self):
        print(f'Имя: {self.name}, класс: {self.group}, оценки: ', end='')
        size = len(self.progress)
        if size > 0:
            for i in range(size - 1):
                print(self.progress[i], end=', ')
            print(self.progress[size - 1])
        else:
            print('нет оценок')


def list_students():
    students = []
    while True:
        name = input('Введите имя студента: ')
        group = input('Введите класс студента: ')
        grades = input('Введите оценки студента (от 1 до 5): ')
        size = len(grades)
        progress = []
        for i in range(size):
            if '1' <= grades[i] <= '5':
                progress.append(int(grades[i]))
        student = Students(name, group, progress)
        students.append((student.name, student.group, student.progress,
                         student.get_avg_grade()))
        stop = input('Нажмите Enter, чтобы продолжить, или отправьте 1, '
                     'чтобы остановиться: ')
        if stop == '1':
            return students

def print_sort_list_students_alph(students):
    print('\nСписок студентов по алфавиту')
    students.sort()
    size = len(students)
    for i in range(size):
        print('Имя: {:11}класс: {:7}оценки: '.format(students[i][0],
                                                     students[i][1]), end='')
        count = len(students[i][2])
        if count > 0:
            for j in range(count - 1):
                print(students[i][2][j], end=', ')
            print(students[i][2][count - 1])
        else:
            print('нет оценок')

def print_students_poor_progress(students, avg_max):
    print('\nСписок студентов с низкой успеваемостью')
    students.sort(key=lambda a: a[3], reverse=True)
    size = len(students)
    if size > 0 and students[size - 1][3] > avg_max:
        print('Отстающих нет')
    elif size == 0:
        print('Список студентов пустой')
    else:
        for i in range(size):
            if students[i][3] <= avg_max:
                print('Имя: {:11}класс: {:7}оценки: '.format(students[i][0],
                                                             students[i][1]), end='')
                count = len(students[i][2])
                if count > 0:
                    for j in range(count - 1):
                        print(students[i][2][j], end=', ')
                    print(students[i][2][count - 1],
                          f'  (средний балл: {students[i][3]})')
                else:
                    print('нет оценок')

# создать и отсортировать списки
list_stud = list_students()
print_sort_list_students_alph(list_stud)  # по алфавиту
print_students_poor_progress(list_stud, 3.5)  # по успеваемости (ср.балл от 3.5 и ниже)

# добавление оценок
print('\nПервый студент:')
stud4 = Students(list_stud[0][0], list_stud[0][1], list_stud[0][2])
stud4.show_student()
stud4.add_progress([4, 5])
stud4.show_student()
print('Средний балл: ', list_stud[0][3], ' --> ', stud4.get_avg_grade())
# print(f'Список:  {list_stud[0][0]}, {list_stud[0][1]}, {list_stud[0][2]}, {list_stud[0][3]}')
# print(f'Студент: {stud4.name}, {stud4.group}, {stud4.progress}, {stud4.avg}')

# Создание экземпляров класса без функций
print()
student1 = Students('Игорь', '5а')
student1.show_student()  # Имя: Игорь, класс: 5а, оценки: нет оценок
print(student1.get_avg_grade())  # 0

student1.add_progress([4, 5, 2, 3])
student1.show_student()  # Имя: Игорь, класс: 5а, оценки: 4, 5, 2, 3
print(student1.get_avg_grade())  # 3.5

student1.add_progress([4])
student1.show_student()  # Имя: Игорь, класс: 5а, оценки: 4, 5, 2, 3, 4
print(student1.get_avg_grade())  # 3.6

student2 = Students('Маша', '4б', [5, 5, 4])
student2.show_student()  # Имя: Маша, класс: 4б, оценки: 5, 5, 4
print(student2.get_avg_grade())  # 4.67



import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Вывести оценки определенного ученика
        5. Вывести средний балл ученика по определенному предмету
        6. Добавить новый предмет
        7. Редактировать название предмета
        8. Удалить предмет
        9. Добавить нового ученика
        10. Редактировать имя ученика
        11. Удалить ученика
        12. Добавить оценки ученика по предмету
        13. Редактировать оценки ученика по предмету
        14. Удалить оценки ученика по предмету
        15. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Вывести оценки определенного ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        if student in students:
            # выводим оценки ученика
            print(f'''{student}
                {students_marks[student]}''')
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 5:
        print('5. Вывести средний балл ученика по определенному предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        if student in students and class_ in classes:
            # находим сумму оценок по предмету
            marks_sum = sum(students_marks[student][class_])
            # находим количество оценок по предмету
            marks_count = len(students_marks[student][class_])
            # выводим средний балл по предмету
            print(f'{class_} - {marks_sum // marks_count}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 6:
        print('6. Добавить новый предмет')
        class_ = input('Введите название предмета: ')
        if class_ not in classes:
            classes.append(class_)
            for student in students:
                students_marks[student][class_] = []
            print(f'Предмет "{class_}" добавлен')
        else:
            print('ОШИБКА: такой предмет уже существует')

    elif command == 7:
        print('7. Редактировать название предмета')
        old_class = input('Введите текущее название предмета: ')
        if old_class in classes:
            new_class = input('Введите новое название предмета: ')
            if new_class not in classes:
                index = classes.index(old_class)
                classes[index] = new_class
                for student in students:
                    if old_class in students_marks[student]:
                        students_marks[student][new_class] = students_marks[student].pop(old_class)
                print(f'Предмет "{old_class}" переименован в "{new_class}"')
            else:
                print('ОШИБКА: предмет с таким названием уже существует')
        else:
            print('ОШИБКА: предмет не найден')

    elif command == 8:
        print('8. Удалить предмет')
        class_ = input('Введите название предмета для удаления: ')
        if class_ in classes:
            classes.remove(class_)
            for student in students:
                if class_ in students_marks[student]:
                    del students_marks[student][class_]
            print(f'Предмет "{class_}" удален')
        else:
            print('ОШИБКА: предмет не найден')

    elif command == 9:
        print('9. Добавить нового ученика')
        student = input('Введите имя ученика: ')
        if student not in students:
            students.append(student)
            students.sort()
            students_marks[student] = {}
            for class_ in classes:
                students_marks[student][class_] = []
            print(f'Ученик "{student}" добавлен')
        else:
            print('ОШИБКА: такой ученик уже существует')

    elif command == 10:
        print('10. Редактировать имя ученика')
        old_name = input('Введите текущее имя ученика: ')
        if old_name in students:
            new_name = input('Введите новое имя ученика: ')
            if new_name not in students:
                index = students.index(old_name)
                students[index] = new_name
                students.sort()
                students_marks[new_name] = students_marks.pop(old_name)
                print(f'Ученик "{old_name}" переименован в "{new_name}"')
            else:
                print('ОШИБКА: ученик с таким именем уже существует')
        else:
            print('ОШИБКА: ученик не найден')

    elif command == 11:
        print('11. Удалить ученика')
        student = input('Введите имя ученика для удаления: ')
        if student in students:
            students.remove(student)
            del students_marks[student]
            print(f'Ученик "{student}" удален')
        else:
            print('ОШИБКА: ученик не найден')

    elif command == 12:
        print('12. Добавить оценки ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students and class_ in classes:
            count_input = input('Сколько оценок добавить? ')
            if count_input.isdigit():
                count = int(count_input)
                for i in range(count):
                    mark_input = input(f'Введите оценку {i + 1}: ')
                    if mark_input.isdigit():
                        mark = int(mark_input)
                        students_marks[student][class_].append(mark)
                    else:
                        print(f'ОШИБКА: оценка "{mark_input}" должна быть числом')
                print(f'Добавлено {count} оценок для {student} по предмету {class_}')
            else:
                print('ОШИБКА: количество оценок должно быть числом')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 13:
        print('13. Редактировать оценки ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students and class_ in classes:
            if students_marks[student][class_]:
                print(f'Текущие оценки: {students_marks[student][class_]}')
                students_marks[student][class_] = []
                count_input = input('Сколько оценок ввести? ')
                if count_input.isdigit():
                    count = int(count_input)
                    for i in range(count):
                        mark_input = input(f'Введите оценку {i + 1}: ')
                        if mark_input.isdigit():
                            mark = int(mark_input)
                            students_marks[student][class_].append(mark)
                        else:
                            print(f'ОШИБКА: оценка "{mark_input}" должна быть числом')
                    print(f'Обновлено {count} оценок для {student} по предмету {class_}')
                else:
                    print('ОШИБКА: количество оценок должно быть числом')
            else:
                print('У ученика нет оценок по этому предмету')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 14:
        print('14. Удалить оценки ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students and class_ in classes:
            students_marks[student][class_] = []
            print(f'Оценки {student} по предмету {class_} удалены')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 15:
        print('15. Выход из программы')
        break
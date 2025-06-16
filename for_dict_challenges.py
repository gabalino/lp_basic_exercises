def sum_dict(elements: list, param='first_name') -> dict:
    result = dict()
    for element in elements:
        k = element[param]
        result[k] = result.get(k, 0) + 1
    return result

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
print('\n# Задание 1')
names = sum_dict(students)
for name, count in names.items():
    print(f"{name}: {count}")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
print('\n# Задание 2')
most_name = ''
names = sum_dict(students)
most_count = max(names.values())
for name, count in names.items():
    if count == most_count:
        most_name = name
print(f"Самое частое имя среди учеников: {most_name}")

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],
    [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
print('\n# Задание 3')
for number, grade in enumerate(school_students, start=1):
    most_name = ''
    names = sum_dict(grade)
    most_count = max(names.values())
    for name, count in names.items():
        if count == most_count:
            most_name = name
    print(f"Самое частое имя в классе {number}: {most_name}")

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
print('\n# Задание 4')
for grade in school:
    boys, girls = 0, 0
    for student in grade['students']:
        if is_male[student['first_name']]:
            boys += 1
        else:
            girls += 1
    print(f"Класс {grade['class']}: девочки {girls}, мальчики {boys} ")
# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
print('\n# Задание 5')
gender = {'boys': {'grade': '', 'count': 0}, 'girls': {'grade': ' ', 'count': 0}}
for grade in school:
    boys, girls = 0, 0
    for student in grade['students']:
        if is_male[student['first_name']]:
            boys += 1
        else:
            girls += 1
    if gender['boys'].get('count', 0) < boys:
        gender['boys']['grade'] = grade['class']
        gender['boys']['count'] = boys
    if gender['girls'].get('count', 0) < girls:
        gender['girls']['grade'] = grade['class']
        gender['girls']['count'] = girls
print(f'Больше всего мальчиков в классе {gender["boys"]["grade"]}')
print(f'Больше всего девочек в классе {gender["girls"]["grade"]}')

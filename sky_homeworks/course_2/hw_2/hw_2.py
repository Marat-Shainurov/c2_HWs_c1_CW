from functions_c2_hw_2 import *

# Объвляем в качестве перенменных названия файлов с данными о студентах и профессиях
students = "students.txt"
professions = "professions.txt"

# Старт программы
print("Введите номер студента: ")
user_number = int(input())

# Сверяем ввод пользователя с допустимым кол-вом студентов, выводим инфо по студенту и eго знаниях
if user_number in range(1, len(load_students(students)) + 1):
    student_info, students_name = get_student_by_pk(user_number)
    print(f"Студент {students_name}")
    for value in student_info.values():
        print(f'Знает {", ".join(value)}')

# Сверяем ввод пользователя с допустимым списком профессий, выводим инфо по пригодности и наличию необходимых знаний
    print("Выберете специальность: ")
    user_profession = input().lower()

    if user_profession in load_professions(professions):
        profession_stats = check_fitness(students_name, user_profession)
        print(f'Пригодность {profession_stats["fit_percent"]}%')

        for element in profession_stats:
            print(f'{students_name} знает', end=" ")
            for language in range(len(profession_stats["has"])):
                print(profession_stats["has"][language], end=", " if language != (len(profession_stats["has"]) - 1) else "")

            print(f'\n{students_name} не знает', end=" ")
            for language in range(len(profession_stats["lacks"])):
                print(profession_stats["lacks"][language], end=", " if language != (len(profession_stats["lacks"]) - 1) else "")

            break
    else:
        print("У нас нет такой профессии")
        quit()

else:
    print("У нас нет такого студента")

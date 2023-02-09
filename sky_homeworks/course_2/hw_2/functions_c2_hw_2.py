import json


def load_students(filename):
    """
    Возвращает список студентов из файла
    """
    with open(filename) as file:
        content = file.read()
        content_json = json.loads(content)
        students_list = []
        for student in content_json:
            student_name = student["full_name"]
            students_list.append(student_name)
        return students_list


def load_professions(filename):
    """
    Возвращает список профессий из файла
    """
    with open(filename) as file:
        content = file.read()
        content_json = json.loads(content)
        professions_list = []
        for profession in content_json:
            profession_name = profession["title"].lower()
            professions_list.append(profession_name)
        return professions_list


def get_student_by_pk(pk):
    """
    Возвращает инфо по cтуденту в словаре по его pk
    """
    with open("students.txt") as file:
        content = file.read()
        content_json = json.loads(content)
        students_info = {}
        for student in range(len(content_json)):
            students_info[content_json[pk - 1]["full_name"]] = content_json[pk - 1]["skills"]
            return students_info, content_json[pk - 1]["full_name"]


def get_profession_by_title(title):
    """
    Получает словарь с инфо о профессии по title
    """
    with open("professions.txt") as file:
        content = file.read()
        content_json = json.loads(content)
        profession_info = {}
        title = title.lower()
        for profession in content_json:
            if title == profession["title"].lower():
                profession_info[title] = profession["skills"]
        return profession_info


def check_fitness(student, profession):
    """
    Возвращает словарь типа:
```python
{
  "has": ["Python", "Linux"],
  "lacks": ["Docker, SQL"],
  "fit_percent": 50
}
```
Эта функция должна использовать методы множеств.
    """

    with open("students.txt") as file:
        content = file.read()
        content_json = json.loads(content)
        res = {}

        for line in content_json:
            if student == line["full_name"]:
                profession_dict = get_profession_by_title(profession)
                for key, value in profession_dict.items():
                    needed_set = set(value)
                    has_set = set(line["skills"])
                    res["has"] = list(has_set.intersection(needed_set))
                    res["lacks"] = list(needed_set.difference(has_set))
                    has_skills = len(needed_set) - len(res["lacks"])
                    res["fit_percent"] = round(has_skills / len(needed_set) * 100)

        return res

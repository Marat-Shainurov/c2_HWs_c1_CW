import json


def get_questions_list(filename, class_name):
    """
    Читает файл filename,
    Созает на его основе список из экземпляров класса class_name, с вопросами, сложностью, правильными ответами.
    """
    with open(filename, encoding='utf-8') as file:
        content = file.read()
        content_python = json.loads(content)
        questions_list = []
        for element in content_python:
            q = element["q"]
            d = element["d"]
            a = element["a"]
            questions_list.append(class_name(q, d, a))
        return questions_list


def get_final_results(questions):
    """
    Возвращает результаты игры,на основе итогового списка questions с ответами
    """
    correct_ans_count = 0
    final_results = 0
    for question in questions:
        if question.user_answer == question.correct_answer:
            round_score = int(question.difficulty) * 10
            final_results += round_score
            correct_ans_count += 1

    return f"Вот и всё! \nОтвечено {correct_ans_count} вопроса из {len(questions)}. \nНабрано баллов: {final_results}"

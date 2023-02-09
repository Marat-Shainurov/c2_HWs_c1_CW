# Импортируем модуль random(shuffle) и функции из файла с функциями "functions_hw_3",
from random import shuffle
from functions_hw_3 import get_questions_list, get_final_results


# создаем класс Questions
class Question:

    def __init__(self, question, difficulty, correct_answer, is_questioned=False, user_answer=None):
        self.question = question
        self.difficulty = difficulty
        self.correct_answer = correct_answer
        self.is_questioned = is_questioned
        self.user_answer = user_answer
        self.score = int(self.difficulty) * 10

    def build_question(self):
        """
        Возвращает вопрос и сложность вопроса
        """
        return f"{self.question} \nСложность: {self.difficulty}/5"

    def is_correct(self, user_answer):
        """
        Возвращает правильность ответа.
        """
        return True if user_answer == self.correct_answer else False

    def get_feedback_and_points(self, is_correct_answer):
        """
        Возвращает комментарий правильности ответа пользователя.
        Возвращает количество баллов.
        """
        return f"Ответ верный, получено {self.score} баллов" if is_correct_answer \
            else f"Ответ неверный, верный ответ {self.correct_answer}"

    def get_points(self):
        """
        Возвращает количество баллов за вопрос.
        """
        return self.score


# Создаем список с экземплярами класса Questions, используя функцию get_questions_list()
questions = get_questions_list("questions_json.txt", Question)
shuffle(questions)

# Старт программы
print("Игра начинается!")
print("")

for element in questions:
    print(element.build_question())
    element.user_answer = input("Ответ: ")
    result = element.is_correct(element.user_answer)
    element.is_questioned = True
    print(element.get_feedback_and_points(result))
    print("")

# Выводим результаты, используя функцию get_final_results()
print(get_final_results(questions))

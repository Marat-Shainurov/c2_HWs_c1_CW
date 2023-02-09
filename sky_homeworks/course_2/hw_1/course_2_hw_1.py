# Импортируем все функции из functions_hw_1
from functions_hw_1 import *

# Переменная для подсчета баллов, переменные с файлами
user_result = 0
history = "history.txt"
words = "words.txt"

# Запуск программы
print("Привет! Введите Ваше имя: ")
user_name = input()

# Присваиваем переменной dict_to_play значение, с помощью функции guess_words()
dict_to_play = guess_words(words)

# Цикл по вопросам и ответам пользователя, с накоплением баллов и выводом правильных/неправильных ответов
for word, anagram in dict_to_play.items():
    print(f"Угадайте слово: {anagram}")
    user_answer = input()
    if user_answer == word:
        user_result += 10
        print("Верно! Вы получаете 10 очков")
    else:
        print(f"Неверно! Верный ответ – {word}")

# Сохраняем результаты игрока в файл history.txt
record_answers(history, user_name, user_result)

# Выводим результаты, с помощью функции result()
results(history)

import random

# Добавляем словарь с переводом символов на язык Морзе
morse_dict = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}

# Создаем список с ответами, список с английскими словами.
answers = []
eng_words = ["fun", "truth", "love", "music", "freedom", "safety"]


def morse_translate(word):
    """
    Функция переводит слово с английского языка на язык Морзе.
    """

    morse_word = []
    for letter in word:
        for symbol, translation in morse_dict.items():
            if letter == symbol:
                morse_word.append(morse_dict[symbol])
    return " ".join(morse_word)


def random_word():
    """
    Функция генерирует случайное слово из списка eng_words.
    """
    element_to_choose = random.choice(eng_words)
    return element_to_choose


def get_stats(user_list):
    """
    Функция выводит результаты игры, на основе ответов, собранных в списке answers.
    """
    print(f"Всего задачек: {len(user_list)}")
    print(f"Отвечено верно: {user_list.count(True)}")
    print(f"Отвечено неверно: {user_list.count(False)}")


# Старт программы
print("Привет! Сегодня мы потренируемся расшифровывать морзянку.")

greeting = input("Нажмите Enter и начнем: ")
while greeting != "":
    greeting = input("Попробуйте еще раз: ")

# Запуск цикла с вопросами и ответами
for x in range(5):
    print("")
    word_per_cycle = random_word()
    print(f"Слово {x + 1}: {morse_translate(word_per_cycle)}")
    user_input = input("Ответ: ")
    if user_input == word_per_cycle:
        print(f"Верно, {word_per_cycle}!")
        answers.append(True)
    else:
        print(f"Неверно, {word_per_cycle}!")
        answers.append(False)

print("")
get_stats(answers)

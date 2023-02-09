# Создаем словари со словами, по уровням сложности
word_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}

words_hard = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
}

# Создаем словарь с уровнями игрока, словарь с ответами, словарь с набором уровней сложности, счетчик правильнх ответов
levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}
answers = {}
words = {}
score = 0

# Старт программы, проверка выбранной сложности и выбор нужного словаря
user_level = input("Выберите уровень сложности - легкий, средний, сложный: ")
user_level_low = user_level.lower()

if user_level_low == "легкий" or user_level_low == "средний" or user_level_low == "сложный":
    if user_level_low == "легкий":
        words = word_easy
    elif user_level_low == "средний":
        words = words_medium
    elif user_level_low == "сложный":
        words = words_hard

    print(f"\nВыбран уровень сложности {user_level_low}, мы предложим 5 слов, подберите перевод.")
    enter = input("Нажмите Enter")
    while enter != "":
        enter = input("Нажмите Enter, пожалуйста")

# Запускаем цикл с вопросами из нужного словаря, принимаем ответы в словарь answers
    for w, t in words.items():
        print(f"\n{w.title()}, {len(t)} букв, начинается на {t[0]}...")
        user_answer = input()
        if user_answer == t:
            score += 1
            answers[w] = True
            print(f"Верно, {w.title()} — это {t}")
        else:
            answers[w] = False
            print(f"Неверно, {w.title()} — это {t}")
        enter = input("Нажмите Enter")

# Выводим итоги с помощью нескольких циклов, обращаясь к собранному словарям с ответами и к словарю с уровнями
    print("\nПравильно отвечены слова: ")

    for a, c in answers.items():
        if c:
            print(a.title())

    print("\nНеправильно отвечены слова: ")

    for a, c in answers.items():
        if not c:
            print(a.title())

    print(f"\nВаш ранг: {levels[score]}")

else:
    print("Вы выбрали некорректный уровень. Перезапустите программу, пожалуйста.")
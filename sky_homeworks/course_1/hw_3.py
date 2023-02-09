# Задаем списки и переменные
questions = ["My name ___ Vova. Ответ: ", "I ___ a coder. Ответ: ", "I live ___ Moscow. Ответ: "]
answers = ["is", "am", "in"]
attempts = [2, 2, 2]
correct_ans_counter = 0
answer_score = 0

# Запускаем цикл по готовности пользователя
print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!')
greeting = input()
while greeting != "ready":
    greeting = input("Кажется, вы не хотите играть. Очень жаль \n")

# Запускаем основной цикл с вопросами. Внутри проверяем правильность ответов, учитываем попытки, рассчитываем кол-во баллов.
for question in range(len(questions)):
    answer = input(questions[question])
    while answer != answers[question] and attempts[question] >= 1:
        answer = input(f"Осталось попыток: {attempts[question]}, попробуйте еще раз!")
        attempts[question] -= 1
    if answer == answers[question]:
        correct_ans_counter += 1
        print("Верно!")
        if attempts[question] == 2:
            answer_score += 3
        elif attempts[question] == 1:
            answer_score += 2
        elif attempts[question] == 0:
            answer_score += 1
    elif attempts[question] < 1:
        print(f"Увы, но нет. Правильный ответ {answers[question]}")

# Производим расчет доли правильных ответов
total_percentage = round(correct_ans_counter / len(questions) * 100)

print(f"Вот и все! \nВы ответили на {correct_ans_counter} вопросов из {len(questions)} верно, это {total_percentage} процентов.")
print(f"Вы набрали {answer_score} баллов.")
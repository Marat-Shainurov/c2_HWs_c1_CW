import random


def shuffle_string(line):
    """
    Получает строку, перемешивает ее буквы, возвращает перемешанную строку
    """

    line_list = []
    for letter in line:
        line_list.append(letter)
    random.shuffle(line_list)
    return "".join(line_list)


def guess_words(filename):
    """
    Читает файл, выводит словарь, где key - слово, value - это же слово, но с перемешанными буквами
    """

    with open(filename) as file:
        words_list = {}
        for line in file:
            line = line.rstrip("\n")
            line_shuffled = shuffle_string(line)
            words_list[line] = line_shuffled
        return words_list


def record_answers(filename, user_name, user_result):
    """
    Записывает результаты в файл, получив название файла, имя игрока и результат игры
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{user_name}: {user_result}\n")


def results(filename):
    """
    Читает файл, выводит накопительное кол-во сыгранных игр, лучший результат
    """

    games_count = 0
    max_res = 0
    with open(filename) as file:
        for line in file:
            games_count += 1
            new_line = line.rstrip("\n").split(": ")
            if int(new_line[1]) > max_res:
                max_res = int(new_line[1])

        print(f"Максимальный рекорд - {max_res}")
        print(f"Всего игр сыграно: {games_count}")

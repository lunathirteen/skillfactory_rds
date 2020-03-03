import numpy as np


def game_core_v1(number):
    '''Просто угадываем на random,
       никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return(count)  # выход из цикла, если угадали


def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v1)  # запускаем


def game_core_v2(number):
    '''Сначала устанавливаем любое random число,
       а потом уменьшаем или увеличиваем его в зависимости от того,
       больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1, 100)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return(count)  # выход из цикла, если угадали


score_game(game_core_v2)  # Проверяем


def game_core_v3(number: int):
    '''Сначала устанавливаем значения левой и правой границ
       возможного диапазона загадываемых чисел.
       Выбираем начальное значение в середине диапазона.
       Далее в зависимости больше или меньше наше число, чем загаданное,
       сдвигаем границы диапазона поиска.

       Функция принимает загаданное число и возвращает число попыток'''

    count = 0
    left = 1
    right = 100
    predict = (right+left)//2

    while number != predict:
        count += 1
        if number > predict:
            left = predict + 1
        else:
            right = predict - 1
        predict = (left+right) // 2

    return count


score_game(game_core_v3)  # Проверяем

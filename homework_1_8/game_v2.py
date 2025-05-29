"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    start = 1 #начало интервала поиска
    finish= 100 #конец интервала поиска
    median =(finish+start)//2 #медиана интервала и в последующем искомое число
    
    while True:
        count += 1
        if start == median or finish == median: #сначала отметаем крайнии случаи когда искомое число 1 или 100
            break
        elif median > number: #узнаем искомое число больше или меньше середины интервала и меняем или начало или конец интервала
            finish = median
            median = (finish + start)//2 
        elif median < number:
            start = median
            median = (finish + start)//2 
        elif median == number: #выходим когда нашли наше число
            break
    return(count)


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return(score)


if __name__ == "__main__":
    # RUN
    score_game(random_predict)

from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_num(num: int) -> bool:
    return num % 2 == 0


def get_num_and_is_even_answer():
    RANDOM_NUM = randint(1, 100)
    is_even = is_even_num(RANDOM_NUM)
    answer = str()
    if is_even:
        answer = 'yes'
    else:
        answer = 'no'
    return RANDOM_NUM, answer

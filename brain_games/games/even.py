from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RANGE = 1
MAX_RANGE = 100


def is_even_num(num: int) -> bool:
    return num % 2 == 0


def get_question_and_answer():
    RANDOM_NUM = randint(MIN_RANGE, MAX_RANGE)
    is_even = is_even_num(RANDOM_NUM)
    if is_even:
        answer = 'yes'
    else:
        answer = 'no'
    return RANDOM_NUM, answer

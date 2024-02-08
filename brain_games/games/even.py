from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
RANDOM_NUM = randint(1, 100)


def is_even_num(num: int) -> bool:
    return num % 2 == 0


def get_yes_or_no_answer(value: bool) -> str:
    if value:
        return 'yes'
    else:
        return 'no'


is_even = is_even_num(RANDOM_NUM)
yes_or_no_answer = get_yes_or_no_answer(is_even)

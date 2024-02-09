from random import randint

GAME_RULE = ('Answer "yes" if given number is prime. '
             'Otherwise answer "no".')
MIN_RANGE = 2
MAX_RANGE = 100


def is_prime_num(num: int) -> bool:
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            return False
            break
    else:
        return True


def get_question_and_answer():
    RANDOM_NUM = randint(MIN_RANGE, MAX_RANGE)
    is_prime = is_prime_num(RANDOM_NUM)
    if is_prime:
        answer = 'yes'
    else:
        answer = 'no'
    return RANDOM_NUM, answer

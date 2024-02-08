from random import randint

GAME_RULE = ('Answer "yes" if given number is prime. '
             'Otherwise answer "no".')
RANDOM_NUM = randint(2, 100)


def is_prime_num(num: int) -> bool:
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            return False
            break
    else:
        return True


def get_yes_or_no_answer(value: bool) -> str:
    if value:
        return 'yes'
    else:
        return 'no'


is_prime = is_prime_num(RANDOM_NUM)
yes_or_no_answer = get_yes_or_no_answer(is_prime)

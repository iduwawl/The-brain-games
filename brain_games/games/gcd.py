from random import randint

GAME_RULE = "Find the greatest common divisor of given numbers."
MIN_RANGE = 1
MAX_RANGE = 100


def get_gcd(num1: int, num2: int) -> int:
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1


def get_question_and_answer():
    RANDOM_NUM1 = randint(MIN_RANGE, MAX_RANGE)
    RANDOM_NUM2 = randint(MIN_RANGE, MAX_RANGE)
    nod = get_gcd(RANDOM_NUM1, RANDOM_NUM2)
    str_numbers = f"{RANDOM_NUM1} {RANDOM_NUM2}"
    return str_numbers, str(nod)

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


def get_question_and_correct_answer():
    random_num1 = randint(MIN_RANGE, MAX_RANGE)
    random_num2 = randint(MIN_RANGE, MAX_RANGE)
    correct_answer = get_gcd(random_num1, random_num2)
    question = f"{random_num1} {random_num2}"
    return question, str(correct_answer)

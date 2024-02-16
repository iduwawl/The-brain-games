from random import randint

GAME_RULE = ('Answer "yes" if given number is prime. '
             'Otherwise answer "no".')
MIN_RANGE = 2
MAX_RANGE = 100


def is_prime_num(num: int) -> bool:
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            return False
    return True


def get_question_and_correct_answer():
    question = randint(MIN_RANGE, MAX_RANGE)
    if is_prime_num(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

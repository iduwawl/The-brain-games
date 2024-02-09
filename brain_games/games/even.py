from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RANGE = 1
MAX_RANGE = 100


def is_even_num(num: int) -> bool:
    return num % 2 == 0


def get_question_and_correct_answer():
    question = randint(MIN_RANGE, MAX_RANGE)
    if is_even_num(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

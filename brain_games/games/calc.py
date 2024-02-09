from random import randint
from random import choice

GAME_RULE = "What is the result of the expression?"
MIN_RANGE = 1
MAX_RANGE = 100


def get_question_and_correct_answer():
    random_num1 = randint(MIN_RANGE, MAX_RANGE)
    random_num2 = randint(MIN_RANGE, MAX_RANGE)
    op1, op2, op3 = "-", "+", "*"
    random_op = choice([op1, op2, op3])
    question = f"{random_num1} {random_op} {random_num2}"
    correct_answer = eval(question)
    return question, str(correct_answer)

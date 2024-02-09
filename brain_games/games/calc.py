from random import randint
from random import choice

GAME_RULE = "What is the result of the expression?"
MIN_RANGE = 1
MAX_RANGE = 100


def get_question_and_answer():
    RANDOM_NUM1 = randint(MIN_RANGE, MAX_RANGE)
    RANDOM_NUM2 = randint(MIN_RANGE, MAX_RANGE)
    OP1, OP2, OP3 = "-", "+", "*"
    random_op = choice([OP1, OP2, OP3])
    expression = f"{RANDOM_NUM1} {random_op} {RANDOM_NUM2}"
    result_of_expression = eval(expression)
    return expression, str(result_of_expression)

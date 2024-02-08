from random import randint
from random import choice

GAME_RULE = "What is the result of the expression?"


def get_expression_and_result():
    RANDOM_NUM1 = randint(1, 100)
    RANDOM_NUM2 = randint(1, 100)
    op1, op2, op3 = "-", "+", "*"
    random_op = choice([op1, op2, op3])
    expression = f"{RANDOM_NUM1} {random_op} {RANDOM_NUM2}"
    result_of_expression = eval(expression)
    return expression, str(result_of_expression)

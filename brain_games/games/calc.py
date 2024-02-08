from random import randint
from random import choice

GAME_RULE = "What is the result of the expression?"
RANDOM_NUM1 = randint(1, 100)
RANDOM_NUM2 = randint(1, 100)
OP1, OP2, OP3 = "-", "+", "*"
random_op = choice([OP1, OP2, OP3])


def get_expression(num1, operator, num2):
    expression = f"{num1} {operator} {num2}"
    return expression


def get_result_of_expression(expression: str) -> str:
    result_of_expression = eval(expression)
    return str(result_of_expression)


expression = get_expression(RANDOM_NUM1, random_op, RANDOM_NUM2)
result_of_expression = get_result_of_expression(expression)

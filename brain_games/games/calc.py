from brain_games.rules import CALC_GAME_RULE
from brain_games.engine import run_game
from random import randint
from random import choice


def get_expression_and_result():
    random_num1 = randint(1, 100)
    random_num2 = randint(1, 100)
    op1, op2, op3 = "-", "+", "*"
    random_op = choice([op1, op2, op3])
    expression = f"{random_num1} {random_op} {random_num2}"
    result_of_calc = eval(expression)
    return expression, str(result_of_calc)


def run_calc_game():
    run_game(get_expression_and_result, CALC_GAME_RULE)

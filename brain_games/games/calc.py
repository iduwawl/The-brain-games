from brain_games.rules import CALC_GAME_RULE
from brain_games.engine import run_game
from random import randint
from random import choice


def get_expression_and_result():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    operators = ("-", "+", "*")
    random_op = choice(operators)
    expression = f"{first_number} {random_op} {second_number}"
    result = eval(first_number, random_op, second_number)
    return expression, str(result)


def run_calc_game():
    run_game(get_expression_and_result, CALC_GAME_RULE)

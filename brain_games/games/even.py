from brain_games.rules import EVEN_GAME_RULE
from brain_games.engine import run_game
from random import randint


def get_num_and_is_even_answer():
    number = randint(1, 100)
    is_even = 'yes' if number % 2 == 0 else 'no'
    return number, is_even


def run_even_game():
    run_game(get_num_and_is_even_answer, EVEN_GAME_RULE)
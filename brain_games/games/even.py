from brain_games.rules import EVEN_GAME_RULE
from brain_games.engine import run_game
from random import randint


def get_num_and_is_even_answer():
    random_num = randint(1, 100)
    is_even = 'yes' if random_num % 2 == 0 else 'no'
    return random_num, is_even


def run_even_game():
    run_game(get_num_and_is_even_answer, EVEN_GAME_RULE)

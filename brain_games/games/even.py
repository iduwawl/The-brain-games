from brain_games.rules import EVEN_GAME_RULE
from brain_games.engine import run_game
from random import randint


def is_even_num(num: int) -> bool:
    return True if num % 2 == 0 else False


def get_num_and_is_even_answer():
    random_num = randint(1, 100)
    is_even = is_even_num(random_num)
    answer = str()
    if is_even:
        answer = 'yes'
    else:
        answer = 'no'
    return random_num, answer


def run_even_game():
    run_game(get_num_and_is_even_answer, EVEN_GAME_RULE)

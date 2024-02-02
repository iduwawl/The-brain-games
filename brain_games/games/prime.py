from brain_games.rules import PRIME_GAME_RULE
from brain_games.engine import run_game
from random import randint


def is_prime_num(number: int) -> str:
    for i in range(2, int(number / 2) + 1):
        if (number % i) == 0:
            return 'no'
            break
    else:
        return 'yes'


def get_num_and_is_prime():
    number = randint(2, 100)
    is_prime = is_prime_num(number)
    return number, is_prime


def run_prime_game():
    run_game(get_num_and_is_prime, PRIME_GAME_RULE)

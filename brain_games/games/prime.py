from brain_games.rules import PRIME_GAME_RULE
from brain_games.engine import run_game
from random import randint


def is_prime_num(num: int) -> str:
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            return 'no'
            break
    else:
        return 'yes'


def get_num_and_is_prime():
    random_num = randint(2, 100)
    is_prime = is_prime_num(random_num)
    return random_num, is_prime


def run_prime_game():
    run_game(get_num_and_is_prime, PRIME_GAME_RULE)

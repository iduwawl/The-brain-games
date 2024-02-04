from brain_games.rules import GCD_GAME_RULE
from brain_games.engine import run_game
from random import randint


def get_nod(num1: int, num2: int):
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1


def get_nums_and_nod():
    random_num1 = randint(1, 100)
    random_num2 = randint(1, 100)
    nod = get_nod(random_num1, random_num2)
    str_numbers = f"{random_num1} {random_num2}"
    return str_numbers, str(nod)


def run_gcd_game():
    run_game(get_nums_and_nod, GCD_GAME_RULE)

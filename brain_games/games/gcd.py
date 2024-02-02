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
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    nod = get_nod(first_number, second_number)
    numbers = f"{first_number} {second_number}"
    return numbers, str(nod)


def run_gcd_game():
    run_game(get_nums_and_nod, GCD_GAME_RULE)

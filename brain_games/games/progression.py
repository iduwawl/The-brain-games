from brain_games.rules import PROGRESSION_GAME_RULE
from brain_games.engine import run_game
from random import choice
from random import randint


def get_list_and_skip_num():
    random_list = [str(x) for x in range(1, 100, randint(1, 10))][0:10]
    random_num = choice(random_list)
    list_with_skip_num = " ".join(random_list).replace(random_num, "..", 1)
    return list_with_skip_num, random_num


def run_progression_game():
    run_game(get_list_and_skip_num, PROGRESSION_GAME_RULE)

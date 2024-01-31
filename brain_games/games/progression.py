from brain_games.rules import PROGRESSION_GAME_RULE
from brain_games.engine import run_game
from random import choice
from random import randint


def get_list_and_skip_num():
    random_list = [str(x) for x in range(1, 100, randint(1, 10))]
    sliced_list = random_list[1:11]
    random_number = choice(sliced_list)
    join_list = " ".join(sliced_list)
    list_with_skip_num = join_list.replace(random_number, "..", 1)
    return list_with_skip_num, random_number


def run_progression_game():
    run_game(get_list_and_skip_num, PROGRESSION_GAME_RULE)

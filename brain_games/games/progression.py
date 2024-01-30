from brain_games.rules import PROGRESSION_GAME_RULE
from brain_games.engine import run_game
from random import choice
from random import randint


def get_list_and_skip_num():
    random_step = randint(1, 10)
    random_list = [str(x) for x in range(1, 100, random_step)]
    sliced_list = random_list[1:11]
    random_number = choice(sliced_list)
    join_list_in_str = " ".join(sliced_list)
    str_with_skip_num = join_list_in_str.replace(random_number, "..", 1)
    return str_with_skip_num, random_number


def run_progression_game():
    run_game(get_list_and_skip_num, PROGRESSION_GAME_RULE)

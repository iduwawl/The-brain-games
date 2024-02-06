from random import choice
from random import randint

GAME_RULE = "What number is missing in the progression?"


def get_random_list():
    random_list = [str(x) for x in range(1, 100, randint(1, 10))][0:10]
    return random_list


def get_transformed_list_to_str(list_progression) -> str:
    list_progression = get_random_list()
    str_progression = " ".join(list_progression)
    return str_progression


def get_str_with_miss_num_and_num(str_progression: str):
    str_progression = get_transformed_list_to_str()
    random_num = choice(str_progression)
    str_with_mis_num = str_progression.replace(random_num, "..", 1)
    return str_with_mis_num, random_num

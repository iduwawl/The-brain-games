from random import choice
from random import randint

GAME_RULE = "What number is missing in the progression?"


def get_random_list():
    random_list = [str(x) for x in range(1, 100, randint(1, 10))][0:10]
    return random_list


def get_transformed_list_to_str(random_list: list) -> str:
    random_list = get_random_list()
    progrss_with_miss_num = " ".join(random_list)
    return progrss_with_miss_num


def get_str_with_miss_num_and_num(random_str: str):
    random_str = get_transformed_list_to_str()
    random_num = choice(random_str)
    str_with_mis_num = random_str.replace(random_num, "..", 1)
    return str_with_mis_num, random_num

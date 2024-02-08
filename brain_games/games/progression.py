from random import choice
from random import randint

GAME_RULE = "What number is missing in the progression?"


def get_random_list() -> list:
    STEP = randint(1, 10)
    random_list = [str(x) for x in range(1, 100, STEP)]
    sliced_list = random_list[0:10]
    return sliced_list


def get_num_from_list(what_list: list) -> str:
    return choice(what_list)


def get_joined_list(list_to_join: list) -> str:
    str_from_list = " ".join(list_to_join)
    return str_from_list


def get_str_with_replaced_num(what_str: str, num: str) -> str:
    return what_str.replace(num, "..", 1)


random_list = get_random_list
num_from_list = get_num_from_list(random_list)
joined_list = get_joined_list(random_list)
str_with_replaced_num = get_str_with_replaced_num(
    joined_list, num_from_list)

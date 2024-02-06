from random import choice
from random import randint

GAME_RULE = "What number is missing in the progression?"


def get_random_list():
    random_list = [str(x) for x in range(1, 100, randint(1, 10))][0:10]
    return random_list


def get_joined_list(list_to_join: list) -> str:
    list_to_join = get_random_list()
    joined_list = " ".join(list_to_join)
    return joined_list


def get_list_with_replaced_num_and_num(list_to_replace_num):
    list_to_replace_num = get_joined_list()
    random_num = choice(list_to_replace_num)
    list_with_replaced_num = list_to_replace_num.replace(random_num, "..", 1)
    return list_with_replaced_num, random_num

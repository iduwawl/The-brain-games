from random import choice
from random import randint

GAME_RULE = "What number is missing in the progression?"


def get_random_list():
    random_list = [str(x) for x in range(1, 100, randint(1, 10))][0:10]
    return random_list


def turn_list_to_str_with_skip_num():
    random_list = get_random_list()
    random_num = choice(random_list)
    list_with_skip_num = " ".join(random_list).replace(random_num, "..", 1)
    return list_with_skip_numm


def get_list_and_skip_num():
    random_list = [str(x) for x in range(1, 100, randint(1, 10))][0:10]
    random_num = choice(random_list)
    list_with_skip_num = " ".join(random_list).replace(random_num, "..", 1)
    return list_with_skip_num, random_num

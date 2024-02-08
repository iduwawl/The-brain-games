from random import choice
from random import randint

GAME_RULE = "What number is missing in the progression?"


def get_random_list_and_num():
    random_list = [str(x) for x in range(1, 100, randint(1, 10))][0:10]
    random_num = choice(random_list)
    return random_list, random_num


def get_joined_list_with_replaced_num_and_num():
    list_to_join, num_to_replace = get_random_list_and_num()
    joined_list = " ".join(list_to_join).replace(num_to_replace, "..", 1)
    return joined_list, num_to_replace

from random import randint

GAME_RULE = "Find the greatest common divisor of given numbers."


def get_gcd(num1: int, num2: int) -> int:
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1


def get_nums_and_gcd():
    random_num1 = randint(1, 100)
    random_num2 = randint(1, 100)
    nod = get_nod(random_num1, random_num2)
    str_numbers = f"{random_num1} {random_num2}"
    return str_numbers, str(nod)

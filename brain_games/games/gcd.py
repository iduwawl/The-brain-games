from random import randint

GAME_RULE = "Find the greatest common divisor of given numbers."
RANDOM_NUM1 = randint(1, 100)
RANDOM_NUM2 = randint(1, 100)


def get_gcd(num1: int, num2: int) -> int:
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1


def get_str_nums(num1: int, num2: int) -> str:
    str_nums = f"{num1} {num2}"
    return str_nums


gcd_of_nums = get_gcd(RANDOM_NUM1, RANDOM_NUM2)
str_nums = get_str_nums(RANDOM_NUM1, RANDOM_NUM2)

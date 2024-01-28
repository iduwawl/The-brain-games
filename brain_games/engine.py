from random import randint
from prompt import string


def welcome_gamer() -> str:
    print("Welcome to the Brain Games!")
    name = string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def congrats(whom: str):
    print(f"Congratulations, {whom}!")


def is_equaly(a, b, name: str) -> str:
    """Check the a == b"""
    if a == b:
        print('Correct')
    else:
        print(f"'{a}' is wrong answer ;(.", end=" ")
        print(f"Correct answer was '{b}'.")
        return print(f"Let's try again, {name}!")


def get_nod(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def get_nums_list() -> list[str]:
    random_step = randint(1, 10)
    random_list = [str(x) for x in range(1, 100, random_step)]
    return random_list[1:11]


def is_prime_num(num: int) -> str:
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return 'no'
                break
        else:
            return 'yes'
    else:
        return 'no'

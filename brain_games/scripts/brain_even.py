from brain_games.engine import welcome_gamer
from brain_games.engine import chek_equality
from random import randint
from prompt import string


def run_game():
    gamers_name = welcome_gamer()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for x in range(3):
        random_number = randint(1, 100)
        modulo = random_number % 2
        is_modulo = 'yes' if modulo == 0 else 'no'
        print(f"Question: {random_number}")
        answer_from_gamer = string("Your answer: ")
        chek_equality(a=is_modulo, b=answer_from_gamer, name=gamers_name)
    return print(f"Congratulations, {gamers_name}!")


def main():
    run_game()


if __name__ == "__main__":
    main()

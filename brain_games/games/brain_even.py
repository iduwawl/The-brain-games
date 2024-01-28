from brain_games.engine import welcome_gamer
from brain_games.engine import congrats
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
        if answer_from_gamer == is_modulo:
            print('Correct')
        else:
            print(f"'{answer_from_gamer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{is_modulo}'.")
            return print(f"Let's try again, {gamers_name}!")
    return congrats(gamers_name)


def main():
    run_game()


if __name__ == "__main__":
    main()

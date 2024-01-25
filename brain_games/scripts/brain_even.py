from brain_games.cli import welcome_user
from random import randint
from prompt import string


def brain_even_game():
    gamers_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for x in range(3):
        random_number = randint(1, 100)
        modulo = random_number % 2
        is_modulo = 'yes' if modulo == 0 else 'no'
        print(f"Question: {random_number}")
        answer_from_gamer = string("Your answer: ")
        if answer_from_gamer == is_modulo:
            print("Correct!")
        elif answer_from_gamer == 'yes' or answer_from_gamer == 'no':
            print(f"'{answer_from_gamer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{is_modulo}'.")
            return print(f"Let's try again, {gamers_name}!")
    return print(f"Congratulations, {gamers_name}!")


def main():
    brain_even_game()


if __name__ == "__main__":
    main()

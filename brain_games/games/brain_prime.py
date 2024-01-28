from brain_games.engine import welcome_gamer
from brain_games.engine import congrats
from brain_games.engine import is_prime_num
from random import randint
from prompt import string


def run_game():
    gamers_name = welcome_gamer()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for x in range(3):
        number = randint(2, 100)
        is_prime = is_prime_num(num=number)
        print(f"Question: {number}")
        gamers_answer = string("Your answer: ")
        if gamers_answer == is_prime:
            print('Correct!')
        else:
            print(f"'{gamers_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{is_prime}'.")
            return print(f"Let's try again, {gamers_name}!")
    return congrats(gamers_name)


def main():
    run_game()


if __name__ == "__main__":
    main()

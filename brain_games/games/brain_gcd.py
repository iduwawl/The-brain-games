from brain_games.engine import welcome_gamer
from brain_games.engine import congrats
from brain_games.engine import get_nod
from random import randint
from prompt import integer


def brain_gcd_game():
    gamers_name = welcome_gamer()
    print("Find the greatest common divisor of given numbers.")
    for x in range(3):
        first_number = randint(1, 100)
        second_number = randint(1, 100)
        nod = get_nod(first_number, second_number)
        print(f"Question: {first_number} {second_number}")
        gamers_answer = integer("Your answer: ")
        if gamers_answer == nod:
            print('Correct')
        else:
            print(f"'{gamers_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{nod}'.")
            return print(f"Let's try again, {gamers_name}!")
    return congrats(gamers_name)


def main():
    brain_gcd_game()


if __name__ == "__main__":
    main()

from brain_games.cli import welcome_user
from brain_games.cli import congrats
from random import randint
from random import choice
from prompt import integer


def brain_calc_game():
    gamers_name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    for x in range(3):
        first_number = randint(1, 100)
        second_number = randint(1, 100)
        operators = ("-", "+", "*")
        random_operator = choice(operators)
        result = int()
        match random_operator:
            case '-':
                result = first_number - second_number
            case '+':
                result = first_number + second_number
            case '*':
                result = first_number * second_number
        print(f"Question: {first_number} {random_operator} {second_number}")
        gamers_answer = integer("Your answer: ")
        if gamers_answer == result:
            print('Correct')
        else:
            print(f"'{gamers_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{result}'.")
            return print(f"Let's try again, {gamers_name}!")
    return congrats(gamers_name)


def main():
    brain_calc_game()


if __name__ == "__main__":
    main()

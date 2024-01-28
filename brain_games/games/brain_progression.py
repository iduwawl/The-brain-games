from brain_games.engine import welcome_gamer
from brain_games.engine import congrats
from brain_games.engine import get_nums_list
from random import choice
from prompt import string


def run_game():
    gamers_name = welcome_gamer()
    print("What number is missing in the progression?")
    for x in range(3):
        list_of_nums = get_nums_list()
        random_number = choice(list_of_nums)
        joined_sliced_list = " ".join(list_of_nums)
        list_with_miss_num = joined_sliced_list.replace(random_number, "..", 1)
        print(f"Question: {list_with_miss_num}")
        gamers_answer = string("Your answer: ")
        if gamers_answer == random_number:
            print('Correct!')
        else:
            print(f"'{gamers_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{random_number}'.")
            return print(f"Let's try again, {gamers_name}!")
    return congrats(gamers_name)


def main():
    run_game()


if __name__ == "__main__":
    main()

from prompt import string


def welcome_user():
    print("Welcome to the Brain Games!")
    gamers_name = string('May I have your name? ')
    print(f"Hello, {gamers_name}!")

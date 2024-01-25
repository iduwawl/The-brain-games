from prompt import string


def welcome_user() -> str:
    """Print welcome message, return input gamer's name"""
    print("Welcome to the Brain Games!")
    gamers_name = string('May I have your name? ')
    print(f"Hello, {gamers_name}!")
    return gamers_name

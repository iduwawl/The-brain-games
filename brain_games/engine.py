from prompt import string
NUM_OF_ROUNDS = 3


def run_game(game):
    gamers_name = string("Welcome to the Brain Games!\n"
                         "May I have your name? ")
    print(f"Hello, {gamers_name}!\n"
          f'{game.GAME_RULE}')
    for _ in range(NUM_OF_ROUNDS):
        question, correct_answer = game.get_question_and_correct_answer()
        gamer_answer = string(f"Question: {question}\n"
                              "Your answer: ")
        if gamer_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{gamer_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {gamers_name}!")
            return
        print(f"Congratulations, {gamers_name}!")

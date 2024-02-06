from prompt import string


def run_game(get_question_and_answer, rule):
    COUNT_CORRECT_ANSWER = 3
    gamers_name = string("Welcome to the Brain Games!\n"
                         "May I have your name? ")
    print(f"Hello, {gamers_name}!\n"
          f'{rule}')
    for _ in range(COUNT_CORRECT_ANSWER):
        question, correct_answer = get_question_and_answer()
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

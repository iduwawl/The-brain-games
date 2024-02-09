from random import randint

GAME_RULE = "What number is missing in the progression?"
MIN_RANGE = 1
MAX_RANGE = 100
MIN_STEP = 1
MAX_STEP = 10


def get_progression(min_value, max_value, step_diff):
    return [str(x) for x in range(min_value, max_value, step_diff)][0:10]


def get_str_question(progression, num_to_replace):
    question = progression
    question[num_to_replace] = '..'
    return ' '.join(question)


def get_question_and_answer():
    diff_step = randint(MIN_STEP, MAX_STEP)
    progression = get_progression(MIN_RANGE, MAX_RANGE, diff_step)
    num_to_replace = randint(0, len(progression) - 1)
    correct_answer = str(progression[num_to_replace])
    str_question = get_str_question(progression, num_to_replace)
    return str_question, correct_answer

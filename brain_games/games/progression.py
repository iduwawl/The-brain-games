from random import randint

GAME_RULE = "What number is missing in the progression?"
MIN_RANGE = 1
MAX_RANGE = 100
MIN_STEP = 1
MAX_STEP = 10
MIN_INDEX_MISS_NUM = 0


def get_progression(min_value, max_value, step_diff) -> list:
    return [str(x) for x in range(min_value, max_value, step_diff)][0:10]


def get_question(progression, index) -> str:
    progression[index] = '..'
    return ' '.join(progression)


def get_question_and_correct_answer():
    step = randint(MIN_STEP, MAX_STEP)
    progression = get_progression(MIN_RANGE, MAX_RANGE, step)
    index_of_miss_num = randint(MIN_INDEX_MISS_NUM, len(progression) - 1)
    correct_answer = progression[index_of_miss_num]
    question = get_question(progression, index_of_miss_num)
    return question, str(correct_answer)

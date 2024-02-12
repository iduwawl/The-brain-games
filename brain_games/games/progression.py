from random import randint

GAME_RULE = "What number is missing in the progression?"
MIN_FIRST_NUM = 1
MAX_FIRST_NUM = 10
MIN_LAST_NUM = 90
MAX_LAST_NUM = 100
MIN_STEP = 2
MAX_STEP = 9
MIN_INDEX_MISS_NUM = 0


def get_progression(first_num, last_num, step_diff) -> list:
    return [x for x in range(first_num, last_num, step_diff)][0:10]


def get_progression_with_hiden_num(progression, index_num_to_hide) -> list:
    progression[index_num_to_hide] = '..'
    return progression


def get_progression_converted_to_str(progression) -> str:
    return ' '.join(map(str, progression))


def get_question_and_correct_answer():
    step = randint(MIN_STEP, MAX_STEP)
    min_num = randint(MIN_FIRST_NUM, MAX_FIRST_NUM)
    max_num = randint(MIN_LAST_NUM, MAX_LAST_NUM)
    progression = get_progression(min_num, max_num, step)
    index_of_miss_num = randint(MIN_INDEX_MISS_NUM, len(progression) - 1)
    correct_answer = progression[index_of_miss_num]
    progression_with_hiden_num = get_progression_with_hiden_num(
        progression, index_of_miss_num)
    question = get_progression_converted_to_str(progression_with_hiden_num)
    return question, str(correct_answer)

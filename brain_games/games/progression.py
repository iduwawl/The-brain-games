from random import randint

GAME_RULE = "What number is missing in the progression?"
MIN_FIRST_NUM = 1
MAX_FIRST_NUM = 10
MIN_AMOUNT_OF_NUM = 25
MAX_AMOUNT_OF_NUM = 30
MIN_DIFF_PROGRESSION = 2
MAX_DIFF_PROGRESSION = 9
MIN_INDEX_MISS_NUM = 0


def get_progression(first_num, difference, how_many_nums) -> list:
    progression = []
    for x in range(how_many_nums):
        progression.append(first_num)
        first_num += difference
    return progression


def get_progression_with_hiden_num(progression, index_num_to_hide) -> list:
    progression[index_num_to_hide] = '..'
    return progression


def get_progression_converted_to_str(progression) -> str:
    return ' '.join(map(str, progression))


def get_question_and_correct_answer():
    first_num = randint(MIN_FIRST_NUM, MAX_FIRST_NUM)
    difference = randint(MIN_DIFF_PROGRESSION, MAX_DIFF_PROGRESSION)
    amount_of_nums = randint(MIN_AMOUNT_OF_NUM, MAX_AMOUNT_OF_NUM)
    progression = get_progression(first_num, difference, amount_of_nums)
    sliced_progression = progression[0:10]
    index_of_miss_num = randint(MIN_INDEX_MISS_NUM, len(sliced_progression) - 1)
    correct_answer = sliced_progression[index_of_miss_num]
    progression_with_hiden_num = get_progression_with_hiden_num(
        sliced_progression, index_of_miss_num)
    question = get_progression_converted_to_str(progression_with_hiden_num)
    return question, str(correct_answer)

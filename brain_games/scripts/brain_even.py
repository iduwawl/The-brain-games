#!/usr/bin/env python3
from brain_games.games import even
from brain_games import engine


def main():
    engine.run_game(even.get_yes_or_no_answer_and_num(get_is_even_num_and_num),
                    even.GAME_RULE)


if __name__ == "__main__":
    main()

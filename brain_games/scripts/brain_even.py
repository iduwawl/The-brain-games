#!/usr/bin/env python3
from games.even import get_num_and_is_even_answer
from games.even import GAME_RULE
from brain_games.engine import run_game


def main():
    run_game(get_num_and_is_even_answer, GAME_RULE)


if __name__ == "__main__":
    main()

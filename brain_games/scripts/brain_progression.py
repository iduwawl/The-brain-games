#!/usr/bin/env python3
from games.progression import get_str_with_miss_num_and_num
from games.progression import GAME_RULE
from brain_games.engine import run_game


def main():
    run_game(get_str_with_miss_num_and_num, GAME_RULE)


if __name__ == "__main__":
    main()

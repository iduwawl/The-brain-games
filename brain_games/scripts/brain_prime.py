#!/usr/bin/env python3
from games.prime import get_num_and_is_prime_answer
from games.prime import GAME_RULE
from brain_games.engine import run_game


def main():
    run_game(get_num_and_is_prime_answer, GAME_RULE)


if __name__ == "__main__":
    main()

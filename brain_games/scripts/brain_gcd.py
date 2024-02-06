#!/usr/bin/env python3
from games.gcd import get_nums_and_nod
from games.gcd import GAME_RULE
from brain_games.engine import run_game


def main():
    run_game(get_nums_and_nod, GAME_RULE)


if __name__ == "__main__":
    main()

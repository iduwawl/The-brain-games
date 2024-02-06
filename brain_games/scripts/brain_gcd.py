#!/usr/bin/env python3
from brain_games.games import gcd
from engine import run_game


def main():
    run_game(gcd.get_nums_and_nod,
             gcd.GAME_RULE)


if __name__ == "__main__":
    main()

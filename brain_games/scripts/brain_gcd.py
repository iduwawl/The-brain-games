#!/usr/bin/env python3
from brain_games.games import gcd
from brain_games import engine


def main():
    engine.run_game(gcd.str_nums,
                    gcd.gcd_of_nums,
                    gcd.GAME_RULE)


if __name__ == "__main__":
    main()

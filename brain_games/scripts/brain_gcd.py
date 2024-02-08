#!/usr/bin/env python3
from brain_games.games import gcd
from brain_games import engine


def main():
    engine.run_game(gcd.get_nums_and_gcd,
                    gcd.GAME_RULE)


if __name__ == "__main__":
    main()

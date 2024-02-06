#!/usr/bin/env python3
import games.gcd
import engine


def main():
    engine.run_game(games.gcd.get_nums_and_nod,
                    games.gcd.GAME_RULE)


if __name__ == "__main__":
    main()

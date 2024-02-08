#!/usr/bin/env python3
from brain_games.games import even
from brain_games import engine


def main():
    engine.run_game(even.RANDOM_NUM,
                    even.yes_or_no_answer,
                    even.GAME_RULE)


if __name__ == "__main__":
    main()

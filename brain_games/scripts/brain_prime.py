#!/usr/bin/env python3
from brain_games.games import prime
from brain_games import engine


def main():
    engine.run_game(prime.RANDOM_NUM,
                    prime.yes_or_no_answer,
                    prime.GAME_RULE)


if __name__ == "__main__":
    main()

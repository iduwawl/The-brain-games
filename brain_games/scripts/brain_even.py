#!/usr/bin/env python3
from brain_games.games import even
from brain_games.engine import run_game


def main():
    run_game(even.get_num_and_is_even_answer,
             even.GAME_RULE)


if __name__ == "__main__":
    main()

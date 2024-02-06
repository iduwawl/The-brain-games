#!/usr/bin/env python3
from games.calc import get_expression_and_result
from games.calc import GAME_RULE
from brain_games.engine import run_game


def main():
    run_game(get_expression_and_result, GAME_RULE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from brain_games.games import calc
from brain_games import engine


def main():
    engine.run_game(calc.get_expression_and_result,
                    calc.GAME_RULE)


if __name__ == "__main__":
    main()
